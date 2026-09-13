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
- `/finish-and-push` completes and lands current work, including linked repo
  changes from the same request. Use `--audit-only` for a read-only readiness
  review and `--cleanup` to remove eligible task-owned local worktrees and branches.

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

For close-out, use the shared `/finish-and-push` validation policy to select and
reuse checks. Conductor's document/record checks are `make methodology-check`
and `make lint`; skill changes use `make skills-check`. Script or repo-check
changes use focused tests, broadening to `make test` when shared effects warrant
it. Refresh generated planning surfaces with `make methodology-compile` when
their sources change, before the final methodology check. Commits and story
bookkeeping do not require repeating checks over unchanged inputs.
