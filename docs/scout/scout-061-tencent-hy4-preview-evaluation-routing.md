# Scout 061 — Tencent Hy4 Preview Evaluation Routing

**Source:** Tencent release and open model repository, Tencent Cloud TokenHub
API/model/privacy documentation, and OpenRouter's public model/provider catalogs;
checked 2026-08-29.
**Status:** Do not adopt in Echo Forge; defer in CineForge
**Stage:** Stage 2 campaign complete. Echo Forge produced a decision-grade
rejection; CineForge exhausted the approved strict and diagnostic transport path.
**Candidate:** Tencent/Hunyuan `hy4-preview`; OpenRouter
`tencent/hy4-preview`, canonical catalog snapshot
`tencent/hy4-preview-20260827`.
**Projects reviewed:** dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge.

## Duplicate and availability check

The evaluated-model ledger has no exact `hy4-preview`,
`tencent/hy4-preview`, or dated-checkpoint match. Keep it distinct from
`stealth/ox-alpha`: no authenticated served-identity evidence links them.

Tencent announced and open-sourced Hy4 preview on 2026-08-28. TokenHub publicly
documents exact model ID `hy4-preview`, OpenAI Chat Completions and Responses,
Anthropic Messages, 1M context, 960K maximum input, 64K maximum output, and
pricing of RMB 6/M input, RMB 18/M output, and RMB 0.3/M cached input. The
official open repository documents a text-only 770B MoE model with 49B active
parameters, reasoning modes `high` and `no_think`, and OpenAI-compatible local
serving with tool-call and reasoning parsers.

OpenRouter's current public catalog lists `tencent/hy4-preview`, canonical slug
`tencent/hy4-preview-20260827`, text input/output, 1,048,576 context, 64K
completion, reasoning efforts `high`, `low`, and `none`, plus advertised strict
structured-output and tool parameters. Its price is US$0.834/M input,
US$2.501/M output, and US$0.042/M cached input. OpenRouter currently describes
the Tencent Cloud endpoint as not training on prompts and zero retention, while
OpenRouter prompt/content logging is opt-in. This route-specific metadata must
still be confirmed in the resolved Stage 2 endpoint and owner policy; native
TokenHub's privacy module permits diagnostic/usage retention generally up to
30 days and potentially longer for billing.

This proves **announced** and **API-listed**. Stage 1 used no credential, so
Cam-account **access is unverified**. Catalog fields do not prove exact served
identity, terminal reliability, provider-enforced strict schema or tools,
owner-fixture capability, actual latency, or billed economics.

Sources:

- <https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/>
- <https://github.com/Tencent-Hunyuan/Hy4-preview>
- <https://intl.cloud.tencent.com/zh/document/product/1300/80695>
- <https://intl.cloud.tencent.com/document/product/1300/78952>
- <https://openrouter.ai/api/v1/models>
- <https://openrouter.ai/tencent/hy4-preview>
- <https://openrouter.ai/providers>
- <https://openrouter.ai/docs/guides/privacy/data-collection>

## Evaluate now

1. **CineForge — `script_bible_v1` exact-runtime screen.** Start with one
   no-cache, concurrency-one Open Frequency call against the provisional
   `gemini-3.5-flash-lite` default. Hy4's long-context, structured-output, and
   productivity profile can change a maintained decision whose current
   incumbent evidence is no longer decision-grade under the updated scorer,
   second corpus, and runtime contract. Require exact requested/served identity,
   terminal completion, provider-enforced strict `ScriptBible` schema, overall
   score `>=0.90`, deterministic score `>=0.70` plus hard assertions, rubric
   `>=0.80`, latency `<=30,000 ms`, and subject cost `<=US$0.01`. Stop before a
   second corpus or comparator on any absolute failure. Open Frequency is
   repo-authored synthetic material; no private corpus is authorized.
   **Provider-spend ceiling: US$0.75.**

