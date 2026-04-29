---
title: "Review Core Story Loop Subagent Contracts"
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
  - "005"
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

# Story 006 — Review Core Story Loop Subagent Contracts

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: Story 005

## Goal

Decide whether the tracked repos' core story loop skills should gain explicit
subagent and verify-loop contracts after the successful `/triage` orchestration
rollout.

The live question is specific but cross-repo: `/create-story`, `/build-story`,
and `/validate` may benefit from contracted sidecar work, but each skill and
each repo has different risk. This story should examine the other repos before
deciding what to upgrade, preserve the useful pattern from Story 005, and avoid
turning every routine story action into a heavy multi-agent process. The result
should make Cam's story workflow easier to trust and review, not more
bureaucratic.

After the skill decisions land, the shared `/setup-methodology` surface across
the tracked repos must also be updated so newly bootstrapped or refreshed repos
receive the same core-loop guidance. That setup surface should remain identical
across the repos where it is intended to be shared; any Conductor-specific
exception must be called out explicitly rather than left as silent drift.

## Acceptance Criteria

- [x] The current `/create-story`, `/build-story`, and `/validate` skills are
  reviewed across Conductor and the tracked product repos against each repo's
  local `docs/ideal.md`, `docs/spec.md`, Story 005, Alignment 017,
  Alignment 018, ADR-001, and ADR-002.
- [x] The story records a per-repo, per-skill decision: upgrade now, adapt
  later, keep local, or explicitly reject, with the reason and expected user
  impact.
- [x] Any upgraded skill keeps the main thread as the intent, Ideal/spec, and
  final-disposition arbiter; subagents gather evidence or execute bounded
  sidecar tasks only.
- [x] Any verify-loop guidance is scoped to cases where repeated parallel
  review is materially useful, not ordinary single-file or low-risk work.
- [x] After the core loop skill decisions are implemented, each tracked repo's
  shared `/setup-methodology` surface is updated to incorporate the new
  guidance and checked for exact identity where it is intended to be identical.
- [x] If a skill changes, wrappers or generated skill surfaces are refreshed as
  required by the repo's existing checks.
- [x] The routed inbox item is removed from `inbox.md`, leaving no stale local
  pressure behind.

## Out of Scope

- Reopening Story 005 or changing the already-landed `/triage` orchestration
  contract.
- Blanket-syncing changes into tracked product repos before the cross-repo
  review shows they are valuable there.
- Adopting Symphony, Linear, or an always-on orchestration service.
- Making subagents mandatory for routine story creation, small validation
  checks, or work where the next local step is blocked on the same answer.
- Replacing `/loop-verify`; this story may reference it, but should not create
  a competing verification-loop skill.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, story, alignment, and
  decision context.
- [x] Review current `.agents/skills/create-story/SKILL.md`.
- [x] Review current `.agents/skills/build-story/SKILL.md`.
- [x] Review current `.agents/skills/validate/SKILL.md`.
- [x] Inspect the other tracked repos' current `/create-story`, `/build-story`,
  and `/validate` surfaces, using isolated worktrees before making any target
  repo edits.
- [x] Compare each skill against the Story 005 / Alignment 018 subagent
  principles:
  - [x] subagents return neutral evidence or bounded sidecar results
  - [x] the main thread keeps the north star and final judgment
  - [x] delegation is useful only when it does not block the immediate next
    local step
  - [x] sequential fallback is explicit when subagents are unavailable or not
    safe
  - [x] verify-loop use is tied to material review/fix rounds
- [x] Decide whether each repo/skill combination should be upgraded, adapted
  later, kept local, or rejected.
- [x] Implement only the warranted Conductor and target-repo skill changes in
  the correct checkout/worktree.
- [x] Update the shared `/setup-methodology` surface across the tracked repos
  after the core skill changes are settled, preserving exact identity where
  that surface is intended to be identical.
- [x] Update related alignment or story memory with the cross-repo decision and
  any intentional local differences.
- [x] Normalize `inbox.md` after routing the original note.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
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

- `.agents/skills/create-story/SKILL.md` — candidate subagent contract for
  story scoping, codebase exploration, and best-practice research in each repo
  where the review warrants it.
- `.agents/skills/build-story/SKILL.md` — candidate sidecar work and
  verification guidance while implementation proceeds in each repo where the
  review warrants it.
- `.agents/skills/validate/SKILL.md` — candidate parallel validation and
  holistic review guidance in each repo where the review warrants it.
- `.agents/skills/setup-methodology/SKILL.md` — shared setup surface that must
  incorporate the accepted core-loop guidance across tracked repos after the
  decisions land.
- `docs/stories/story-006-core-loop-subagent-contract-review.md` — story
  source of truth and work log.
- `inbox.md` — remove the routed raw capture item.
- `docs/alignments/` and `docs/align-projects.md` — record the cross-repo
  decision, shared setup-methodology identity rule, and any intentional local
  differences.

## Notes

- The inbox item that created this story asked whether `/create-story`,
  `/build-story`, and `/validate` should use subagents and verify-loop
  patterns.
