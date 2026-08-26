---
title: "Separate Setup Friction From Evaluation Evidence"
status: "Promoted"
created: "2026-08-19"
target_surface: ".agents/skills/scout/SKILL.md"
trigger_class: "user-correction"
review_cadence: "Terminal after promotion; route reversals or follow-up behavior changes through a new candidate."
confidence: "high"
source_runs:
  - "Story 030"
  - "SkillEvaluator run 20260819_232745_71167_f9eb86a05346"
  - "SkillEvaluator run 20260820_040023_98790_58edbfed38f2"
user_corrections:
  - "Cam rejected the premature verdict: setup taking longer than expected did not establish that the scouted tool was not worthwhile, and the evaluation had to continue."
evidence_summary: "Story 030 initially deferred standing adoption after a cold Docker evaluator build completed no matrix trials. Cam corrected that reasoning. After setup diagnosis and an isolated compatibility repair, the unchanged 16-trial canary completed and supplied decision-bearing evidence for optional advisory adoption."
evidence:
  - "docs/stories/story-030-skillevaluator-conductor-skill-discovery-spike.md"
  - "docs/scout/scout-055-nvidia-skillevaluator-clawhub-skill-lift.md"
proposed_change: "Add a scout guardrail requiring external-tool evaluations to distinguish bootstrap, environment, and compatibility evidence from task-result evidence. Setup friction may count as recurring overhead or operational risk, but it must not by itself produce an adopt, adapt, defer, reject, or spike verdict before the declared decision-bearing test runs; when the test cannot run after bounded in-scope diagnosis, report the evaluation as blocked or incomplete instead."
promotion_gate: "Met on 2026-08-19: Cam explicitly accepted and then separately approved promotion after reviewing that the wording preserves legitimate cost, safety, time, and hard-blocker stop gates."
promotion_evidence:
  - ".agents/skills/scout/SKILL.md diff"
  - "Story 030 validation and close-out"
  - "make skills-sync"
  - "make skills-check"
  - "make lint"
  - "git diff --check"
---

# Candidate - Separate Setup Friction From Evaluation Evidence

## Summary

An external tool's cold setup cost, runtime bootstrap delay, or compatibility
failure is operational evidence, not a substitute for the evaluation that was
supposed to determine its value. A scout should keep those evidence classes
separate and report an honest blocker when the decision-bearing test has not
run.

## Evidence

- Evidence summary: Story 030 initially stopped NVIDIA SkillEvaluator during a
  cold Docker evaluator build and inferred a standing `Defer` verdict even
  though zero planned matrix trials had completed. Cam rejected that inference.
- The first retained run,
  `20260819_232745_71167_f9eb86a05346`, preserved cancellation evidence but no
  behavioral scores, lift measurement, pass@k result, or trial cost.
- Bounded diagnosis separated a stalled Docker Hub pull from a Harbor 0.13.2 /
  Docker Compose 28.5.1 healthcheck incompatibility. An isolated compatibility
  repair allowed the same predeclared canary to run without changing its cases,
  model, attempts, provider, or baseline contract.
- The completed run, `20260820_040023_98790_58edbfed38f2`, scored all 16 trials
  and supported a materially different, evidence-backed decision: optional,
  advisory adoption with neutral overall lift, useful workflow-adherence
  signal, and explicit compatibility overhead.

## Source Runs And User Corrections

- Source runs: Story 030; SkillEvaluator runs
  `20260819_232745_71167_f9eb86a05346` and
  `20260820_040023_98790_58edbfed38f2`.
- User correction: Cam stated that taking longer than expected to set up did
  not determine whether the scout was worthwhile and instructed the evaluation
  to continue because no decision-bearing result existed yet.

## Required Evidence Gate

- Concrete source provenance present? Yes: Story 030, Scout 055, and both
  retained run identifiers.
- Evidence summary present? Yes.
- User-correction evidence quoted/summarized, or explicitly `none recorded`?
  Yes, summarized without importing the whole conversation.
- Draft, propose, accept, or promote? Promoted. The correction, causal mistake,
  completed counterfactual evidence, and target skill were clear; Cam
  explicitly accepted the candidate and then separately approved promotion.

## Trigger And Cadence

- Trigger class: user-correction.
- Review cadence: terminal after promotion. Route reversals or follow-up
  behavior changes through a new candidate.

