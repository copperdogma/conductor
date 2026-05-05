---
title: "Add Reviewed Learning Candidate Workflow"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I5"
spec_refs:
  - "spec:3.2"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.2"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
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

# Story 008 — Add Reviewed Learning Candidate Workflow

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn Scout 029's strongest holaOS takeaway into a small Conductor-native
workflow: agents should notice durable workflow-learning opportunities at the
end of selected work episodes, draft inspectable candidates when evidence is
real, and keep live skills, policy, and durable memory unchanged until an
explicit review/promote step.

This should give Cam compounding workflow improvement without adding a heavy
runtime, daemon, per-run manifest system, or reflection spam. The default result
of the detector should be "no learning candidate."

## Acceptance Criteria

- [x] Conductor adds a `learning-review` skill that evaluates completed work
      episodes for reusable workflow corrections with a strict no-candidate
      default.
- [x] Conductor adds a `learning-candidate` skill or equivalent writer that
      turns a warranted finding into a structured draft candidate without
      changing live skills, policy, memory, or target projects.
- [x] The candidate lifecycle is explicit: normal promotion goes
      `Draft -> Proposed -> Accepted -> Promoted`, while dismissal goes
      `Draft -> Proposed -> Dismissed`; an accepted candidate can move to
      `Dismissed` only before promotion when Cam explicitly reverses
      acceptance; dismissed candidates remain terminal unless fresh evidence
      reopens them.
- [x] Candidate storage is lightweight and inspectable, with clear fields for
      target surface, evidence summary, proposed change, trigger/cadence,
      promotion gate, status, source runs, and user corrections.
- [x] The selected closeout workflows call or reference `learning-review` only
      where it is likely to help: `/validate`, `/finish-and-push`,
      `/loop-verify`, noisy or failed `/build-story`, and explicit user
      correction cases.
- [x] The workflow rejects candidates based only on novelty, vibes, one-off
      success, generic process advice, or model-era harness compensations that
      are likely to become obsolete.
- [x] At least one repo-local dry-run or fixture example proves the detector can
      say both "no candidate" and "candidate warranted" without creating live
      changes.
- [x] The story leaves a clear recommendation on whether to keep the workflow
      Conductor-only, roll it into shared methodology, or discard/reshape it
      after local use.
- [x] The reviewed-learning workflow is rolled out to each tracked target repo
      from isolated worktrees, with repo-local adaptation where local skills
      differ.
- [x] Each target repo receives the two learning skills, lightweight candidate
      docs/template/examples, generated wrappers where applicable, and selected
      closeout-skill hooks without changing live candidate status or memory.
- [x] Cross-repo rollout evidence is recorded in an alignment note, including
      target worktrees, validation commands, known local limits, and any
      intentional divergence.
- [x] `/loop-verify` runs across the rollout scope until one full round finds no
      material issues or an unresolved blocker is reported honestly.

## Out of Scope

- Building a background daemon, automatic run scanner, database-backed memory
  system, or always-on self-improvement service.
- Automatically mutating live `.agents/skills/`, `AGENTS.md`, methodology docs,
  memory files, or target-project repos from a candidate.
- Creating a full per-run capability manifest system.
- Treating ordinary successful work as a reason to draft process changes.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Re-read Scout 029 and this planning discussion to preserve the actual
      decision: borrow reviewed learning, not the holaOS runtime
- [x] Design `learning-review`:
  - [x] define eligible trigger points
  - [x] define the no-candidate default and rejection rules
  - [x] define evidence thresholds for user corrections, repeated friction,
        repeatable procedure discovery, missing guardrails, and high-risk
        failures
  - [x] define the exact output contract
- [x] Design `learning-candidate`:
  - [x] decide whether it is a second skill or a writer section inside
        `learning-review`
  - [x] define candidate file location, naming, status lifecycle, and required
        fields
  - [x] define promotion gates and what "promoted" means for each target type:
        skill patch, runbook/methodology doc, memory, alignment note, or no
        current target
- [x] Implement the selected Conductor skill(s), docs, and any candidate
      template/index files
- [x] Wire the detector into selected closeout skills with minimal ceremony and
      no requirement to draft when the answer is no
- [x] Add at least one example or fixture that demonstrates:
  - [x] no candidate from ordinary clean work
  - [x] candidate warranted from a concrete user correction or repeated
        workflow failure
