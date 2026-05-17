---
title: "Add Loop Verify Discovery and Candidate-Close Phases"
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
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on:
  - "012"
  - "013"
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

# Story 016 — Add Loop Verify Discovery and Candidate-Close Phases

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: Story 012, Story 013

## Goal

Refine `/loop-verify` after the doc-web Story 229 failure showed a second
runaway class: strict verification started paying full closeout costs after
each accepted finding while the defect landscape was still moving.

The desired behavior is:

- strict loops discover cross-cutting defect classes before fixing instances
- repeated same-class findings trigger systemic audit or class-level repair
- focused probes and regression tests run while findings are likely
- generated docs, proof artifacts, full suites, changelog/story updates, and
  advisory review wait until candidate-close
- target repos inherit the behavior through isolated worktrees, preserving
  repo-local adaptation

## Acceptance Criteria

- [x] Conductor's `.agents/skills/loop-verify/SKILL.md` describes strict-mode
      phases: discovery, systemic-fix, focused-confirmation, and
      candidate-close.
- [x] The skill defaults strict cross-cutting contract work to find-only
      discovery before fix-capable workers.
- [x] The skill defines validation tiers from direct probes through full suite
      and advisory review.
- [x] The skill tells the coordinator to stay in Tier 0-1 while findings are
      likely and to reserve Tier 3-4 closeout work for candidate-close.
- [x] The skill groups the finding ledger by defect class and treats repeated
      same-class findings as a systemic-fix trigger.
- [x] The skill defines a non-convergence/systemic-audit stop condition for
      repeated same-class findings, material resets without narrowing, scope
      expansion, or repeated expensive closeout work before convergence.
- [x] Alignment memory records the portable recommendation and target rollout
      evidence.
- [x] Target repos that already carry `/loop-verify` receive the wording in
      isolated worktrees, not primary checkouts.
- [x] Repo-native checks pass or pre-existing unrelated warnings are recorded.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Fixing the doc-web Story 229 runtime behavior directly.
- Reopening old Storybook, Echo Forge, or doc-web verification loops.
- Removing strict-until-clean mode; the clean-round proof remains useful once a
  candidate is stable.
- Turning `/loop-verify` into `/validate`, story closure, or code-review-only
  automation.
- Creating a central canonical harness repo or forcing exact text identity
  where a target repo has justified local adaptation.
- Committing, pushing, or landing target-repo work without an explicit closeout
  request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context.
- [x] Read the current `/loop-verify` skill and the doc-web post-mortem.
- [x] Implement the Conductor `/loop-verify` phase and validation-tier changes.
- [x] Create alignment memory and update `docs/align-projects.md`.
- [x] Roll the skill wording to tracked repos in isolated worktrees.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required; no scripts
        or repo checks changed
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

- `.agents/skills/loop-verify/SKILL.md` — primary behavior contract for strict
  discovery phases, validation tiers, defect-class ledgering, and systemic
  audit stops.
- `docs/alignments/align-033-loop-verify-discovery-candidate-close.md` —
  portable alignment memory for the recommendation and rollout evidence.
- `docs/align-projects.md` — alignment index entry.
- `docs/stories/story-016-loop-verify-discovery-candidate-close.md` — story
  source of truth and work log.
- `CHANGELOG.md` — user-visible workflow change.
- Generated methodology surfaces after compile: `docs/stories.md` and
  `docs/methodology/graph.json`.
- Target repo `.agents/skills/loop-verify/SKILL.md` files and generated
  wrappers or methodology surfaces only where local tooling requires them.

## Notes

- Trigger: doc-web reported that a Story 229 loop ran for roughly four hours.
  The post-mortem said the problem was interleaving discovery and expensive
  closure work too early, not simply "too much verification."
- Related prior work:
  - Story 012 / Alignment 029 fixed recursive workers, uncapped docs loops,
    docs/ADR materiality, and expansion gates.
  - Story 013 / Alignment 030 kept `/validate` as the closure authority and
    added only general finding-disposition discipline to `/loop-verify`.
- This story keeps those boundaries but adds a stricter runtime-phase model for
  objective, cross-cutting contract work.

## Plan

Cam approved implementation from the discussion. Implementation plan:

1. Patch Conductor `/loop-verify` with strict-mode phase discipline, validation
   tiers, defect-class ledgering, and systemic-audit stop conditions.
2. Create Alignment 033 and update the alignment index.
3. Regenerate Conductor methodology surfaces and run local checks.
4. Inspect tracked repo primary checkout state.
5. Create isolated target worktrees and roll the wording to repos that carry
   `/loop-verify`.
6. Run each target repo's native skill/methodology checks plus
   `git diff --check`.
