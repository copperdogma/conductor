---
title: "Build and Refine Provider-Native Model Evaluation"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:2.1"
  - "spec:2.2"
  - "spec:4.2"
  - "spec:5.1"
decision_refs:
  - "ADR-001"
depends_on: []
category_refs:
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
  - "doc-web"
  - "storybook"
  - "cine-forge"
---

# Story 027 — Build and Refine Provider-Native Model Evaluation

> **Historical boundary note (2026-08-19):** Story 031 supersedes this story's
> handoff-only Conductor boundary after explicit all-or-subset selection. The
> provider-native transport, fairness, privacy, provenance, and owner-verdict
> requirements remain current; see Alignment 042 for the evolved contract.

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001
**Depends On**: None

## Goal

Build and refine a Conductor-owned `/evaluate-model` reference skill that
prevents future target-repo evaluations from confusing transport, provider
configuration, transient availability, structured-output, harness, or scorer
failures with model quality.

Conductor can validate the skill's reasoning against controlled incident
packets, but it cannot prove integration with a real model harness because it
owns no model runtime or decision-bearing eval lane. Doc-web's owning agent has
now completed the real-world pilot. This story must absorb its generic lessons,
record the evidence boundary, and route only justified repo-local adaptations.

Dossier is explicitly excluded while its large refactor is active.

## Acceptance Criteria

- [x] Conductor has one concise, user-invocable `/evaluate-model` reference
      skill whose description triggers on new-model evaluations, replacement
      benchmarks, provider/model challengers, and model refresh requests.
- [x] The skill requires a decision contract before spend: owning repo,
      target runtime surface, maintained winner, fixtures, quality threshold,
      latency/cost limits, privacy constraints, and an explicit adoption
      question.
- [x] The skill preserves the ownership boundary: Conductor scouts and routes;
      the owning target repo performs model calls, benchmarks, artifact review,
      registry updates, and adoption changes.
- [x] The skill requires current first-party docs and live callability evidence
      for the exact model slug, endpoint/API family, input format, structured
      output, tools, reasoning/thinking controls, output limits, incompatible
      parameters, pricing, rate limits, and data policy when relevant.
- [x] Transport qualification proves a minimal native call and the actual
      runtime contract before quality scoring. Pre-score failures cannot be
      recorded as model-quality failures.
- [x] The skill uses a bounded, symmetric tuning budget: provider-recommended
      defaults plus only task-appropriate reasoning/output-contract variants,
      without challenger cherry-picking.
- [x] Failure triage distinguishes transient availability, auth/quota/region,
      unsupported parameters or wrong endpoint, missing structured-output
      enforcement, truncation/token exhaustion, harness/scorer/golden defects,
      and genuine semantic model failures.
- [x] Busy/429/5xx failures get bounded retries and reliability evidence;
      repeated instability may fail the production reliability gate but cannot
      masquerade as poor semantic quality.
- [x] JSON/schema failures are not attributed to model quality until supported
      schema/JSON enforcement and adequate output budget are proven.
- [x] The evaluation ladder is progressive: native probe, representative
      smoke, failing slice, then promotion-grade repeated comparison. Reports
      include quality, latency, cost, variance, provider-error rate, and retry
      overhead where measurable.
- [x] Final output separates access, transport, reliability, capability, and
      adoption verdicts and records the tested configuration matrix plus why it
      was fair.
- [x] Independent synthetic tests cover at least: transient overload,
      unsupported reasoning, missing JSON enforcement, truncation, and a
      source-backed semantic mismatch. Expected diagnoses are not leaked to
      test workers.
- [x] Test results drive at least one explicit review/refinement pass, even if
      the first draft needs no material correction.
- [x] Conductor records the limits of synthetic testing and the precise
      doc-web-agent handoff used for the completed owner-run pilot; no doc-web
      files were changed from this Conductor story.
- [x] The completed doc-web pilot is recorded with its strict-schema repair,
      fresh comparison, model-quality verdict, skipped-surface limitation,
      spend, provenance, and post-pilot validation boundary.
- [x] The skill accepts natural, rambly, narrow, self-correcting, and
      multi-model briefs while preserving supplied constraints and later
      corrections.
- [x] The skill distinguishes Conductor handoff, read-only evidence audit,
      owning-repo execution, and force-fresh/reproducibility intent without
      granting Conductor provider-call or target-write authority.
- [x] The owner handoff requires a default US$5 aggregate spend ceiling when no
      tighter cap exists, per-surface contract qualification, fail-closed
      prompt-payload/terminal/identity/schema checks, exact dirty-run
      provenance, and `not measured` for skipped surfaces.
