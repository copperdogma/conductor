---
title: "Qualify SkillEvaluator for Conductor Skill Intake"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I3"
  - "I5"
spec_refs:
  - "spec:3.1"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.2"
  - "spec:5.3"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on:
  - 22
category_refs:
  - "scouting"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
---

# Story 030 — Qualify SkillEvaluator for Conductor Skill Intake

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: Story 022

## Goal

Determine whether NVIDIA SkillEvaluator is useful to the Conductor agent as a
bounded qualification tool when Cam supplies a new skill or when Conductor
later discovers candidate skills for the tracked portfolio.

The intended user is Conductor itself. Product repositories remain the owners
of their local skills and truth surfaces; this spike should help Conductor
decide whether a candidate skill is well formed, relevant, non-duplicative, and
behaviorally useful before recommending anything downstream.

This matters because a future recurring skill-discovery pass could otherwise
rank candidates by descriptions, popularity, or intuition. SkillEvaluator may
add reproducible quality and with-skill/without-skill evidence, but only if its
reports improve Conductor's judgment without creating a heavyweight canonical
skill harness or replacing repo-native verification.

## Acceptance Criteria

- [x] The exact SkillEvaluator revision, installation boundary, license,
      runtime dependencies, data exposure, credential behavior, local writes,
      and sandbox assumptions are recorded before execution.
- [x] A keyless, report-only qualification runs against two representative
      Conductor-owned skills and is compared with the existing structural
      skill-surface audit for useful findings, false positives, and duplication.
- [x] If the keyless gate adds useful signal, one bounded behavioral canary
      compares the same realistic Conductor skill-intake/scouting task with and
      without one selected skill, using hand-authored explicit, implicit,
      contextual, and negative cases plus repeated attempts.
- [x] The canary preserves raw results and distinguishes deterministic checks,
      model-judge opinion, hand-authored observable assertions, pass@k, and
      measured skill lift. Manual trajectory review records where the default
      grader disagrees with the task contract.
- [x] The final decision is one of: adopt as an optional Conductor intake
      signal, defer pending a better canary or stable release, or reject. It
      explicitly states what SkillEvaluator may and may not decide.
- [x] Scout 055 and any accepted Conductor guidance reflect Cam's clarified
      boundary: qualify skills for Conductor's cross-project recommendations,
      with no product-repo rollout from this story.
- [x] No recurring weekly search is created. The story records the separate
      future gate for scheduling discovery only after manual skill-intake use
      proves recurring value.

## Out of Scope

- Installing SkillEvaluator in tracked product repositories or adding it to
  their CI pipelines.
- Replacing repo-native goldens, acceptance tests, security review, or human
  judgment with a generic quality, similarity, or lift score.
- Creating an automatic skill marketplace ranking, automatic recommendation,
  automatic skill installation, or automatic skill mutation workflow.
- Creating the possible future weekly skill-discovery schedule.
- Treating SkillEvaluator as the discovery engine itself; it qualifies
  candidates found through scouting, links, registries, or future searches.
- Depending on the announced ClawHub integration before its live evidence and
  ranking contract can be inspected.
- Modifying any tracked product checkout.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Pin and inspect the upstream SkillEvaluator source and execution boundary
- [x] Select two representative Conductor skills and predeclare qualification
      questions, stop gates, and expected evidence
- [x] Run the keyless report-only qualification in an isolated temporary
      environment and compare it with the existing skill-surface audit
- [x] If warranted, design and run one repeated behavioral lift canary
- [x] Record the adopt, defer, or reject decision and the future manual-intake
      contract
- [x] Implement only the Conductor doc, skill, script, or log changes justified
      by the evidence
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [ ] If agent tooling changed: `make skills-check` (not applicable; no skill changed)
  - [ ] If scripts or repo checks changed: `make test` (not applicable; no script or check changed)
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

- `docs/stories/story-030-skillevaluator-conductor-skill-discovery-spike.md` —
  scope, plan, evidence, and final decision.
- `docs/scout/scout-055-nvidia-skillevaluator-clawhub-skill-lift.md` — update
  the scout with the Conductor-only boundary and spike result.
- `docs/scout.md` — keep the indexed decision consistent with the detailed
  scout.
- A temporary directory outside tracked checkouts — upstream package and
  report artifacts during qualification, unless the final decision justifies
  retaining a small sanitized fixture or report in Conductor.
- Optional Conductor-only skill/runbook changes — only if the spike proves a
  stable manual skill-intake contract.

## Notes

- Triggered by Cam's approval after Scout 055 and his clarification that the
  tool is for Conductor's personal/operator use between projects.
