---
name: evaluate-model
description: Plan, route, execute, or audit a fair evaluation of one or more AI models against an owning repo's maintained decision surface. Use for natural-language new-model, replacement, comparison, rerun, reproducibility, or evidence-audit requests, including broad, narrow, or informal briefs where API contract, structured output, reasoning, reliability, cost, latency, or quality affect adoption. In Conductor, prepare or audit the handoff only; the owning repo executes and decides. Use scout for generic launch or portfolio-fit questions without a decision-bearing eval request.
user-invocable: true
---

# /evaluate-model [natural-language evaluation brief]

Evaluate each candidate through its best defensible production-relevant call
shape, not by changing model names and accepting the first harness result.

## Invocation Contract

Treat everything after `/evaluate-model` as an evaluation brief, not positional
arguments. A model name alone is sufficient. The brief may be long, informal,
tightly scoped, self-correcting, or name several candidates. Extract and retain:

- candidate names, possible slugs/providers/access paths, and any incumbent
- target repo, runtime stage, eval lane, fixtures, or narrow capability
- requested reasoning, output, schema, tool, sampling, modality, or route
- cost, latency, concurrency, privacy, safety, repeat, and deadline constraints
- execution intent such as evaluate/run/test/compare versus plan/design/recommend
- freshness intent such as reuse, audit, rerun from scratch, reproduce, check
  variance, or exercise the workflow fresh
- exclusions and later corrections; the latest clear instruction wins

Resolve routine omissions from current first-party documentation and repo truth.
Do not require an exact slug, eval ID, incumbent, or provider when those are
discoverable. Preserve a narrow request rather than widening it into a model
tournament. For multiple candidates, qualify each independently and compare each
against the same maintained incumbent per surface, using provider-valid call
shapes and progressive screening rather than pairwise tournaments.

Inside Conductor, `evaluate`, `run`, `test`, or `compare` means prepare an
execution-ready owning-repo handoff; it never authorizes Conductor to call the
provider or edit the target repo. `Plan`, `design`, `scope`, or `recommend`
produces a handoff plan. `Audit`, `inspect`, or `review existing evidence`
produces a read-only evidence audit with no provider call, harness execution,
artifact creation, or repo mutation. In an owning repo, execution verbs authorize
only the smallest bounded run under that repo's credentials and policies.

Treat a clear request to rerun from scratch, reproduce prior evidence, measure
variance, or exercise the workflow fresh as **force-fresh intent**. In Conductor,
record that requirement in the handoff; do not execute it. In the owning repo,
force-fresh overrides duplicate avoidance only: preserve prior evidence, use new
artifact identities and uncached subject calls, and report whether the result
reproduces, weakens, or contradicts the prior result. It never relaxes scope,
privacy, spend, fairness, tuning, retry, truth, commit, or rollout controls.

When force-fresh intent leaves comparison shape unstated, a workflow-acceptance
or fresh adoption comparison reruns the incumbent and candidate on the same
frozen inputs. Candidate-variance or transport reproduction may be
candidate-only, but cannot support a current superiority claim.

Ask only when authority, credentials, private-payload approval, materially higher
spend, or an unresolved product choice is required. If no maintained owner lane
could change a decision, return an evidence-backed no-eval or defer result.

## Operating Mode

State one mode before proceeding:

- **Conductor handoff** — while working in Conductor, research current
  first-party documentation and existing public or authorized access evidence,
  then prepare or audit the owning-repo packet according to the invocation.
  Do not run provider probes, use target credentials or fixtures, execute
  another repo's harness, mutate its eval surfaces, or issue its adoption
  verdict. Sections 3–7 become handoff or audit requirements, not actions.
- **Owning-repo execution** — only while working under the authority of the repo
  that owns the runtime, credentials, fixtures, and decision. Follow the full
  workflow and retain evidence under that repo's policies.

If the mode or owning repo is unclear, stop and resolve ownership before any
model call.

## Non-Negotiable Rule

Do not call a model bad when the request, provider path, harness adapter, or
output contract failed before a valid answer was produced. Preserve those
failures as access, transport, or reliability evidence; keep them separate from
semantic capability.

## 1. Establish Ownership and the Decision

