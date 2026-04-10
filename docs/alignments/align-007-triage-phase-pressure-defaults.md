# Alignment 007 — Triage Phase Pressure Defaults

**Date**: 2026-04-10
**Focus**: Port doc-web's phase-driven triage follow-up so methodology phase
creates default action pressure instead of drifting toward false `no-op`
recommendations
**Source Project**: `doc-web`
**Target Projects**: `dossier`, `storybook`, `cine-forge`

## Surfaces Compared

- doc-web commit `0d258aa`
- doc-web `.agents/skills/triage/SKILL.md`
- doc-web `.agents/skills/triage-stories/SKILL.md`
- doc-web `.agents/skills/triage-evals/SKILL.md`
- Dossier `.agents/skills/triage/SKILL.md`
- Dossier `.agents/skills/triage-stories/SKILL.md`
- Dossier `.agents/skills/triage-evals/SKILL.md`
- Storybook `.agents/skills/triage/SKILL.md`
- Storybook `.agents/skills/triage-stories/SKILL.md`
- Storybook `.agents/skills/triage-evals/SKILL.md`
- CineForge `.agents/skills/triage/SKILL.md`
- CineForge `.agents/skills/triage-stories/SKILL.md`
- CineForge `.agents/skills/triage-evals/SKILL.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the sync target is shared triage meaning, not exact file identity.
- Alignment 005 already spread the compiled actionability model across the
  tracked product repos. doc-web commit `0d258aa` is the next-layer follow-up:
  phase itself now creates default pressure to pick a bounded move instead of
  treating missing novelty as a reason to stall.
- Dossier, Storybook, and CineForge already had some blocker / exhausted-retry
  honesty, but they did not all say the same thing when the repo still had a
  live `converge`, `climb`, or meaningful `hold` line with no fresh external
  prompt.
- Conductor itself is not a sync target for this pass. The change belongs to
  the tracked product repos' triage package, not to the supervisor loop.

## Key Differences

- doc-web now explicitly:
  - inserts an `Apply phase-pressure defaults` step into `/triage`
  - treats `converge`, `climb`, and `hold` as default action pressure, not
    tie-break metadata
  - warns that `no-op` is only honest when every plausible phase-aligned move
    is blocked, exhausted, or lacks a bounded falsifiable next step
  - tells `/triage-stories` not to call the backlog effectively empty when the
    methodology state still has pressure but no story shell
  - tells `/triage-evals` that phase alone can justify a bounded proof refresh
    or experiment
- Dossier already had the strongest methodology-first ordering and compiled
  actionability reads, but it still lacked explicit phase-default pressure in
  the triage-family skills.
- Storybook and CineForge both had local extensions that needed to stay local:
  Storybook keeps the architecture and `ui-scout` cadence lanes plus direct
  yes/no handoff formatting; CineForge keeps its own architecture / dashboard
  framing and expected-fail eval language.
- The portable improvement is the phase-pressure contract and anti-false-`no-op`
  guidance across `triage`, `triage-stories`, and `triage-evals`, not a literal
  copy of doc-web's wording or report shapes.

## Classification

- **Portable improvement**: teach the triage family that methodology phase
  creates default pressure for the next bounded move, even without a fresh bug
  report, inbox item, or product prompt.
- **Intentional adaptation**: keep each repo's own architecture lane,
  `ui-scout` references, output contract, and helper-script wording.
- **Methodology conflict**: none in this slice once the sync is framed as a
  policy carry-through instead of a literal file transplant.
- **Unclear drift**: none strong enough to justify holding the sync.

## Recommendation

- **dossier**: Sync partially. Add phase-pressure defaults to `/triage`,
  backlog-shell pressure to `/triage-stories`, and bounded phase-aware
  anti-`no action` guidance to `/triage-evals`.
- **storybook**: Sync partially. Add the same pressure defaults while keeping
  Storybook's architecture lane, `ui-scout` lane, and default yes/no handoff
  surface intact.
- **cine-forge**: Sync partially. Add the same pressure defaults while keeping
  CineForge's local architecture framing, health-flag language, and expected-fail
  eval context intact.

## Result

- Prepared dedicated target-repo worktrees on branch
  `codex/triage-phase-pressure-defaults`:
  - Dossier: `/Users/cam/.codex/worktrees/triage-phase-pressure-defaults/dossier`
  - Storybook: `/Users/cam/.codex/worktrees/triage-phase-pressure-defaults/storybook`
  - CineForge: `/Users/cam/.codex/worktrees/triage-phase-pressure-defaults/cine-forge`
- Applied the phase-pressure sync inside each target repo's local task
  worktree:
  - Dossier: updated `.agents/skills/triage/SKILL.md`,
    `.agents/skills/triage-stories/SKILL.md`, and
    `.agents/skills/triage-evals/SKILL.md`
  - Storybook: updated `.agents/skills/triage/SKILL.md`,
    `.agents/skills/triage-stories/SKILL.md`, and
    `.agents/skills/triage-evals/SKILL.md`
  - CineForge: updated `.agents/skills/triage/SKILL.md`,
    `.agents/skills/triage-stories/SKILL.md`, and
    `.agents/skills/triage-evals/SKILL.md`
- Verified the target patches with repo-local checks:
  - Dossier: `./scripts/sync-agent-skills.sh`,
    `./scripts/sync-agent-skills.sh --check`,
    `make methodology-check PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python`
  - Storybook: `./scripts/sync-agent-skills.sh`,
    `./scripts/sync-agent-skills.sh --check`,
    `pnpm methodology:check`
  - CineForge: `./scripts/sync-agent-skills.sh`,
    `./scripts/sync-agent-skills.sh --check`,
    `pnpm methodology:check`
- Existing non-blocking warnings remained present in validation:
  - Dossier methodology check still reports its pre-existing non-local ADR /
    legacy-metadata warnings
  - CineForge's final post-rebase methodology check reported no new warnings;
    the earlier pre-landing `ui_scout` freshness warning did not persist on the
    landed tip

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  line is the alignment record plus the prepared target-repo patches.
- Conductor itself was not a sync target for this pass. The change belongs to
  the tracked product repos' methodology package, not to the supervisor loop.
