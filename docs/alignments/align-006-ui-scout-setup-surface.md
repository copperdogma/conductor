# Alignment 006 — UI Scout Setup Surface

**Date**: 2026-04-10
**Focus**: Compare the new internal `ui-scout` lane against
`setup-methodology` surfaces and decide whether it belongs in the shared setup
package
**Source Project**: Baseline across `storybook`, `cine-forge`, `dossier`, and
`doc-web`
**Target Projects**: `storybook`, `cine-forge`, `dossier`, `doc-web`

## Surfaces Compared

- Storybook `AGENTS.md`
- Storybook `.agents/skills/triage/SKILL.md`
- Storybook `.agents/skills/setup-methodology/SKILL.md`
- Storybook `.agents/skills/setup-methodology/templates/setup-checklist.md`
- Storybook `docs/runbooks/setup-methodology.md`
- Storybook `docs/runbooks/ui-scout.md`
- Storybook `docs/ui-scout.md`
- Storybook `docs/methodology/state.yaml`
- CineForge `AGENTS.md`
- CineForge `.agents/skills/triage/SKILL.md`
- CineForge `.agents/skills/setup-methodology/SKILL.md`
- CineForge `.agents/skills/setup-methodology/templates/setup-checklist.md`
- CineForge `docs/runbooks/setup-methodology.md`
- CineForge `docs/runbooks/full-pipeline-ui-manual-walkthrough.md`
- CineForge `docs/ui-scout.md`
- CineForge `docs/methodology/state.yaml`
- Dossier `AGENTS.md`
- Dossier `.agents/skills/setup-methodology/SKILL.md`
- Dossier `.agents/skills/setup-methodology/templates/setup-checklist.md`
- Dossier `docs/runbooks/setup-methodology.md`
- doc-web `AGENTS.md`
- doc-web `.agents/skills/setup-methodology/SKILL.md`
- doc-web `.agents/skills/setup-methodology/templates/setup-checklist.md`
- doc-web `docs/runbooks/setup-methodology.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the goal is to align the meaning of the setup package, not to force
  exact file identity across every repo.
- No narrower Conductor decision record was found for `ui-scout` or for how
  optional methodology lanes should appear in `setup-methodology`.
- Storybook and CineForge already treat internal UI product-truth scouting as a
  real methodology signal: AGENTS routes qualitative UX questions there, triage
  reads `state.ui_scout`, and the lane has its own runbook plus persistent
  history under `docs/ui-scout/`.
- Dossier and doc-web currently have no `docs/ui-scout.md` lane and no
  matching AGENTS or setup-surface references, so a universal sync would
  overreach the evidence.

## Key Differences

- Storybook and CineForge both wire `ui-scout` into their live methodology
  package after bootstrap:
  - AGENTS quick-routing sends qualitative UX freshness questions to the local
    `ui-scout` lane
  - triage always checks `state.ui_scout` before deciding whether a fresh scout
    run or follow-up story is the right next action
  - `docs/methodology/state.yaml` persists freshness cadence and follow-up story
    links for the lane
  - repo-local runbooks and `docs/ui-scout.md` define the scenario set and
    evidence contract
- Yet neither repo's `setup-methodology` skill, runbook, or checklist says what
  to do when a repo has that lane. Their setup surfaces enumerate methodology
  docs, state/graph, eval/golden bootstrap, story wiring, AGENTS wiring, and
  skill sync, but omit `ui-scout` entirely.
- Storybook already has one setup-surface precedent for optional methodology
  lanes: its checklist and skill explicitly mention `architecture_audits` /
  `/triage-architecture` only when that lane is part of the package. `ui-scout`
  lacks the same optional-module treatment.
- The lane itself is intentionally product-specific:
  - Storybook uses four canonical scenarios centered on onboarding, Home,
    artifact review, and knowledge correction
  - CineForge uses one full-pipeline fixture plus desktop/mobile spot-checks
- Dossier and doc-web have no corresponding `ui-scout` surface today, which
  makes their absence a current intentional adaptation rather than unexplained
  drift.

## Classification

- **Portable improvement**: teach `setup-methodology` to preserve or install an
  optional `ui-scout` lane when a repo's methodology state, AGENTS wiring, and
  triage contract already depend on it.
- **Intentional adaptation**: keep each repo's own `ui-scout` scenario set,
  cadence, runbook name, evidence shape, and product-language framing.
- **Methodology conflict**: none once the change is framed as an optional
  UI-only module instead of a mandatory bootstrap surface for every repo.
- **Unclear drift**: none strong enough to justify adding `ui-scout` to Dossier
  or doc-web right now.

## Recommendation

- **storybook**: Sync partially. Update `setup-methodology` skill, runbook, and
  checklist so they document `ui-scout` as an optional recurring lane when
  `state.ui_scout` and the supporting docs already exist. Keep Storybook's
  four-scenario structure and warm-product-language local.
- **cine-forge**: Sync partially. Update `setup-methodology` skill, runbook,
  and checklist so they mention the optional `ui-scout` lane for UI-heavy
  repos. Keep the full-pipeline walkthrough, fixture choice, and mobile
  spot-check contract local.
- **dossier**: Keep local. No current `ui-scout` lane exists, so do not add
  setup-surface boilerplate for it by default.
- **doc-web**: Keep local. No current `ui-scout` lane or AGENTS routing exists,
  so do not install the lane just for surface symmetry.

## Human Decision Needed

- None for the classification pass itself.
- If execution is desired, the narrow scope is to update Storybook and
  CineForge `setup-methodology` surfaces so `ui-scout` is documented as an
  optional installed lane when present, not as a required baseline for all
  repos.

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  question is the alignment record.
- Conductor itself is not a sync target for this pass; `ui-scout` is a
  tracked-project product-methodology lane rather than a supervisor workflow.