7. Update story/alignment evidence with the final result.

## Work Log

20260516-2251 — story-created: created Story 016 after Cam approved the
doc-web post-mortem recommendations. Scope is the `/loop-verify`
discovery/candidate-close split, validation tiers, defect-class ledgering, and
systemic-audit stops, with target-repo propagation through isolated worktrees.

20260516-2258 — conductor-skill-patched: updated Conductor `/loop-verify` so
strict mode starts with find-only discovery for cross-cutting contracts, uses
validation tiers, groups accepted findings by defect class, switches to
systemic-fix for repeated classes, and freezes Tier 3-4 closeout work until
candidate-close.

20260516-2314 — target-rollout-complete: copied the updated `/loop-verify`
wording into isolated target worktrees on branch
`codex/loop-verify-discovery-close-20260516`, all based on current
`origin/main`:

| Project | Base | Changed files | Checks |
| --- | --- | --- | --- |
| Dossier | `998db9c` | `.agents/skills/loop-verify/SKILL.md` | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python make methodology-check`, and `git diff --check` passed. Existing legacy/non-local metadata warnings remain unrelated. |
| Storybook | `e2348f6` | `.agents/skills/loop-verify/SKILL.md`, `docs/methodology/graph.json`, `docs/stories.md` | `pnpm methodology:compile`, `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`, and `git diff --check` passed. Generated diff only advanced UI-scout freshness from 11 to 12 days. |
| doc-web | `0000863` | `.agents/skills/loop-verify/SKILL.md` | `PYTHONDONTWRITEBYTECODE=1 make skills-check methodology-check` and `git diff --check` passed. |
| CineForge | `16cb6be` | `.agents/skills/loop-verify/SKILL.md`, `docs/build-map.md`, `docs/methodology/graph.json`, `docs/stories.md` | `npm run methodology:compile`, `./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, and `git diff --check` passed. Existing architecture-audit and UI-scout freshness warnings remain unrelated; generated diff advanced the last-generated date and freshness count. |
| Board Game Ingester | `75491af` | `.agents/skills/loop-verify/SKILL.md` | `PYTHONDONTWRITEBYTECODE=1 make skills-check methodology-check lint` and `git diff --check` passed. |
| Robo Rally | `673c979` | `.agents/skills/loop-verify/SKILL.md` | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |
| Echo Forge | `1cf191c` | `.agents/skills/loop-verify/SKILL.md` | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. Existing `No Ideal requirements parsed` warning remains unrelated. |

Primary target checkouts were inspected and left untouched. Storybook,
CineForge, and Echo Forge had unrelated dirty files; Board Game Ingester's
primary checkout was on a feature branch.

Conductor local checks passed before final story evidence updates:
`PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`,
`PYTHONDONTWRITEBYTECODE=1 make skills-check`, and `git diff --check`.

20260516-2320 — validation-complete: reviewed the current diff against Story
016 acceptance criteria. No material findings found. `codex review` was skipped
because this diff is docs, skills, alignment memory, changelog, and generated
methodology output rather than non-trivial application code. A new
`/loop-verify` round was intentionally not used to validate a `/loop-verify`
correction. Fresh Conductor checks passed:
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`,
`PYTHONDONTWRITEBYTECODE=1 make skills-check`, and `git diff --check`.

Learning-review result:

```text
RESULT: no-candidate
Reason: The missing guardrail has already been promoted into live
/loop-verify wording, Story 016, Alignment 033, and the target rollout.
Evidence checked: doc-web post-mortem, Story 016, Alignment 033,
/loop-verify diff, target rollout checks, and Conductor validation checks.
```

20260516-2324 — story-done: marked Story 016 done after build, target rollout,
validation, and learning-review detection. No commits or pushes were performed.

20260516-2338 — loop-verify-validation-trial: used `/loop-verify` in docs/ADR
alignment mode to validate this work with four find-only shards: skill-contract
semantics, story/alignment/generated surfaces, target rollout evidence, and the
primary-versus-session checkout path from Cam's invoked skill link. Three shards
returned `RESULT: no-issue`. The checkout-path shard returned `RESULT:
blocked` because `/Users/cam/Documents/Projects/conductor` contained the
uncommitted implementation while the invoked
`/Users/cam/.codex/worktrees/a82d/conductor` skill path was still clean at the
old contract. Accepted finding: checkout/path mismatch. Resolution: mirrored
the same Conductor diff into the session worktree path and reran targeted
checks there. Session worktree checks passed: `make methodology-check`,
`make lint`, `make skills-check`, and `git diff --check`; the session and
primary `/loop-verify` skill files now match.