- The likely future workflow is: Cam supplies a skill, or Conductor discovers a
  candidate; Conductor checks relevance and evidence; only then does it
  recommend adoption, adaptation, deferral, or rejection for specific projects.
- A possible weekly discovery pass is future work. This story may identify its
  evidence prerequisites but does not schedule or automate it.
- Story 022 provides the existing report-only structural skill-surface audit.
  The new tool must add behavioral or qualification value beyond that audit.
- Scout 052's SkillOpt boundary remains intact: evaluation evidence does not
  authorize automatic editing or promotion of skills.
- No commits, pushes, target-repo edits, credential changes, or recurring tasks
  are implicit in this story.

## Decision

**Adopt SkillEvaluator as an optional, non-authoritative Conductor intake
diagnostic.** The deterministic tier adds checks the current structural audit
does not cover, especially PII, Unicode, license/provenance, and undocumented
bundled-resource inspection. Its aggregate quality grade is not trustworthy
enough to guide adoption: both local skills received generic publication and
section-shape findings, including a false claim that `scout` lacked connector
guidance.

The behavioral tier adds a useful question that Conductor did not previously
answer consistently: does the candidate skill improve the same agent on the
same hand-authored tasks relative to no skill? The completed `scout` canary
scored all 16 planned matrix trials with no runtime errors. Both arms passed all
four cases at pass@2, so pass@k lift was zero. Aggregate overall score moved
from `0.8705` without the skill to `0.8953` with it, a neutral `+0.0248` lift by
SkillEvaluator's own threshold. The skill improved behavior adherence by
`+0.1027` and discovery/execution by `+0.0859`, while correctness fell `-0.05`
and efficiency was flat.

Those mixed results are decision-bearing: the current `scout` skill modestly
improves workflow adherence but did not make this easy four-case suite pass
more often than the base agent. They also prove why the report cannot be an
authority. The default efficiency grader repeatedly called the required read
of `candidate-skill/SKILL.md` a wrong-skill read, forcing a false `0.5` routing
score. LLM judges also disagreed across attempts about whether `Reject as
written while retaining the discovery idea` matched the expected `Adapt or
Spike` outcome.

Conductor may therefore use pinned, isolated Tier 1 checks for suspicious or
externally sourced skills and Tier 3 A/B evaluation when a recommendation is
important enough to justify hand-authored cases, baseline cost, and manual raw
trajectory review. SkillEvaluator may not rank candidates, authorize
installation, replace the existing skill-surface audit, overrule repo-native
truth, or justify a recurring discovery schedule. Promotion decisions still
need exact/custom checks where possible; default grades and generated cases
remain advisory.

The current runtime also needs a temporary compatibility adaptation: Harbor
0.13.2 calls Docker Compose with `up --wait`, while SkillEvaluator emits
`HEALTHCHECK NONE`; Docker Compose 28.5.1 rejects that combination. The
isolated run removed the redundant Compose wait and retained Harbor's own next
step healthcheck. Do not normalize a permanent package install until upstream
resolves that compatibility issue or Conductor deliberately owns a pinned
wrapper.

## Plan

1. Pin NVIDIA SkillEvaluator at upstream commit
   `aa195cacf1f115c86fd11d3c2821ea267c843ef2` and create an isolated temporary
   Python 3.13 environment from that checkout. Install the base package only for
   the first gate; do not modify the user's global uv tool inventory or install
   Tier 2/Tier 3 dependencies unless the preceding gate earns them.
2. Copy the Conductor-owned `scout` and `skill-surface-audit` skills into the
   temporary workspace. Run only the documented deterministic checks
   (`schema,pii,license,quality,unicode,lint`) with deduplication disabled and
   reports written outside the repository. Inspect the JSON and Markdown
   findings manually, including incomplete/unsupported evidence rather than
   treating non-zero exit status as a semantic failure.
3. Run the existing Conductor skill-surface audit and compare its structural
   findings with SkillEvaluator's results. The first stop gate is whether
   SkillEvaluator contributes at least one reproducible, decision-relevant
   signal for candidate-skill intake that the existing audit does not already
   provide. If it adds only generic style scoring, publication metadata noise,
   or duplicate structural findings, stop and record `defer` or `reject`.
4. Only if the keyless gate passes, install the pinned Tier 3 extra in the same
   temporary environment and build one synthetic, non-private `scout` canary.
   Hand-author four cases: explicit invocation, implicit skill evaluation,
   realistic Conductor context, and a negative request that must not trigger
   scouting. Stage a local candidate `SKILL.md`, minimal frozen Ideal/spec and
   project-registry fixtures, and exact observable assertions; use no live web
   source or target-project checkout.
