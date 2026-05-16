---
title: "Add Optional Detector Guidance to Codebase Improvement"
status: "Done"
priority: "Medium"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
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
  - "005"
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

# Story 014 - Add Optional Detector Guidance to Codebase Improvement

**Priority**: Medium
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: Story 005

## Goal

Adapt Scout 033's useful complexity-hotspot workflow into Cam's existing
codebase-improvement lane without importing a brand-new global Codex skill or
turning heuristic scanner output into automatic refactor pressure. After Scout
034, the same lane also owns occasional report-only semantic review tools such
as Clawpatch, which look for latent bugs outside the current diff.

The intended behavior is:

- `/codebase-improvement-scout` remains report-first and story-oriented.
- Algorithmic complexity signals become one optional detector category alongside
  churn, size, known risk, user impact, maintenance drag, and drift pressure.
- Periodic AI semantic review becomes a separate optional detector category for
  stale, high-churn, thinly-tested, or pre-cleanup code areas.
- Reports consistently ask for current pattern, estimated current complexity,
  recommended change, estimated complexity after, risk level, and tests or
  measurements needed.
- Any helper script is reviewed, vendored, or recreated locally before it is
  trusted in live workflows; `npx codex-complexity-optimizer` is not a default
  operating step.
- External semantic review tools are pinned, run in isolated worktrees, kept
  report-only, and never allowed to run fix paths during scout-mode use.
- Target repos receive wording only through explicit rollout work, with each
  repo preserving its own proof surface.

## Acceptance Criteria

- [x] Conductor records the portable adoption decision from Scout 033 in
      alignment memory: algorithmic complexity scanning is useful as a
      deterministic lead source, not as a standalone optimizer.
- [x] The shared guidance for `/codebase-improvement-scout` names the detector
      categories worth checking: nested scans, membership/search in loops,
      sort-in-loop, render-derived collection work, N+1-shaped IO/query loops,
      and repeated expensive derivations.
- [x] The guidance requires scanner findings to be verified by local code reads
      before they become stories or patches.
- [x] The guidance requires tests, benchmarks, profiler/browser evidence, or
      manual measurements before claiming a performance improvement.
- [x] Scout 034's Clawpatch recommendation is folded into this story's owning
      lane: periodic report-only semantic review belongs in
      `/codebase-improvement-scout`, not `/validate`, CI, or always-on story
      closeout.
- [x] The story decides whether instruction-level guidance is enough or whether
      a reviewed local helper script should be vendored/recreated.
- [x] If target-project rollout is warranted, it is done in isolated worktrees
      and adapted to each repo's existing `codebase-improvement-scout` and
      validation surfaces.
- [x] No target repo receives generic complexity backlog noise or unverified
      scanner findings.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Installing `codex-complexity-optimizer` globally in Cam's Codex environment.
- Adding `npx codex-complexity-optimizer` as a required validation,
  codebase-improvement, or CI step.
- Installing Clawpatch globally, running it as a required validation/CI step, or
  using `clawpatch fix` as part of a codebase-improvement scout.
- Creating a new parallel `complexity-optimizer` lane beside
  `/codebase-improvement-scout`.
- Creating a parallel Clawpatch lane beside `/codebase-improvement-scout`.
- Running broad auto-refactors from scanner output.
- Treating performance tuning as higher priority than current product,
  artifact, provider, or UI-taste work without repo-local triage evidence.
- Routing target-repo inbox items from Scout 033 before Conductor defines the
  shared rule.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Scout 033 and the current codebase-improvement alignment memory
- [x] Inspect the existing target-repo `/codebase-improvement-scout` skill
      variants before choosing wording
- [x] Create or update Conductor alignment memory with the portable detector
      decision
- [x] Update the smallest shared Conductor setup/methodology surface that owns
      future codebase-improvement guidance
- [x] Decide whether a local helper script is justified; if so, keep it
      reviewed, local, and optional
- [x] If approved by the build findings, roll wording to target repos in
      isolated worktrees
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required; no
        scripts or runtime checks changed
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

- `docs/scout/scout-033-codex-complexity-optimizer-codebase-improvement.md` -
  source scout and adoption boundary.
- `docs/scout/scout-034-clawpatch-automated-code-review.md` - source scout and
  periodic report-only semantic review boundary.
- `docs/alignments/` and `docs/align-projects.md` - portable alignment record if
  the build confirms cross-project guidance.
- `.agents/skills/setup-methodology/SKILL.md` - likely shared Conductor surface
  for future codebase-improvement lane setup wording.
- Target repo `.agents/skills/codebase-improvement-scout/SKILL.md` files -
  possible rollout targets if the Conductor wording is mature enough.
- `docs/stories/story-014-algorithmic-complexity-detector-codebase-improvement.md`
  - story plan, evidence, and outcome log.

## Notes

Scout 033 classified `codex-complexity-optimizer` as `Adapt`: useful
report-first detector discipline, but not a tool to install globally or trust as
a standalone optimizer. The npm package is very new, has one release, and uses
a heuristic scanner. That makes it a good reference and a poor default runtime
dependency.