Identify the repo that owns the runtime and maintained eval. Conductor may
scout availability and prepare a handoff, but the owning repo must run model
calls, inspect artifacts, update eval records, and decide adoption.

Before spending tokens, record:

- candidate and incumbent model/provider
- exact runtime stage or product surface that could change
- maintained prompt, fixtures, scorer/golden, and current winning evidence
- quality threshold plus latency, cost, reliability, privacy, and safety limits
- the decision this evidence can support: adopt, conditional adopt, do not
  adopt, or defer

If no result could change a maintained decision, stop and recommend no eval.

## 2. Refresh External Truth

Use current first-party documentation. In owning-repo execution mode, add live
provider evidence; in Conductor handoff mode, use existing public or authorized
evidence only. Do not rely on model-family memory, announcement copy, or a
harness alias alone.

Build a dated call-contract sheet covering every item relevant to the target:

- exact model slug, aliases/tiers, availability, region, and access path
- native endpoint/API family and current SDK or harness support
- actual served-model/provider metadata, router fallback policy, and parameter
  enforcement when an intermediary is used
- required text, image/file, tool, streaming, or long-context input shape
- supported instruction/message roles when they affect the call contract
- structured-output or strict JSON Schema support and its required flags
- tool-choice behavior when the runtime uses tools
- reasoning/thinking controls and supported values
- output-token controls and whether reasoning consumes that budget
- supported or rejected sampling, stop, seed, and penalty parameters
- pricing, rate/concurrency limits, service tier, and availability guidance
- retention, training, zero-data-retention, and other payload policy

Prefer the direct provider when it is the cleanest supported path. Check
OpenRouter when it is the best practical access or normalization path. A model
is not reproducibly evaluable from an interactive preview, announcement, or
automation-prohibited plan alone.

Resolve unknowns that can invalidate the eval. Otherwise mark them as explicit
blockers; do not fill them with guesses.

## 3. Qualify Transport Before Scoring

In owning-repo execution mode, advance through this ladder and retain the
sanitized request payload, response, terminal status, latency, usage, served
identity, and error/incomplete evidence at each step:

1. **Access probe** — confirm the exact model ID is visible and authorized with
   the intended credentials and region. Catalog visibility alone is not
   callability.
2. **Native probe** — make the smallest raw provider call, outside the eval
   harness when practical; confirm the requested model/provider was actually
   served when response metadata exposes it.
3. **Contract probe** — exercise what production actually needs: strict schema,
   tools, images/files, long context, or another required feature.
4. **Harness-parity probe** — send the same small case through the repo adapter
   or eval harness and compare it with the native result.

Qualify every materially distinct runtime surface and output contract
separately. A schema proven for one task does not qualify another task with a
different output contract merely because both use the same provider. Do not
start a surface's scored matrix until its required contract and harness-parity
probe pass. If raw native succeeds but the harness fails, investigate the
adapter. If the provider lacks a required production feature, record a genuine
compatibility limit rather than a semantic failure.

Fail closed before scoring. HTTP success is insufficient: require the provider's
documented terminal-success state, no provider error or incomplete condition,
the expected served model/provider, and complete output from the documented
message field. Verify the actual outgoing prompt/input payload and required
schema/tool flags rather than trusting adapter configuration names. Reject
malformed envelopes, wrong identities, partial output, invalid usage/cost, and
contract-invalid responses as operational evidence; do not pass them to the
semantic scorer.

Follow the owner's artifact policy. Never persist authorization headers, API
keys, signed URLs, or equivalent secrets. Keep private inputs and outputs only
in an owner-approved protected or ignored location; committable evidence uses
redacted excerpts, hashes, or safe pointers rather than raw private payloads.

When JSON is required, use strict schema enforcement when supported. If only a
weaker documented JSON mode exists, test and label that limitation. Prompt-only
JSON is not equivalent to API-enforced structure. Ensure the output budget can
hold the schema before judging malformed or incomplete JSON. A passing unit
parse or harness smoke is not contract parity without inspecting the native
request, raw output, terminal state, and served identity.

## 4. Predeclare a Fair Configuration Budget

Write the configuration matrix before looking at scores:

