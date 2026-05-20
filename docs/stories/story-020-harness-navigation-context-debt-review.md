---
title: "Harness Navigation and Context-Debt Review"
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
  - "spec:2.1"
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.3"
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

# Story 020 — Harness Navigation and Context-Debt Review

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn Scout 039's Claude Code large-codebase lesson into a careful
Conductor-owned review of the current distributed harness.

The story should not start by adding new guidance, tools, files, or checklist
items. It should first inspect each tracked repo from current truth surfaces
and document what already exists, how it currently works, and where agents
actually pay context, navigation, validation, or generated-artifact overhead.

Only changes with high expected value should survive the review. A change is
high expected value only when the evidence points to a recurring or likely
failure mode, the expected improvement is concrete, and the ongoing overhead is
small enough to justify carrying more methodology surface.

## Acceptance Criteria

- [x] A read-only inventory covers Conductor plus every tracked project from
      current checkout or `origin/main` truth surfaces before any adoption
      recommendation is made.
- [x] The inventory records what already exists and how it works for:
      - root instructions and agent-facing entry guidance
      - skill surfaces and compatibility links
      - build maps, setup docs, README command tables, or equivalent
        navigation aids
      - targeted validation/eval/runtime commands
      - generated files, dependency artifacts, media outputs, and third-party
        code that may add context noise
      - local runtime/worktree setup surfaces where present
- [x] Each possible adoption is scored as `adopt`, `adapt`, `defer`, or
      `reject` with an explicit expected-value note:
      - observed or likely failure mode
      - expected benefit
      - added overhead
      - reversibility
      - confidence
- [x] Low-confidence, speculative, or "might be useful" additions are rejected
      or deferred by default.
- [x] LSP/code-intelligence work is recommended only for repos with evidence of
      wrong-symbol, wrong-module, or search-noise failures that text search and
      local docs do not already handle.
- [x] Any proposed cross-repo wording or setup change is framed as a
      recommendation-first Conductor alignment/story, not a blanket sync.
- [x] Target repo edits, if later warranted and explicitly approved, use
      isolated worktrees and preserve repo-local adaptation.
- [x] Conductor and any touched files pass the relevant methodology, lint,
      skill, and whitespace checks.

## Out of Scope

- Installing Claude Code-specific infrastructure.
- Adding new required tools, hooks, LSP servers, ignore rules, or generated
  checklists before the inventory proves they are worth their overhead.
- Centralizing the distributed harness in Conductor.
- Rewriting all repo AGENTS/skills because a new upstream article recommends a
  pattern.
- Editing target primary checkouts during the review.
- Treating context-debt review as a recurring ceremony unless the story proves
  a lightweight trigger has net value.
- Committing, pushing, or landing target repo changes without an explicit
  closeout request.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Read Scout 039 and the linked Claude large-codebase source
- [x] Inventory each tracked repo before proposing changes:
  - [x] conductor
  - [x] dossier
  - [x] storybook
  - [x] doc-web
  - [x] cine-forge
  - [x] boardgame-ingester
  - [x] roborally
  - [x] echo-forge
- [x] For each repo, record the existing navigation/context/validation
      surfaces and how they currently work
- [x] Identify candidate improvements only after the full inventory exists
- [x] Score each candidate by expected value, overhead, confidence, and
      reversibility
- [x] Reject or defer speculative additions whose value is not clear
- [x] Create or update a Conductor alignment record only if the review finds
      a portable improvement worth recording
- [x] Implement only the smallest Conductor-side doc, skill, script, or log
      changes justified by the scored review
- [x] If target repo changes are warranted, stop for explicit approval before
      creating isolated target worktrees
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: not applicable; no scripts or repo
        checks changed
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

- `docs/stories/story-020-harness-navigation-context-debt-review.md` — story
  source of truth and work log.
- `docs/scout/scout-039-claude-code-large-codebase-practices.md` — optional
  follow-up note if the build changes the recommendation.
