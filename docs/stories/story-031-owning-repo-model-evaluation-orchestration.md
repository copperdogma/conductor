---
title: "Owning-Repo Model Evaluation Orchestration"
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
  - "spec:3.1"
  - "spec:3.2"
  - "spec:3.3"
  - "spec:4.1"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.3"
decision_refs:
  - "Alignment 042"
depends_on:
  - "Story 027"
category_refs:
  - "registry-routing"
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

# Story 031 — Owning-Repo Model Evaluation Orchestration

**Priority**: High
**Status**: Done
**Decision Refs**: Alignment 042
**Depends On**: Story 027

## Goal

Make `/evaluate-model <model>` the single Conductor entry point for a complete
cross-project model-evaluation campaign. The first turn verifies current API
existence and access evidence, inspects the tracked portfolio, and returns a
numbered set of recommended repo evaluations plus explicit deferrals. A simple
follow-up such as `yes` or `only do 1, 5, and 6` then authorizes Conductor to
execute the selected work inside isolated owning-repo worktrees.

The owning repository must still control every prompt, fixture, scorer, gate,
credential, artifact, story/attempt/scout convention, and adoption verdict.
Conductor orchestrates the context switch and later synthesizes the results; it
does not become a canonical benchmark harness or call providers from its own
checkout.

## Acceptance Criteria

- [x] A model-only `/evaluate-model` invocation verifies current first-party
      availability evidence, reviews every tracked project, and returns ordered
      positive recommendations with an executable number plus explicit
      evidence-backed `defer`/`do not evaluate` dispositions for all remaining
      projects.
- [x] The recommendation response states each proposed lane, decision, key
      gates, privacy boundary, per-repo spend cap, and campaign maximum, then
      accepts `yes` for all positives or `only do ...`/named repos for a subset.
- [x] After approval, the skill creates or reuses a clean current-base worktree
      for each selected owner, reads that repo's complete instructions and
      local `/evaluate-model` skill when present, and runs its maintained
      progressive evaluation rather than inventing a Conductor benchmark.
- [x] Each owning repo creates only its normal durable evidence surfaces—such
      as a story, attempt, registry row, scout, raw artifact manifest, and
      tests—and issues its own access, transport, reliability, capability,
      economics, and adoption verdict.
- [x] The selection approval authorizes bounded eval work only. It does not
      implicitly authorize private-data use, spend beyond the disclosed cap,
      product-default changes, deployment, commit, push, merge, or destructive
      checkout operations.
- [x] Conductor's AGENTS route, Ideal/spec, Alignment 042, UI metadata, and
      changelog all describe the same two-stage contract without renaming the
      skill or erasing distributed ownership.
- [x] A clean-context forward test demonstrates the intended model-only
      recommendation, subset-selection, owner-context execution, evidence, and
      stop boundaries; methodology, skill, lint, metadata, and diff checks pass.

## Out of Scope

- Building a shared evaluator or copying target fixtures into Conductor.
- Running a live Grok 4.6 campaign as part of this workflow-contract change.
- Automatically evaluating **Defer** or **Do not evaluate** projects because
  they appear in the portfolio inventory.
- Silent prompt, golden, scorer, privacy, runtime-default, deployment, commit,
  push, merge, or remote changes.
- Modifying any target project's primary checkout or the unrelated Story
  029/030 work in Conductor's primary checkout.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, registry, prior model scout,
      Story 027, and Alignment 042 context
- [x] Rewrite the Conductor `/evaluate-model` entry contract and factor the
      detailed owner-run protocol into progressive-disclosure reference guidance
- [x] Align AGENTS, Ideal/spec, Alignment 042, UI metadata, and changelog
- [x] Run an independent clean-context behavior review and repair real gaps
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: not applicable; no executable script or repo-check change
- [x] Search docs and update any related current surfaces
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

- `.agents/skills/evaluate-model/SKILL.md` — two-stage portfolio recommendation
  and approved owning-repo orchestration contract.
- `.agents/skills/evaluate-model/references/owning-repo-execution.md` — detailed
  provider-native qualification and repo-local evaluation protocol loaded only
  during execution.
- `.agents/skills/evaluate-model/agents/openai.yaml` — accurate invocation copy.
- `AGENTS.md` — advertise recommendation-first orchestration and repo-local runs.
- `docs/ideal.md` and `docs/spec.md` — preserve distributed ownership while
  authorizing selected repo-local execution after approval.
- `docs/alignments/align-042-provider-native-model-evaluation.md` — evolve the
  historical handoff boundary into the current orchestration boundary.
- `docs/stories/story-027-provider-native-model-evaluation.md` — label its
  handoff-only boundary historical while retaining its provider safeguards.
- `CHANGELOG.md` — record the user-visible skill behavior change.
- `docs/stories/story-031-owning-repo-model-evaluation-orchestration.md` — plan,
  acceptance contract, and build evidence.
- Generated `docs/stories.md` and `docs/methodology/graph.json` — compiled story
  indexes.

## Notes

- Cam approved this exact direction after comparing rename versus behavior
  change: retain the public `evaluate-model` name and make it orchestrate owner
  work rather than turning Conductor into a model client.
- Cam's ordinary invocation is `evaluate-model grok 4.6`. The first response
  should answer existence, portfolio fit, and per-repo recommendation. The next
  `yes` means all positively recommended numbered runs; `only do 1, 5, and 6`
  means that subset.
