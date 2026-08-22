# Owning-Repo Model Evaluation Protocol

Read this file completely after a repository has been selected for execution
and before the first live provider call. The selected repository's own
instructions, privacy rules, maintained fixtures, scorers, thresholds, and
artifact conventions remain authoritative.

## 1. Establish the Decision Contract

Before spending tokens, record:

- candidate, exact provider/access path, and maintained incumbent
- exact runtime stage or product surface that could change
- maintained prompt, fixtures, scorer/golden, and current winning evidence
- quality threshold plus latency, cost, reliability, privacy, and safety limits
- the decision this run can support: adopt, conditional adopt, do not adopt, or
  defer
- freshness mode, cache policy, proposed configuration arms, retry budget,
  per-repo spend ceiling, and progressive stop gates

If no result can change a maintained decision, stop with an evidence-backed
defer/no-eval result. For multiple candidates, qualify each independently and
compare each against the same maintained incumbent per surface; do not create a
pairwise tournament.

For force-fresh work, create a new run/artifact identity and bypass subject
output caches even when model and configuration are unchanged. A cache hit is
not fresh evidence.

## 2. Refresh Current Provider Truth

Use current first-party documentation, model discovery, pricing, and a minimal
live probe to establish every contract fact relevant to the selected task:

- exact slug, aliases/tiers, availability, region, and authorized access path
- native endpoint/API family and current SDK or harness support
- served-model/provider metadata and router fallback/parameter enforcement
- text, image/file, tool, streaming, role, or long-context input shape
- structured-output or strict JSON Schema support and required flags
- tool-choice behavior and supported reasoning/thinking controls
- output-token controls and whether reasoning consumes that budget
- supported or rejected sampling, stop, seed, and penalty parameters
- pricing, rate/concurrency limits, service tier, and availability guidance
- retention, training, ZDR, and other payload policy

Prefer the direct provider when it is the cleanest supported production path.
Use a router such as OpenRouter only when it is the intended or best practical
path, and record fallback behavior and actual served identity. Interactive
preview access is not reproducible API access.

Record source URLs or API evidence and checked date. Do not use a stale provider
matrix or model-family assumptions to fill unknowns that could invalidate the
run.

## 3. Qualify Transport Before Quality

Resolve credentials before the access probe. If the owner lacks an evaluation-
only provider key, use the Conductor coordinator's credential-custody protocol
to inject exactly that provider into an ignored owner environment. Do not
receive or request the raw value in task text. An injected key does not relax
the owner's privacy rules or authorize provider-account setting changes, and it
must be removed after the run.

Advance through this ladder and retain sanitized evidence at each stage:

1. **Access probe** — confirm the exact model ID is visible and authorized for
   the intended credentials and region. Catalog visibility alone is not
   callability.
2. **Native probe** — make the smallest raw provider call outside the harness
   when practical and confirm the requested model/provider was served.
3. **Contract probe** — exercise the production requirement: strict schema,
   tools, images/files, long context, or another output contract.
4. **Harness-parity probe** — send the same small case through the repo adapter
   and compare the request/response contract with the native result.

Qualify every materially distinct runtime surface separately. A schema proven
for one task does not qualify another task with a different output shape. Do
not start scored evaluation on a surface until its required native contract and
harness-parity probe pass.

HTTP success is insufficient. Fail closed unless all of these hold:

- the provider reports documented terminal success with no error/incomplete
  condition
- served model/provider identity matches the intended arm
- the documented final output field is complete and unambiguous
- the actual outgoing prompt/input payload is lossless
- required schema/tool flags were sent and the output satisfies the contract
- usage, finish reason, latency, and cost evidence are valid

Quarantine malformed envelopes, wrong identities, partial output, invalid
usage, prompt loss, cache contamination, and contract-invalid responses from
semantic scoring. If native succeeds but harness parity fails, treat it as an
adapter problem until disproved.

Never retain authorization headers, API keys, signed URLs, or equivalent
secrets. Keep private inputs and outputs only in owner-approved protected or
ignored storage. Committable evidence uses redacted excerpts, hashes, sizes,
and safe pointers. `store=false` is not by itself proof of ZDR.

When JSON is required, use strict schema enforcement when supported. Label a
weaker documented JSON mode honestly. Prompt-only JSON is not API-enforced
structure. Ensure the output budget can hold the required schema before
classifying malformed or incomplete JSON as model behavior.

## 4. Predeclare a Fair Configuration and Spend Budget

Use the per-repo ceiling disclosed in the approved recommendation. It covers
access/contract probes, candidate and incumbent calls, retries, and judge calls.
Stop for approval before exceeding it or when pricing cannot be bounded
conservatively. For a direct targeted invocation with no prior disclosed cap,
use US$5 as the maximum fallback, but propose a lower task-specific cap whenever
possible.

Before looking at scores:

- start a cost ledger and conservative estimate
- rerun the incumbent on its maintained production configuration when current
  superiority evidence is needed
- run the challenger with provider-recommended defaults plus required contract
  flags
- predeclare the exact challenger arms and transport-debug retry/repair cap;
  use the recommended configuration plus at most two justified variants
- give incumbent and challenger comparable tuning opportunity
- select variants on a predeclared calibration slice when possible, then freeze
  one configuration before promotion
- label same-decision-fixture variant selection exploratory; require held-out or
  predeclared repeated confirmation before promotion
- freeze prompt, fixtures, scorer, golden, and downstream cleanup during the
  comparison unless separately verified eval-validity work proves a defect
- bypass the subject-output cache for a model/config change; force-fresh work
  always bypasses it, while ordinary reuse requires proof that the key includes
  the exact model and relevant parameters
- begin at low documented-safe concurrency; test production concurrency
  separately

