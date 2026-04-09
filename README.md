# Conductor

Conductor is the supervisor project for Cam's active AI-first projects.

It exists to reduce cross-project busywork by turning vague notes into ready
work, comparing shared infrastructure surfaces across projects, and scouting
external ideas for project-specific adoption.

## Core loops

- `inbox.md` captures cross-project notes, links, and sync requests.
- `/triage` turns inbox items and backlog pressure into one recommended action.
- `/align-projects` compares infrastructure drift across tracked projects.
- `/scout` investigates external sources and recommends which projects should
  adopt what.

## Key surfaces

- `projects.yaml`
- `inbox.md`
- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `docs/align-projects.md`
- `docs/scout.md`

## Commands

```bash
make methodology-compile
make methodology-check
make skills-sync
make skills-check
make lint
make test
```

