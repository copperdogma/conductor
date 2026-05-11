---
title: "Roll Out Loop Verify Upstream and Model-Sizing Guardrails"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "alignment"
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

# Story 009 — Roll Out Loop Verify Upstream and Model-Sizing Guardrails

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Carry Alignment 025's Conductor seed into the tracked repos so expensive
parallel verification loops stop when the remaining issue is upstream-owned,
and so delegated worker model strength is sized to shard risk instead of
implicitly using the strongest available model for every task.

The practical target is not exact text sync. Each repo should learn the same
behavioral contract:

- define the local/upstream boundary before launching workers
- report upstream-owned blockers separately from local findings
- stop or continue based on whether local verification can still close honestly
- choose worker model/reasoning strength by task complexity and failure cost
- preserve repo-local dependency lanes, especially Storybook's Dossier/doc-web
  upstream surface

## Acceptance Criteria

- [x] Each tracked target repo is inspected in an isolated worktree before any
      edit: Dossier, Storybook, doc-web, CineForge, Board Game Ingester,
      Robo Rally, and Echo Forge.
- [x] Each target repo's `/loop-verify` skill receives or already contains the
      upstream-boundary behavior from Alignment 025, adapted to local repo
      language where needed.
- [x] Each target repo's subagent-spawning skills are inspected for blanket
      "best model" or equivalent guidance; `/validate`, `/build-story`,
      `/create-story`, `/triage`, and repo-local leaf skills get risk-sized
      worker model guidance only where they actually launch workers.
- [x] Storybook's upstream dependency reality is preserved: Dossier/doc-web
      issues should be reported and routed, not papered over inside Storybook
      loops.
- [x] Alignment 025 is updated with rollout execution evidence: target
      worktrees, branch name, base commits, per-repo adaptations, validation
      commands, and any known limits.
- [x] Each touched target repo passes its repo-native skill/methodology checks
      plus `git diff --check`, or unrelated baseline failures are called out
      with enough evidence to distinguish them from this rollout.
- [x] Conductor methodology surfaces are regenerated and checked after the
      story/update work.

## Out of Scope

- Provider-model eval policy, PromptFoo setup, aspirational eval planning, and
  browser-tool evaluation.
- Adding automatic issue/story creation for upstream findings unless a repo
  already has an explicit local routing surface for that behavior.
- Editing target-project primary checkouts in place.
- Claiming target repos have the guardrail before their own isolated patches
  are applied and validated.
- Creating a fixed model matrix. The rule should stay risk-based because
  available models and costs change.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, ADR-001, ADR-002, Alignment
      011, Alignment 019, Alignment 025, and Story 008 context.
- [x] Inspect every target repo's current git state and create isolated
      worktrees/branches for this rollout.
- [x] Compare each repo's `/loop-verify` skill against Conductor's seeded
      upstream-boundary and model-sizing contract.
- [x] Patch `/loop-verify` in target repos where the behavior is missing.
- [x] Search target repo skills for subagent spawning and blanket model-strength
      guidance; patch only the skills that actually delegate work.
- [x] Regenerate skill wrappers or methodology surfaces required by each repo.
- [x] Update Alignment 025 with final rollout evidence and any intentional
      divergence.
- [x] Update this story work log with concrete evidence.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
- [x] Search docs and update any related surfaces.
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

- `docs/stories/story-009-loop-verify-upstream-model-guardrail-rollout.md` —
  story source of truth and work log.
- `docs/alignments/align-025-loop-verify-upstream-model-guardrails.md` —
  rollout evidence, per-repo decisions, and known limits.
- `docs/align-projects.md` — already indexes Alignment 025.
- Target repo worktrees after `/build-story` approval:
  - `.agents/skills/loop-verify/SKILL.md`
  - `.agents/skills/validate/SKILL.md`, `.agents/skills/build-story/SKILL.md`,
    `.agents/skills/create-story/SKILL.md`, `.agents/skills/triage/SKILL.md`,
    or repo-local leaf skills only where subagent model guidance is actually
    needed
  - repo-native generated wrappers or methodology surfaces required by checks

## Notes

- Source decision: Alignment 025.
- The Conductor seed change is already present in this branch's
  `.agents/skills/loop-verify/SKILL.md`.
- The inbox item that triggered this was a Storybook loop-verify run that spent
  too much time on issues eventually understood as Dossier/doc-web upstream
  problems.
- This story should keep Conductor's recommendation-first stance: target
  projects own their local wording and validation, and local adaptations are
  expected when they preserve the same behavior more clearly.

## Plan

1. Use isolated target worktrees under
   `/Users/cam/.codex/worktrees/loop-verify-upstream-model-guardrails/`.
