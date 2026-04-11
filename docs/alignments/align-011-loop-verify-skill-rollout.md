# Alignment 011 — Loop Verify Skill Rollout

**Date**: 2026-04-11
**Focus**: Compare the new shared `loop-verify` skill against the tracked
project skill surfaces and decide whether it should roll out portfolio-wide
**Source Project**: Conductor `loop-verify` skill baseline
**Target Projects**: `dossier`, `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- Conductor `.agents/skills/loop-verify/SKILL.md`
- Dossier `.agents/skills/`
- Storybook `.agents/skills/`
- doc-web `.agents/skills/`
- CineForge `.agents/skills/`
- Shared `scripts/sync-agent-skills.sh` behavior in all four target repos

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: this should align reusable workflow meaning, not force text sync for
  its own sake.
- Alignment 004 already established that the tracked repos share the same
  invocable-skill and Gemini-wrapper sync substrate, so a new shared skill can
  roll out without additional tooling changes if the skill itself is portable.
- The user explicitly requested portfolio rollout after the Conductor-local
  skill was drafted and checked.
- No narrower decision record was found that would make repeated
  delegation-loop verification a repo-specific methodology lane.

## Key Differences

- None of the four tracked target repos currently include
  `.agents/skills/loop-verify/SKILL.md`.
- All four target repos already share compatible local-skill layout and
  wrapper-generation behavior:
  - canonical skills under `.agents/skills/`
  - `user-invocable` frontmatter as the wrapper-generation gate
  - generated Gemini command wrappers under `.gemini/commands/`
- Storybook's primary checkout currently has unrelated local modifications, and
  CineForge's primary checkout currently has unrelated untracked local files, so
  in-place edits there would violate the shared-workspace guardrail.
- The skill itself is methodology-shaped rather than product-shaped: bounded
  sharding, parallel worker ownership, full-round reruns after any real fix,
  and clean-stop only after an entirely clean round. Those rules are portable
  across all four targets.

## Classification

- **Portable improvement**: the `loop-verify` skill is a reusable coordination
  pattern that fits the shared local-skill surface across all four target
  repos.
- **Intentional adaptation**: none required in the initial rollout; the current
  Conductor wording is generic enough to travel as-is.
- **Methodology conflict**: none found. The skill complements each repo's
  existing subagent guidance rather than replacing it.
- **Unclear drift**: none strong enough to block rollout.

## Recommendation

- **dossier**: Sync now. Add `loop-verify` to the shared skill surface and
  regenerate wrappers.
- **storybook**: Sync now, but only from a dedicated worktree because the
  primary checkout is already dirty.
- **doc-web**: Sync now. Add `loop-verify` to the shared skill surface and
  regenerate wrappers.
- **cine-forge**: Sync now, but only from a dedicated worktree because the
  primary checkout has unrelated untracked files.

## Human Decision Needed

- None for the classification pass itself.
- The requested execution scope is narrow: add the shared skill and regenerate
  wrappers only. Do not broaden this into other methodology edits.

## Result

- Prepared dedicated target-repo worktrees on branch
  `codex/loop-verify-rollout`:
  - Dossier: `/Users/cam/.codex/worktrees/loop-verify-rollout/dossier`
  - Storybook: `/Users/cam/.codex/worktrees/loop-verify-rollout/storybook`
  - doc-web: `/Users/cam/.codex/worktrees/loop-verify-rollout/doc-web`
  - CineForge: `/Users/cam/.codex/worktrees/loop-verify-rollout/cine-forge`
- Applied the shared skill rollout in each target repo:
  - added `.agents/skills/loop-verify/SKILL.md`
  - regenerated `.gemini/commands/loop-verify.toml`
- Verified each target patch with fresh repo-local wrapper checks:
  - Dossier: `./scripts/sync-agent-skills.sh --check`
  - Storybook: `./scripts/sync-agent-skills.sh --check`
  - doc-web: `./scripts/sync-agent-skills.sh --check`
  - CineForge: `./scripts/sync-agent-skills.sh --check`
- Landed the validated target branches onto remote `main`:
  - Dossier: `a9fd1f1` (`Add loop-verify skill`)
  - Storybook: `f74df2e` (`Add loop-verify skill`)
  - doc-web: `7a3b721` (`Add loop-verify skill`)
  - CineForge: `3ffe492` (`Add loop-verify skill`)
- The target rollout worktrees remain in place on `codex/loop-verify-rollout`
  because cleanup was not requested.

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  line is the alignment record plus the target-repo patches.
