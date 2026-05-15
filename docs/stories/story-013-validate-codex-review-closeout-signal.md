---
title: "Add Codex Review as a Validate Closeout Signal"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:2.1"
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.2"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on:
  - "012"
category_refs:
  - "alignment"
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
  - "dossier"
  - "storybook"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 013 - Add Codex Review as a Validate Closeout Signal

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: Story 012

## Goal

Adapt the useful parts of Peter Steinberger's `codex-review` workflow into
Cam's existing closeout methodology without replacing `/validate` or narrowing
`/loop-verify` into a code-review-only story-closure loop.

The intended behavior is:

- `/validate` remains the essential closure checkpoint.
- `codex review` becomes an extra review signal inside `/validate` for
  non-trivial code diffs when it can materially improve confidence.
- `/loop-verify` keeps its task-shaped role for any bounded verification task
  and only borrows general findings-ledger and clean-stop discipline.
- Target repos receive the same behavior through isolated rollout worktrees,
  with local adaptation preserved.

## Acceptance Criteria

- [x] Scout 032 is revised so the adoption target is `/validate`, with
      `/loop-verify` receiving only task-agnostic finding-disposition and
      clean-stop guidance.
- [x] Conductor's `.agents/skills/validate/SKILL.md` adds `codex review` as an
      extra signal for non-trivial code diffs while keeping `/validate` as the
      final closure authority.
- [x] The validate wording explains when to run or skip `codex review`, how to
      choose `--uncommitted`, `--base`, or `--commit`, and how to handle
      accepted versus rejected findings.
- [x] The validate wording requires focused tests and a fresh review signal
      after accepted review-triggered code fixes.
- [x] Conductor's `.agents/skills/loop-verify/SKILL.md` gains general
      accepted/rejected/follow-up finding ledger and clean-stop guidance
      without turning `/loop-verify` into a story-closure or code-review-only
      skill.
- [x] Alignment memory records the recommendation and target-repo rollout
      evidence.
- [x] All tracked repos receive the validate and loop-verify wording updates in
      isolated worktrees, not in primary checkouts.
- [x] Repo-native checks pass or any pre-existing unrelated warnings are
      recorded explicitly.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Replacing `/validate` with `codex review`.
- Requiring `codex review` for docs-only, scout, alignment, inbox-routing,
  generated-index, tiny obvious patch, or taste/product-validation work.
- Importing Peter's helper script wholesale.
- Treating the helper's `[P0]` through `[P3]` parser as a stable local contract.
- Making `/loop-verify` mean story closure.
- Committing, pushing, or landing target-repo work without an explicit closeout
  request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Update Scout 032 to reflect the validate-first adoption decision
