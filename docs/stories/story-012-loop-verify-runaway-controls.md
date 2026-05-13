---
title: "Harden Loop Verify Runaway Controls"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:1.2"
  - "spec:2.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on:
  - "009"
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

# Story 012 - Harden Loop Verify Runaway Controls

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: Story 009

## Goal

Tighten `/loop-verify` so it remains useful for broad, objective
verification/fix loops without letting documentation or ADR alignment work run
for hours.

The immediate trigger is an Echo Forge report, confirmed by Cam firsthand, that
`/loop-verify` ran away twice. The failure was not just one bad orchestration
choice. The shared skill currently encourages the pattern by normalizing
uncapped rounds, defaulting workers to fix-capable behavior, defining broad
documentation materiality, and giving workers a prompt shape that says to use
`$loop-verify` inside their shard.

The desired behavior is sharper:

- workers never recursively invoke `/loop-verify`
- routine loop verification has a default budget and explicit continuation gate
- docs/ADR alignment defaults to single-pass, find-only worker review
- the main agent owns cross-file judgment and applies documentation fixes
- newly discovered related ADR/spec/story work is reported as expansion, not
  silently pulled into the current loop
- strict-until-clean loops remain available for objective, contract-critical
  work when Cam explicitly asks for them

## Acceptance Criteria

- [x] Conductor's `.agents/skills/loop-verify/SKILL.md` no longer instructs
      workers to use `$loop-verify` or spawn agents inside a shard.
- [x] The worker prompt contract requires single-pass shard work: inspect/fix or
      inspect-only as assigned, do not recurse, do not spawn subagents, do not
      widen scope.
- [x] The skill defines a default budget for ordinary loops, such as one full
      round or roughly 10-15 minutes, after which the main agent reports results
      or asks for explicit continuation if more full rounds are warranted.
- [x] The skill preserves a strict-until-clean mode only for explicitly approved
      or objectively contract-critical work: executable behavior, tests,
      generated outputs, schemas, eval correctness, security, or similarly
      bounded validation surfaces.
- [x] ADR/docs alignment gets a dedicated default: find-only workers, main-agent
      fixes, narrow materiality, and a stop/report gate when findings imply
      related ADRs, stories, specs, generated outputs, or target repos outside
      the intended scope.
- [x] Documentation materiality is narrowed so prose clarity does not reset a
      full loop unless it changes accepted status, contradictions, frontmatter,
      explicit checklist requirements, generated-output truth, or a named
      cross-file contract.
- [x] The skill tells the coordinator to close or ignore stale worker agents
      before a loop and to treat unexpected old-agent summaries as noise unless
      they are tied to the current round.
- [x] Alignment memory records the updated recommendation and explains how this
      changes, but does not discard, the earlier no-hard-cap rationale from
      Story 005 and Story 009.
- [x] If the behavior should propagate, target repos receive the change only via
      isolated worktrees and repo-local checks; do not edit primary checkouts in
      place.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Reworking the Echo Forge ADR or source-model docs that exposed the failure.
- Running `/loop-verify` as the validation mechanism for this story creation.
- Removing `/loop-verify` or making it sequential-only.
- Creating a central canonical skill repo or forcing exact text identity across
  tracked projects.
- Changing provider/model selection policy beyond the existing risk-sized
  worker guidance from Story 009.
- Committing, pushing, or landing target-repo work without an explicit closeout
  request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, ADR-001, ADR-002, Story 005,
      Alignment 011, Alignment 019, Alignment 024, Alignment 025, and Story 009.
- [x] Inspect Conductor's current `/loop-verify` skill for runaway triggers:
      recursive worker prompt, no-hard-cap language, ten-round normalization,
      fix-capable defaults, broad materiality, docs/ADR behavior, stale-agent
      handling, and output shape.
- [x] Patch Conductor `/loop-verify` with the smallest behavior change that
      satisfies the acceptance criteria.
- [x] Decide whether `/validate`, `/build-story`, `/create-story`, or
      `/setup-methodology` need small references to the new loop modes, and
      avoid touching them if `/loop-verify` alone owns the behavior clearly.