5. Before live calls, run `doctor --verify-models` with Docker and explicitly
   select the OpenAI provider because both OpenAI and Anthropic credentials are
   present. Use the upstream-documented `gpt-5.4-mini` default only if the
   authenticated preflight proves it callable. Recheck current official API
   pricing, predeclare two attempts per case in both arms, and enforce a hard
   US$2 ceiling from a conservative worst-case estimate. Stop before calls if
   the model, Docker daemon, token/call bound, or cost cannot be verified; do
   not silently substitute a provider or model.
6. If the live gate proceeds, keep Tier 3 advisory, retain raw Harbor jobs and
   reports in the temporary workspace, and manually compare with-skill versus
   without-skill trajectories, exact assertion outcomes, judge dimensions,
   pass@k, token/tool efficiency, and skill lift. A positive generic judge score
   is not enough; the result must agree with the hand-authored routing and
   output contract.
7. Record one final decision in Story 030 and Scout 055: adopt SkillEvaluator as
   an optional Conductor intake signal, defer it pending a stable release or
   better canary, or reject it. Add a small Conductor-only intake runbook/skill
   change only if the evidence proves lower recurring effort. Do not create a
   weekly schedule or product-repo follow-up in this build.
8. Update the story tasks, acceptance criteria, and work log, regenerate
   methodology surfaces, then run `make methodology-check`, `make lint`,
   `make skills-check` only if a skill changed, `make test` only if a script or
   repo check changed, and `git diff --check`. Manually inspect all retained
   repository changes and leave the story `In Progress` with Build complete
   checked for the separate `/validate` gate.

**Manual inspection**: upstream dependency/runtime boundary; deterministic
report findings and false positives; any Tier 3 case fixtures, raw trajectories,
judge-versus-assertion agreement, token/tool counts, and result status; final
adopt/defer/reject language.

**Autonomy**: Go after approval. The plan is Conductor-only, isolated, capped,
and reversible. Stop before live calls if the keyless gate does not add distinct
value; record that result without forcing Tier 3. Pause if execution would
exceed US$2, expose private data, alter credentials or provider routing, modify
a target repo, require a different model/provider, or create recurring work.

## Work Log

Timestamps are UTC.

20260819-1700 — story-created: created from Cam's approval of Scout 055's
bounded canary and narrowed to Conductor's own skill-intake and cross-project
recommendation domain. Product-repo rollout and the possible weekly discovery
schedule are explicitly excluded.

20260819-1730 — build-exploration-complete: read Story 030, Conductor
Ideal/spec/state/graph, ADR-001, ADR-002, Story 022, and current upstream source.
Pinned NVIDIA SkillEvaluator main at
`aa195cacf1f115c86fd11d3c2821ea267c843ef2` (2026-08-18). Upstream is
Apache-2.0, version `0.1.0`, experimental/community-supported, requires Python
3.12-3.13, keeps the base deterministic package separate from Tier 2/Tier 3,
and warns that live local mode is only for trusted skills. Tier 3 reads
operator credentials from the host, rejects credential names in skill config,
writes evaluator datasets/results, and uses Harbor for Docker execution. This
Mac has uv, Docker 28.5.1, Codex CLI 0.143.0, and both OpenAI and Anthropic keys
present; explicit provider selection is therefore mandatory. Planned files are
Story 030, Scout 055/index, generated methodology surfaces, and only an
evidence-justified optional Conductor intake surface. No target project is
affected. Main risks are generic/false-positive quality findings, unexpected
package footprint, evaluator/agent data exposure, nondeterministic model-judge
scores, and unbounded live-call cost. Expected evidence is two deterministic
reports, comparison with Story 022's audit, and—only if earned—one synthetic
four-bucket A/B report under a US$2 ceiling.

20260819-1740 — plan-approved: Cam approved the written Conductor-only plan.
Implementation started at the isolated keyless gate; live model evaluation
remains conditional on distinct value from deterministic qualification.

20260819-2130 — keyless-gate-complete: installed pinned SkillEvaluator `0.1.0`
in an isolated Python 3.13.7 virtual environment under
`/var/folders/8f/3nlcf3sj1s5bbk1g_3dt3djm0000gn/T/conductor-skillevaluator-plan.XXXXXX.SS4gfJDkTM`.
Ran `schema,pii,license,quality,unicode,lint --no-dedup` against temporary
copies of `scout` and `skill-surface-audit`, retaining CLI, JSON, and Markdown
reports. PII, license validation, Unicode, quality threshold, and lint passed;
the external profile failed only because local skills omit publisher-oriented
`metadata.author`. `scout` scored 78.8/C and `skill-surface-audit` 89.8/B, but
most deductions were generic section/metadata advice. One actionable `scout`
finding was that bundled `templates/scout.md` is not documented in its
`SKILL.md`. The existing Conductor audit found no target-skill duplicate,
cache, body-size, or usage issue, confirming that provenance/safety/resource
checks are distinct but the numeric grade is not an adoption authority.

