# Scout 056 - GLM-5.3 CineForge Script-Bible Evaluation Handoff

**Mode**: Conductor handoff
**Date checked**: 2026-08-20
**Status**: Defer
**Owner**: CineForge (`/Users/cam/Documents/Projects/cine-forge`)
**Decision surface**: `script-bible` / production `script_bible_v1`

## Decision and Owner

CineForge owns the only first evaluation recommended for GLM-5.3. The decision
is whether hosted Z.ai `glm-5.3` can replace the provisional
`gemini-3.5-flash-lite` default for one-call script-bible extraction while
clearing the repaired exact-runtime quality, latency, cost, reliability,
schema, and privacy gates.

This is a challenger screen, not an adoption recommendation. Conductor must not
call the provider, run CineForge's benchmark, edit its eval registry, or change
the runtime default.

Why this lane:

- it is a maintained, default-driving, text-only long-context lane;
- the production prompt, `ScriptBible` Pydantic schema, two source fixtures,
  two hand-authored goldens, deterministic scorer, and cross-provider rubric
  already exist;
- GLM-5.3's 1M context and 128K maximum output are relevant;
- the repaired lane has a real unresolved decision because its configured
  Gemini default remains provisional at the exact runtime boundary.

Do not route GLM-5.3 first to Dossier. Its primary checkout currently contains
an active semantic/runtime refactor touching model behavior, benchmarks,
scorers, and the registry, so it cannot provide a clean frozen comparison.
Doc Web's current decision-bearing lanes need image input; Storybook chat is a
poor fit; Echo Forge is on an active dirty story branch; Board Game Ingester
and RoboRally do not currently expose a stronger maintained subject-model lane.

## External Evidence

First-party Z.ai sources checked 2026-08-20:

- model ID: `glm-5.3`;
- input/output: text only, 1M-token context, 128K maximum output;
- hosted general API example:
  `POST https://api.z.ai/api/paas/v4/chat/completions`;
- documented compatible surfaces also include Coding Plan Chat Completions,
  OpenAI Responses, and Anthropic Messages endpoints, but account/path parity
  is not established;
- reasoning cannot be disabled; `reasoning_effort` accepts `low`, `high`, or
  `max`, defaults to `max`, and `thinking.type` must be `enabled`;
- function calling and JSON output are documented, but the detailed API
  reference exposes `response_format: {"type":"json_object"}`, not a strict
  API-enforced `json_schema` contract. Official schema examples validate
  client-side. Strict `ScriptBible` enforcement is therefore unverified and a
  hard transport gate;
- pay-as-you-go list price per 1M tokens is `$1.40` input, `$0.26` cached
  input, and `$4.40` output;
- public account-specific rate/concurrency limits are not stated; the docs
  route signed-in users to their rate-limit dashboard;
- the API DPA says API input/output content is processed in real time and not
  stored, other customer data may be temporarily stored, and processing is
  generally in Singapore. The docs do not expose a named ZDR request control,
  so the owning repo must confirm that the account and exact access path meet
  its privacy policy before using the non-synthetic fixture.

Sources:

- https://docs.z.ai/guides/llm/glm-5.3
- https://docs.z.ai/guides/overview/migrate-to-glm-new
- https://docs.z.ai/api-reference/llm/chat-completion
- https://docs.z.ai/guides/capabilities/struct-output
- https://docs.z.ai/guides/overview/pricing
- https://docs.z.ai/legal-agreement/privacy-policy
- https://z.ai/blog/glm-5.3

## Owning-Repo Decision Contract

Use CineForge's current repo-local surfaces without changing their meaning:

- registry: `docs/evals/registry.yaml`, eval ID `script-bible`;
- production prompt/schema provider: import `EXTRACTION_PROMPT` and
  `ScriptBible` from the production `script_bible_v1` boundary;
- runtime matrix: `benchmarks/runtime_tasks/script-bible-runtime.yaml`;
- deterministic scorer: `benchmarks/scorers/script_bible_scorer.py`;
- synthetic/public first case:
  `tests/fixtures/ingest_inputs/open_frequency_short.fountain` with
  `benchmarks/golden/open-frequency-script-bible.json`;
- second case, only after privacy eligibility:
  `benchmarks/input/the-mariner.md` with
  `benchmarks/golden/the-mariner-script-bible.json`;
- incumbent: production `gemini-3.5-flash-lite`, 65,536 output tokens and
  minimal thinking.

Maintained pass gates:

- aggregate quality `>= 0.90`;
- deterministic score threshold `>= 0.70` plus all existing exact-field,
  structure, grounding, exclusion, confidence, and source-event hard gates;
- frozen Claude Opus 4.6 rubric `>= 0.80`;
- latency `<= 30,000 ms` per subject call;
- subject cost `<= $0.01` per call;
- exact requested/served identity, no fallback, documented terminal success,
  complete output, valid raw usage/cost, and provider-enforced strict
  `ScriptBible` JSON;
- concurrency `1`, subject cache bypassed, and no semantic retry after a valid
  completion.

The older Gemini `0.9100 / 6,074 ms / $0.0049` row is not exact-runtime
decision evidence. Rerun the incumbent on the same frozen case only after the
candidate clears every absolute gate.

## Access and Transport Ladder

Run this only from an isolated CineForge worktree under CineForge's credentials
and policies:

1. Confirm the intended account can list or call exact `glm-5.3` on the
   pay-as-you-go general API. Do not assume Coding Plan quota or endpoints are
   valid for benchmark/application use.
