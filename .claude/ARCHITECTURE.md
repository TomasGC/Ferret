# Ferret — Architecture

## Overview

```
Android app (Kotlin)  --HTTPS/JWT-->  FastAPI (Azure App Service F1)  <--reads/writes-->  Postgres (Neon, free tier)
                                              ^
GitHub Actions (daily cron) --scrapes Greenhouse/Lever/Workday--> writes offers into same Postgres DB
```

Backend is the only thing that touches the database. The GitHub Actions workflow and the FastAPI app live in this repo and share the same Python scraper/filter modules — no duplicated logic between the cron job and the API.

## Data model (Postgres tables)

- `users`: `id`, `email` (unique), `password_hash` (bcrypt), `created_at`
- `domains` (shared, seeded from Engine's `domains.json`): `id`, `name` (unique)
- `companies` (shared, seeded from Engine's `companies.json`): `id`, `name`, `site`, `ats_platform: enum(greenhouse|lever|workday|none)`, `ats_token`
- `company_domains` (junction table, many-to-many `companies` ↔ `domains`): `company_id`, `domain_id`
- `follows` (junction table, many-to-many `users` ↔ `companies`): `user_id`, `company_id`
- `criteria` (one row per user, seeded shape from Engine's `criteria.json`): `id`, `user_id` (unique FK), `allowed_job_names: text[]`, `forbidden_languages: text[]`
- `criteria_forbidden_domains` (junction table, many-to-many `criteria` ↔ `domains`): `criteria_id`, `domain_id`
- `offers` (shared, written by scraper): `id`, `company_id` (FK), `title`, `description`, `url`, `posted_at`, `scraped_at`, unique constraint on `(company_id, url)` for idempotent upserts

Real foreign keys throughout — renaming a domain or company is one row update, not a fan-out across documents. A user's feed = `offers` joined through `follows` on `company_id`, filtered by their own `criteria` row (title match, forbidden languages, forbidden domains) — applied at read time in the API query, not baked into storage, so changing criteria doesn't require re-scraping.

## Scraper (GitHub Actions, daily cron)

- One parser module per ATS (`greenhouse.py`, `lever.py`, `workday.py`), each hitting that platform's JSON endpoint directly (no HTML scraping for these three).
- Only scrapes companies that at least one user follows — skips the rest of the catalog.
- Companies with `ats_platform: none` are browse-only: shown in the app with a link to their site, never auto-scraped.
- Idempotent upsert into `offers` via the `(company_id, url)` unique constraint (`ON CONFLICT DO UPDATE`) to avoid duplicates on re-runs.
- Domain/language exclusion logic ported from Engine's `JobFilterEngine.kt` into `backend/app/filters.py`.

## API (FastAPI)

- `POST /auth/register`, `POST /auth/login` → JWT
- `GET /companies` (catalog + domains)
- `GET/POST/DELETE /me/follows`
- `GET/PUT /me/criteria`
- `GET /me/offers` → filtered feed per above
- All routes except `/auth/*` require a Bearer JWT.

## Android app (V1 screens)

- Login / register
- Company browser (list + domain filter, follow/unfollow toggle)
- Criteria editor (job titles, forbidden languages, forbidden domains)
- Offers feed (from `GET /me/offers`)

No local filtering logic, no local database beyond the stored JWT — the app is a pure API client. All filtering happens server-side per user.

## Hosting

- **GitHub Actions** (scheduled workflow, daily cron): runs the scraper, writes to Postgres. Free — a few minutes/day is nowhere near the free-tier minute allowance.
- **Azure App Service, Free tier (F1)**: hosts the FastAPI read API.
- **Neon, free tier** (~0.5GB Postgres): shared storage for catalog + offers + per-user data. Compute auto-suspends after inactivity, wakes automatically on the next query (short cold-start delay, no data loss, no manual restart).

$0/month at this scale.

## Testing

- Backend: pytest — unit tests per ATS parser (fixture JSON → parsed offers), unit tests for the criteria-filter function, integration test for `/me/offers` against a test Postgres (or SQLite in-memory for speed).
- Android: unit tests on the repository/viewmodel layer — no scraping or filtering logic lives client-side, so there's nothing else to cover there.

## Roadmap (later phases, not V1)

- V3: bulk update companies/criteria via CSV or JSON import.
- V4: additional search engines (Welcome to the Jungle, LinkedIn, job.makesense, others) — likely needs HTML scraping or auth'd APIs, revisit backend/scraper design when targets are picked.
- V5: save/bookmark offers.
- V6: apply directly through the app, track application status.
- V7: push notifications on new matching offers for followed companies (backend already has the data shape for this — daily scrape + per-user criteria).