2. Use branch `codex/loop-verify-upstream-model-guardrails` in each target repo
   unless an existing branch requires a safe alternate.
3. For each target repo, inspect:
   - `.agents/skills/loop-verify/SKILL.md`
   - skills that spawn subagents or mention model/reasoning selection
   - repo-local upstream/dependency lanes such as Storybook's Dossier/doc-web
     guidance
4. Patch only the missing behavioral contract:
   - upstream boundary and reporting in `/loop-verify`
   - risk-sized worker model/reasoning defaults where delegation actually
     happens
5. Regenerate wrappers or methodology surfaces as required by each repo.
6. Run repo-native validation. At minimum, run each repo's skill sync/check and
   `git diff --check`; add methodology/lint/test checks when the repo normally
   requires them for skill or methodology edits.
7. Update Alignment 025 and this story with actual evidence.
8. Stop before commit/push unless Cam explicitly asks for closeout.

## Work Log

20260511-0000 — story created from Alignment 025 follow-up approval. Scope is a
target-repo rollout of upstream-boundary and model-sizing guardrails, not a
provider-eval, PromptFoo, aspirational-eval, or browser-tool pass. Next step:
run `/build-story 009` to create isolated target worktrees and apply the
rollout.

20260511-0100 — build complete. Created isolated target worktrees under
`/Users/cam/.codex/worktrees/loop-verify-upstream-model-guardrails/` on branch
`codex/loop-verify-upstream-model-guardrails` for Dossier, Storybook, doc-web,
CineForge, Board Game Ingester, RoboRally, and Echo Forge. Patched each target
repo's `/loop-verify` with the upstream-boundary contract and risk-sized worker
model guidance. Patched `/create-story`, `/build-story`, `/validate`, and
`/triage` where they launch or route subagents. Patched target `golden-verify`
skills that still forced every worker to `model: "opus"` so semantic golden
verification still defaults to high-capability workers while mechanical or
validator-only follow-up can downshift with an explicit rationale.

Target repo checks run:

- Dossier: `skills-check` passed; `methodology-check` passed using
  `/Users/cam/Documents/Projects/dossier/.venv/bin/python` because bare
  `python3` in the isolated worktree lacked `yaml`; `git diff --check` passed.
- Storybook: `bash scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, and `git diff --check` passed.
- doc-web: `make skills-check methodology-check` and `git diff --check`
  passed.
- CineForge: `make skills-check` passed; `npm run methodology:compile` was
  needed because the fresh `origin/main` graph had a date-based UI scout
  freshness count stale by five days; after regeneration,
  `npm run methodology:check` and `git diff --check` passed.
- Board Game Ingester: `make skills-check methodology-check lint` and
  `git diff --check` passed.
- RoboRally: `npm run skills:check`, `npm run methodology:check`, and
  `git diff --check` passed.
- Echo Forge: `npm run skills:check`, `npm run methodology:check`, and
  `git diff --check` passed.

Conductor checks run after story and alignment updates:
`make methodology-compile`, `make methodology-check`, `make lint`,
`make skills-check`, `make test`, and `git diff --check`.

Impact: future wide verification loops in these repos now have a clear stop
rule for upstream-owned blockers and a lower-overhead default for low-risk
worker shards without weakening semantic review. Recommended next step: run
`/validate 009`.

20260511-0130 — validation complete. Findings-first review found one low-risk
documentation issue: `docs/align-projects.md` still described Alignment 025 as
pre-rollout after Story 009 had applied the target-project rollout. Fixed the
index wording so it points to the seed plus Story 009 rollout evidence.

Fresh validation evidence:

- Target worktree checks passed again for Dossier, Storybook, doc-web,
  CineForge, Board Game Ingester, RoboRally, and Echo Forge.
- Structural searches found exactly one `/loop-verify` upstream-boundary
  section per target repo, exactly one triage worker-model-sizing section per
  target repo, risk-sized validation packet guidance in each target
  `/validate`, and no remaining blanket `model: "opus"` / "All subagents use
  opus" / "launch an opus" guidance.
- The handled inbox item was absent from both this branch inbox and the primary
  Conductor checkout inbox.
- Conductor checks passed: `make methodology-compile`,
  `make methodology-check`, `make lint`, `make skills-check`, `make test`, and
  `git diff --check`.

Disposition: Close now. The remaining unchecked gate is only
`/mark-story-done` close-out bookkeeping. Recommended next step: run
`/mark-story-done 009`.

20260511-0200 — story marked done via `/mark-story-done`. Close-out evidence:
build and validation gates were already checked, all Story 009 acceptance
criteria were met, all seven target repos were committed from isolated
worktrees and fast-forwarded to their remote `main` branches, and Conductor was
ready for final check-in after refreshing generated methodology surfaces.