A request-shape or schema-flag repair needed to obtain any valid response is
transport work. A change that can alter answer content—including reasoning
level, output budget, or prompt—becomes a declared configuration arm. Do not
expand the tuning or debug budget after observing scores without a new causal
hypothesis and explicit approval.

## 5. Run Progressively

Use the smallest run that answers the current question:

1. one representative smoke case
2. the known failing or differentiating slice
3. a bounded maintained fixture set
4. promotion-grade comparison with the repo's required repeats and artifacts

Inspect raw outputs and artifacts between stages. Do not launch a broad matrix
to debug one malformed call. Stop weak, incompatible, or operationally failed
candidates at the predeclared gate and retain their evidence.

Before the first paid multi-case run, resolve the harness without inference and
inspect its topology: rendered cases, conversation/session grouping, exact
prompt snapshot versus the intended runtime prompt, subject and judge
providers, judge pricing, cache keys, concurrency, and output paths. A harness
that silently chains independent cases, selects an implicit judge, or renders a
stale production contract is not ready for paid scoring. Correct the execution
topology or stop; do not discover these facts through a broad live run.

If a prerequisite stops a later materially different surface, report the later
surface as `capability: not measured` and `adoption: not advanced`. A deliberate
progressive stop is not evidence that the skipped surface failed.

## 6. Classify and Respond to Failures

Identify the failing stage first: subject request, provider/router, adapter,
parser, downstream cleanup, scorer, or judge. Then assign one primary class.

| Failure class | Required response |
| --- | --- |
| Transient provider capacity, timeout, `5xx`, or capacity-coded `429` | Respect provider guidance or `Retry-After`; retry within the declared cap; retain every attempt plus added latency/cost. Persistent instability affects reliability, not semantic quality. |
| Auth, quota, region, tier, plan, or policy | Correct only within existing authorization; otherwise mark access blocked/constrained and do not score capability. |
| Client concurrency or rate-limit `429` | Inspect error details, advertised limits, and harness concurrency. Client overload is harness/configuration evidence; a plan limit is access/economics. |
| Wrong endpoint, API family, input shape, or unsupported parameter | Recheck current docs, correct one contract variable, rerun native qualification, then harness parity. |
| Missing structured-output enforcement | Enable the supported schema/JSON contract and adequate output budget before judging JSON behavior. |
| Truncation or reasoning-token exhaustion | Inspect finish reason and usage; correct documented output/reasoning controls and rerun the affected slice. |
| Native call passes but harness fails | Treat as adapter/harness incompatibility until disproved; inspect payload, cache, terminal state, and served identity. |
| Parser, cleanup, judge, scorer, rubric, or golden mismatch | Isolate the stage and use the owner's eval-improvement/source-verification workflow; reuse safe cached subject output where honest. |
| Valid output contradicts source-backed expectation | Count as model-quality evidence only after transport and configuration validity are proven. |
| Refusal, filter, or safety behavior | Classify separately as policy/safety compatibility and decide whether it blocks the selected use. |

Change one causal variable at a time. Never keep tuning until a desired score
appears. When retries or operational failures matter, report both:

- conditional semantic quality on valid responses
- end-to-end production result including failures, retries, latency, and cost

Never hide an initial failure by reporting only the successful retry.

## 7. Verify Evidence and Provenance

Before an adoption recommendation:

- classify important mismatches against source evidence
- reject empty, malformed, partial, or internally inconsistent artifacts
- compare quality, latency, cost, variance, success rate, retry overhead, and
  privacy/safety eligibility
- confirm the winning configuration is supported on the intended runtime path
- record commands, model/provider IDs, parameters, source dates, fixture scope,
  repeats, cache state, concurrency, code identity, and actual spend
- retain safe raw or sanitized outputs in an owner-approved durable location;
  when raw content cannot be tracked, record a stable protected pointer plus
  hash, byte size, privacy classification, and regeneration command in a
  tracked manifest. A temporary path and hash alone are not durable evidence
- update the owner's normal story/attempt/registry/scout and work log, including
  failed and inconclusive attempts
- preflight required services before broad suites, then run focused
  adapter/scorer tests and validation proportional to the touched runtime
  surfaces; do not spend time on unrelated frontend/backend suites merely for
  symmetry

For a dirty run, a base commit alone is not reproducible identity. Record the
base SHA plus hashes or an exact tracked snapshot/patch for every changed
adapter, prompt, task, scorer, and golden that affected the result. Hash and
size ignored raw artifacts in a tracked manifest with safe regeneration
commands. Never claim that later-hardened code produced an earlier score.

Do not change a runtime default merely because a model is newer, faster,
cheaper, or stronger on vendor benchmarks.

## 8. Issue the Owner's Layered Verdict

Return a compact evaluation record with:

1. **Decision and owner** — repo, surface, incumbent, adoption question
2. **External evidence** — checked sources/date, exact model and access path
3. **Configuration** — arms, rationale, freshness, fairness, and spend cap
4. **Access** — available, constrained, blocked, or unverified
5. **Transport** — qualified, blocked, or inconclusive
6. **Reliability** — acceptable, degraded, failed, or not measured
7. **Capability** — better, equivalent, worse, or not measured
8. **Economics** — measured latency/cost/retry overhead, or not measured
9. **Adoption** — adopt, conditional adopt, do not adopt, or defer for the exact
   owner surface
10. **Evidence limits and next step** — unmeasured surfaces, remaining proof,
    and the smallest honest follow-up

An access or transport block normally means `capability: not measured` and
`adoption: defer`, unless the missing production feature itself makes the model
ineligible. A valid semantic loss can support `do not adopt`. No adoption
verdict may hide an unqualified required contract.