- set an aggregate provider-spend ceiling covering access/contract probes,
  candidates, incumbent, retries, and judge calls; if the user and repo provide
  no tighter cap, default to **US$5** for the owning-repo invocation
- estimate and start a cost ledger before the first paid call; stop and request
  an explicit higher cap when the smallest valid run may exceed the ceiling or
  pricing cannot be bounded conservatively
- rerun the incumbent on its maintained production configuration when fresh
  comparison evidence is needed
- run the challenger with provider-recommended defaults plus the required
  production output/tool contract
- predeclare the exact challenger arm count and the transport-debug retry and
  repair cap; use the recommended configuration plus at most two justified
  variants, such as a lower or higher documented reasoning level or a necessary
  output-budget adjustment
- give incumbent and challenger comparable opportunity; do not exhaustively
  tune only the challenger
- choose among variants on a predeclared calibration slice when possible, then
  freeze one configuration before the decision-bearing comparison
- if variants share the scored decision fixtures, label selection exploratory;
  do not present the best observed score as independent evidence without a
  predeclared held-out or repeated confirmation run
- do not expand the tuning or debug budget after seeing scores without explicit
  owning-repo approval; a new causal hypothesis starts a separately declared
  experiment with comparable incumbent treatment
- keep prompt, fixtures, scorer, golden, and downstream cleanup fixed during
  model comparison
- bypass the subject-output cache for a model/configuration change, or prove
  the cache key includes the exact model and relevant parameters
- start at low, documented-safe concurrency; test intended production
  concurrency separately so client-induced overload is not mislabeled

A request-shape or documented schema-flag repair needed to obtain any valid
response is transport work, not score optimization. A repair that can change
answer content—including prompt, reasoning level, or output budget—becomes a
declared configuration arm and its exploratory score is not promotion evidence.
If a model-specific prompt is later justified, record it as a separate
prompt-plus-model candidate with its maintenance cost; never silently move the
goalposts.

## 5. Run Progressively

Use the smallest run that answers the current question:

1. one representative smoke case
2. the known failing or differentiating slice
3. a bounded maintained fixture set
4. promotion-grade comparison with the repo's required repeats and artifacts

Inspect raw outputs and artifacts between stages. Do not launch a broad matrix
to debug one malformed call. Stop weak or incompatible candidates before
expensive promotion runs, but retain their evidence.

If an earlier prerequisite stops a later materially distinct surface, report
that surface as `capability: not measured` and `adoption: not advanced`. A
deliberate progressive stop is not semantic evidence that the skipped surface
failed.

## 6. Classify and Respond to Failures

For every non-pass, first identify the stage that produced it: subject-model
request, provider/router, harness adapter, parser, downstream cleanup, scorer,
or judge. Do not charge a judge or post-processing failure to the subject
model. Then record the evaluation phase and one primary class:

| Failure class | Required response |
| --- | --- |
| transient provider capacity, timeout, `5xx`, or capacity-coded `429` | Respect provider guidance or `Retry-After`; retry within a declared cap; retain every attempt and include retry latency/cost. Persistent instability affects reliability, not semantic quality. |
| auth, quota, region, tier, or policy | Correct only within existing authorization; otherwise mark access blocked or constrained. Do not score capability. |
| client concurrency or rate-limit `429` | Inspect advertised limits and harness concurrency, then rerun within the declared cap. Client-induced overload is harness/configuration evidence; a plan limit is access or economics evidence. |
| wrong endpoint, API family, input shape, or unsupported parameter | Recheck current docs, correct one contract variable, rerun the native probe, then rerun harness parity. |
| structured output not enforced | Enable supported schema/JSON controls and ensure the schema is supported before judging JSON compliance. |
| truncation or thinking-token exhaustion | Inspect finish reason and usage; correct documented output/thinking controls and rerun the affected slice. |
| native call passes but harness fails | Treat as adapter/harness incompatibility until disproved; check cache and actual served-model metadata; do not blame the model. |
| parser, cleanup, judge, scorer, rubric, or golden mismatch | Isolate the failing stage and use the owning repo's eval-improvement and source-verification workflow before changing truth surfaces. |
| valid output contradicts source-backed expectation | Count as model-quality evidence after transport and configuration validity are proven. |
| refusal, content filter, or safety behavior | Classify separately as policy/safety compatibility and decide whether it blocks the target use. |