2. **Echo Forge — `scene-to-soundscape-golden` strict semantic screen.** Run
   Tavern first, then Dungeon only after exact identity, terminal response, and
   strict schema pass. The current contract has no eligible winner:
   `gpt-5.4-mini` and the latest frontier comparators scored `0/2`, so a Hy4
   `2/2` can change the production Sound Extractor decision. Require semantic
   `2/2`, mean latency `<=5,000 ms`, and cost `<=US$0.01` per fixture; rerun the
   incumbent on the same frozen inputs only if Hy4 remains eligible. The two
   checked-in scenes are repo-authored public/synthetic fiction. Require the
   OpenRouter adapter's parameter enforcement, data-collection denial, resolved
   endpoint/privacy record, and protected raw-response provenance.
   **Provider-spend ceiling: US$0.25.**

**Campaign maximum: US$1.00.**

## Not recommended now

- **Dossier — Defer.** C5 is explicitly on hold while Story 161's
  construction/adoption line remains open, and today's stable base does not yet
  route `tencent/*` through its OpenRouter adapter. Reopen after that owner gate
  closes or C5 is explicitly reopened on a stable base; then start with a
  synthetic contract probe and the bounded extraction quick-smoke.
- **Storybook — Defer.** The only plausible text lane is the synthetic
  `luna-persona` suite, but Hy4 has no current evidence of meeting its warm,
  fast, cheap conversational contract. Reconsider only when a low-reasoning
  route is plausibly inside the `1.0` pass-rate, `<=5s`, and `<=US$0.01/turn`
  gates; no private family content is eligible without a provider-policy update.
- **doc-web — Do not evaluate.** Its open decision-bearing model gap is
  image/PDF handwriting OCR, while Hy4 is text-only. Existing text repair lanes
  are green and have no retry trigger.
- **Board Game Ingester — Defer.** Long-context structured extraction could
  eventually challenge manual component inventory, but the maintained evidence
  is still a perfect single-game deterministic seed. A broader eligible corpus,
  reviewed goldens, and provider privacy clearance are prerequisites.
- **Robo Rally — Defer.** It has no maintained live-model lane, and its
  canonical rulebook is private. First create a synthetic/project-owned model
  subject through the legal-action boundary or approve a privacy-cleared
  extracted-rules task.

## Approval and retry boundary

The Stage 1 approval handles are the two numbered owner evaluations above. An
approval authorizes only those isolated owner campaigns and their disclosed
caps; it does not authorize private fixtures, account-policy changes, defaults,
deployment, commits, pushes, merges, or landing.

For deferred owners, re-run portfolio routing only after the named owner gate,
fixture, modality, or privacy prerequisite changes. For the two selected lanes,
stop at access/transport/reliability evidence rather than scoring Hy4 when no
valid terminal owner-contract answer exists.

## 2026-08-29 follow-through — selected owner campaign

Cam approved both numbered evaluations with a combined US$1.00 ceiling. Each
owner ran from a fresh isolated current-base worktree with a temporary
Conductor-custodied OpenRouter credential. Both credentials were removed by
variable name after the owners stopped; no owner-managed credential was
overwritten or removed. No commits, pushes, merges, default changes,
deployments, private fixtures, or provider-account changes occurred.

### CineForge

