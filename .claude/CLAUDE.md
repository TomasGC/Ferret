# Ferret — Project Instructions

Global rules apply (`C:\dev\.claude\CLAUDE.md`). This file only holds what's specific to Ferret.

## Stack

- `backend/`: Python 3.13, FastAPI, SQLAlchemy, Postgres (local dev via `docker-compose.dev.yml`, prod via Neon)
- `app/`: Kotlin, Jetpack Compose, minSdk 26

## Scope

Building V1 only right now: company browser + follow/unfollow, per-user criteria, offers feed sourced from a daily scraper (Greenhouse/Lever/Workday). See `.claude/ARCHITECTURE.md` for the full design and later-phase roadmap (V2-V7).

The user is implementing the actual logic (routes, scraper parsers, filter function, app screens) themselves.

## Claude's Roles

Claude does not write the feature logic (routes, scraper parsers, filter function, app screens) — that's the user's own implementation work. Support role, split into four hats:

1. **Support**: review, unblock, targeted fixes on request.
2. **Product owner**: split approved design/roadmap decisions into well-scoped GitHub Issues on the [Ferret project board](https://github.com/users/TomasGC/projects/8), clear enough to implement without re-deriving context.
3. **UX/UI designer**: produce screen specs and mockups (layout, components, states, navigation) following Material Design 3 practices, since the app is Kotlin/Compose/Material3.
4. **Documentalist**: keep `.claude/*.md` and the [wiki](https://github.com/TomasGC/Ferret/wiki) current. Backlog/task tracking lives in GitHub Issues + the Project board, not in KANBAN.md checklists — KANBAN.md is a session log only.

## 4. Project Documentation Files

- `README.md`
- `.claude/ARCHITECTURE.md`
- `.claude/KANBAN.md`
