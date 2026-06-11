---
title: "Cost-Aware Delegation Rollout"
status: "In Progress"
priority: "High"
ideal_refs: ["I1", "I2", "I3", "I4", "I5"]
spec_refs: ["spec:2.2", "spec:4.2", "spec:5.1", "spec:5.3"]
decision_refs: ["Alignment 041"]
depends_on: []
category_refs: ["alignment", "story-prep", "memory"]
tracked_projects:
  - conductor
  - dossier
  - storybook
  - doc-web
  - cine-forge
  - boardgame-ingester
  - roborally
  - echo-forge
---

# Story 026 — Cost-Aware Delegation Rollout

**Priority**: High
**Status**: In Progress
**Decision Refs**: Alignment 041
**Depends On**: None

## Goal

Roll Alignment 041's model-name-free cost-aware delegation policy into the
tracked project repos that have suitable validate, check-in, finish/push,
deploy, loop-verify, or skill-surface-audit style surfaces.

The result should let future agents downshift mechanical sidecars when that is
honest for the shard, while leaving scope, judgment, commits, pushes, deploy
decisions, rollback decisions, security judgment, and eval correctness with the
main thread.

## Acceptance Criteria

- [x] Each tracked target repo is inspected in a dedicated worktree before
      editing, with local dirty primary checkouts left untouched.
- [x] Repo-local instruction and skill surfaces receive small, model-name-free
      guidance only where delegation is already appropriate.
- [x] No target repo guidance names or hard-codes a specific model.
- [x] Target repo validation commands run and are recorded per repo, or a
      precise blocker/defer reason is recorded.
- [x] Conductor alignment/story surfaces record what changed, what stayed local,
      and what still needs human or repo-specific follow-up.

## Out of Scope

- Changing runtime model defaults, provider config, or tool APIs.
- Adding new deploy behavior, validation scripts, or subagent automation.
- Editing target project primary checkouts.
- Committing, pushing, or landing target repo branches without a separate
  explicit request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Use `/loop-verify` in docs/ADR alignment mode for target surface
      inventory and rollout-risk review
- [x] Create isolated target worktrees/branches for each repo that needs edits
- [x] Implement the needed AGENTS/skill guidance changes in target repos
- [x] Update related alignment memory with per-repo results
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
- [x] Search docs and update any related surfaces
- [ ] Verify Conductor tenets:
  - [ ] I1 — Meaning over text
  - [ ] I2 — Distributed ownership
  - [ ] I3 — Recommendation-first supervision
  - [ ] I4 — Honest divergence
  - [ ] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [ ] Story marked done via `/mark-story-done`

## Files to Modify

- `AGENTS.md` — already patched with Conductor's repo-level cost-aware
  delegation default
- `.agents/skills/*/SKILL.md` — already patched in Conductor for local
  validate/check-in/finish/loop/audit surfaces
- `docs/alignments/align-041-cost-aware-delegation-defaults.md` — record the
  decision and target rollout results
- `docs/align-projects.md` — index the alignment
- target repo `AGENTS.md` and applicable `.agents/skills/*/SKILL.md` files in
  isolated worktrees only

## Notes

- User approved proceeding from Alignment 041 and explicitly requested
  `/loop-verify` to work slowly and methodically across repos.
- This is a policy/instruction rollout. Fresh external provider docs are not
  needed because no provider, API, SDK, or concrete model ID is being changed.
- The target repos remain owners of their local adaptations. Conductor records
  the rollout plan and evidence; target project changes are not complete until
  their own worktrees are patched and validated.

## Plan

Autonomy: Go after approval. The user approved the rollout and requested
`/loop-verify`. Pause only if a target repo has dirty-state ambiguity, missing
validation tooling, or a local skill shape that would require a human policy
choice rather than a small adaptation.

1. Run a find-only `/loop-verify` inventory over disjoint target repo groups to
   identify which instruction/skill surfaces should receive the policy.
2. Create isolated worktrees under
   `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/<project-key>` on
   branch `codex/cost-aware-delegation-rollout`.
3. Apply the smallest model-name-free guidance to each repo:
   - root `AGENTS.md` for the general rule when present
   - `loop-verify` for worker strength/reasoning guidance
   - `validate` for mechanical validation sidecars
   - `check-in` or equivalent landing skills for mechanical preflight only
   - `finish-and-push` or deploy orchestrators only as leaf-skill inheritance,
     not a second policy
   - `skill-surface-audit` where present for report-only scan workers
4. Run each repo's skill/methodology/lint checks appropriate to touched
   surfaces.
5. Update Alignment 041 and this story with per-repo worktree, files, and
   validation evidence.

## Work Log

- 20260610 — story created and planned from Alignment 041 after user approval;
  next step is `/loop-verify` inventory across tracked target repos.
- 20260610 — `/loop-verify` Round 1 completed find-only inventory across all
  tracked target repos. Accepted exact-model delegation-table drift in Dossier,
  Storybook, doc-web, and CineForge. Treated missing optional skill surfaces as
  local adaptation rather than blockers.
- 20260610 — created isolated target worktrees under
  `/Users/cam/.codex/worktrees/cost-aware-delegation-rollout/` on
  `codex/cost-aware-delegation-rollout`, patched root `AGENTS.md`,
  `loop-verify`, and `validate` surfaces across all seven target repos, and ran
  repo-local skill/methodology/diff checks.
- 20260610 — `/loop-verify` Round 2 inspected patched target diffs. Clean for
  Dossier/Storybook, Board Game Ingester/RoboRally/Echo Forge, and doc-web.
  Rejected CineForge UTC build-map date finding because the generator
  intentionally uses UTC. Alignment 041 now records per-repo evidence and
  validation.
- 20260610 — regenerated Conductor methodology surfaces and validated with
  `make methodology-compile`, `make methodology-check`, `make skills-check`,
  `make lint`, `make test`, and `git diff --check`.
