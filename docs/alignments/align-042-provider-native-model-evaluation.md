# Alignment 042 — Provider-Native Model Evaluation

**Date**: 2026-07-21
**Updated**: 2026-07-22
**Classification**: Portable improvement with repo-local execution
**Story**: [Story 027](../stories/story-027-provider-native-model-evaluation.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge
**Reference Build**: conductor
**Completed Real-World Pilot**: doc-web, executed by doc-web's own agent
**Next Selective Rollout**: Storybook and CineForge

## Focus

Prevent model evaluations from treating a mechanical model-name substitution
as a fair benchmark. A candidate must be called through a valid,
provider-native contract and given a bounded task-appropriate configuration
before semantic quality is judged.

Conductor owns the portable reference workflow and cross-project routing. It
does not own model runtimes, eval fixtures, provider credentials, benchmark
artifacts, or adoption decisions for target repos. Current provider facts remain
external and drift-prone; each target repo owns its prompts, adapters, scorers,
thresholds, and final evidence.

## Current Surface Inventory

| Project | `discover-models` | `improve-eval` | Dedicated new-model workflow | Classification |
| --- | --- | --- | --- | --- |
| Dossier | yes | yes | `refresh-model-evals` | Closest implementation; defer during active refactor. |
| Storybook | yes | yes | no | Portable gap with maintained model lanes; adapt now from the validated contract. |
| doc-web | yes | yes | `evaluate-model` | Real-world pilot complete; retain the repo-local adaptation and evidence. |
| CineForge | yes | yes | no | Portable gap with maintained model lanes; adapt now from the validated contract. |
| Board Game Ingester | yes | yes | no | Later only if a maintained model lane exists. |
| RoboRally | no | yes | no | Defer; no decision-bearing model-discovery lane established. |
| Echo Forge | yes | yes | no | Defer until a maintained model/provider eval needs it. |
| Conductor | no | no | `evaluate-model` reference | Portable routing reference; never claim target eval proof. |

The shared `/improve-eval` meaning is useful after an eval exists: inspect the
registry, classify prompt/pipeline versus test/golden mismatches, improve the
result, and record verified evidence. `discover-models` is useful for catalog
freshness. Neither forces provider-native transport qualification before the
first scored run.

Dossier's `refresh-model-evals` adds runtime-first smoke and promotion passes,
quality/speed/cost ranking, and artifact gates. It still does not require the
full provider-docs, transport, transient-error, structured-output, and bounded
settings contract. It is evidence, not a canonical file to copy.

## Repeated Failure Class

Recent evals have repeatedly needed dynamic repair before their results became
meaningful:

- the exact model slug or tier differed from the announcement name
- a built-in harness provider sent the wrong API-family or multimodal shape
- a model rejected sampling, reasoning, or forced-tool parameters
- JSON was requested only in prose instead of through supported API/schema
  enforcement
- reasoning/thinking consumed the output budget or needed a task-appropriate
  level
- provider quota, `429`, `503`, or high-demand responses prevented a stable run
- transport succeeded but a source-backed artifact still proved the model
  wrong

The process currently relies on an unusually diligent agent noticing these
distinctions. The portable improvement is to make them mandatory gates.

## Portable Evaluation Contract

### 1. Establish ownership and the decision

Identify the repo that owns the runtime and eval. Before API spend, name the
target surface, incumbent, maintained fixtures and scorers, quality threshold,
latency/cost limits, privacy boundary, and precise adoption question. Do not
test a prestigious model where it cannot change a decision. Conductor scouts
and routes; the owning repo executes and decides.

Treat the invocation as a natural-language brief: it may be broad, narrow,
rambling, self-correcting, or name several candidates. Preserve explicit
settings and constraints, let later corrections win, and resolve routine slugs,
providers, incumbents, and eval IDs from current evidence rather than demanding
positional arguments. Multiple candidates should share the same maintained
incumbent per surface and advance through progressive screening, not a pairwise
tournament.

Declare one operating mode. `Conductor handoff` may research first-party docs
and existing public or authorized access evidence, but it does not run provider
probes, use target credentials or fixtures, execute another repo's harness, or
issue the adoption verdict. A Conductor `audit` is read-only; execution verbs
produce an execution-ready owner handoff. `Owning-repo execution` performs the
qualification and benchmark under the repo's authority and policies.

A request to rerun from scratch, reproduce, check variance, or exercise the
workflow fresh is force-fresh intent. It bypasses duplicate avoidance only and
does not relax privacy, spend, fairness, retry, truth, or rollout controls. A
fresh adoption comparison reruns incumbent and candidate on frozen inputs;
candidate-only transport or variance reproduction cannot support a current
superiority claim.

### 2. Refresh external truth

Use current first-party docs, model discovery, pricing, and—only in owning-repo
execution mode—a minimal live probe to establish the exact slug, endpoint/API
family, supported inputs, structured outputs, tools, reasoning/thinking
controls, output limits, incompatible parameters, rate limits, and data policy
relevant to the repo task. Record source URLs or API evidence and checked date;
do not embed a stale provider matrix in the skill.

### 3. Qualify transport before quality

In the owning repo, prove a minimal native call, then prove the actual runtime
contract separately for every materially distinct surface: strict schema/JSON,
tools, images/files, long context, or another output shape as applicable.
Inspect the actual outgoing prompt/input payload and contract flags. HTTP 200
alone is insufficient: fail closed unless terminal status is complete, no
provider error/incomplete state exists, the served identity matches, and the
documented final output satisfies the selected contract. Quarantine pre-score
failures from semantic results. If no stable valid call can be established,
report transport-blocked or inconclusive rather than poor model quality. Keep
secrets out of artifacts and store private payloads only through the owner's
approved protected or ignored channel; committable evidence must be redacted.

### 4. Use a bounded fair configuration ladder

Start from provider-recommended defaults, add required production-contract
flags, then predeclare the exact arm count and bounded transport-debug budget.
The owning repo must also predeclare one aggregate provider-spend ceiling that
includes probes, candidate and incumbent calls, retries, and judges. When the
user and repo provide no tighter cap, use US$5; stop for explicit approval if
the smallest valid run may exceed it or pricing cannot be bounded.
Use no more than two task-appropriate challenger variants without explicit
owning-repo approval for a separate experiment. Select on a declared
calibration slice where possible, freeze one configuration before promotion,
and confirm it on held-out or predeclared repeated evidence. A best-of-many
score on the same decision fixtures is exploratory, not independent promotion
evidence. Apply a comparable tuning budget to incumbent and challenger; do not
expand it after seeing scores. Preserve the maintained task prompt and scoring
surface unless verified mismatch work proves they are wrong.

### 5. Triage dynamically

| Class | Required response |
| --- | --- |
| Transient busy, capacity-coded `429`, or `5xx` | Bounded retry/backoff; record reliability and retry overhead. |
| Auth, quota, region, tier, plan, or policy | Correct access if authorized or report blocked/constrained; no quality verdict. |
| Client concurrency or rate-limit `429` | Inspect provider error details, advertised limits, and harness concurrency; classify client overload as harness/configuration and plan limits as access/economics. |
| Unsupported parameter or wrong endpoint | Consult current docs, correct the call contract, and rerun the probe. |
| Missing structured-output enforcement | Enable supported JSON/schema controls and adequate output budget before judging JSON behavior. |
| Truncation or thinking-token exhaustion | Correct output limits or documented thinking controls, then rerun the affected slice. |
| Harness, scorer, or golden defect | Route to the owning repo's eval-improvement workflow; reuse cached subject output where honest. |
| Source-backed semantic mismatch | Count as model quality only after transport/configuration validity is proven. |

Repeated provider instability can fail a production reliability gate. It must
remain separate from semantic capability so the report says what actually
failed.

### 6. Promote progressively

Run native probe, representative smoke, calibration/failing slice, freeze the
configuration, then use an independent or predeclared repeated promotion-grade
comparison. Report quality, latency, cost, variance, provider-error rate,
retry overhead, configuration matrix, and confidence. A broad expensive matrix
is not the debugging tool for one malformed call. If an earlier prerequisite
stops a later materially different surface, that surface is `not measured` and
its adoption is not advanced; it is not a semantic failure.

### 7. Issue layered verdicts

Every result must state:

- access: available, constrained, blocked, or unverified
- transport: qualified, blocked, or inconclusive
- reliability: acceptable, degraded, failed, or not measured
- capability: better, equivalent, worse, or not measured
- adoption in the owning repo: adopt, conditional adopt, do not adopt, or defer
- adoption in Conductor: not evaluated — target-repo handoff required

Conductor reports access as `unverified` unless dated owner-run callability
evidence establishes another state. Conductor's lack of execution authority is
not evidence that the model itself is inaccessible.

No adoption recommendation may hide an unqualified transport or untested
required runtime contract.

Reproducibility requires the exact evaluated bytes. For a dirty run, retain the
base SHA plus hashes or a tracked snapshot/patch for changed adapters, prompts,
tasks, scorers, and goldens. Hash and size ignored raw artifacts in a tracked
manifest with safe regeneration commands. Never claim that later-hardened code
produced an earlier score.

## Why Build in Conductor First

Conductor can make the portable contract concise, internally coherent, and
resistant to known reasoning failures. Independent workers can test whether it
classifies raw incidents correctly and preserves ownership and verdict layers.

Conductor cannot establish:

- that a real provider's current docs were interpreted correctly
- that a provider adapter sends the right wire format
- that retry/backoff behavior works against live service conditions
- that strict schema enforcement succeeds for a specific model
- that the chosen setting matrix is fair on a real maintained task
- that quality, latency, cost, and variance beat a target repo's incumbent

Those claims require an owning repo's real harness, credentials, artifacts, and
acceptance gates. Synthetic success is readiness for a pilot, not adoption
proof.

## Synthetic Validation Plan

Forward-test the Conductor reference skill against raw scenarios without
supplying the intended classification:

1. a candidate returning repeated busy/`503` responses before a later healthy
   probe
2. a call rejected because the chosen reasoning parameter is unsupported
3. malformed JSON from a call that never enabled supported schema enforcement
4. JSON truncated because output or thinking-token budget was inadequate
5. a stable valid call whose artifact contradicts a source-backed golden
6. router fallback plus stale model-agnostic cache evidence
7. correct subject outputs hidden by judge and downstream-cleanup failures
8. interactive-only or privacy-ineligible access for private fixtures

Success means workers quarantine or repair pre-quality failures before
semantic scoring, distinguish rate-limit/account/client causes, count the
source-backed miss as genuine model-quality evidence, refuse invalid
cache/router provenance, attribute downstream failures to their actual stage,
and preserve privacy boundaries. Workers must also freeze a bounded settings
matrix before independent promotion, reject same-fixture best-of-many fishing,
preserve target-repo ownership, and report distinct
access/transport/reliability/capability/adoption verdicts.

## Doc-Web Real-World Pilot

Doc-web's own agent installed a repo-local adaptation and ran a fresh Grok 4.5
pilot against its maintained image-crop decision surface. The workflow found a
real pre-score flaw: the xAI adapter requested JSON only in prose even though
the model and production contract supported strict structured output. Doc-web
repaired and qualified that contract before scoring, proving the skill changes
evaluation behavior rather than merely documenting it.

The bounded comparison then produced valid semantic evidence:

| Arm | Result | Overall | Average latency | Cost |
| --- | ---: | ---: | ---: | ---: |
| Gemini 3 Flash incumbent | 13/13 | 0.9629 | 7,303 ms | $0.05530 |
| Grok 4.5 low reasoning | 11/13 | 0.7667 | 2,782 ms | $0.07598 |
| Grok 4.5 high-reasoning failed-case retry | 0/2 | 0.4553 mean | 2,674 ms | $0.01247 |

The complete Grok workflow cost $0.10955; including the fresh incumbent, total
provider spend was $0.16485. Both Grok misses were source-verified model errors,
and higher reasoning repaired neither. The detector verdict was `do not adopt`.
The page-context validator was deliberately skipped after the detector failed
its predeclared prerequisite, so page-context capability is `not measured` and
its adoption was not advanced. That distinction is a required workflow result,
not an inferred model failure.

The pilot also proved exact identity and bounded privacy handling: direct xAI
served `grok-4.5`, strict JSON Schema succeeded, and the live ZDR header was
false, so only public fixtures were eligible. Doc-web retained exact evaluated
dirty-adapter bytes, fixed-surface hashes, raw-artifact hashes and sizes, and
sanitized regeneration commands in its attempt 019 evidence. A base commit by
itself would not have reproduced the scored adapter.

Acceptance hardening after the score added natural/rambly/narrow/multi-model
brief parsing, force-fresh and read-only audit semantics, a default US$5
all-provider ceiling, per-surface contract qualification, and fail-closed
prompt-payload/terminal-status/served-identity/schema handling. Doc-web
validated the adapter with 20 focused tests, 58 adversarial envelope/contract
cases, and 889 full-suite tests. One public-fixture hardened smoke passed for
the exact served model at $0.0062944; the final lossless-input,
final-message, served-model, and schema rejection additions were then tested
locally only, without claiming a second live provider proof.

The skill verdict is **keep and refine**, not reject. The portable refinements
are now incorporated in Conductor's reference without copying doc-web-specific
PromptFoo commands, adapter schemas, fixture counts, or thresholds.

## Selective Rollout Decision

Adapt the refined skill into **Storybook and CineForge now**. Both have
maintained model-evaluation lanes, model/provider churn, and enough distinct
runtime surfaces for the contract to prevent repeat transport and scoring
mistakes. Their owning agents must adapt the reference to repo-local eval,
credential, artifact, privacy, and methodology conventions; rollout is not
evidence that any model should be adopted.

Defer the remaining repos:

- **Dossier** — closest existing workflow, but its active refactor makes this
  the wrong time to add or reconcile another eval surface.
- **Board Game Ingester** — wait for a maintained decision-bearing model lane.
- **RoboRally** — wait for a model-discovery and maintained eval lane.
- **Echo Forge** — wait for concrete maintained provider/model eval pressure.

Doc-web retains its accepted repo-local pilot copy. Conductor remains the
portable routing reference, not a canonical harness implementation.

## Stop Conditions

- Do not touch Dossier.
- Do not edit target repos or run their evals from this Conductor worktree.
- Do not treat synthetic reasoning tests as live transport or benchmark proof.
- Do not change target runtime defaults, prompts, scorers, goldens, or eval
  records.
- Do not run paid live benchmarks from Conductor.
- Do not copy target credentials or private payloads into Conductor artifacts.
- Do not call selective skill installation an eval or adoption result; each
  target repo must execute and decide under its own authority.
- Do not commit, push, or land without explicit closeout approval.

## Practical Impact

Agents should stop discarding promising models because the first call was busy,
misconfigured, truncated, or asked for JSON only in prose. Cam should receive a
decision that distinguishes access/provider trouble from actual model quality
and shows the strongest defensible, production-relevant configuration rather
than a one-shot default.

## Synthetic Evidence

Story 027's initial session-local exploration used two rounds with three
independent workers and drove the first refinement pass. During `/validate`, a
fresh contract review found additional ambiguity around Conductor authority,
same-fixture best-of-many selection, UI promises, artifact privacy, and `429`
attribution. Those findings were corrected before a durable replay.

The replay used three fresh workers with no parent-turn context. Each received
only the current skill path and one raw incident packet, not the intended
diagnosis; each then received one new raw packet in a follow-up. Two fresh
workers replayed final-review fixes against the final skill bytes. The
[exact task messages and verbatim responses](evidence/provider-native-model-evaluation-synthetic.md)
are retained so independence, no-answer leakage, and behavior can be audited.

| Incident | Observed skill behavior | Result |
| --- | --- | --- |
| Account rate-limit `429` at concurrency 12 versus documented limit 4 | Rejected the `33% unintelligent` conclusion, classified client-induced overload, preserved conditional `4/4` semantic evidence, and required a concurrency-4 rerun with a bounded retry cap. | pass |
| Capacity-coded `503` at supported concurrency with provider status incident | Preserved first-attempt reliability failure and retry cost, separated conditional `4/4` semantic evidence, rejected the semantic-loss verdict, and required one bounded `Retry-After` replay. | pass |
| Wrong API family, unsupported reasoning parameter, prompt-only JSON, and output exhaustion | Classified every attempt as transport/configuration failure, removed them from semantic scoring, and required native strict-schema then harness-parity probes. | pass |
| Fully qualified transport with three source-confirmed semantic misses plus proposed settings sweep | Issued `do not adopt`, rejected same-fixture settings fishing, and required a separately approved calibration/frozen/held-out experiment to reopen. | pass |
| Conductor offered a doc-web API key and private fixtures | Refused credentials, fixtures, provider calls, target-checkout edits, and adoption judgment; final replay returned `access: unverified` and `adoption: not evaluated — target-repo handoff required`. | pass |
| Correct subject outputs hidden by judge `401`, zero-filling collector, and retired cleanup field | Attributed failures by stage, preserved safe frozen artifacts, and recommended judge/scorer plus cleanup repair rather than new paid subject calls. | pass |
| Router fallback plus model-agnostic stale cache | Refused to credit the requested model, required fail-closed served-model proof and cache bypass/key repair, and treated capability/reliability/economics as unmeasured. | pass |

The combined exploration, independent review, and replay produced these
concrete hardenings:

- verify actual served-model/provider metadata and router fallback behavior
- bypass or validate model/config-aware caches
- control concurrency before treating overload as provider reliability
- attribute failures across subject, router, adapter, parser, cleanup, scorer,
  and judge stages
- split explicit Conductor-handoff and owning-repo-execution modes
- use `not evaluated` rather than an adoption verdict in Conductor
- freeze one configuration before promotion and reject post-score budget
  expansion or uncorrected same-fixture best-of-many selection
- align UI copy with Conductor's planning/handoff authority
- define owner-controlled artifact retention, secret redaction, and private-data
  storage rules
- classify `429` from error details, account limits, and concurrency rather than
  assuming provider instability

The durable replay plus targeted final round exercised seven distinct packets
across eight worker executions and found no further material classification or
ownership defect. Every output kept synthetic evidence distinct from live
qualification.

### What this proves

- The skill consistently separates pre-response failures from semantic quality.
- It preserves operational failures in end-to-end reliability rather than
  erasing them with retries.
- It proposes bounded, predeclared repairs instead of open-ended tuning.
- It recognizes a real source-backed semantic loss and can issue `do not adopt`.
- It rejects post-score settings fishing and requires independent promotion
  evidence after configuration selection.
- It keeps Conductor in handoff mode and refuses target credentials or private
  fixtures.
- It keeps target credentials, fixtures, registry changes, and defaults in the
  owning repo.

### What this does not prove

- provider-doc interpretation against a currently shipping model
- actual request/response wire compatibility
- harness adapter behavior, retries, caching, concurrency, or schema support
- real quality, latency, cost, variance, reliability, or artifact integrity
- whether the workflow is concise enough during a live target-repo evaluation

Those were the acceptance surface for the doc-web-owned pilot. Its result now
provides one real integration proof, but only for doc-web's Grok 4.5 crop lane;
it does not prove another provider, adapter, task, repo, or runtime contract.

## Portable Rollout Packet

For each approved target repo, its owning agent should:

1. read local `AGENTS.md`, Ideal, Spec, methodology state/graph, eval registry,
   discovery, eval-improvement, credential, privacy, and artifact conventions
2. adapt the Conductor reference semantically rather than byte-copying
   doc-web-specific commands, schemas, fixtures, scores, or thresholds
3. keep natural-language, read-only audit, force-fresh, aggregate spend,
   per-surface transport, fail-closed scoring, provenance, and unmeasured-surface
   semantics intact
4. integrate through the repo's canonical cross-CLI skill surface and run its
   skill, methodology, lint, and test gates
5. treat installation as workflow readiness only; wait for a real
   decision-bearing request before spending or issuing an adoption verdict

This sequencing is intentional: Conductor supplies the portable reasoning
contract; each owning repo owns integration, provider calls, artifact
inspection, and adoption judgment.
