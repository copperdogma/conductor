---
name: build-story
description: Execute a Conductor story with explicit planning and evidence
user-invocable: true
---

# /build-story [story-number]

Use this to take a Conductor story from story text to implemented supervisor artifact.

## Phase 1 — Explore

1. Read the story.
2. Read:
   - `docs/ideal.md`
   - `docs/spec.md`
   - `docs/methodology/state.yaml`
   - `docs/methodology/graph.json`
   - relevant decision refs
3. Verify that the work really belongs in Conductor and is not better executed directly in a target project first.
4. If the implementation will touch a tracked project repo, inspect that repo's
   git/worktree state first and choose an isolated execution worktree/branch.
   Do not edit the target project's primary checkout unless the user explicitly
   asked for in-place work.
5. Add a work-log entry describing:
   - files to change
   - tracked projects affected
   - risks
   - expected evidence

## Phase 2 — Plan

Write `## Plan` in the story with:

- the concrete file changes
- the expected outputs
- what should be inspected manually
- which checks need to run

Pause for user approval before implementation.

## Optional Delegation After the Plan Gate

After the user approves the Phase 2 plan, the main thread may use
subagents/sidecars for non-trivial work when delegation reduces risk or protects
context. Keep routine small stories single-threaded.

- The main thread owns the approved plan, Ideal/spec fit, target-repo worktree
  isolation, integration, final implementation judgment, and handoff.
- Useful post-gate sidecars include bounded exploration that no longer blocks
  approval, disjoint implementation slices, test or eval writing, artifact
  inspection, and review of already-written changes.
- Before delegated code edits, assign explicit, disjoint file or module
  ownership. Do not let multiple agents edit overlapping files or settle shared
  design questions independently.
- Subagents do not reopen scope, choose the final design, mark workflow gates,
  or decide whether the story is ready for `/validate`.
- If delegation is unavailable, unsafe for the checkout, or explicitly disabled,
  run the same work sequentially and note the fallback.

## Phase 3 — Implement

1. Set the story to `In Progress`.
2. Implement the planned changes.
3. Run the narrowest honest checks:
   - `make methodology-compile`
   - `make methodology-check`
   - `make lint`
   - `make skills-check` if skill files changed
   - `make test` if scripts or repo checks changed
4. Update the work log with concrete evidence.
5. Leave the story `In Progress` with `Build complete` checked, give a short
   plain-language note about what improved for Cam or the target projects, and
   recommend `/validate` as a yes-ready next step.

## Guardrails

- Do not implement before the human gate.
- Supervisor outputs must be inspectable artifacts, not just chat summaries.
- Do not call cross-project sync complete until the affected projects have their own applied work or explicit queued follow-up.
- If target-project edits are required, isolate them in a dedicated worktree so
  supervisor upgrades do not pollute the project's live working environment.
