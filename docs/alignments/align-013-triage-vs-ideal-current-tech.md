# Alignment 013 — Triage Vs-Ideal Current-Tech Calibration

**Date**: 2026-04-17
**Focus**: Evaluate Dossier's new triage framing for Ideal distance under
current technology limits and whether it should sync into other tracked product
repos
**Source Project**: `dossier`
**Target Projects**: `doc-web`, `storybook`, `cine-forge`

## Surfaces Compared

- Dossier `.agents/skills/triage/SKILL.md`
- doc-web `.agents/skills/triage/SKILL.md`
- Storybook `.agents/skills/triage/SKILL.md`
- CineForge `.agents/skills/triage/SKILL.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the goal is to carry over useful supervisory meaning, not to force
  textual identity.
- Alignment 005 spread stronger actionability metadata, and Alignment 007
  spread phase-pressure defaults. Dossier's newer update adds a different layer
  of judgment: triage should say not only what the biggest gap is, but how far
  the repo is from the literal Ideal versus a strong present-day version that
  today’s tools can actually support.
- No narrower decision record was found for Ideal-distance calibration or
  current-tech framing in product-repo triage output.

## Key Differences

- Dossier now asks triage to answer an extra question up front: how close is
  the project to the Ideal on today's technology, not just against the literal
  north-star?
- Dossier also adds a compact `Vs Ideal` output section that separates:
  - literal north-star distance
  - current-tech progress
  - direction of travel
- doc-web, Storybook, and CineForge already identify the primary gap and next
  action, but they do not yet make the same explicit distinction between an
  impossible-perfect Ideal and a strong present-day read.
- That missing distinction matters because product repos can otherwise sound
  flatter or harsher than the evidence justifies: they may report a large gap
  without making clear whether the remaining distance is due to repo mistakes or
  current model/tool limits.
- The portable improvement is the calibration behavior and compact reporting
  contract, not Dossier's exact prose or the rest of its full-sweep ordering.

## Classification

- **Portable improvement**: teach triage to separate literal Ideal distance
  from current-tech progress and report that calibration explicitly.
- **Intentional adaptation**: keep each repo's existing local lanes, output
  template, and domain-specific evidence surfaces.
- **Methodology conflict**: none found in this slice.
- **Unclear drift**: none strong enough to block a targeted sync.

## Recommendation

- **doc-web**: Sync partially. Add the current-tech versus north-star
  calibration so large methodology gaps can be reported without overstating
  repo-local failure when platform limits are the real constraint.
- **storybook**: Sync partially. Add the same compact `Vs Ideal` framing while
  preserving Storybook's architecture and `ui-scout` surfaces.
- **cine-forge**: Sync partially. Add the same compact `Vs Ideal` framing while
  preserving CineForge's architecture/dashboard context and report shape.

## Human Decision Needed

- None for the classification pass itself.
- The executed rollout stayed narrow: triage framing/output only, not a
  broader rewrite of each repo's methodology stack.

## Result

- Prepared dedicated target-repo worktrees on branch
  `codex/triage-vs-ideal-current-tech`:
  - doc-web: `/Users/cam/.codex/worktrees/triage-vs-ideal-current-tech/doc-web`
  - Storybook: `/Users/cam/.codex/worktrees/triage-vs-ideal-current-tech/storybook`
  - CineForge: `/Users/cam/.codex/worktrees/triage-vs-ideal-current-tech/cine-forge`
- Applied the `Vs Ideal` carry-through in each target repo's local task
  worktree:
  - doc-web: updated `.agents/skills/triage/SKILL.md`
  - Storybook: updated `.agents/skills/triage/SKILL.md`
  - CineForge: updated `.agents/skills/triage/SKILL.md`
- The rollout preserved repo-local differences while adding the shared
  calibration behavior:
  - triage now asks how close the repo/project is to the Ideal on today's
    technology, not just against the literal north-star
  - full-sweep mode now includes a compact `Vs Ideal` calibration step
  - the report contract now includes `Literal north-star`, `Current-tech read`,
    and `Direction`
- Verified the target patches with repo-local checks:
  - doc-web: `./scripts/sync-agent-skills.sh`, `./scripts/sync-agent-skills.sh --check`, `make methodology-check`, `git diff --check`
  - Storybook: `./scripts/sync-agent-skills.sh`, `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`, `git diff --check`
  - CineForge: `./scripts/sync-agent-skills.sh`, `./scripts/sync-agent-skills.sh --check`, `git diff --check`
- Committed the target patches in their dedicated worktrees:
  - doc-web: `c5000dd` (`Add triage vs-ideal calibration`)
  - Storybook: `d4bc305` (`Add triage vs-ideal calibration`)
  - CineForge: `b742f6a` (`Add triage vs-ideal calibration`)
- Pushed the `codex/triage-vs-ideal-current-tech` branches to `origin` for all
  three target repos.
- Opened draft PRs for review:
  - doc-web: `https://github.com/copperdogma/doc-web/pull/1`
  - Storybook: `https://github.com/copperdogma/storybook/pull/13`
  - CineForge: `https://github.com/copperdogma/cine-forge/pull/1`
- 2026-04-18 merge follow-up: merged the draft PRs onto the target `main`
  branches:
  - doc-web: PR `#1`, merge commit `bb15757`
  - Storybook: PR `#13`, merge commit `716ec9b`
  - CineForge: PR `#1`, merge commit `60d70a5`
- CineForge verification caveat:
  - `pnpm methodology:check` failed in the fresh task worktree because
    `docs/build-map.md` is out of date on the current repo baseline and the
    check asks for `pnpm methodology:compile`; this was left untouched to avoid
    expanding this triage-only rollout into an unrelated generated-surface
    refresh.

## Follow-Up

- No Conductor story was created.
- Conductor itself is not a sync target for this pass.
- The target-repo patches are now landed on their `main` branches.
- Supervisor memory now captures both the comparison and the active PR-backed
  rollout plus the final merge state, so future closeout work can start from
  the landed `main` tips rather than reconstructing the patch set.
