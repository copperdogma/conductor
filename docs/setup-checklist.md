# Conductor — Methodology Bootstrap Checklist

> Working copy generated during initial setup.

## Mode

- [x] Mode chosen: `greenfield`
- [x] Core references reviewed and adapted for Conductor's supervisor role

## Canonical surface

- [x] `AGENTS.md` defines the mission and operating rule
- [x] `docs/ideal.md` and `docs/spec.md` exist
- [x] Ideal quality gate: concise desired outcomes, zero implementation;
      distinct needs preserved and mechanisms retained in Spec/ADRs/runbooks
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

- [x] Local skill folders exist for triage, ADR triage, story flow, scouting,
      alignment, and setup
- [x] `scripts/sync-agent-skills.sh` exists
- [x] `.agents/skills` is the canonical skill surface; provider-specific command aliases are optional compatibility only
- [x] `scripts/methodology_graph.py` exists
- [x] `Makefile` exposes `methodology-compile`, `methodology-check`, `skills-sync`, and `skills-check`

## Validation

- [x] `make methodology-compile`
- [x] `make methodology-check`
- [x] `make skills-sync`
- [x] `make skills-check`
- [x] `make lint`
- [x] `make test`

## Research before reinvention (Alignment 053)

- [x] Kickoff and setup skills/runbooks carry conditional problem-class research
      guidance and preserve the lean setup variant
- [x] Conductor `AGENTS.md`, `/build-story`, `/validate`, `/loop-review`, and
      `/loop-verify` implement the approved local guidance and checkpoints
- [x] Local checks and independent scenario review completed; evidence and
      validator compatibility note recorded in
      [Alignment 053](alignments/align-053-research-before-reinvention.md)

## Reusable source package (Alignment 058)

- [x] Source inventory distinguishes shared guidance and product/supervisor roles
- [x] Product setup assets and missing evidence/triage skills are available
- [x] Existing target truths and local files are preserved by copy preflight
- [x] Core/optional module selection and source receipts are explicit
- [x] Sparse product compiler/facts reject invalid evidence instead of quiet zeroes
- [x] Focused tests and independent review completed; findings fixed
- [x] Disposable product setup exercised from final source with honest deferrals
- [x] Failed first exercise, recovery, checks and applicability limits retained in
      [Alignment 058](alignments/align-058-reusable-setup-package.md)
- [x] Scoped landing authorized on 2026-10-20 and candidate validated; remote
      identities are verified in the close-out handoff