- [x] Alignment 042 recommends adapting the validated contract in Storybook and
      CineForge now while deferring Dossier, Board Game Ingester, RoboRally, and
      Echo Forge for their recorded local reasons.
- [x] Conductor methodology, skill, lint/static, and diff checks pass.

## Out of Scope

- Editing, evaluating, or preparing a worktree for Dossier.
- Editing any target repo or running its evals from this Conductor worktree.
- Treating synthetic reasoning tests as proof that a provider adapter or real
  benchmark works.
- Treating installation in Storybook or CineForge as model-eval or adoption
  proof; their owning repos must execute and decide.
- Changing runtime model defaults, prompts, providers, scorers, goldens, or eval
  results.
- Spending on live model benchmarks.
- Creating a central provider registry or embedding drift-prone provider
  parameter tables in the skill.
- Committing, pushing, landing, or deleting worktrees without explicit
  closeout approval.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Audit tracked model-eval skill surfaces and classify the portable gap
- [x] Prepare Alignment 042 and re-scope it to a Conductor reference build
- [x] Create an isolated Conductor worktree from `origin/main`
- [x] Create Conductor's `/evaluate-model` reference skill
- [x] Add the narrow Conductor workflow route and ownership boundary
- [x] Run independent synthetic failure-scenario tests without expected-answer
      leakage
- [x] Review and refine the skill from observed test behavior
- [x] Write the doc-web-agent real-world pilot handoff
- [x] Record synthetic evidence and the honest validation boundary in Alignment
      042
- [x] Incorporate the completed doc-web pilot's portable lessons without
      copying its provider, adapter, fixture, or PromptFoo specifics
- [x] Record the selective rollout decision: Storybook and CineForge now;
      Dossier, Board Game Ingester, RoboRally, and Echo Forge deferred
- [x] Run required Conductor checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] `make skills-check`
  - [x] `make test` not required; no executable code or repo check changed
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

- `.agents/skills/evaluate-model/SKILL.md` — provider-native reference workflow
  and target-repo ownership boundary.
- `.agents/skills/evaluate-model/agents/openai.yaml` — concise skill UI metadata.
- `AGENTS.md` — route model-eval planning to the new skill while preserving
  target-repo execution ownership.
- `docs/stories/story-027-provider-native-model-evaluation.md` — scope,
  plan, work log, and evidence.
- `docs/alignments/align-042-provider-native-model-evaluation.md` — portable
  contract, synthetic evidence, limitations, and doc-web handoff.
- `docs/alignments/evidence/provider-native-model-evaluation-synthetic.md` —
  exact blind-test packets and verbatim worker outputs.
- `docs/align-projects.md` — alignment index.
- `CHANGELOG.md` — operator-facing summary of the validated reference and
  selective rollout decision.
- Generated Conductor methodology surfaces produced by
  `make methodology-compile`.

## Notes

- Triggered by Cam's observation that agents often swap a model name, run the
  harness once, and issue a verdict without noticing busy-provider responses,
  incompatible APIs, missing JSON enforcement, truncation, or unsuitable
  thinking/reasoning settings.
- The portfolio audit found `/improve-eval` in all seven tracked target repos,
  `/discover-models` in six, and a dedicated `/refresh-model-evals` only in
  Dossier. None contains the full provider-native qualification contract.
- Alignment 028 already makes current upstream docs an active dependency. This
  story connects that general rule to model-evaluation execution.
- Conductor has no real model evals or model API calls. Its legitimate proof is
  limited to skill structure, scenario reasoning, failure classification,
  routing quality, and validation checks.
- Doc-web's own agent later completed the pilot in a separate owning-repo
  worktree. Conductor records its returned evidence but did not issue provider
  calls, inspect private payloads, or make doc-web's adoption decision.

## Plan

1. Add a concise Conductor `/evaluate-model` reference skill with required
   gates for ownership, decision framing, provider-native research, transport
   qualification, bounded configuration, failure triage, progressive
   benchmarking, and layered verdicts.
2. Keep provider-specific details out of the skill. Require dated first-party
   sources and live probes when an owning repo later invokes it.
3. Make Conductor's boundary explicit: it may scout access and prepare a
   handoff, but it may not run or judge another repo's benchmark.
4. Forward-test the skill with independent workers on raw synthetic incident
   packets covering overload, unsupported reasoning, missing schema
   enforcement, truncation, and genuine semantic failure. Do not provide the
   intended classification.
5. Review the workers' outputs against the acceptance contract and refine the
   skill for any missed classification, unsafe retry, unfair settings matrix,
   or collapsed verdict layer.