- [x] Update related scout or alignment memory if applicable, including a link
      back to Scout 029
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` — skipped; no scripts
        or repo checks changed
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead
- [x] Create a cross-project alignment record for the approved rollout decision
- [x] Prepare isolated worktrees for Dossier, Storybook, doc-web, CineForge,
      Board Game Ingester, Robo Rally, and Echo Forge
- [x] Apply the portable learning-review and learning-candidate surfaces to
      each target repo with repo-local hook adaptation
- [x] Regenerate skill wrappers or methodology surfaces required by each target
      repo
- [x] Run repo-local validation in each target worktree
- [x] Run `/loop-verify` over the full Conductor plus target-repo rollout scope
      and rerun after material fixes until a full round is clean

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `.agents/skills/learning-review/SKILL.md` — detector skill for deciding
  whether a completed work episode revealed a durable workflow-learning
  candidate.
- `.agents/skills/learning-candidate/SKILL.md` — likely writer/promoter skill
  for structured candidate drafts, unless implementation proves one combined
  skill is simpler.
- `docs/learning-candidates/` — candidate template/index if a dedicated
  candidate surface earns its keep.
- `.agents/skills/validate/SKILL.md` — closeout hook for learning review after
  meaningful validation outcomes.
- `.agents/skills/finish-and-push/SKILL.md` — closeout hook for learning review
  after full landing runs.
- `.agents/skills/loop-verify/SKILL.md` — closeout hook for learning review
  after repeated parallel review/fix loops.
- `.agents/skills/build-story/SKILL.md` — optional hook for failed/noisy builds
  only, if the implementation can keep it non-intrusive.
- Generated skill wrapper surfaces such as `.gemini/commands/*.toml` if
  Conductor's skill sync requires them.
- `docs/alignments/align-024-reviewed-learning-rollout.md` — approved
  cross-project rollout record and evidence trail.
- `docs/scout/scout-029-holaos-environment-engineering.md` — link the scout
  finding to this story if not already linked.
- `docs/methodology/graph.json` — generated story graph.
- `docs/stories.md` — generated story backlog view.

## Notes

- Scout 029 concluded that holaOS should not replace Cam's distributed
  workflow. Its highest-value idea is the reviewed learning boundary:
  auto-draft or propose candidates, never silently mutate live behavior.
- The target shape discussed with Cam is two small skills:
  `learning-review` as a detector and `learning-candidate` as a writer/review
  workflow.
- The detector should only consider completed work episodes, not every chat
  turn. Good trigger points include `/finish-and-push`, `/validate`,
  `/loop-verify`, failed/noisy `/build-story`, explicit user corrections, and
  repeated same-class friction.
- Promotion should require concrete evidence. One strong user correction, a
  repeated failure pattern, or a high-risk process miss can warrant a proposal.
  Generic "this felt useful" should not.
- The implementation should preserve Conductor's existing lightweight style.
  If a new candidate folder feels too heavy during build, the story should
  document the simpler alternative rather than force a new artifact surface.

## Local Adoption Recommendation

Conductor-local `/loop-verify` has now proven the shape enough to justify a
tracked-repo rollout, and Cam approved beginning that rollout. The adoption
stance is still "portable meaning with local adaptation": copy the lightweight
learning surfaces and hook them into compatible closeout skills, but do not
introduce a daemon, canonical core, automatic promotion, or exact-text sync
requirement.

After rollout, keep the workflow under review and promote future changes only
when it proves one of these:

- it catches at least two real same-class workflow corrections without creating
  reflection noise
- it turns one explicit high-value user correction into a clean promoted skill
  or runbook patch
- it gives `/validate`, `/finish-and-push`, or `/loop-verify` a clearer
  closeout path without increasing ordinary successful-run overhead

Discard or reshape it if most invocations produce speculative candidates, if
agents start treating clean work as a reason to draft, or if model improvements
make the proposed guardrails feel like stale harness compensation.

## Plan

- Add two Conductor-local skills:
  - `.agents/skills/learning-review/SKILL.md` as the detector with a strict
    no-candidate default, trigger boundaries, rejection rules, and an exact
    output contract.
  - `.agents/skills/learning-candidate/SKILL.md` as the structured
    draft/review/promote workflow for warranted findings.
- Add lightweight candidate storage under `docs/learning-candidates/` with a
  README, template, and dry-run examples for both `no-candidate` and
  `candidate-warranted` outcomes.
- Wire the detector into selected closeout skills only:
  `/validate`, `/finish-and-push`, `/loop-verify`, and noisy or failed
  `/build-story` runs.
- Regenerate any skill wrappers and methodology surfaces required by the new
  skills.
- Manually inspect the new learning workflow against Scout 029, ADR-001,
  ADR-002, and the minimal-overhead tenet.
- Run:
  - `make methodology-compile`
  - `make methodology-check`
  - `make lint`
  - `make skills-check`
  - `git diff --check`

## Work Log

20260505-0000 — story created from Scout 029 follow-up discussion: scoped to
Conductor-only reviewed learning candidates before any target-project rollout.

20260505-0010 — `/build-story` exploration complete. Scope stays Conductor-only;
no tracked project repos require worktree isolation. Planned file changes are
two local skills, candidate storage docs/examples, narrow closeout-skill hooks,
generated skill wrappers, and generated methodology story surfaces. Main risk is
turning useful learning into recurring reflection overhead, so the detector will
default to no candidate and reject novelty, vibes, one-off success, generic
advice, and model-era compensations.

20260505-0025 — build implementation complete. Added `learning-review`,
`learning-candidate`, `docs/learning-candidates/` README/template/examples,
generated Gemini wrappers, and narrow hooks in `/validate`, `/finish-and-push`,
`/loop-verify`, and noisy/failed `/build-story`. Ran
`make methodology-compile`, `make methodology-check`, `make lint`,
`make skills-check`, and `git diff --check`; all passed. `make test` was
skipped because no scripts or repo checks changed.

20260505-0714 — `/loop-verify` refinement found and fixed material guardrail
gaps after the initial build: candidate storage fields/examples now carry
source runs, user corrections, review cadence, and promotion gates; the
lifecycle now keeps dismissed candidates terminal unless fresh evidence reopens
them; accept/promote paths require the candidate to pass through `Proposed` and
`Accepted`; and closeout hooks skip ordinary success while blocking promotion
unless Cam separately approves it. Story status remains `In Progress`,
validation remains open, and the recommendation remains Conductor-only through
validation and first local use.

20260505-0730 — continued `/loop-verify` refinement tightened the core contract
further: candidate required fields now separate `source runs`, `user
corrections`, and `evidence summary`; `Promoted` is terminal/idempotent; no-op
lifecycle requests return `RESULT: candidate-unchanged`; accept/dismiss mode
cannot perform promotion directly; and examples now prove both candidate-file
and live-change outcomes. The invariant is now explicit: closeout workflows may
report or draft warranted candidates, but live promotion is a separate reviewed
operation.

20260505-0742 — `/loop-verify` refinement aligned the required-evidence rule
across the skill and candidate docs: missing user corrections must be recorded
as `none recorded`, but missing concrete source runs or evidence summary blocks
drafting, proposal, acceptance, and promotion rather than encouraging
fabricated provenance.

20260505-0752 — Round 12 correctness pass aligned Story 008 and Scout 029 with
the current lifecycle contract: accepted candidates may be dismissed only before
promotion when Cam explicitly reverses acceptance; dismissed candidates require
fresh evidence before reopening; and promoted candidates remain terminal.

20260505-0758 — `/loop-verify` converged after a correctness-only Round 13.
Final clean shards covered the core learning skills, closeout hooks and Gemini
wrappers, candidate docs/examples, and Story 008/Scout 029/generated surfaces.
No material issues or blockers remained. The final learning-review result for
this loop is `RESULT: no-candidate`: the reusable corrections found by the
loop were all in scope for Story 008 and were applied directly to the reviewed
learning workflow, so there is no separate candidate to draft.

20260505-0806 — Cam approved expanding Story 008 from Conductor-local
incubation into a tracked-repo rollout. Scope now includes Dossier, Storybook,
doc-web, CineForge, Board Game Ingester, Robo Rally, and Echo Forge, with
isolated target worktrees, a new alignment record, repo-local validation, and
another `/loop-verify` pass required before closeout.

20260505-0928 — tracked-repo rollout implemented in isolated worktrees under
`/Users/cam/.codex/worktrees/story008-reviewed-learning/` on branch
`codex/story-008-reviewed-learning-rollout`. Each target repo now has
`learning-review`, `learning-candidate`, lightweight candidate docs/examples,
generated Gemini wrappers, and narrow closeout hooks in `/build-story`,
`/validate`, `/finish-and-push`, and `/loop-verify`. Product repos use a
repo-local candidate contract: candidates may promote local skills/docs only,
outside-repo or global-memory changes are routing needs, and cross-project
methodology still requires a Conductor alignment/story route.

20260505-0934 — rollout `/loop-verify` converged after four full rounds. Rounds
1-3 found material issues and reset the loop: stale Conductor-only wording in
target docs, lifecycle mismatch between skill and README, promote semantics for
bare `Proposed` candidates, target-repo outside-repo/memory promotion wording,
and one Storybook-specific skill-check command. Round 4 returned clean across
all four original shards: Conductor supervisor artifacts, Dossier/Storybook,
doc-web/CineForge, and Board Game Ingester/Robo Rally/Echo Forge. Final
learning-review result for this loop is `RESULT: no-candidate`; every finding
was a Story 008 rollout correctness issue and was fixed directly in scope.

20260505-1758 — `/mark-story-done`: Story 008 closed after fresh validation and
target-repo landing. Target commits pushed to remote `main`: Dossier `b4faec2`,
Storybook `f2888ac`, doc-web `65c30d4`, CineForge `4ae4b9d`, Board Game
Ingester `8e8026e`, Robo Rally `14bff21`, and Echo Forge `5e79523`. Conductor
validation passed with `methodology-check`, `skills-check`, `lint`, `test`, and
`git diff --check`; target repo validation passed with repo-local skill,
methodology, lint/test, or validate commands as recorded in Alignment 024.