- `docs/alignments/align-NNN-*.md` — only if the inventory finds a portable
  improvement or meaningful divergence worth recording.
- `docs/align-projects.md` — only if a new alignment record is created.
- Shared methodology or skill surfaces — only if the scored review proves a
  small high-value change.
- Target repo files — out of initial scope unless Cam explicitly approves a
  follow-up rollout from isolated worktrees.

## Notes

- Triggered by Scout 039, which evaluated Anthropic's Claude Code
  large-codebase practices article and mapped it to Cam's distributed harness.
- Cam explicitly approved this story with the constraint that the first step
  must be to inspect each repo and understand what already exists and how it
  currently works.
- Cam also set the adoption bar: only high expected value changes should be
  adopted. Additions that might have value are net negative unless their value
  clears the overhead cost of carrying more stuff.
- Current hypothesis to test, not assume: the local framework already has many
  equivalents of the upstream guidance, so the likely value is selective
  cleanup, context-debt review, and targeted command discoverability rather
  than new infrastructure.

## Plan

1. Re-read Conductor intent and decision context, especially ADR-001's
   recommendation-first/distributed-harness boundary and ADR-002's rule that
   investigative lanes must solve repeated problems.
2. Re-read Scout 039 and treat its proposed ideas as hypotheses, not a work
   queue.
3. Inventory each tracked repo from the primary checkout and compare
   `origin/main` where the checkout is behind or active. Capture root guidance,
   skill count, compat links, setup/runtime commands, validation entrypoints,
   generated/noise exclusions, and any existing story/report evidence of
   context debt or wrong-navigation failures.
4. Score only after the full inventory exists. Reject/defer any idea whose
   benefit is plausible but not evidenced.
5. Record the smallest durable Conductor artifact: an alignment with the
   inventory, candidate scoring, and recommendation. Do not edit target repos.

## Work Log

20260520-1305 — story-created: created from Scout 039 follow-up approval with
explicit review-first and high-expected-value adoption gates. No target repo
edits made.

20260520-1307 — inventory-started: read Conductor Ideal/spec/state/graph,
projects registry, ADR-001, ADR-002, Scout 039, and target repo status. Fetched
target origins for comparison but made no target repo edits.

20260520-1313 — inventory-complete: reviewed Conductor, Dossier, Storybook,
Doc Web, CineForge, Board Game Ingester, Robo Rally, and Echo Forge root
instructions, skill surfaces, setup/runtime commands, validation entrypoints,
and generated/noise exclusions. Primary checkout state was recorded because
several targets were behind, active, or dirty.

20260520-1315 — scoring-complete: rejected a portfolio-wide LSP requirement,
new global ignore/checklist work, blanket path-command table work, and immediate
target story creation. Deferred Dossier/Storybook/Doc Web root slimming until a
repo-local trigger exists. Adopted only the low-overhead Conductor review rule
and noted that CineForge already has high-value local ownership through draft
Story 103 AGENTS runbook extraction.

20260520-1317 — build-artifact: created
[Alignment 038](../alignments/align-038-harness-navigation-context-debt-review.md),
updated `docs/align-projects.md`, and linked the result from Scout 039. Build
made no target repo edits and no blanket adoption recommendation.

20260520-1318 — checks-passed: ran `make methodology-compile`,
`make methodology-check`, `make lint`, `make skills-check`, and
`git diff --check`. Restored only the generated
`scripts/__pycache__/methodology_graph.cpython-314.pyc` bytecode noise.

20260520-1350 — validation-complete: findings-first validation found one small
docs consistency issue where Scout 039's pre-inventory scope could be misread
as a live rollout queue after Alignment 038 narrowed the recommendation. Added
a controlling post-inventory note to Scout 039. Re-ran methodology, lint, skill,
and whitespace checks successfully.

20260520-1352 — marked-done: Story 020 had build and validation gates checked,
all acceptance criteria complete, and no target repo edits. Marked done,
updated changelog, and regenerated methodology indexes.