Scout 034 classified Clawpatch as `Spike`: useful as an occasional report-only
semantic review pass for latent bugs, but too expensive and noisy for normal
validation, CI, or every-story closeout. Optional target-repo guidance should
land now; first natural use in each repo is the pilot. Runs still need isolated
worktrees, pinned tool versions or source commits, generated state kept outside
the repo where possible, and no `clawpatch fix` execution during scout-mode
use.

Conductor does not currently own a live local
`.agents/skills/codebase-improvement-scout/SKILL.md`; the lane lives in tracked
product repos and Conductor alignment/setup memory. This story should therefore
start by defining the portable rule in Conductor and only then decide whether a
target-repo rollout is warranted.

## Plan

1. Add Conductor alignment memory:
   - Create `docs/alignments/align-031-algorithmic-complexity-detector-codebase-improvement.md`.
   - Update `docs/align-projects.md`.
   - Record the decision as a portable improvement: algorithmic-complexity
     scanning is an optional deterministic lead source inside
     `/codebase-improvement-scout`, not a standalone optimizer or required npm
     tool.

2. Update Conductor's shared setup/methodology surface:
   - Patch `.agents/skills/setup-methodology/SKILL.md` so future setup/refresh
     work knows how to treat codebase-improvement lanes when enough code exists.
   - Keep the rule lightweight: instruction-level detector guidance first; no
     vendored helper script in this story unless implementation proves the
     wording is insufficient.

3. Roll out the wording to target repos in isolated worktrees:
   - Create fresh task worktrees under `/Users/cam/.codex/worktrees/story014/`
     from each target repo's current `origin/main` or safe base branch.
   - Update only each repo's
     `.agents/skills/codebase-improvement-scout/SKILL.md`.
   - Preserve local variants while adding the same detector meaning:
     nested scans, membership/search in loops, sort-in-loop,
     render-derived collection work, N+1-shaped IO/query loops, and repeated
     expensive derivations.
   - Add report requirements for current pattern, estimated current complexity,
     recommended change, estimated complexity after, risk level, and tests or
     measurements needed.
   - Require local code reads before promoting findings and require tests,
     benchmarks, profiler/browser evidence, or manual measurements before
     claiming performance wins.

4. Update Story 014 evidence:
   - Set the story to `In Progress` during implementation.
   - Check off completed acceptance criteria and tasks.
   - Record target worktrees, files changed, validation commands, and any
     repo-specific divergence.
   - Leave the story `In Progress` with `Build complete` checked, per
     `/build-story`, and recommend `/validate`.

5. Run checks:
   - Conductor: `make methodology-compile`, `make methodology-check`,
     `make lint`, `make skills-check`, and `git diff --check`.
   - Target repos: run each repo's skill wrapper check where available
     (`make skills-check`, `scripts/sync-agent-skills.sh --check`, or the
     repo-local equivalent) plus `git diff --check`.
   - Do not run product tests unless implementation touches scripts or runtime
     code; this story should be docs/skills-only.

Manual inspection points:

- Confirm Scout 033 remains the source scout and does not imply direct npm
  adoption.
- Confirm no target repo receives unverified complexity backlog or scanner
  output.
- Confirm the wording does not make performance tuning outrank current
  product/artifact/provider/UI-taste work without repo-local triage evidence.

Upstream evidence:

- Current source evidence was gathered during Scout 033 on 2026-05-16 by
  inspecting the X post metadata, GitHub repository, npm package metadata, and
  npm tarball without installing the package.
- No additional upstream docs are needed for this implementation because the
  build changes methodology wording only; it does not run, vendor, install, or
  depend on `codex-complexity-optimizer`.

Post-closeout extension:

- Scout 034 adds a second optional detector family to the same story boundary:
  periodic AI semantic review. The target-repo guidance should be rolled out
  now as optional wording rather than waiting for a separate RoboRally-only
  pilot. Natural use supplies the evidence; repo-local fixes can later be
  propagated through `/align-projects` when they generalize.

## Work Log

- 20260516-1040 — story creation: created Story 014 from Scout 033 follow-up
  approval, scoped it as a Conductor-owned methodology/adaptation story rather
  than a target-repo inbox item or global npm install.
- 20260516-1049 — build exploration: read Ideal/spec/state/graph, ADR-001,
  ADR-002, Scout 033, existing codebase-improvement alignment memory, Conductor
  setup-methodology, and target repo codebase-improvement skill variants. All
  target repos already have a `codebase-improvement-scout` skill, so the
  expected implementation is a small wording rollout through isolated worktrees,
  not a new tool lane. Primary target checkouts are behind, dirty, or on other
  work, so direct in-place edits are excluded.
- 20260516-1100 — implementation: added Alignment 031 and updated Conductor
  setup-methodology with instruction-level algorithmic-complexity detector
  guidance. Decision: no helper script in this story; the guidance is small,
  new, and better proven through existing report-first scans before adding
  maintained code.