- **Base / branch / worktree:** `2530ca6c0910672a20594bd2c3908b4b7df43535` /
  `codex/hy4-preview-script-bible` /
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge`.
- **Execution:** the zero-cost resolved matrix contained exactly Hy4 Preview via
  OpenRouter x synthetic Open Frequency, production `script_bible_v1` prompt
  and schema, deterministic scorer, Opus 4.6 rubric, no cache, and concurrency
  one. The tiny native strict-schema probe and its one provider-directed retry
  both returned HTTP 429 before invocation: Tencent `429001`,
  `limit_source=upstream_provider_shared_pool`, `Retry-After: 60`.
- **Spend / stopped surfaces:** US$0.00 of US$0.75. No model output, usage,
  full screenplay, harness-parity case, scorer, judge, comparator, or private
  corpus ran.
- **Verdicts:** access constrained; production transport and strict schema
  unmeasured; reliability failed for the dated route; capability and subject
  economics unmeasured; adoption deferred with provisional
  `gemini-3.5-flash-lite` retained.
- **Owner evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/attempts/031-script-bible-hy4-preview.md`
  and
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/story-217-hy4-preview-access-transport-evidence.json`.
- **Validation:** 12 focused provider tests, 55 focused
  provider/scorer/registry tests, methodology compilation, JSON/YAML parsing,
  Ruff, diff check, then 32 contract/provider/registry tests passed. The full
  unit suite reached 2,174 passes with one expected rolling-manifest hash drift;
  refreshing only the changed shared-surface hashes made the focused manifest
  validation green.

### Echo Forge

- **Base / branch / worktree:** `1bf974a5388e6a63b256f661c6de343fb99d13a9` /
  `codex/hy4-preview-scene-soundscape` /
  `/Users/cam/.codex/worktrees/hy4-preview-echo-forge`.
- **Execution:** zero-cost preflight passed. Three identical Tencent-only Tavern
  calls used fallback disabled, parameter enforcement, denied data collection,
  ZDR, strict JSON Schema, reasoning `none`, and 4,000 output tokens. All three
  returned HTTP 429 before inference; the retained envelopes identify Tencent
  `429001` / `upstream_provider_shared_pool`, and the final attempt followed the
  60-second provider guidance.
- **Spend / stopped surfaces:** US$0.00 of US$0.25. No valid response, schema or
  semantic score, inference latency/cost, Dungeon case, or incumbent rerun
  existed.
- **Verdicts:** access constrained; transport blocked before inference;
  reliability failed for the dated route at 0/3 valid responses; capability
  and inference economics unmeasured; adoption deferred. The capacity stop is
  not Hy4 model-quality evidence.
- **Owner evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20260829-openrouter-tencent-hy4-preview.md`
  plus its paired decision record and tracked transport manifests.
- **Validation:** 54 focused tests, provider-free expected fixtures 2/2,
  methodology check, JSON validation, protected-response hashes, and diff check
  passed. A broadened test command was interrupted during closeout after no
  reported failure; typecheck and lint were therefore not reached.

### Campaign verdict and retry trigger

Aggregate spend was **US$0.00 of US$1.00**. Exact-route catalog and routing
evidence exist, but callability, strict output, capability, latency, and model
economics remain unmeasured. Do not recommend or rerun this exact route merely
because time passed. Resume CineForge at its tiny strict `ScriptBible` probe and
Echo Forge at Tavern only after Tencent shared-pool capacity materially changes
or the affected owner separately authorizes an exact Tencent BYOK route.

## 2026-08-30 follow-through — scheduled heartbeat 1

The approved 12-hour automation resumed both owners at their exact failed
transport gates. Both retained worktrees still matched their refreshed remote
bases. Temporary OpenRouter credentials were injected through Conductor's
custody helper and removed by variable name after the owners stopped. No
private fixture, broadened lane, prompt/golden/scorer/default change, commit,
push, merge, deployment, or provider-account change occurred.

### CineForge retry

- **Attempt:** 032 on retained base
  `2530ca6c0910672a20594bd2c3908b4b7df43535`.
- **Result:** the exact single Tencent endpoint remained catalog-listed. One
  tiny production-shaped strict `ScriptBible` request returned no headers,
  request ID, model/provider identity, output, usage, or cost after more than
  115 seconds. The client was terminated because the 30-second latency and
  terminal-response gates had already failed.
- **Stopped surfaces:** no Open Frequency harness case, scorer, judge,
  incumbent, private fixture, or second corpus ran. Strict schema and capability
  remain unmeasured; Gemini remains the provisional owner.
- **Economics:** confirmed spend US$0.00. Provider-reported cost was unavailable,
  so the owner retained a conservative unreconciled maximum exposure of
  US$0.162 within the US$0.75 cumulative ceiling.
- **Evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/attempts/032-script-bible-hy4-preview-capacity-retry.md`
  and
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/story-217-hy4-preview-retry-2026-08-30-evidence.json`.
- **Validation:** registry consistency, 37 focused tests, Ruff, methodology
  compile/check, and diff checks passed.

### Echo Forge retry

- **Attempt:** `20260830-openrouter-tencent-hy4-preview-heartbeat-1` on retained
  base `1bf974a5388e6a63b256f661c6de343fb99d13a9`.