- Cam clarified that the real ask is to examine the other repos to decide
  whether they would benefit from these upgrades, not just to patch Conductor.
- Cam also clarified that the final rollout should update `/setup-methodology`
  across the repos, and that the shared setup-methodology surface should be
  identical where it is intended to be shared.
- Story 005, Alignment 017, and Alignment 018 already cover `/triage` and the
  shared `loop-verify` skill. This story should not treat that completed work
  as live pressure.
- ADR-001 keeps Conductor recommendation-first and prevents this from becoming
  a canonical shared core by accident.
- ADR-002 says new investigative lanes or repeated review loops must earn their
  overhead by solving a real repeated problem.

## Plan

### Current Read

- `/create-story` is currently lightweight and deterministic. It checks whether
  a new story is warranted, runs `start-story.sh`, fills story metadata, and
  compiles the graph. Conductor's copy has no explicit sidecar exploration
  contract; the target repos still need to be inspected before deciding whether
  this is a shared gap.
- `/build-story` already has the strongest process boundary: explore, write a
  plan, pause for approval, then implement. Any subagent guidance must preserve
  that human gate and avoid delegating the immediate blocking decision. The
  target repos may have stronger local build-story contracts that should be
  preserved rather than overwritten.
- `/validate` already requires fresh diff review, story acceptance review,
  honest checks, output inspection, and a disposition. It is the most natural
  place for bounded parallel validation or `/loop-verify` escalation because it
  happens after implementation and can benefit from independent review shards.
  The cross-repo pass must confirm whether each repo already has comparable
  guidance.

### Proposed Decisions

- `/create-story`: likely upgrade narrowly where the repo would benefit. Add
  optional sidecar evidence gathering
  for non-trivial story creation, such as codebase impact scans, relevant prior
  story/alignment lookup, or source-specific research. Do not add a verify-loop
  default; story creation should stay cheap and main-thread owned.
- `/build-story`: likely upgrade moderately where the repo would benefit. Add
  guidance that after the plan gate,
  subagents may handle independent sidecar work such as bounded exploration,
  disjoint implementation slices, tests, or review of already-written changes.
  Preserve the current pause-before-implementation gate.
- `/validate`: likely strongest upgrade where the repo would benefit. Add
  optional parallel validation packets for
  changed-file review, acceptance criteria review, test/check execution, and
  holistic architecture or intent review. Add a rule for when to escalate to
  `/loop-verify`: broad/high-risk diffs, repeated material fixes, cross-repo
  rollout surfaces, or validation where one complete clean round matters.
- `/setup-methodology`: update after the accepted core-loop guidance lands so
  the setup package installs or refreshes the same story-loop expectations
  across tracked repos. Preserve exact identity for the shared setup surface;
  record any justified exception explicitly.

### Final Decisions

- All eight tracked repos were upgraded for `/create-story`, `/build-story`,
  and `/validate` because the same optional, bounded subagent guidance improves
  story quality without making routine work heavier.
- The core story-loop skill texts remain repo-local rather than byte-identical,
  preserving each repo's existing story, build, and validation details.
- `/setup-methodology` is now byte-identical across all eight repos and uses
  repo identity to distinguish product setup from Conductor's supervisor
  package.
- Alignment 019 records the cross-repo decision and validation evidence.

### Concrete File Changes

- Inspect each tracked repo's `.agents/skills/create-story/SKILL.md`,
  `.agents/skills/build-story/SKILL.md`, `.agents/skills/validate/SKILL.md`,
  and `.agents/skills/setup-methodology/SKILL.md` before edits.
- Update `.agents/skills/create-story/SKILL.md` where warranted with an
  "Optional sidecar evidence" section and guardrails that keep the main thread
  responsible for the story boundary and final artifact.
- Update `.agents/skills/build-story/SKILL.md` where warranted with a
  "Delegation after the plan gate" section. The guidance should say subagents
  can run in parallel only for non-blocking, bounded work with clear ownership
  and disjoint write scopes.
- Update `.agents/skills/validate/SKILL.md` where warranted with a "Parallel
  validation and loop-verify escalation" section. The guidance should require
  fresh evidence, bounded validation packets, and main-thread synthesis of the
  final disposition.
- Update the shared `.agents/skills/setup-methodology/SKILL.md` surface across
  tracked repos after the core skill edits settle, ensuring the setup package
  incorporates the accepted guidance and remains identical where intended.
- Update this story with the per-skill final decisions, work-log evidence, task
  checkboxes, and build-complete gate once implementation is done.
- Add a Conductor alignment entry capturing the cross-repo decision and any
  intentional repo-local differences.
- Leave `inbox.md` as `No live items.` unless a new raw note arrives.

### Expected Outputs

- The cross-repo review says which repos and skills benefit from the upgrades,
  rather than assuming one answer for every checkout.
- The accepted core loop skills describe when subagents help and when they add
  overhead, in each repo where the guidance lands.