- Story 031 is intentional. The primary checkout contains unrelated untracked
  Story 029 and Story 030 work, so this clean branch reserves the next
  non-colliding identifier without importing or modifying those files.
- Recommendation-first does not mean handoff-only. The recommendation and
  selection gate comes first; execution then occurs under each selected repo's
  authority and local methodology.

## Plan

1. Replace the handoff-only Conductor mode with a two-stage portfolio contract:
   verify the model and map repo fit first, then wait for all/subset selection.
2. Define the approval grammar and its exact authority, including disclosed
   campaign spend, isolated worktrees, repo-local evidence, and explicit
   exclusions for private data, defaults, remotes, and higher spend.
3. On selection, require a true owner-context switch: read the target's
   instructions and local skill completely, use its maintained decision lane,
   and create the artifacts that repo normally requires.
4. Move detailed transport, fairness, progressive-run, failure-classification,
   provenance, and verdict guidance into an owner-execution reference so the
   common discovery turn stays compact.
5. Align root routing, product intent, spec, Alignment 042, UI copy, and
   changelog; compile generated methodology surfaces.
6. Give the final bytes to an independent worker with only representative
   invocations and ask it to identify ambiguity, overreach, or missing evidence.
   Repair material findings, then run all relevant checks.

**Autonomy**: Go after approval. Cam approved this exact bounded skill and
methodology change with `Sounds good. Go ahead.` No live model campaign,
target-repo write, provider spend, default change, commit, push, or merge is
part of this story. Pause if implementation would require any of those actions.

## Work Log

- 20260819-2307 — story-created-and-approved: read the current Conductor
  handoff-only skill, Story 027, Alignment 042, Ideal/spec/state, project
  registry, and Grok 4.6 Scout 053. Cam's approval satisfies the build-story
  plan gate. Created an isolated current-base Conductor worktree so unrelated
  primary-checkout Story 029/030 and scout/alignment work remain untouched.
- 20260819-2312 — implementation: rewrote `/evaluate-model` around a model-only
  recommendation stage and an explicitly selected owner-execution stage; added
  stable positive-only numbering, per-repo and campaign spend ceilings,
  all/subset parsing, isolated owner-context worktrees, normal repo-local
  story/scout/attempt/registry evidence, and separate closeout authority. Moved
  provider-native qualification, fairness, progressive gates, failure triage,
  privacy, provenance, and layered verdicts into a reference loaded only for
  execution. Aligned AGENTS, Ideal/spec, UI metadata, changelog, and Alignment
  042; marked Story 027's handoff boundary historical.
- 20260819-2318 — independent-forward-review-and-repair: three clean-context
  workers exercised `evaluate-model grok 4.6`, `yes`, subset selection,
  unnumbered repo overrides, read-only audit, protocol regression, and surface
  consistency. Accepted findings required a new numbered approval for a
  previously deferred repo, exact disposition vocabulary, no Stage 1 target
  credentials, semantic equivalence before reusing portfolio approval for a
  local plan gate, and fresh artifact identities plus uncached subject calls.
  After repairs, all three reviewers reported no material findings.
- 20260819-2321 — validation-complete: fresh `make methodology-compile`,
  `make methodology-check`, `make lint`, `make skills-check`, metadata-contract
  parsing, and `git diff --check` passed. The generic skill-creator validator
  remains incompatible with Conductor's required `user-invocable` extension;
  its initial environment also lacked PyYAML, while the repo-native skill check
  and explicit YAML/UI contract check passed. `make test` was not applicable
  because no script or repo-check code changed. `codex review` was skipped for
  this documentation/skill authority contract; three independent contract
  reviews provided the relevant signal. Learning review returned
  `RESULT: no-candidate` because the user correction is already fully codified
  in the live skill, AGENTS, spec, story, and alignment. Story is validated and
  ready for closeout; no commit, push, merge, target eval, or provider spend
  occurred.
- 20260819-2324 — story-closed: `/mark-story-done` confirmed every substantive
  acceptance criterion, task, Build gate, and Validation gate is complete.
  Updated status to Done and queued a fresh methodology compile/check before
  check-in. Story closure adds no target-repo work or broader authority.
- 20260819 — live-campaign orchestration correction: Cam clarified during the
  first multi-repo Grok 4.6 campaign that separate owning repositories should
  be executed by separate subagents, with Conductor's root agent acting as
  scope/cost coordinator and final judge. Added that rule to Stage 2, including
  per-worker repo/cap/privacy isolation and an explicit ban on delegation
  broadening authority. The generic skill-creator validator again reached the
  skill but rejected the pre-existing Conductor `user-invocable` extension;
  `git diff --check` passed. Echo Forge and Storybook were then assigned to
  independent owning-repo workers under their previously approved caps.
- 20260820 — live-campaign efficiency and evidence follow-up: Cam approved the
  audit recommendations while preserving each target repo's native
  attempt/registry/story vocabulary. Added a zero-cost resolved-harness
  topology preflight, fail-closed handling for known-invalid aggregate
  commands, durable raw/sanitized artifact requirements, proportional
  dependency-aware validation, dispatch-before-provider-call coordination, and
  mandatory Conductor campaign follow-through when execution differs from the
  dated scout recommendation. Updated Scout 053 with the user-selected Echo
  Forge and Storybook results without rewriting its original recommendation.