2. Make the smallest native Chat Completions call. Retain a sanitized request,
   raw response, terminal state, latency, usage, request ID, and returned model.
3. Exercise the exact production schema contract. JSON-object mode or
   post-response Pydantic validation is not equivalent to provider-enforced
   strict schema. Function arguments count only if the provider reliably
   enforces the complete supported schema and the call cannot silently answer
   outside it.
4. Send the same small public/synthetic case through the CineForge adapter and
   compare the actual outgoing request and raw envelope with the native call.
5. Stop before semantic scoring if access, served identity, terminal state,
   exact schema, usage accounting, or harness parity fails.

## Predeclared Configuration Matrix

Freshness mode is a new-candidate uncached screen. It is not force-fresh
incumbent parity unless the candidate advances.

Aggregate provider-spend ceiling: **US$5**, including probes, candidate,
incumbent, bounded retries, and judge calls.

Predeclare two transport/calibration arms before scores:

1. `low`: `thinking.type=enabled`, `reasoning_effort=low`, sampling omitted,
   and an output budget large enough for the exact schema. This is the primary
   value/default arm because the slot has hard latency and cost limits and the
   incumbent uses minimal thinking.
2. `max`: `thinking.type=enabled`, `reasoning_effort=max`, sampling omitted,
   on the same tiny public transport case only. This preserves the provider's
   default/recommended deep-reasoning call shape as a ceiling calibration.

Freeze one arm before the scored Open Frequency case using only contract
validity plus the predeclared latency/cost plausibility gates. Do not choose the
arm from semantic scores. If `max` cannot plausibly clear the slot's absolute
operational limits, freeze `low`; if `low` cannot meet the exact schema
contract, do not weaken the contract or score it. No `high`, prompt, sampling,
or output-budget arm may be added after seeing a score without a separately
declared experiment.

Transport/capacity retry cap: one retry only for a documented transient
capacity/timeout condition, respecting provider guidance. Retain both attempts
and include retry latency/cost. Contract repair cap: change one documented
request variable, rerun native, then rerun harness parity. A content-changing
repair becomes a new exploratory configuration arm.

## Progressive Execution and Stops

1. Complete the transport ladder on a tiny synthetic payload.
2. Run one uncached exact-runtime Open Frequency case.
3. Inspect raw output, deterministic mismatches, rubric evidence, latency,
   usage, cost, identity, and privacy metadata.
4. Stop on any absolute gate failure. Do not run the incumbent or second
   corpus to rescue an ineligible candidate.
5. Only after GLM-5.3 clears every gate, rerun the incumbent on identical
   frozen Open Frequency input/configuration opportunity.
6. Advance both frozen configurations to The Mariner only when its privacy
   classification is eligible for the proven route. Complete the repo's
   required repeat/provenance policy before any adoption recommendation.

Classify access, provider, adapter, parser, scorer, judge, and model failures
separately. In particular, JSON/schema or reasoning-envelope failures before a
valid answer are transport evidence, not semantic misses.

## Required Durable Evidence

CineForge owns the attempt record, registry update, story/work log, result
artifacts, and adoption verdict. Record exact command, base SHA plus any dirty
adapter/prompt/scorer hashes, prompt/rendered-input hashes, golden/scorer
hashes, model/provider/endpoint, parameters, cache state, concurrency, retries,
request/response terminal metadata, served identity, raw/normalized usage,
latency, price source, privacy classification, artifact hashes/sizes, and safe
regeneration commands. Never persist keys, authorization headers, or private
raw payloads in committable evidence.

## Conductor Verdict

- **Access**: unverified
- **Transport**: inconclusive; strict schema support is the first hard blocker
  to test
- **Reliability**: not measured
- **Capability**: not measured
- **Economics**: list pricing known; lane-specific latency, token use, cost,
  and retry overhead not measured
- **Adoption**: not evaluated - target-repo handoff required
- **Evidence limit**: Z.ai's launch evidence is concentrated in coding,
  terminal, agent, and cyber tasks. It is a reason to screen transport and one
  maintained long-context case, not evidence that GLM-5.3 will beat CineForge's
  incumbent on screenplay semantics.

Smallest next step: a CineForge owner creates an isolated worktree, proves the
exact pay-as-you-go access and strict `ScriptBible` contract on synthetic data,
then runs only the Open Frequency case if transport qualifies.

## Owner Follow-Through — 2026-08-20

CineForge executed the handoff in an isolated owner worktree and closed Eval
Attempt 027 and Story 214 as `deferred — no key configured`. No Z.ai credential
or authenticated account session was available; a credential-free request to
the exact general endpoint returned HTTP 401/provider code 1001 before model
inference. Current official documentation still exposed JSON-object output plus
client-side validation rather than provider-enforced strict `ScriptBible` JSON.

The owner therefore stopped before native authenticated transport, harness
parity, semantic scoring, incumbent, judge, or Mariner calls. Spend was `$0` of
the `$5` ceiling. Access and transport were blocked; reliability, capability,
and lane economics were not measured; adoption remained `defer`, and
`gemini-3.5-flash-lite` stayed unchanged. CineForge landed the sanitized
owner-owned record in commit `9486191`.

Retry only after a CineForge-scoped pay-as-you-go Z.ai credential exists and
current first-party or live native evidence can qualify provider-enforced strict
schema. Do not repeat credential-free probes or substitute a router silently.