- [x] Create or update one alignment record for the portable recommendation and
      update `docs/align-projects.md`.
- [x] If Cam approves propagation during build, update target repos in isolated
      worktrees, regenerate wrappers or methodology surfaces as each repo
      requires, and record per-repo evidence.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required; no scripts
        or repo checks changed
- [x] Search docs and update any related surfaces.
- [x] Verify Conductor tenets:
  - [x] I1 - Meaning over text
  - [x] I2 - Distributed ownership
  - [x] I3 - Recommendation-first supervision
  - [x] I4 - Honest divergence
  - [x] I5 - Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `.agents/skills/loop-verify/SKILL.md` - primary behavior contract for
  recursion, budget, mode selection, docs/ADR materiality, and expansion gates.
- `docs/alignments/` and `docs/align-projects.md` - portable alignment memory
  for the refined loop contract and target-repo recommendation.
- `docs/stories/story-012-loop-verify-runaway-controls.md` - story source of
  truth and work log.
- Generated methodology surfaces after compile: `docs/stories.md` and
  `docs/methodology/graph.json`.
- Target repo `.agents/skills/loop-verify/SKILL.md` files and generated wrappers
  only if build scope explicitly includes propagation.

## Notes

- Source report: Echo Forge AI analyzed why `/loop-verify` ran away twice; Cam
  confirmed the behavior firsthand and asked Conductor for a take.
- Key failure classes from the report:
  - no fixed budget or continuation gate
  - default fix-capable workers in tightly coupled doc graphs
  - broad materiality for semantic doc wording
  - nested loop behavior from `Use $loop-verify for this shard`
  - missing expansion stop when new related ADR/story/spec work appears
  - overly broad orchestration scope
  - stale subagent summaries adding coordinator noise
- Current Conductor evidence:
  - `.agents/skills/loop-verify/SKILL.md` says not to impose a fixed round cap.
  - It says ten rounds is acceptable when material issues keep appearing.
  - The sample worker prompt says `Use $loop-verify for this shard.`
  - Story 009 already hardened upstream-boundary and worker model-sizing rules,
    but it did not address recursion, default budgets, or docs/ADR alignment
    mode.
- Previous no-hard-cap rationale should be preserved where it is actually
  valuable: objective, bounded, contract-critical verification where material
  fixes are converging and Cam asked for a full clean round.

## Plan

For `/build-story 012`:

1. Patch Conductor `/loop-verify` first and keep the behavior easy to read.
2. Add or update alignment memory with a clear recommendation: adopt the new
   loop modes across tracked repos, with local wording allowed.
3. Run Conductor checks before deciding on propagation.
4. If propagation is approved, use isolated target worktrees and only update the
   loop skill plus generated wrappers/surfaces required by each repo.
5. Validate with repo-native skill/methodology checks and `git diff --check`.

## Work Log

20260512-2303 - story-created: created Story 012 from Cam's approved Echo Forge
runaway-loop report. The story is scoped to `/loop-verify` hardening:
no-recursion worker prompts, a default budget/continuation gate, docs/ADR
inspect-only mode, narrower doc materiality, stale-agent hygiene, and an
expansion gate for newly discovered related work. Next step: run `/build-story
012`.

20260512-2313 - build complete: patched Conductor `/loop-verify` with three
explicit modes: budgeted, docs/ADR alignment, and strict-until-clean. The worker
prompt contract now forbids recursive `/loop-verify`, subagent spawning, scope
widening, and extra rounds from inside shards. Updated `setup-methodology` so it
no longer teaches the old no-budget loop behavior, and created Alignment 029 as
the portable recommendation.

Target rollout used isolated worktrees under
`/Users/cam/.codex/worktrees/loop-verify-runaway-controls/` on branch
`codex/loop-verify-runaway-controls`. Updated `.agents/skills/loop-verify` and
`.agents/skills/setup-methodology` in Dossier, Storybook, doc-web, CineForge,
Board Game Ingester, Robo Rally, and Echo Forge; regenerated Gemini wrappers in
each. Storybook also regenerated `docs/methodology/graph.json` and
`docs/stories.md`; CineForge regenerated `docs/build-map.md`,
`docs/methodology/graph.json`, and `docs/stories.md`.