6. Record what synthetic testing does and does not prove, then write a precise
   doc-web handoff instructing doc-web's own agent to create a local story,
   adapt the reference skill, select one decision-bearing new-model lane, run
   real native probes and a bounded eval, and return adoption evidence.
7. After the owner-run pilot, fold only generic proven lessons back into the
   Conductor reference: natural briefs, explicit audit/force-fresh semantics,
   aggregate spend, per-surface qualification, fail-closed scoring, exact dirty
   provenance, and honest skipped-surface reporting.
8. Record the pilot result and choose a selective rollout from portfolio fit:
   Storybook and CineForge now; defer Dossier, Board Game Ingester, RoboRally,
   and Echo Forge without manufacturing work.
9. Run `make methodology-compile`, `make methodology-check`, `make lint`,
   `make skills-check`, the skill-creator validator if compatible with repo
   frontmatter, and `git diff --check`. Run `make test` only if executable code
   changes.
10. Stop before target-repo edits, provider calls, commit, push, landing, or
    story closeout in this Conductor worktree.

Autonomy: Go after approval. Cam approved incorporating the owner-run pilot and
promoting the refined skill outward. This Conductor slice remains reference and
routing work only; target-repo writes occur in their own worktrees. Pause if
work would require Conductor-side provider calls, runtime/default changes, or
golden/scorer edits.

## Work Log

20260721-1435 — story-created: initially created a doc-web-first provider-native
model evaluation pilot after Cam redirected the reference implementation away
from Dossier's active refactor. Verified the primary checkouts were active and
dirty, then created clean isolated worktrees from `origin/main`. No primary
checkout or Dossier file was changed.

20260721-1450 — exploration-and-plan: confirmed doc-web has current
`discover-models`, `improve-eval`, PromptFoo, registry, provider-adapter, skill
sync, and methodology surfaces. Recent durable evidence includes an API-family
image adapter, reasoning-level retries, structured-output correction, and
recovery from quota/`503` responses.

20260721-1510 — scope-corrected-and-approved: Cam identified that Conductor is
the right place to build and refine the portable reference but the wrong place
to claim a real model-eval test because it has no model runtime or eval lane.
Re-scoped Story 027 to build and synthetic-test the skill in Conductor, then
recommend a doc-web-owned real-world pilot for doc-web's own agent to execute.
Cam approved this corrected plan with `Go for it`. The existing doc-web
worktree remains clean and unused.

20260721-1530 — reference-skill-built: created
`.agents/skills/evaluate-model/SKILL.md` plus concise UI metadata, then added the
narrow `/evaluate-model` route to `AGENTS.md`. The skill requires target-repo
ownership, current first-party evidence, native/contract/harness transport
qualification, a predeclared bounded configuration matrix, progressive runs,
stage-aware failure classification, separate conditional and end-to-end
results, and layered access/transport/reliability/capability/economics/adoption
verdicts. `scripts/sync-agent-skills.sh` and its `--check` mode both passed with
21 canonical skills.

20260721-1550 — blind-forward-tests-and-refinement: ran two scenario rounds
through three independent workers. Round one used fresh workers with no parent
context and covered overload, unsupported reasoning plus missing schema/token
budget, and a transport-qualified source-backed semantic loss. All three
classified the failures correctly, used bounded follow-ups, and preserved the
Conductor/target boundary. Review added actual served-model/router checks,
cache provenance, concurrency fairness, and explicit subject/router/adapter/
parser/cleanup/scorer/judge stage attribution. Round two directly tested router
fallback plus stale cache, judge `401` plus stale cleanup, and private-data
privacy/automation blockers; all three passed. Alignment 042 records the six
case outcomes, proof limits, and the ready handoff for doc-web's own agent.

20260721-1605 — build-validation: `make methodology-compile`,
`make methodology-check`, `make lint`, `make skills-check`, and
`git diff --check` passed. The active skill-surface audit recognized the
then-current `evaluate-model` description and route as enabled; the
overall active-context budget remains under pre-existing global/plugin
pressure rather than a new repo-local duplicate. The generic skill-creator
validator parsed the skill when run with PyYAML but rejected Conductor's
required top-level `user-invocable` extension. `make skills-check` passed with
21 canonical skills, proving local discovery/symlink consistency but not
frontmatter or UI-schema validity; those metadata files were inspected
separately against the local and skill-creator conventions. `make test` was not
required because no executable code or repository check changed. Build is
complete; independent `/validate` and story closeout remain pending.

20260721-1610 — learning-review: `RESULT: no-candidate`. Cam's correction about
building the portable reference in Conductor but reserving real provider/harness
proof for the owning repo is reusable, but this build already codifies it in
the new skill's Conductor boundary, `AGENTS.md`, Story 027, and Alignment 042.
A separate learning candidate would duplicate the newly installed guardrail.

