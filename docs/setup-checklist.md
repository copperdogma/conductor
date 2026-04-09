# Conductor — Methodology Bootstrap Checklist

> Working copy generated during initial setup.

## Mode

- [x] Mode chosen: `greenfield`
- [x] Core references reviewed and adapted for Conductor's supervisor role

## Canonical surface

- [x] `AGENTS.md` defines the mission and operating rule
- [x] `docs/ideal.md` and `docs/spec.md` exist
- [x] `docs/methodology/state.yaml` exists
- [x] `projects.yaml` exists as the tracked-project registry
- [x] `docs/runbooks/setup-methodology.md` exists
- [x] `docs/setup-checklist.md` exists

## Memory surfaces

- [x] `inbox.md` exists
- [x] `docs/scout.md` and `docs/scout/` exist
- [x] `docs/align-projects.md` and `docs/alignments/` exist
- [x] `docs/stories/` exists

## Skill and check surface

- [x] Local skill folders exist for triage, story flow, scouting, alignment, and setup
- [x] `scripts/sync-agent-skills.sh` exists
- [x] `scripts/methodology_graph.py` exists
- [x] `Makefile` exposes `methodology-compile`, `methodology-check`, `skills-sync`, and `skills-check`

## Validation

- [x] `make methodology-compile`
- [x] `make methodology-check`
- [x] `make skills-sync`
- [x] `make skills-check`
- [x] `make lint`
- [x] `make test`