- [x] Update Conductor `/validate`
- [x] Update Conductor `/loop-verify`
- [x] Create alignment memory for the portable recommendation and rollout
- [x] Roll out the skill wording to tracked repos in isolated worktrees
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required; no scripts
        or repo checks changed
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/scout/scout-032-codex-review-loop-verify-enhancements.md` - refine the
  scout decision after the validate-vs-loop-verify discussion.
- `docs/scout.md` - keep the scout index aligned with the refined decision.
- `.agents/skills/validate/SKILL.md` - add `codex review` as an optional
  code-diff closeout signal.
- `.agents/skills/loop-verify/SKILL.md` - add task-agnostic finding ledger and
  clean-stop guidance.
- `docs/alignments/` and `docs/align-projects.md` - record the portable
  alignment and rollout evidence.
- `docs/stories/story-013-validate-codex-review-closeout-signal.md` - story
  source of truth and work log.
- Generated methodology surfaces after compile: `docs/stories.md` and
  `docs/methodology/graph.json`.
- Target repo `.agents/skills/validate/SKILL.md` and
  `.agents/skills/loop-verify/SKILL.md` files, plus generated wrappers or
  methodology surfaces only where local tooling requires them.

## Notes

- Source scout: Scout 032, based on the May 14, 2026 X post and the linked
  `agent-scripts` `codex-review` skill.
- Local CLI evidence: `codex review --help` describes a non-interactive code
  review command with `--uncommitted`, `--base`, and `--commit` targets.
- Alignment 022 already established that findings-first review improves
  `/validate` but does not replace it.
- Alignment 029 already hardened `/loop-verify` against recursion, runaway
  docs loops, and scope expansion. This story must not undo that boundary.

## Plan

Cam approved implementation and target-repo rollout in the same request that
created the story, so this plan is recorded as the implementation gate.

1. Patch Conductor first:
   - revise Scout 032 and its index entry
   - add `codex review` signal guidance to `/validate`
   - add accepted/rejected/follow-up finding ledger and clean-stop guidance to
     `/loop-verify`
   - add an alignment record for the portable recommendation
2. Regenerate Conductor methodology surfaces and run local checks.
3. Inspect target repo primary checkout state.
4. Create isolated target worktrees from current `origin/main` where possible
   on branch `codex/validate-codex-review-signal`.
5. Apply the same behavior to each repo's `/validate` and `/loop-verify`,
   preserving repo-local wording and check commands.
6. Run each repo's native skill/methodology checks plus `git diff --check`.
7. Update the story work log and alignment evidence with the final per-repo
   results.

## Work Log

20260515-0000 - story-created: created Story 013 from Scout 032 and Cam's
decision that `codex review` belongs in `/validate`, while `/loop-verify` should
only borrow task-agnostic finding-disposition and clean-stop discipline. Cam
explicitly approved starting the story and rolling the change out to all
tracked repos.

20260515-0909 - build complete: revised Scout 032, added Alignment 030, patched
Conductor `/validate` and `/loop-verify`, regenerated Conductor methodology
surfaces, and rolled the same behavior into all seven tracked repos using
isolated worktrees under
`/Users/cam/.codex/worktrees/validate-codex-review-signal/` on branch
`codex/validate-codex-review-signal-20260515`.

Conductor checks passed: `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`,
`PYTHONDONTWRITEBYTECODE=1 make skills-check`, and `git diff --check`.

Target repo evidence:

| Project | Base | Changed files | Checks |
| --- | --- | --- | --- |
| Dossier | `0f22845` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 PYTHON='uv run --frozen python' make methodology-check`, and `git diff --check` passed. Methodology check reported existing legacy/non-local metadata warnings. |
| Storybook | `377bcf6` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md`, `docs/methodology/graph.json`, `docs/stories.md` | `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. |
| doc-web | `c0075f5` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 make methodology-check`, and `git diff --check` passed. |
| CineForge | `4bfedb5` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md`, `docs/build-map.md`, `docs/methodology/graph.json`, `docs/stories.md` | `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. Methodology check still reports existing architecture-audit and UI-scout freshness warnings. |
| Board Game Ingester | `d00c742` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 make methodology-check`, `PYTHONDONTWRITEBYTECODE=1 make lint`, and `git diff --check` passed. |
| Robo Rally | `e463af7` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md` | `./scripts/sync-agent-skills.sh --check`, `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |
| Echo Forge | `68bfff8` | `.agents/skills/validate/SKILL.md`, `.agents/skills/loop-verify/SKILL.md` | `./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, and `git diff --check` passed. Methodology check reported existing `No Ideal requirements parsed` warning. |

Primary target checkouts were inspected before rollout. Storybook, CineForge,
and Echo Forge had unrelated dirty files; Board Game Ingester was on a feature
branch. The rollout kept those live workspaces untouched.

Next step: run `/mark-story-done 013` before any check-in or push.

20260515-0922 - loop-verify validation pass: ran `/loop-verify` in docs/ADR
alignment mode with four find-only worker shards: Conductor skill semantics,
target repo skill rollout, scout/alignment/generated surfaces, and worktree
hygiene. Three shards returned `RESULT: no-issue`. The worktree-hygiene shard
returned `RESULT: blocked` because the Conductor worktree also contains Scout
031 (`docs/scout/scout-031-openclaw-fs-safe-filesystem-primitives.md` plus its
`docs/scout.md` index entry) from the earlier fs-safe scout. Accepted finding:
Story 013 evidence should not imply every current Conductor diff belongs to
this rollout. Disposition: Scout 031 is a separate prior routed scout, not part
of Story 013; it should be included in a later check-in only as separate
intended scout work, not as validate/codex-review rollout evidence.

20260515-0928 - validation complete: Story 013 acceptance criteria are met. The
loop-verify pass produced one accepted scope/evidence finding and no
behavioral-methodology defects; the accepted finding was fixed by recording the
Scout 031 worktree boundary above. `codex review` was skipped because the
current Story 013 diff changes docs, skills, generated methodology outputs, and
scout/alignment records rather than non-trivial application code. Fresh
Conductor checks passed after the fix: methodology compile, methodology check,
lint, skills check, and `git diff --check`. Closure recommendation: close now
after `/mark-story-done`.

20260515-0940 - story done: target repo rollout landed on each target `main`
branch before Conductor closeout:

| Project | Commit |
| --- | --- |
| Dossier | `8babd53` |
| Storybook | `0741e13` |
| doc-web | `8ebe99b` |
| CineForge | `700a429` |
| Board Game Ingester | `c67b2a1` |
| Robo Rally | `7b7006c` |
| Echo Forge | `4dcdb84` |

Marked Story 013 done after current validation, target rollout landing, and
fresh Conductor checks.
