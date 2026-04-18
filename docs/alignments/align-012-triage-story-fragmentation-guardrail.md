# Alignment 012 — Triage Story Fragmentation Guardrail

**Date**: 2026-04-17
**Focus**: Evaluate doc-web's anti-fragmentation triage update and whether it
should sync into other tracked product repos
**Source Project**: `doc-web`
**Target Projects**: `dossier`, `storybook`, `cine-forge`

## Surfaces Compared

- doc-web `.agents/skills/triage/SKILL.md`
- Dossier `.agents/skills/triage/SKILL.md`
- Storybook `.agents/skills/triage/SKILL.md`
- CineForge `.agents/skills/triage/SKILL.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the sync target is shared triage meaning, not exact file identity.
- Alignment 005 already spread compiled actionability reasoning across the
  tracked product repos, and Alignment 007 already spread phase-pressure
  defaults. doc-web's newer change is a narrower follow-up: do not let those
  stronger signals trick triage into minting a fresh story shell when the real
  work is still the same line.
- No narrower decision record was found for story-shell fragmentation,
  same-line consolidation, or anti-fragmentation review in the triage family.

## Key Differences

- doc-web now treats compiled actionability as a strong signal but not
  automatic permission to recommend a new story. It explicitly says a
  `Pending` or `recommended_now` story can still be the wrong vehicle if it is
  a same-line fragment.
- doc-web also adds a pre-create-story guardrail: before recommending a new
  story, compare it against the last 2-4 stories on the same problem line and
  prefer `continue`, `expand`, `reopen`, or `consolidate` when the subsystem,
  validation boundary, and operator-facing outcome are still effectively the
  same.
- Dossier already has stronger continuity language than the other repos, but it
  does not yet teach the same explicit anti-fragmentation review step or the
  same-line story challenge against recent history.
- Storybook and CineForge already prefer continuity over novelty in some cases,
  but they still do not name story-shell fragmentation as a first-class risk in
  the same way doc-web now does.
- The portable improvement is the anti-fragmentation decision rule, not
  doc-web's exact report shape, leaf-sweep structure, or wording.

## Classification

- **Portable improvement**: teach triage to challenge new-story recommendations
  against recent same-line work and prefer continuation/consolidation when the
  real work boundary has not changed.
- **Intentional adaptation**: preserve each repo's own report format, local
  lanes, and domain-specific sweep surfaces.
- **Methodology conflict**: none found in this slice.
- **Unclear drift**: none strong enough to block the recommendation.

## Recommendation

- **dossier**: Sync partially. Keep Dossier's richer Ideal calibration and
  why-now framing, but add the explicit same-line anti-fragmentation review
  before recommending a new story shell.
- **storybook**: Sync partially. Add the same anti-fragmentation rule while
  keeping Storybook's architecture and `ui-scout` lanes plus its yes/no
  handoff shape.
- **cine-forge**: Sync partially. Add the same anti-fragmentation rule while
  keeping CineForge's architecture/dashboard framing and local wording.

## Human Decision Needed

- None for the classification pass itself.
- The executed rollout stayed narrow: update the triage skill behavior only,
  not the broader story taxonomy or repo-local output templates.

## Result

- Prepared dedicated target-repo worktrees on branch
  `codex/triage-story-fragmentation-guardrail`:
  - Dossier: `/Users/cam/.codex/worktrees/triage-story-fragmentation-guardrail/dossier`
  - Storybook: `/Users/cam/.codex/worktrees/triage-story-fragmentation-guardrail/storybook`
  - CineForge: `/Users/cam/.codex/worktrees/triage-story-fragmentation-guardrail/cine-forge`
- Applied the anti-fragmentation triage carry-through in each target repo's
  local task worktree:
  - Dossier: updated `.agents/skills/triage/SKILL.md`
  - Storybook: updated `.agents/skills/triage/SKILL.md`
  - CineForge: updated `.agents/skills/triage/SKILL.md`
- The rollout preserved repo-local differences while adding the shared guardrail:
  - explicit challenge against the last 2-4 same-line stories before creating
    a new story shell
  - preference for `continue`, `expand`, `reopen`, or `consolidate` when the
    subsystem, validation boundary, and operator-facing outcome are still
    materially the same
  - guardrail wording that blocks story-shell fragmentation from later-state
    progression, truth-surface codification, or container/input permutations
    that do not materially change the work boundary
- Verified the target patches with repo-local checks:
  - Dossier: `./scripts/sync-agent-skills.sh`, `./scripts/sync-agent-skills.sh --check`, `git diff --check`
  - Storybook: `./scripts/sync-agent-skills.sh`, `./scripts/sync-agent-skills.sh --check`, `git diff --check`
  - CineForge: `./scripts/sync-agent-skills.sh`, `./scripts/sync-agent-skills.sh --check`, `git diff --check`
- Committed the target patches in their dedicated worktrees:
  - Dossier: `6897dea` (`Add triage anti-fragmentation guardrail`)
  - Storybook: `f300ba8` (`Add triage anti-fragmentation guardrail`)
  - CineForge: `63864b7` (`Add triage anti-fragmentation guardrail`)
- Pushed the `codex/triage-story-fragmentation-guardrail` branches to `origin`
  for all three target repos.
- Opened draft PRs for review:
  - Dossier: `https://github.com/copperdogma/dossier/pull/2`
  - Storybook: `https://github.com/copperdogma/storybook/pull/14`
  - CineForge: `https://github.com/copperdogma/cine-forge/pull/2`
- 2026-04-18 merge follow-up: merged the draft PRs onto the target `main`
  branches:
  - Dossier: PR `#2`, merge commit `def5804`
  - Storybook: PR `#14`, merge commit `cedf922`
  - CineForge: PR `#2`, merge commit `549f41e`

## Follow-Up

- No Conductor story was created.
- Conductor itself is not a sync target for this pass.
- The target-repo patches are now landed on their `main` branches.
- Supervisor memory now captures both the comparison and the active PR-backed
  rollout plus the final merge state, so future closeout work can start from
  the landed `main` tips rather than reconstructing the patch set.
