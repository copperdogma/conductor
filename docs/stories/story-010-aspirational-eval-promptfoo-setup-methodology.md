---
title: "Clarify PromptFoo and Deletion-Eval Setup Guidance"
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
  - "spec:1.2"
  - "spec:2.2"
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

# Story 010 — Clarify PromptFoo and Deletion-Eval Setup Guidance

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Shrink the original aspirational-eval and PromptFoo inbox pressure into the
smallest useful supervisor change.

The evidence pass showed that the tracked product repos already have strong
compromise/eval-ladder guidance: root evals or explicit deferrals, parent
failures, child evals, compromise gates, registry lineage, and phase-aware
`/triage-evals` routing. Story 010 should therefore avoid a redundant
portfolio-wide audit and instead record the decision plus clarify the one vague
setup point: when PromptFoo is the right default and when custom proof surfaces
are more honest.

## Acceptance Criteria

- [x] The story records that existing product-repo methodology already covers
      compromise/deletion eval enforcement strongly enough to avoid a broad
      cross-repo audit.
- [x] The story does not create a new "aspirational eval" lane; it keeps the
      existing terms: compromise eval, deletion gate, simplification baseline,
      eval ladder, and explicit deferral trigger.
- [x] Conductor records the decision in alignment memory and updates
      `docs/align-projects.md`.
- [x] The shared setup-methodology surface clarifies PromptFoo as the default
      when prompt/model comparison or rubric/judge scoring fits, and custom
      runners when structural/runtime/browser/artifact truth is the real proof.
- [x] The shared setup-methodology surface clarifies that new AI compromises
      should attach/create an owning compromise/deletion eval or record an
      explicit deferral trigger.
- [x] Target repos receive only the shared setup-methodology wording update in
      isolated worktrees; no product code, repo-local stories, or repo-local
      inbox notes are changed.
- [x] The inbox items for aspirational evals and PromptFoo setup are removed
      from `inbox.md` after this story became the durable work surface.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Running broad paid model sweeps or long live evals across all projects.
- Changing production model defaults, project runtime behavior, or prompt
  architecture.
- Auditing every tracked repo for missing aspirational/deletion evals without
  fresh evidence of actual drift.
- Adding a new "aspirational eval" lane or recurring audit requirement.
- Forcing PromptFoo into repos or eval lanes where a deterministic script,
  browser proof, visual artifact inspection, or runtime benchmark is the more
  honest substrate.
- Editing target-project primary checkouts in place.
- Changing target-project product code, repo-local stories, or repo-local inbox
  notes.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, ADR-001, ADR-002, current
      setup-methodology guidance, and prior eval/alignment records.
- [x] Confirm the existing eval-ladder, compromise eval, registry, and
      setup-methodology surfaces already cover most of the original pressure.
- [x] Rewrite this story to the smaller accepted scope.
- [x] Produce a Conductor alignment record with the narrowed recommendation and
      no target-repo handoff list.
- [x] Patch the shared setup-methodology surface with the smallest PromptFoo vs
      custom-runner and compromise/deletion-eval wording.
- [x] Update `docs/align-projects.md`.
- [x] Propagate the shared setup-methodology wording to target repos in isolated
      worktrees.
- [x] Confirm repo-local follow-up stories or inbox notes are not warranted now.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] `make skills-check`
- [x] Search docs and update related surfaces.
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

- `docs/stories/story-010-aspirational-eval-promptfoo-setup-methodology.md` —
  story source of truth and work log.
- `docs/alignments/align-026-promptfoo-deletion-eval-setup-guidance.md` —
  alignment record for the narrowed decision.
- `docs/align-projects.md` — index the alignment record if created.
- `.agents/skills/setup-methodology/SKILL.md` — shared setup wording.
- Target repo isolated worktrees under
  `/Users/cam/.codex/worktrees/story010-promptfoo-deletion-eval/` — exact
  shared setup-methodology propagation only.
- `inbox.md` — remove the processed raw capture items now represented by this
  story.

## Notes

- Source inbox items:
  - "Aspriational Eval" cross-repo note, including the Echo Forge
    soundscape-pipeline example.
  - "PromptFoo" setup-methodology note about agents inventing eval harnesses
    from scratch.
- Related handled inbox items:
  - GPT-5.5 Instant routing was already pushed into target repo inboxes.
  - Loop-verify upstream/model-sizing was already handled by Alignment 025 and
    Story 009.
- ADR-001 applies: Conductor should recommend and route, not become the
  canonical copy of every repo's eval system.
- ADR-002 applies: this is an investigative alignment lane first. Promote it
  into setup-methodology defaults only if the audit proves repeated value.
- Scope reduction: the accepted result is a small shared setup-methodology
  wording update and alignment decision, not a broad audit or product-code
  rollout.

## Plan

1. Rewrite this story to record the smaller accepted scope.
2. Create Alignment 026 explaining the existing enforcement and the narrowed
   decision.
3. Patch the shared setup-methodology skill with the two clarified
   setup rules:
   - new AI compromises need an owning compromise/deletion eval or explicit
     deferral trigger
   - PromptFoo is the default for prompt/model/rubric proof, while custom
     runners remain preferred for structural/runtime/browser/artifact proof
4. Propagate the exact shared setup-methodology wording to target repos from
   isolated worktrees because the setup skill is a shared surface.
