# Conventions - Ferret

Coding and commit conventions for the Ferret project.

---

## Commit Format

**Format**: `#XXX: type: description`

**Types**: feat, fix, refactor, test, docs, chore

**Examples**:
```
#5: feat: implement greenhouse scraper
#5: fix: handle missing ats_token gracefully
#5: test: add greenhouse fixture parsing tests
```

**Rules**:
- Always prefix with the GitHub issue number the work is for.
- A commit not tied to a specific issue (e.g. logging past work in kanban, a repo-wide reorg) has no `#XXX:` prefix — don't invent one.
- Description: WHAT/WHY, not HOW/WHO.
- No stats (+XX lines), no implementation details, no emoji.

## Branch Naming

- Features: `feature/#XXX-description`
- Bugfixes: `bugfix/#XXX-description`

---

## Python (backend/)

- Type hints on all function signatures.
- One SQLAlchemy model per file under `app/models/`.
- Routers stay thin — business logic belongs in the module it's about (`filters.py`, `scrapers/*`), not inline in route handlers.
- No hardcoded config — everything through `app/config.py` (`pydantic-settings`, reads `.env`).

### Package Structure

```
backend/app/
├── auth/        # password hashing, JWT issue/verify
├── models/      # SQLAlchemy table models, one per file
├── routers/     # FastAPI route handlers, one router per resource
├── scrapers/    # one module per ATS platform
├── config.py    # settings
├── db.py        # engine/session
├── filters.py   # per-user criteria filtering logic
└── main.py      # FastAPI app + router registration
```

---

## Kotlin (app/)

### Package Structure

```
com.ferret.app.*
```

(Flat for now — introduce `ui.*`/`data.*`/`domain.*` layering once there's more than a placeholder screen; see `contexts/architecture.md` for the planned screens.)

### Naming

- Composables: PascalCase functions.
- ViewModels: `*ViewModel.kt`.
- API client models: mirror the backend's Pydantic/SQLAlchemy field names so payloads map 1:1.

---

## Code Quality (both languages)

1. No hardcoded values — config/constants only.
2. One class/model/interface per file.
3. Strong typing — no bare `Any`/`dict` payloads crossing a function boundary without a type.
4. DRY — no duplicated logic between the scraper modules or between screens.
5. Comments explain WHY, not WHAT.