## Lifecycle State

- Current status: Promoted.
- Allowed next transition: none. Reversals or follow-up changes require a new
  candidate or story.
- Live changes in this candidate operation: added the approved evidence-class
  guardrail to `.agents/skills/scout/SKILL.md`.
- Accepted-state check: not applicable after promotion.
- Terminal-state check: `Promoted` must not apply the same live change again.

## Observed Pattern

During an executable-tool scout, the work substituted a one-time environment
setup delay for the result of the declared behavioral test. That collapsed
three different questions into one: whether the environment could be made to
run, what recurring operational burden the tool carried, and whether the tool
actually improved the target work. The first failed attempt answered only part
of the first question.

## Proposed Change

Add a narrow guardrail to `.agents/skills/scout/SKILL.md`: when a scout includes
an executable evaluation, distinguish bootstrap, environment, and
compatibility evidence from task-result evidence. Setup friction may be
reported and weighed as recurring overhead or operational risk, but it must not
alone determine `Adopt`, `Adapt`, `Defer`, `Reject`, or `Spike` before the
declared decision-bearing test runs. If bounded, safe, in-scope diagnosis still
cannot make the test run, report the evaluation as blocked or incomplete and
name the missing evidence.

This rule does not require unlimited persistence and does not override declared
cost, safety, credential, scope, or runtime stop gates.

## Why It Matters

The guardrail prevents confident tool verdicts from being based on zero trial
results while retaining setup burden as legitimate adoption evidence. Future
scouts should become easier to audit: Cam can see whether a conclusion rests on
tool behavior, recurring operating cost, a compatibility boundary, or an
unresolved execution blocker.

## Rejection Checks

- Novelty only? No. The initial conclusion changed after the missing
  decision-bearing evaluation completed.
- Vibes only? No. The retained first run had zero completed trials; the later
  unchanged matrix produced 16 scored trials and the final adoption evidence.
- One-off success? No. This is based on an explicit correction of a reasoning
  error, not on celebrating the successful workaround.
- Generic process advice? No. The target is Conductor's external-source scout
  lane and its explicit adoption vocabulary.
- Model-era compensation likely to go stale? No. Separating environment
  evidence from task-result evidence remains useful with stronger agents.
- Already covered by an existing skill, doc, or memory? No matching scout
  guardrail was found. Current guidance requires a decision and source-backed
  research but does not say how to classify an evaluation that never reaches
  its decision-bearing trials.

## Promotion Gate

Met on `2026-08-19`: Cam explicitly accepted the candidate and then separately
approved promotion after confirming that it preserves legitimate cost, safety,
time, credential, scope, and hard-blocker stop gates.

## Promotion Action

Applied the narrow evidence-classification guardrail to
`.agents/skills/scout/SKILL.md`. No other skills, methodology docs, memory, or
target-project repositories changed through this promotion.

## Validation Plan

- Run `make skills-check` after the live skill patch.
- Run `make lint` and `git diff --check`.
- Manually confirm the wording does not require persistence past declared
  safety, cost, credential, scope, or runtime limits.
- Manually test the rule against Story 030: the first stopped run should yield
  `blocked/incomplete with setup evidence`, while the completed run may support
  the recorded optional-adoption verdict.

Completed on `2026-08-19`: `make skills-sync`, `make skills-check`, `make lint`,
and `git diff --check` passed. Manual inspection confirmed the promoted wording
preserves the declared stop gates and classifies the first Story 030 run as
blocked or incomplete rather than decision-bearing.

## Decision History

- `2026-08-19` — Proposed from the Story 030 user correction, retained failed
  and completed SkillEvaluator runs, validation finding, and Scout 055 outcome.
  No live skill changed.
- `2026-08-19` — Cam explicitly accepted the candidate for possible promotion.
  The rationale is that it preserves valid stop gates while preventing setup
  friction from being substituted for missing evaluation results. No live skill
  changed; promotion remains a separate decision.
- `2026-08-19` — Cam separately approved promotion. Added the bounded
  evidence-classification guardrail to `.agents/skills/scout/SKILL.md`, refreshed
  compatibility links, and passed `make skills-check`, `make lint`, and
  `git diff --check`. The candidate is terminal at `Promoted`; no commit or push
  was performed.