- **Result:** exact `tencent/hy4-preview` through pinned Tencent returned HTTP
  200, proving dated callability. The response exhausted the frozen 4,000-token
  output budget with `finish_reason=length`; it was quarantined before strict
  schema or semantic scoring. The same incomplete Tavern call took 51,255 ms
  and cost US$0.011015642, independently missing the 5-second and
  US$0.01-per-fixture gates.
- **Stopped surfaces:** Dungeon and the incumbent did not run. Access is now
  available, but terminal production transport failed; strict schema,
  capability, and semantics remain unmeasured. Adoption remains deferred.
- **Economics:** cumulative Echo Forge spend is US$0.011015642 of US$0.25;
  US$0.238984358 remains.
- **Evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20260830-openrouter-tencent-hy4-preview-heartbeat-1.md`
  and its tracked Tavern transport manifest.
- **Validation:** provider-free fixtures 2/2, focused tests 54/54, methodology,
  JSON, hash, and diff checks passed. A pre-existing tracked generated `.pyc`
  deletion remained untouched and outside the campaign conclusion.

### Current campaign state

Neither owner succeeded, so the automation remains active. Confirmed aggregate
spend is **US$0.011015642**, with CineForge also reserving a conservative
unreconciled exposure of at most US$0.162. The next heartbeat may retry only the
unchanged tiny CineForge transport probe and unchanged Echo Forge Tavern gate.
Changing reasoning, output budget, prompt, schema, scorer, golden, route, or
privacy posture is a new configuration arm and is not authorized by the
heartbeat.

## 2026-08-30 follow-through — scheduled heartbeat 2

The second scheduled retry again used the retained current-base owner
worktrees and temporary Conductor-custodied OpenRouter credentials. Both
injected variables were removed afterward. No private fixture, broadened lane,
contract/configuration change, commit, push, merge, deployment, default change,
or provider-account change occurred.

### CineForge retry

- **Attempt:** 033 on retained base
  `2530ca6c0910672a20594bd2c3908b4b7df43535`.
- **Result:** the unchanged Tencent-pinned strict `ScriptBible` probe accepted
  response headers and began reading a chunked body, but no complete body was
  available at the hard 30-second latency boundary. The client was interrupted
  immediately. No request ID, served identity, terminal output, schema result,
  usage, provider-reported cost, or raw artifact existed.
- **Stopped surfaces:** Open Frequency, scorer, judge, incumbent, private
  fixtures, and second corpus did not run. Transport, reliability, and latency
  failed; strict schema and capability remain unmeasured. Gemini remains the
  provisional owner.
- **Economics:** confirmed spend remains US$0.00. Conservative unreconciled
  exposure is at most US$0.162 for this attempt and US$0.324 cumulative, leaving
  US$0.426 under the US$0.75 owner ceiling.
- **Evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/attempts/033-script-bible-hy4-preview-heartbeat-2.md`
  and
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/story-217-hy4-preview-retry-2026-08-30-heartbeat-2-evidence.json`.
- **Validation:** evidence and registry parsing, registry consistency, 37
  focused tests, Ruff, methodology compile/check, and diff checks passed.

### Echo Forge retry

- **Attempt:** `20260830-openrouter-tencent-hy4-preview-heartbeat-2` on retained
  base `1bf974a5388e6a63b256f661c6de343fb99d13a9`.
- **Result:** Tavern returned HTTP 200 with exact `tencent/hy4-preview` identity,
  pinned Tencent provider, terminal `stop`, strict JSON Schema, deterministic
  normalization, and version-3 provenance. This qualified the production
  transport contract for the dated Tavern call.
- **Capability:** the maintained semantic gate failed 0/1. The output omitted
  the optional muted-music lane, classified the primary mood as neutral rather
  than tense, and did not preserve `Dice on wood` as a distinct scene-detail
  layer. These are valid-output semantic misses under the frozen golden.
- **Operations:** latency was 27,126 ms, failing the 5-second gate. Cost was
  US$0.004915703, passing the US$0.01 fixture gate. Dungeon and the incumbent
  did not run under the progressive stop.
- **Economics:** cumulative Echo Forge spend is US$0.015931345 of US$0.25,
  leaving US$0.234068655.
- **Evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-echo-forge/docs/evals/attempts/scene-to-soundscape-golden/20260830-openrouter-tencent-hy4-preview-heartbeat-2.md`
  and its tracked Tavern attempt group.