Change one causal variable at a time while debugging. Use bounded retries; do
not keep experimenting until a desired score appears.

Classify `429` responses from the provider error code/body, headers, account
limits, and tested concurrency. Do not assume every `429` is transient provider
instability.

Report two views when retries or provider failures matter:

- **conditional semantic quality** on valid responses
- **end-to-end production result** including provider failures, retries, added
  latency, and added cost

Never hide initial failures by reporting only the successful retry.

## 7. Verify and Decide

Before recommending adoption:

- classify important mismatches against source evidence
- validate result artifacts and reject empty, malformed, or partial bundles
- compare quality, latency, cost, variance, success rate, retry overhead, and
  privacy/safety eligibility
- confirm the winning configuration is supported on the intended runtime path
- record exact commands, model/provider IDs, relevant parameters, checked docs,
  dates, fixture scope, repeats, cache state, concurrency, and code identity
- update the owning repo's eval registry and work log, including failed and
  inconclusive attempts

For a dirty run, a base commit alone is not exact code identity. Record the base
SHA plus hashes or an exact tracked snapshot/patch for every changed adapter,
prompt, scorer, golden, and task that affected the result. Hash and size raw
artifacts; if they remain ignored or protected, keep a tracked manifest with
safe regeneration commands and redacted pointers. Distinguish evaluated code
from later hardening so a newer adapter is never claimed to have produced an
older score.

Do not change defaults merely because a model is newer, faster, or cheaper. It
must clear the maintained quality and operational gates for a named surface.

## Required Output

Return a compact evaluation record with these separate verdicts:

1. **Decision and owner** — repo, target surface, incumbent, adoption question
2. **External evidence** — checked sources/date, exact model and access path
3. **Configuration matrix** — variants tried, rationale, aggregate spend cap,
   freshness mode, and fairness statement
4. **Access** — available, constrained, blocked, or unverified
5. **Transport** — qualified, blocked, or inconclusive
6. **Reliability** — acceptable, degraded, failed, or not measured
7. **Capability** — better, equivalent, worse, or not measured
8. **Economics** — measured latency/cost and retry overhead, or not measured
9. **Adoption** — in the owning repo: adopt, conditional adopt, do not adopt,
   or defer, naming the exact surface; in Conductor: not evaluated, target-repo
   handoff required
10. **Evidence limits and next step** — unmeasured surfaces, what remains
    unproven, and the smallest honest follow-up

In owning-repo execution mode, an access or transport block normally yields
`capability: not measured` and `adoption: defer` unless the missing production
feature itself makes the model ineligible. A valid semantic loss may support
`do not adopt`. In Conductor mode, use the handoff-only adoption state above.
State which one happened.

## Conductor Boundary

When invoked from Conductor:

- inspect portfolio fit and current access evidence
- choose the owning repo and one decision-bearing eval lane
- prepare a repo-local handoff containing the decision contract, required docs
  and probes, proposed bounded matrix and aggregate spend ceiling, pass/fail
  gates, freshness requirement, privacy constraints, and durable provenance
- do not run another repo's benchmark, modify its eval surfaces, or claim model
  quality from Conductor
- report `adoption: not evaluated — target-repo handoff required`; Conductor's
  routing recommendation is not the owning repo's adoption verdict
- report `access: unverified` unless dated owner-run callability evidence proves
  another state; lack of Conductor execution authority is not proof that the
  model itself is blocked
- never copy or persist target-repo credentials or private payloads in
  Conductor

Synthetic incident tests may validate this skill's reasoning, but they do not
qualify live transport or benchmark performance. Say so explicitly.

## Guardrails

- Do not score pre-response infrastructure failures as semantic misses.
- Do not dismiss repeated instability; keep it in production reliability.
- Do not weaken schema, tools, or input requirements merely to make a candidate
  pass unless the runtime can accept that weaker contract.
- Do not alter goldens or scorers to rescue a model without source-backed
  verification.
- Do not send private fixtures through a provider path that has not cleared the
  owning repo's privacy policy.
- Do not commit, push, change defaults, or broaden rollout without explicit
  authorization.