- 20260516-1110 — target rollout: created isolated worktrees under
  `/Users/cam/.codex/worktrees/story014/` for dossier, storybook, doc-web,
  cine-forge, boardgame-ingester, roborally, and echo-forge from `origin/main`.
  Updated only `.agents/skills/codebase-improvement-scout/SKILL.md` in each
  target. Local adaptations preserved: doc-web and boardgame-ingester tie proof
  to driver/artifact truth, roborally ties proof to deterministic scenario
  output, CineForge keeps provider/runtime/artifact-flow truth ahead of simple
  loop complexity, and Echo Forge keeps browser/live-scene evidence ahead of
  generic scanner output.
- 20260516-1115 — target validation: passed target skill checks and whitespace
  checks in all seven isolated worktrees:
  - dossier: `make skills-check` and `git diff --check`
  - storybook: `bash scripts/sync-agent-skills.sh --check` and
    `git diff --check`
  - doc-web: `make skills-check` and `git diff --check`
  - cine-forge: `./scripts/sync-agent-skills.sh --check` and
    `git diff --check`
  - boardgame-ingester: `make skills-check` and `git diff --check`
  - roborally: `bash scripts/sync-agent-skills.sh --check` and
    `git diff --check`
  - echo-forge: `bash scripts/sync-agent-skills.sh --check` and
    `git diff --check`
- 20260516-1120 — Conductor validation for build: passed
  `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
  `PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
  `PYTHONDONTWRITEBYTECODE=1 make lint`,
  `PYTHONDONTWRITEBYTECODE=1 make skills-check`, and `git diff --check`.
  `make test` was not run because the build changed docs and skill wording
  only, not scripts or runtime code.
- 20260516-1130 — loop-verify validation: ran one docs/ADR alignment
  inspect-only round across four shards: Conductor contract, TypeScript/UI
  target skills, Python/pipeline target skills, and rollout evidence/boundary.
  All workers returned `RESULT: no-issue`. Coordinator checks also passed:
  `PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
  `PYTHONDONTWRITEBYTECODE=1 make lint`,
  `PYTHONDONTWRITEBYTECODE=1 make skills-check`, and `git diff --check`.
  No material findings, blockers, upstream-owned issues, or expansion findings
  remained.
- 20260516-1145 — target landing: committed and pushed the
  `codebase-improvement-scout` wording to each target repo `main`: Dossier
  `85fe02c`, Storybook `3484e84`, doc-web `c165bf7`, CineForge `3f0d050`,
  Board Game Ingester `9c57a6c`, RoboRally `7e9c32a`, and Echo Forge
  `744d0e1`.
- 20260516-1150 — closeout: marked Story 014 `Done` via `/mark-story-done`
  after target landing and loop-verify validation.
- 20260516-1225 — post-main Clawpatch fold-in: pulled `origin/main` first,
  confirmed this checkout was already at `e4572ea`, broadened Story 014 from
  algorithmic-complexity-only detector guidance to optional detector guidance,
  and recorded Scout 034 as the same `/codebase-improvement-scout` family:
  occasional report-only semantic review, not `/validate`, CI, or normal story
  closeout.
- 20260516-1240 — rollout correction: accepted Cam's correction that a separate
  pre-rollout pilot is unnecessary. Updated the rule so optional target-repo
  guidance lands now and first natural use in each repo is the pilot; noisy or
  awkward repo-local behavior should be fixed locally first, then generalized
  through `/align-projects`.
- 20260516-1255 — target worktree rollout prep: created isolated target
  worktrees under `/Users/cam/.codex/worktrees/story014-clawpatch/` from each
  repo's current `origin/main` and updated only
  `.agents/skills/codebase-improvement-scout/SKILL.md` in Dossier, Storybook,
  doc-web, CineForge, Board Game Ingester, RoboRally, and Echo Forge.
- 20260516-1305 — target validation: all seven target worktrees passed their
  repo-native skill-wrapper checks plus `git diff --check`. No product/runtime
  tests were run because the target changes are skill wording only.
- 20260516-1310 — landing boundary: no commits or pushes were made in Conductor
  or target repos during this post-closeout extension; the prepared target
  patches remain in isolated worktrees pending an explicit check-in/push step.
- 20260516-1335 — target landing: committed and pushed the Scout 034 optional
  semantic-review guidance to each target repo `main`: Dossier `c67ae6b`,
  Storybook `63da5ca`, doc-web `5beca37`, CineForge `48cb9fa`, Board Game
  Ingester `59cd4e5`, RoboRally `d4776f8`, and Echo Forge `5eac351`. All seven
  target task branches remain available as
  `codex/story014-clawpatch-detector-20260516`, and each target worktree is
  clean with `HEAD == origin/main`.
- 20260516-1345 — finish validation: refreshed Conductor generated surfaces and
  passed `PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
  `PYTHONDONTWRITEBYTECODE=1 make lint`,
  `PYTHONDONTWRITEBYTECODE=1 make skills-check`,
  `PYTHONDONTWRITEBYTECODE=1 make test`, and `git diff --check`.
- 20260516-1355 — primary inbox fold-in: after pushing the Conductor branch and
  `main`, checked the primary checkout at
  `/Users/cam/Documents/Projects/conductor` and found one additional
  user-capture line in `inbox.md` about broad per-project port blocks. Folded
  that line into this landing set so primary-checkout inbox capture is not
  dropped.