- **Validation:** provider-free fixtures 2/2, focused tests 54/54, methodology,
  JSON/hash, and diff checks passed. The pre-existing tracked generated `.pyc`
  deletion remained untouched.

### Campaign closeout and authorization boundary

The approved campaign did not succeed. Echo Forge now has decision-grade
evidence to reject this frozen configuration: access and strict transport
qualified, but the first fixture failed both semantic and latency gates.
Repeating that unchanged arm would not be a reliability retry and is not
justified. CineForge remains blocked at its unchanged terminal-response and
latency gate, with capability unmeasured.

Confirmed aggregate spend is **US$0.015931345**, plus CineForge conservative
unreconciled exposure bounded at **US$0.324**, within the US$1 campaign ceiling.
Pause the 12-hour automation. Any further attempt now requires a material
model/checkpoint or provider-contract change, or explicit authorization for a
new owner configuration arm; do not repeat the unchanged campaign.

## 2026-08-31 follow-through — requested capability diagnostic

Cam asked whether the full evaluation had been completed and authorized any
legitimately missing work under `/evaluate-model`. Echo Forge required no
additional call: its terminal strict Tavern result already completed the
decision-bearing first gate and supported `do not adopt`; running Dungeon after
that semantic and latency failure would have violated the frozen progressive
stop.

CineForge still lacked any terminal model response, so the current evaluation
protocol allowed one bounded diagnostic on the approved synthetic micro-source.
Attempt 034 preserved the exact model, Tencent provider pin, prompt, input,
reasoning, 64,000-token ceiling, parameter enforcement, cache, concurrency, and
route. It relaxed only provider-enforced `response_format` / strict JSON Schema
and extended the observation window to 180 seconds for diagnostic capability
isolation; the 30-second production latency gate remained failed.

OpenRouter returned HTTP 200 headers and generation ID
`gen-1788190415-zAmnrXHfWcL1fbYk8NZ6`, but delivered zero response-body bytes
before the 180.006-second diagnostic stop. There was therefore no terminal
response, served identity, finish reason, usage, provider-reported cost, schema
or parse result, semantic output, or score. Omitting strict schema did not
isolate strict mode as the cause. The progressive gate correctly stopped before
Open Frequency, scorer, judge, comparator, private fixture, or second corpus.

- **Evidence:**
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/attempts/034-script-bible-hy4-preview-capability-diagnostic.md`
  and
  `/Users/cam/.codex/worktrees/hy4-preview-cineforge/docs/evals/story-217-hy4-preview-capability-diagnostic-2026-08-31-evidence.json`.
- **Economics:** confirmed CineForge spend remains US$0.00. Attempt 034 adds a
  conservative unreconciled exposure bound of US$0.162, bringing CineForge's
  cumulative bound to US$0.486 and leaving US$0.264 under its US$0.75 ceiling.
  Confirmed campaign spend remains US$0.015931345.
- **Validation:** registry/evidence parsing and consistency, 37 focused tests,
  Ruff, methodology compile/check, and diff checks passed. The temporary
  OpenRouter variable was removed by name after the owner stopped.

### Final owner verdicts

- **Echo Forge:** access and strict transport qualified. Capability was worse
  than the maintained Tavern gate, latency failed, and the frozen configuration
  is **do not adopt**. Dungeon and incumbent are intentionally unmeasured.
- **CineForge:** access remains constrained; strict production transport and
  the one-variable diagnostic both failed to deliver a terminal body.
  Reliability failed, capability/schema/semantics remain unmeasured, and
  adoption is **defer** with Gemini retained.

The campaign is complete rather than successful. No unchanged retry is
justified. Reopen only for a material model/checkpoint or provider-transport
change, or a separately approved configuration/route decision.
