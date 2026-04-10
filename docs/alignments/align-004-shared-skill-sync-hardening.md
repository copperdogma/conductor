# Alignment 004 — Shared Skill Sync Hardening

**Date**: 2026-04-10
**Focus**: Compare the remaining shared infrastructure skill surface and
skill-sync tooling across tracked projects
**Source Project**: Baseline across `dossier`, `storybook`, `doc-web`, and
`cine-forge`
**Target Projects**: `dossier`, `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- The 18 skills present in all four tracked repos: `align`, `build-story`,
  `check-in-diff`, `codebase-improvement-scout`, `create-adr`,
  `create-cross-cli-skill`, `create-story`, `discover-models`,
  `finish-and-push`, `improve-eval`, `mark-story-done`, `scout`,
  `setup-methodology`, `triage-evals`, `triage-inbox`, `triage-stories`,
  `triage`, and `validate`
- `scripts/sync-agent-skills.sh`
- Generated `.gemini/commands/*.toml` wrappers as verified by
  `./scripts/sync-agent-skills.sh --check`
- Storybook
  `docs/decisions/adr-019-compromise-convergence-tracking/migration.md`
- Dossier Story 095 to confirm the earlier build-map-first migration conflict
  is no longer the main explanation for shared-skill drift

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: this pass should compare semantic workflow shape and only recommend
  narrow sync where it removes repeated work.
- Storybook ADR-019 migration notes make Gemini wrapper sync an explicit
  methodology surface, but they do not settle how strict wrapper drift
  detection must be.
- Dossier Story 095 completed the state/graph methodology migration, so the
  earlier build-map-first conflict from Alignment 001 is no longer the active
  explanation for the remaining shared-skill differences.
- No narrower decision record was found in Dossier, doc-web, or CineForge for
  shared-skill text identity or wrapper-drift enforcement.

## Key Differences

- Only 18 skills are shared across all four tracked repos. Total skill
  inventories still diverge materially: Dossier has 26 skills, Storybook 28,
  doc-web 24, and CineForge 32.
- None of the 18 shared skills are text-identical across all four repos. That
  is not automatically drift; the common skills still preserve the same
  workflow spine around story creation/build/validation/close-out, inbox
  triage, scouting, alignment, eval triage, and cross-CLI skill generation.
- The remaining text differences are mostly repo-local methodology wiring:
  Dossier keeps Dossier-native story and eval expectations, Storybook carries
  the most opinionated state/graph-first package wording, doc-web routes some
  decisions through runbooks/notes in addition to ADRs, and CineForge keeps
  design- and dashboard-aware language for its own product workflow.
- Storybook's `scripts/sync-agent-skills.sh` is the only implementation that
  fails when `user-invocable` frontmatter is missing, verifies Gemini wrapper
  file contents rather than only file presence, and enforces exact wrapper
  count equality with the invocable skill set.
- Dossier, doc-web, and CineForge all currently pass
  `./scripts/sync-agent-skills.sh --check`, so there is no live breakage in the
  generated wrapper surface today. Their current scripts are simply weaker:
  they would not catch stale extra wrappers or hand-edited Gemini wrapper
  content drift.
- CineForge's shared core skills still mention generated dashboards and
  `docs/design/` in their generic alignment checks. Those surfaces are real in
  CineForge's local methodology package and should not be treated as accidental
  drift or copied outward by default.

## Classification

- **Intentional adaptation**: repo-specific extra skills, local story/eval
  wording inside the shared skills, doc-web's broader decision-source routing,
  and CineForge's dashboard/design references should stay local.
- **Portable improvement**: Storybook's stricter
  `scripts/sync-agent-skills.sh` drift detection ports cleanly to Dossier,
  doc-web, and CineForge.
- **Methodology conflict**: none found in this slice. The earlier Dossier
  methodology conflict was already resolved by the completed state/graph
  migration.
- **Unclear drift**: none strong enough to justify bulk text sync across the 18
  shared skills.

## Recommendation

- **storybook**: Keep local. Treat it as the current reference implementation
  for skill-sync guardrails.
- **dossier**: Sync partially. Port the stricter
  `scripts/sync-agent-skills.sh` checks, but keep Dossier-native story/eval
  wording in the shared skills.
- **doc-web**: Sync partially. Port the stricter
  `scripts/sync-agent-skills.sh` checks, but keep doc-web's leaf-skill routing
  and decision-source variations local.
- **cine-forge**: Sync partially. Port the stricter
  `scripts/sync-agent-skills.sh` checks, but keep CineForge's
  design/dashboard-aware wording local and do not force its shared skills to
  match the other repos textually.

## Human Decision Needed

- None for the classification pass itself.
- The clean execution scope was: update `scripts/sync-agent-skills.sh` in
  Dossier, doc-web, and CineForge to match Storybook's wrapper-drift checks
  without treating the 18 non-identical shared skills as a bulk text-sync
  project.

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  line remains the alignment record.
- 2026-04-10 execution follow-up: landed the wrapper-drift hardening to target
  `main` branches from dedicated `codex/skill-sync-hardening` worktrees:
  - Dossier: `a6fa9b1`
  - doc-web: `9d046a3`
  - CineForge: `86e298d`
- Those landings kept repo-local shared-skill wording intact and only ported
  the stricter `sync-agent-skills` enforcement, plus the narrow missing
  `user-invocable` declarations required for honest wrapper parity in doc-web
  and CineForge.