5. Update `docs/align-projects.md`.
6. Regenerate and check Conductor methodology surfaces:
   `make methodology-compile`, `make methodology-check`, `make lint`,
   `make skills-check`, and `git diff --check`.

## Work Log

20260511-1756 — `/triage inbox` follow-up: created this story from the
highest-leverage live inbox pressure after reconciling the primary Conductor
checkout with current `origin/main`. The loop-verify item is already covered by
Story 009, and the GPT-5.5 Instant item is already routed to target repos, so
this story intentionally owns only the aspirational/deletion eval plus
PromptFoo setup-methodology pressure. Next step: `/build-story 010`.

20260511-1810 - `/build-story 010` exploration: read the story, Conductor
Ideal/spec/state/graph, ADR-001, ADR-002, current setup-methodology guidance,
tracked-project registry, and prior alignment/story hits for aspirational
evals, PromptFoo, and create/improve-eval surfaces. This work belongs in
Conductor because the first-order output is a cross-project recommendation and
setup-methodology decision, not one target repo's implementation. Target
primary checkout state argues against in-place edits: Dossier is behind 1,
Storybook is behind 3 with untracked input PDFs, doc-web is behind 1,
CineForge is behind 4 with modified deploy-log and inbox files, Board Game
Ingester is on an active story branch, RoboRally is behind 2, and Echo Forge is
behind 1. Expected Conductor files are this story, an alignment record, and the
alignment index; setup-methodology and target-repo handoffs stay conditional on
the audit evidence.

20260511-1842 - build complete after scope reduction: shrank Story 010 away
from a broad tracked-repo audit and implemented the small setup-methodology
clarification. Added
Alignment 026, indexed it from `docs/align-projects.md`, clarified
`.agents/skills/setup-methodology/SKILL.md` with PromptFoo-vs-custom-runner
proof-shape guidance and the compromise/deletion-eval deferral rule, and
initially left target repos untouched. Checks passed:
`PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`, `make skills-check`, and
`git diff --check`. Next step: `/validate 010`.

20260511-1846 - learning-review detector: RESULT: no-candidate. Reason: the
scope correction is already covered by Conductor's existing minimal-overhead
and recommendation-first rules, and the story now records the narrowed
decision directly. Evidence checked: Cam's correction, this story, Alignment
026, setup-methodology wording, and the passing build checks.

20260511-1858 - target propagation correction: Cam pointed out that leaving the
target repos untouched was wrong because `.agents/skills/setup-methodology`
is a shared surface. Created isolated worktrees at
`/Users/cam/.codex/worktrees/story010-promptfoo-deletion-eval/` on branch
`codex/story-010-promptfoo-deletion-eval-setup` and propagated the exact shared
setup-methodology wording to Dossier, Storybook, doc-web, CineForge, Board Game
Ingester, RoboRally, and Echo Forge. Target primary checkouts were not touched.
Checks passed: Dossier `PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python make methodology-check skills-check`
plus `git diff --check`; Storybook `bash scripts/sync-agent-skills.sh --check`,
`pnpm methodology:compile`, `npm run methodology:check --silent`, and
`git diff --check`; doc-web `make methodology-check skills-check` plus
`git diff --check`; CineForge `make skills-check`, `pnpm methodology:compile`,
`npm run methodology:check --silent`, and `git diff --check`; Board Game
Ingester `make methodology-check skills-check` plus `git diff --check`;
RoboRally `npm run methodology:check --silent`,
`npm run skills:check --silent`, and `git diff --check`; Echo Forge
`npm run methodology:check --silent`, `npm run skills:check --silent`, and
`git diff --check`. Storybook and CineForge generated date/freshness-only
methodology surface updates during compile.

20260512-0005 - validation: no material findings found. One stale wording issue
was corrected during validation: Alignment 026 still said "Conductor Seed
Change" even though the current scope is shared setup-methodology propagation;
the heading and matching story phrasing now say shared setup surface. Fresh
Conductor checks passed: `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
`PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
`PYTHONDONTWRITEBYTECODE=1 make lint`, `make skills-check`, and
`git diff --check`. Fresh target-worktree checks also passed for Dossier,
Storybook, doc-web, CineForge, Board Game Ingester, RoboRally, and Echo Forge.
Residual limit: this validation was a direct findings-first review plus
repo-native checks, not a `/loop-verify` subagent round. Closure
recommendation: close now via `/mark-story-done 010`.

20260512-0007 - learning-review detector after validation: RESULT:
no-candidate. Reason: Cam's correction exposed an execution miss against an
already-written rule that shared setup skill changes should be copied exactly
to target repos, not a missing workflow guardrail. Evidence checked: Story 010,
Alignment 026, `.agents/skills/setup-methodology/SKILL.md`, target worktree
status/diffs, and fresh validation checks.

20260512-0016 - `/mark-story-done 010`: closure criteria met. Build and
validation gates were checked, Alignment 026 records the narrowed decision and
target rollout evidence, the shared setup-methodology wording landed on target
`main` branches, and remaining work is only Conductor check-in. Target commits:
Dossier `820af37`, Storybook `83f653c`, doc-web `4f62f8a`, CineForge
`dbd688e`, Board Game Ingester `862718d`, RoboRally `3856eae`, Echo Forge
`4c9abaa`. Ran `make methodology-compile` after marking Done.