20260819-2245 — behavioral-canary-prepared: installed the pinned Tier 3 extra
in the same temporary environment. Hand-authored explicit, implicit,
contextual, and negative cases around a synthetic `weekly-skill-radar`
candidate that improperly promotes popularity, automatic cross-repo copying,
and implicit commit/push. The dataset passed strict validation. Official
OpenAI documentation priced `gpt-5.4-mini` at $0.75 per million input tokens
and $4.50 per million output tokens; the planned two attempts per case in both
arms remained under the predeclared US$2 ceiling. With Cam's approval, the run
reused the existing OpenAI credential while explicitly selecting the OpenAI
provider; no credential value was printed, copied, or committed.

20260819-2340 — behavioral-canary-stopped: `doctor --verify-models` passed for
Codex 0.143.0, Docker 28.5.1, the OpenAI provider, and `gpt-5.4-mini`. The live
evaluation planned 16 trials, then remained in `agent-runtime-preflight` for
more than ten minutes while Docker built the evaluator image and installed its
large Python evaluation stack. Stopped it at the declared runtime gate. The
retained run directory is
`tier3-results/scout/20260819_232745_71167_f9eb86a05346` beneath the temporary
workspace. Its cancellation result and traceback show zero completed trials;
there are no matrix results or cost/token measurements. No evaluation
container or process remained afterward. A premature decision deferred standing
adoption; the following work-log entry retracts it. No weekly task was created.

20260820-0340 — premature-defer-retracted: Cam correctly challenged the
decision because a one-time cold build had been mistaken for evidence about
the tool's recurring usefulness. Retracted that conclusion and resumed the
same prepared evaluation rather than changing its cases, model, attempts,
provider, or baseline contract.

20260820-0400 — runtime-compatibility-repaired: the second untouched run proved
Harbor's 600-second environment-start timeout was consumed by Docker Desktop's
stalled Docker Hub pull path. Fetched the official arm64
`python:3.12-slim` manifest and blobs through the working host registry path,
loaded the exact image into Docker, and prebuilt the generated evaluator image.
The next run exposed a separate Harbor 0.13.2 and Docker Compose 28.5.1
compatibility bug: Harbor used `compose up --wait` while SkillEvaluator emitted
`HEALTHCHECK NONE`. Applied a temporary isolated-venv patch to start detached;
Harbor's own immediate task healthcheck remained active and passed in 57
seconds. No repository or global Python package was modified.

20260820-0430 — behavioral-canary-complete: completed run
`20260820_040023_98790_58edbfed38f2` in 1074.7 seconds after preflight. All 16
planned matrix trials completed without runtime or security errors. With-skill
and without-skill pass@2 were both 4/4. Overall moved `0.8705 -> 0.8953`
(`+0.0248`, neutral); behavior `+0.1027`, execution/discoverability `+0.0859`,
goal accuracy `+0.01`, efficiency flat, and correctness `-0.05`. The 16 trials
plus one runtime preflight used 769,798 input tokens, including 616,448 cached,
51,341 output tokens, and $0.3922806. Manual review found the default routing
grader falsely penalized the task-required candidate-skill read and LLM judges
inconsistently classified the same reject/adapt reasoning. Raw jobs, reports,
and trajectories remain under the isolated temporary workspace. Final decision
changed to optional, advisory adoption with mandatory human inspection; no
weekly task or target-repo rollout was created.

20260820-0445 — validation-complete: independently rechecked the retained Tier
3 result, all 16 trial artifacts, token/cost accounting, current official model
pricing, story acceptance criteria, Scout 055, the complete repository diff,
and the generated methodology surfaces. `make methodology-check`, `make lint`,
and `git diff --check` passed. No skill or script changed, so `skills-check` and
`test` remain not applicable. Validation found no material defect; it clarified
that Work Log timestamps are UTC. Residual limits are the synthetic four-case,
two-attempt canary, default-judge noise, a temporary upstream compatibility
patch, and no persistent Conductor wrapper. These limits are already reflected
in the optional, advisory adoption boundary. Learning review found one separate
candidate warranted from Cam's correction: cold setup or preflight friction
must not be treated as evidence of a tool's recurring value. Drafting or
promoting that learning is outside this validation and requires its own review.

20260820-0446 — story-closed: `/mark-story-done` closed Story 030 after Build
and Validation were complete, every acceptance criterion was met, the optional
advisory adoption boundary was recorded in Scout 055, and current repository
checks passed. No weekly automation, target-project rollout, persistent wrapper,
commit, or push was created. The separate learning candidate remains
unpromoted and does not block closure.