Target checks passed:

- Dossier: `./scripts/sync-agent-skills.sh --check`, methodology check using
  `/Users/cam/Documents/Projects/dossier/.venv/bin/python`, and
  `git diff --check`.
- Storybook: `bash scripts/sync-agent-skills.sh --check`,
  `npm run methodology:compile`, `npm run methodology:check`,
  `git diff --check`.
- doc-web: `make skills-check`, `make methodology-check`, `git diff --check`.
- CineForge: `make skills-check`, `npm run methodology:compile`,
  `npm run methodology:check`, `git diff --check`. Existing architecture-audit
  and UI-scout freshness warnings remain unrelated baseline warnings.
- Board Game Ingester: `make skills-check`, `make methodology-check`,
  `git diff --check`.
- Robo Rally: `npm run skills:check`, `npm run methodology:check`,
  `git diff --check`.
- Echo Forge: `npm run skills:check`, `npm run methodology:check`,
  `git diff --check`.

Conductor checks passed after generated methodology refresh:
`make methodology-compile`, `make methodology-check`, `make lint`,
`make skills-check`, and `git diff --check`. `make test` was not required
because no scripts or repo checks changed. The practical improvement is that
docs/ADR verification now has an inspect-only default and expansion stop, while
objective contract-critical work can still request a strict clean-round proof.
Recommended next step: run `/validate 012`.

20260512-2324 - validation complete: validated Story 012 with the new
`/loop-verify` contract in budgeted, inspect-only mode. The worker round covered
Conductor-local story/skill/alignment surfaces, Dossier/Storybook/doc-web target
worktrees, and CineForge/Board Game Ingester/Robo Rally/Echo Forge target
worktrees. Results: target shard A returned `RESULT: no-issue`, target shard B
returned `RESULT: no-issue`, and the Conductor shard found one material
out-of-scope generated bytecode change in
`scripts/__pycache__/methodology_graph.cpython-314.pyc`. Restored only that
bytecode file, then reran targeted status/diff hygiene.

Fresh validation checks passed:

- Conductor: `PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
  `PYTHONDONTWRITEBYTECODE=1 make lint`, `make skills-check`,
  `PYTHONDONTWRITEBYTECODE=1 make test`, `git diff --check`.
- Dossier: `./scripts/sync-agent-skills.sh --check`, methodology check using
  `/Users/cam/Documents/Projects/dossier/.venv/bin/python`, `git diff --check`.
- Storybook: `bash scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, `git diff --check`.
- doc-web: `make skills-check`, `make methodology-check`, `git diff --check`.
- CineForge: `make skills-check`, `npm run methodology:check`,
  `git diff --check`; existing architecture-audit and UI-scout freshness
  warnings remain unrelated baseline warnings.
- Board Game Ingester: `make skills-check`, `make methodology-check`,
  `git diff --check`.
- Robo Rally: `npm run skills:check`, `npm run methodology:check`,
  `git diff --check`.
- Echo Forge: `npm run skills:check`, `npm run methodology:check`,
  `git diff --check`; existing "No Ideal requirements parsed" warning remains a
  baseline warning.

Learning-review result:

```text
RESULT: no-candidate
Reason: The only validation fix was tracked bytecode churn, an already-known
Conductor hygiene issue handled by restore plus PYTHONDONTWRITEBYTECODE rather
than a new workflow rule.
Evidence checked: Story 012 validation run, loop-verify worker results,
Conductor status, and fresh check outputs.
```

Disposition: close now. The implementation met acceptance criteria, target
rollout stayed in isolated worktrees, and the new `/loop-verify` contract
successfully bounded the validation round instead of recursing or widening.
Recommended next step: run `/mark-story-done 012`.

20260512-2342 - marked done: closed Story 012 via `/mark-story-done 012` after
confirming the build and validation gates were checked and the remaining work
was closeout only. Added the changelog entry for the user-visible
`/loop-verify` runaway-control change and regenerated methodology outputs.
No target-repo landing, commit, or push was performed; the target repo updates
remain in isolated worktrees for an explicit closeout flow.
