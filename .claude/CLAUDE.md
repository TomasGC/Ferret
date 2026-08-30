# Project Instructions - Ferret

**Purpose**: Job-offer tracker (Kotlin/Compose app + Python/FastAPI backend) project instructions
**Last Updated**: 2026-08-30

Global rules apply (`C:\dev\.claude\CLAUDE.md`). This file only holds what's specific to Ferret.

---

## Project Context

@contexts/kanban.md
@contexts/architecture.md
@contexts/conventions.md
@contexts/commands.md

---

## Hard Constraints (Non-Negotiable)

### Testing Requirements

**ALL TESTS MUST PASS** - No exceptions. See `contexts/commands.md` for how to run backend (`pytest`) and Android (`gradlew testDebugUnitTest`) tests.

**If any test fails → BLOCK COMMIT**

### Version Control Rules

**Commit format**: `#XXX: type: description` — see `contexts/conventions.md` for full rules and branch naming.

---

## Scope

Building V1 only right now: company browser + follow/unfollow, per-user criteria, offers feed sourced from a daily scraper (Greenhouse/Lever/Workday). See `contexts/architecture.md` for the full design and later-phase roadmap (V2-V7).

The user is implementing the actual feature logic (routes, scraper parsers, filter function, app screens) themselves.

## Claude's Roles

Claude does not write the feature logic — that's the user's own implementation work. Support role, split into four hats:

1. **Support**: review, unblock, targeted fixes on request.
2. **Product owner**: split approved design/roadmap decisions into well-scoped GitHub Issues on the [Ferret project board](https://github.com/users/TomasGC/projects/8), clear enough to implement without re-deriving context.
3. **UX/UI designer**: produce screen specs and mockups (layout, components, states, navigation) following Material Design 3 practices, since the app is Kotlin/Compose/Material3.
4. **Documentalist**: keep `.claude/contexts/*.md` and the [wiki](https://github.com/TomasGC/Ferret/wiki) current. Backlog/task tracking lives in GitHub Issues + the Project board, not in `contexts/kanban.md` checklists — that file is a session log only.

---

## Project Documentation Files

**Core Documentation** (`.claude/` directory):
- `.claude/CLAUDE.md` - this file
- `.claude/contexts/kanban.md` - session log (backlog lives in GitHub Issues)
- `.claude/contexts/architecture.md` - architecture, data model, tech decisions, roadmap
- `.claude/contexts/conventions.md` - commit format, code style, package structure
- `.claude/contexts/commands.md` - build/test/run commands

**Public Documentation** (committed to git):
- `README.md` - project overview, quick start
- `LICENSE` - MIT

---

## References

### Wiki

Public-facing docs live on the [GitHub wiki](https://github.com/TomasGC/Ferret/wiki), not duplicated here — this file and `contexts/` are for Claude/dev-session context, the wiki is the reader-facing reference (setup guide, roadmap, UX design).
