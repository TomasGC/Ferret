# KANBAN - Ferret

Track of work sessions and completed tasks. All tasks tracked in GitHub: [Issues](https://github.com/TomasGC/Ferret/issues) / [Project board](https://github.com/users/TomasGC/projects/8).

---

2026-08-30 - #1 First commit with Skeleton
- Brainstormed V1 design: backend+app split, Postgres/Neon, Greenhouse/Lever/Workday scraper scope, GitHub Actions daily cron, closed-group auth
- Scaffolded backend (FastAPI/SQLAlchemy/Postgres boilerplate: config/db/models/auth security/router+scraper stubs) and Android (Kotlin/Compose skeleton)
- Logic left as TODO stubs — user implementing it themselves
- Set repo + Project board descriptions, added MIT LICENSE
tags: #scaffold #v1
Ref: https://github.com/TomasGC/Ferret/issues/1
Commit: 3de0d6f

---

2026-08-30 - Documentation reorg, wiki, and V1 issue breakdown
- Reorganized `.claude/` into `contexts/` (kanban, architecture, conventions, commands), matching the convention used across other projects; defined Claude's four roles (support, product owner, UX/UI designer, documentalist)
- Created the GitHub wiki: Home, Getting Started, Architecture, Roadmap (V1-V7), UX Design
- Produced UX mockups (login/register, company browser, criteria editor, offers feed) as a Claude Design canvas, linked from the UX Design wiki page
- Split the V1 backlog into 20 GitHub issues (#2-#21: 12 backend, 6 Android, 2 infra), each with acceptance criteria and relevant files, added to the Project board
tags: #docs #wiki #ux #product-management
Refs:
- https://github.com/TomasGC/Ferret/wiki
- https://github.com/users/TomasGC/projects/8
Commits: 6ce1706

---

## Notes

- **One entry per issue** — updated each time you work on it
- **Date** — last update date
- **Title line**: `YYYY-MM-DD - #ID Title`
- **Description** — bullet points describing work done (max 6 lines)
- **Tags** — `tag:` (singular) or `tags:` (plural) with # prefix
- **Ref/Refs** — link to the issue
- **Commit/Commits** — short hashes (7 chars)
- **Language**: English only
- **All tasks tracked in GitHub Issues** - This file is just a log
