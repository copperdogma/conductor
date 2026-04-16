# Alignment 002 — Inbox Check-In Landing Guardrail

**Date**: 2026-04-10
**Focus**: Close-out workflow parity for landing inbox capture
**Source Project**: `conductor`
**Target Projects**: `dossier`, `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- Conductor `.agents/skills/check-in/SKILL.md`
- Conductor `.agents/skills/finish-and-push/SKILL.md`
- Dossier `.agents/skills/check-in-diff/SKILL.md`
- Dossier `.agents/skills/finish-and-push/SKILL.md`
- Storybook `.agents/skills/check-in-diff/SKILL.md`
- Storybook `.agents/skills/finish-and-push/SKILL.md`
- doc-web `.agents/skills/check-in-diff/SKILL.md`
- doc-web `.agents/skills/finish-and-push/SKILL.md`
- CineForge `.agents/skills/check-in-diff/SKILL.md`
- CineForge `.agents/skills/finish-and-push/SKILL.md`

## Key Differences

- Conductor already taught its close-out flow to treat `inbox.md` as normal
  user capture that should ride along with the landing by default. The tracked
  product repos did not yet teach the equivalent rule for `docs/inbox.md`.
- The portable behavior is semantic, not textual: Conductor lands root
  `inbox.md`, while the tracked product repos land `docs/inbox.md`.
- The check-in entrypoints differ by repo (`/check-in` in Conductor versus
  `/check-in-diff` elsewhere), and each repo keeps its own validation commands,
  but the inbox-capture rule ports cleanly across all four tracked repos.

## Classification

- **Portable improvement**: close-out skills should treat inbox capture as
  expected operator input and stage it with the validated landing set unless the
  user explicitly excludes it.
- **Intentional adaptation**: keep repo-local inbox paths and validation
  commands. Do not force text identity between Conductor and the tracked repos.
- **Methodology conflict**: none. [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies as the governing supervisor constraint; no narrower decision record
  was found for this workflow detail.
- **Unclear drift**: none found in the compared close-out surfaces.

## Result

- Prepared dedicated task branches/worktrees for each tracked repo:
  `codex/inbox-checkin-landing`
- Updated each repo's `/check-in-diff` prompt to:
  - treat `docs/inbox.md` edits as expected user capture during audit
  - stage `docs/inbox.md` by default when it belongs to the validated landing set
  - avoid treating `docs/inbox.md` as dirty-worktree drift unless the user says
    to leave it out
- Updated each repo's `/finish-and-push` prompt to:
  - treat `docs/inbox.md` edits as normal close-out input
  - exclude those inbox edits from the "unrelated changes" blocker class
  - keep them in the landing set by default unless the user says otherwise
- Regenerated cross-CLI skill wrappers in each repo with
  `./scripts/sync-agent-skills.sh`
- Verified wrapper parity with:
  - Dossier: `make skills-check`
  - Storybook: `./scripts/sync-agent-skills.sh --check`
  - doc-web: `make skills-check`
  - CineForge: `make skills-check`
- Landed the validated branch tip onto each target repo's `main`:
  - Dossier: `f7f82d7`
  - Storybook: `9241441` after rebasing the task branch onto current
    `origin/main` and resolving the resulting `CHANGELOG.md` conflict
  - doc-web: `218ae08`
  - CineForge: `ff82e9d`

## Follow-Up

- 2026-04-16 verification follow-up: checked the current dedicated
  `codex/inbox-checkin-landing` worktree tip commits against target `main`
  branches and confirmed they are already merged:
  - Dossier: `f7f82d7`
  - Storybook: `9241441`
  - doc-web: current worktree tip `daaf848` is an ancestor of `main`; the
    original alignment landing commit remains `218ae08`
  - CineForge: `ff82e9d`
- 2026-04-16 cleanup follow-up: removed the dedicated local
  `codex/inbox-checkin-landing` worktrees after verification. The local
  worktree cleanup for this line is complete.
- 2026-04-16 branch cleanup follow-up: deleted the merged local
  `codex/inbox-checkin-landing` branches after confirming no remaining
  worktree still had them checked out.
- Supervisor memory for this line is current; no further local worktree or
  merged-branch cleanup is pending.
