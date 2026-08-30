# 🦡 Ferret

Job-offer tracker: follow companies, set your own filtering criteria, get matching offers pulled from their career pages automatically.

## How it works

- A shared catalog of companies and business domains.
- Each user follows a subset of companies and defines their own criteria (job titles, forbidden languages, forbidden domains).
- A daily job scrapes followed companies' career pages (Greenhouse, Lever, Workday) and stores new offers.
- The Android app reads your personalized offer feed through a small API.

## Structure

- `backend/` — Python/FastAPI API + scrapers, data in Postgres (Neon)
- `app/` — Android app (Kotlin, Jetpack Compose)

## Status

V1 in progress. See the [wiki](https://github.com/TomasGC/Ferret/wiki) for architecture, roadmap, and UX design, and the [Project board](https://github.com/users/TomasGC/projects/8) for current tasks.

## License

MIT — see [LICENSE](LICENSE).