20260721-2145 — independent-validation-findings: two read-only reviewers
checked the skill contract and story/alignment/generated evidence. They found
real defects despite green local checks: ambiguous Conductor execution
authority, no handoff-only adoption state, same-fixture best-of-many selection
risk, misleading `Run` UI copy, incomplete artifact/privacy rules, ambiguous
`429` attribution, and no durable raw synthetic packets. They also found that a
pushed branch already owns Story 026 and that the graph generator does not
reject duplicate story IDs. The work was renumbered to Story 027 before
integration; Alignment 042 remains collision-free.

20260721-2227 — validation-repair-and-replay: split explicit Conductor-handoff
and owning-repo-execution modes; reserved provider calls and adoption decisions
for the owner; added exact arm/debug budgets, configuration freeze,
held-out/repeated confirmation, and post-score expansion controls; aligned UI
copy; defined secret/private-artifact handling; and classified `429` from error,
account, and concurrency evidence. Replayed seven distinct raw incidents across
eight worker executions without expected diagnoses. The final targeted round
added explicit `access: unverified` and true provider-capacity `503` coverage;
all cases passed overload, API/schema/token, source-backed semantic,
Conductor/private-data, judge/cleanup, and router/cache boundaries. Exact
prompts, hashes, and verbatim responses are retained in
`docs/alignments/evidence/provider-native-model-evaluation-synthetic.md`.

20260721-2237 — validation-complete: final findings-first re-reviews reported no
material defects. The last access-vocabulary gap was fixed with Conductor's
`unverified` default, and a final-byte boundary replay confirmed it. Fresh
`make methodology-compile`, `make methodology-check`, `make lint`,
`make skills-check`, tracked `git diff --check`, explicit checks for every
untracked file, and YAML parsing of skill/UI metadata passed. Story 027 has no
current remote-ref collision; the isolated doc-web worktree remains clean and
`0/0` versus `origin/main`; Dossier remains untouched. `codex review` was not
used because this is a documentation/skill contract rather than executable
code; two independent contract/evidence reviewers supplied the relevant review
surface. Residual limit: no live provider, adapter, harness, or maintained
quality benchmark was exercised in Conductor. That proof belongs to the
doc-web-owned pilot. Validation recommendation: close now.

20260722-1653 — owner-pilot-feedback-integrated: doc-web's owning agent returned
a fresh Grok 4.5 pilot that found and repaired prompt-only JSON before scoring,
then produced a valid detector loss against a fresh incumbent. The pilot also
exposed missing force-fresh semantics, per-surface qualification, aggregate
spend, lossless prompt-payload enforcement, fail-closed response handling, and
exact dirty-run provenance. Folded those generic lessons into Conductor's reference without copying doc-web's
PromptFoo commands, xAI schemas, fixtures, thresholds, or adoption authority.
Recorded detector `do not adopt`, page-context `not measured`, the $0.16485
total invocation spend, and the local-only boundary of the final post-smoke
adapter rejection hardening. A final pre-push review added fail-closed prompt
normalization and final-message selection; doc-web's focused provider coverage
finished at `20/20` and its full suite at `889 passed` without another provider
call.

20260722-1653 — selective-rollout-routed: updated Alignment 042 to recommend
repo-local adaptations in Storybook and CineForge, which have maintained model
lanes and current provider churn. Kept Dossier deferred during its refactor and
Board Game Ingester, RoboRally, and Echo Forge deferred until their recorded
decision-bearing conditions exist. Story 027 remains `In Progress`; build is
complete, but fresh independent validation and closeout remain pending.

20260722-1700 — refreshed-build-checks: `make methodology-compile`,
`make methodology-check`, canonical skill sync, `make skills-check`, `make
lint`, and `git diff --check` passed after the pilot-feedback refinement. The
skill is 356 lines, below the 500-line authoring budget. `make test` remains not
required because this slice changes documentation and skill instructions, not
executable code or repository checks.

20260722-1715 — final-validation-and-closeout: an independent findings-first
review reported no material defects and confirmed the generic skill, Story 027,
Alignment 042, routing, changelog, and generated surfaces agree. The reviewer
also verified doc-web's final `20/20` focused adapter coverage and recorded
`889 passed` full-suite evidence. Fresh Conductor methodology, lint, skill-sync,
YAML, secret-pattern, and diff-hygiene checks passed. No provider call was made
from Conductor. Marked Story 027 Done; the remaining live proof belongs to each
owning repo when `/evaluate-model` is invoked there.