- Routine story creation and ordinary validation remain lightweight.
- Bigger story work gets clearer hooks for evidence gathering, sidecar
  implementation, and independent validation.
- Shared setup-methodology installs or refreshes the accepted story-loop
  guidance consistently across the tracked repos.
- Story 006 records the reasoning so a later alignment pass can decide whether
  any pattern should sync to target repos.

### Manual Inspection

- Confirm the final skill text does not imply subagents are mandatory.
- Confirm `/build-story` still clearly pauses before implementation.
- Confirm `/validate` still produces one final disposition and yes-ready next
  step, rather than delegating judgment to reviewers.
- Confirm target-project edits happen only in dedicated worktrees/branches
  unless explicitly approved otherwise.
- Confirm the setup-methodology files that should be identical are actually
  byte-identical after sync.

### Checks

- `make methodology-compile`
- `make methodology-check`
- `make skills-check`
- `make lint`
- `git diff --check`
- `make test` only if scripts or repo checks change; the planned work is skill
  and story text only, so this should not be required unless implementation
  broadens.
- Repo-native wrapper, methodology, lint, test, and diff checks for any target
  repo that receives changes.

## Work Log

20260428-2040 — story-created: created Story 006 from the remaining Conductor
inbox item after routing the already-handled `/triage` and `loop-verify` parts
to Story 005 plus Alignments 017-018. Next step is `/build-story 006` to
evaluate the three core loop skills and make only the warranted local changes.

20260428-2048 — build-story-exploration: read Story 006, Conductor Ideal/Spec,
state/graph, ADR-001, ADR-002, Alignment 017, Alignment 018, Story 005, and the
current Conductor `/create-story`, `/build-story`, and `/validate` skills. The
initial plan was too Conductor-local and is superseded by Cam's clarification
that the story must examine the other repos before deciding where upgrades
belong.

20260428-2057 — scope-corrected: updated the story to make the work
cross-repo. The build must inspect each tracked repo's core story loop skills,
record per-repo/per-skill decisions, implement only warranted changes in the
right worktrees, and then update the shared `/setup-methodology` surface across
the repos so refreshed methodology packages incorporate the accepted guidance
with exact identity where intended.

20260428-2131 — loop-verify-converged: ran `/loop-verify` over four shards:
`create-story`, `build-story`, `validate`, and `setup-methodology`. Round 1
found material missing-contract issues in all four shards and fixed them.
Round 2 found stale generated setup wrappers and missing validate fallback
language, then fixed both. Round 3 returned clean across the full original
scope. Setup-methodology is byte-identical across all eight repos with hash
`d86cdd2f5ce279d6f28130016699c88c367ff3241a1ab9a1da131c7daf747680`.

20260428-2131 — build-complete: updated Conductor and the seven isolated target
worktrees under `/Users/cam/.codex/worktrees/story006-core-loop/`. The accepted
changes add optional sidecar evidence for `/create-story`, post-plan bounded
delegation for `/build-story`, optional parallel validation and `/loop-verify`
escalation for `/validate`, and shared setup-methodology refresh guidance. Also
created Alignment 019 and updated `docs/align-projects.md`. Validation evidence:
Conductor methodology/skills/lint/diff checks passed; Dossier methodology,
skills, and diff checks passed with known unrelated broad-lint failures; all
target repo wrapper/methodology/diff checks passed; Storybook lint and
triage-facts checks passed using a temporary primary `node_modules` symlink;
doc-web lint passed; CineForge methodology and wrapper checks passed with
known unrelated broad-lint failures and existing architecture/UI freshness
warnings; Board Game Ingester methodology/wrapper/diff checks passed; Robo
 Rally `npm run validate` passed; Echo Forge methodology/lint/triage-facts
checks passed using a temporary primary `node_modules` symlink. Build is ready
for `/validate 006`.

20260428-2138 — validate-complete: ran fresh `/validate 006` evidence against
the current diff and the isolated target worktrees. Conductor passed
`make methodology-compile`, a sequential `make methodology-check`,
`make skills-check`, `make lint`, `make test`, and `git diff --check` after
discounting a transient parallel compile/check race. Target repo touched-surface
checks passed in Dossier, Storybook, doc-web, CineForge, Board Game Ingester,
Robo Rally, and Echo Forge. Setup-methodology remains byte-identical across all
eight repos with hash
`d86cdd2f5ce279d6f28130016699c88c367ff3241a1ab9a1da131c7daf747680`, and the
temporary Storybook/Echo Forge `node_modules` symlinks were removed. Validation
disposition: Met, with only pre-existing Dossier/CineForge health warnings
remaining outside this rollout.

20260428-2145 — story-done: marked Story 006 done after landing the linked
target repo commits to `main`: Dossier `f5bf1c3`, Storybook `ea4ceaf`,
doc-web `e224844`, CineForge `08a9655`, Board Game Ingester `a279158`, Robo
Rally `c523607`, and Echo Forge `2d2650f`. The Conductor close-out will land
the story, Alignment 019, Scout 025, inbox routing, and shared skill updates in
the supervisor repo.
