---
name: setup-methodology
description: Install or refresh Conductor's methodology package
user-invocable: true
---

# /setup-methodology [greenfield|refresh]

Use this to bootstrap or refresh Conductor's own supervisor methodology.

## What it owns

- `AGENTS.md`
- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology/state.yaml`
- `projects.yaml`
- `docs/methodology/graph.json`
- `docs/stories.md`
- `inbox.md`
- `docs/scout.md`
- `docs/align-projects.md`

## Product-repo setup surface

Conductor's own setup surface is supervisor-specific, but the tracked product
repos should keep their `/setup-methodology` skill text identical. When a
triage, loop-verify, or bootstrap improvement affects new product repos:

- upgrade the shared product `/setup-methodology` skill in one product worktree
- run a local propagation sweep against the no-code/greenfield case before
  copying
- copy the exact skill file into the other product repos
- regenerate/check wrappers in every target repo
- avoid per-repo rewrites unless a repo has a documented local exception

The shared product skill must handle repos with no code yet. It should require
real `docs/ideal.md` and `docs/spec.md` from `/init-project` or equivalent
intake, install upgraded triage/triage-health/loop-verify surfaces, mark
code-dependent lanes as absent or deferred, and run cheap checks instead of
long subagent loops over evidence that cannot exist yet.

## Steps

1. Read `AGENTS.md`, `docs/ideal.md`, `docs/spec.md`, `projects.yaml`, and `docs/methodology/state.yaml`.
2. Refresh `docs/setup-checklist.md`.
3. Ensure the inbox, scout, alignment, story, and decision surfaces still match the mission.
4. Refresh the local skills if they drift from actual practice.
5. Run:
   - `make methodology-compile`
   - `make methodology-check`
   - `make skills-sync`
   - `make skills-check`
   - `make lint`
   - `make test`
6. Summarize what changed and what still needs follow-up.

## Guardrails

- Keep Conductor lightweight.
- Do not import pipeline-specific methodology baggage from the tracked projects.
- Do not add structure that does not remove recurring work.
