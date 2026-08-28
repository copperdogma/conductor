# Scout 060 — Qwen3.8-Flash-Next Evaluation Routing

**Source:** Qwen first-party release blog, official GitHub and Hugging Face
model cards, Alibaba Cloud Model Studio's public model catalog and lifecycle
pages, QwenCloud's public model surface, and OpenRouter's live public catalog;
checked 2026-08-26.
**Status:** Defer
**Stage:** Stage 2 completed for CineForge and doc-web; both owner evaluations
stopped at the managed route's upstream shared-pool capacity gate before their
semantic benchmarks could run. Dossier was excluded by user direction.
**Candidate:** exact open checkpoint `Qwen/Qwen3.8-Flash-Next`
**Projects reviewed:** conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Duplicate check

The exact Flash-Next checkpoint has not been evaluated in the tracked repos.
Prior Qwen3.8 evidence is for a different model: `qwen/qwen3.8-max`. CineForge
Attempt 021 rejected Qwen3.8 Max on the `script-bible` lane after a valid strict
response missed both the 30-second latency and $0.01/call gates. doc-web
Attempt 024 rejected Qwen3.8 Max after its crop detector reached `12/13` and
`0.9411`, below the `13/13` and `>=0.95` entry gate. Those results are useful
comparators and retry triggers, not Flash-Next capability evidence.

## Current identity and access evidence

Qwen released `Qwen/Qwen3.8-Flash-Next` on 2026-08-26 as an open-weight,
experimental preview of the architecture intended for Qwen4. It is a native
multimodal MoE model with a 125B main model, 6B activated parameters per token,
51B additional n-gram embedding parameters, and 4B MTP parameters. The model
card documents text, image, and video input; text output; 262,144 native context
with optional YaRN extension to 1,000,000 tokens; thinking enabled by default;
and self-hosted OpenAI-compatible serving through Transformers, SGLang, vLLM,
and TokenSpeed.

The official materials do not yet establish a stable exact managed-API
contract suitable for an owning-repo evaluation:

- The Qwen release blog describes the production derivative as
  `Qwen3.8-Flash`, with 1M context and built-in tools, at $0.16/M input and
  $0.47/M output. QwenCloud's current developer guide now lists the managed
  API model code `qwen3.8-flash`. That production derivative is available but
  is not the exact requested checkpoint, so it cannot be substituted silently.
- The official GitHub/model-card quickstarts mention QwenCloud and use
  `Qwen/Qwen3.8-Flash-Next` in generic OpenAI-compatible examples, but the
  public QwenCloud and Alibaba Model Studio catalogs checked on 2026-08-26 do
  not expose that exact checkpoint as a managed model code distinct from
  `qwen3.8-flash`, or specify exact-checkpoint limits, price, and strict-output
  behavior.
- OpenRouter's live public catalog returned no exact case-insensitive
  Qwen3.8-Flash-Next match on 2026-08-26.

Therefore: **announced and weights-released; exact managed API listing not
verified; access/callability unverified.** Self-hosting is technically
documented, but no registered owner has a declared serving target for this
roughly 180B-parameter artifact. Self-hosting cost, latency, quantization,
strict-schema behavior, and owner reproducibility are consequently unbounded.
Provider-enforced strict JSON Schema is also not established by the generic
self-host examples. A prompt, parser, or tool-call parser is not a substitute
for that production-contract proof.

No exact managed route means there is no managed retention/training or ZDR
posture to approve yet. A truly owner-local deployment would keep eligible
payloads local, subject to the model license and owner infrastructure controls;
that observation does not authorize acquiring or operating the required
hardware.

Official sources:

- <https://qwen.ai/blog?id=qwen3.8-flash-next>
- <https://github.com/QwenLM/Qwen3.8-Flash-Next>
- <https://huggingface.co/Qwen/Qwen3.8-Flash-Next>
- <https://www.qwencloud.com/>
- <https://docs.qwencloud.com/developer-guides/getting-started/introduction>
- <https://help.aliyun.com/en/model-studio/models>
- <https://help.aliyun.com/en/model-studio/newly-released-models>
- <https://openrouter.ai/api/v1/models>

## Portfolio disposition

There are no **Evaluate now** items. The access and reproducibility prerequisite
fails before any repo can make a decision-grade exact-checkpoint comparison,
so the campaign maximum is **US$0.00** and no approval prompt is warranted.

### Not recommended now

- **Dossier — Defer.** Its maintained attributable extraction/value lane could
  test a low-cost exact Flash-Next route against its current value incumbent,
  but only after an exact managed slug or an owner-approved reproducible local
  deployment proves strict structured output, pricing, and latency. Start with
  one synthetic extraction contract probe; do not substitute Qwen3.8-Flash.
- **doc-web — Defer.** Flash-Next's new multimodal architecture is a credible
  trigger for the maintained `image-crop-extraction` ladder, especially because
  Qwen3.8 Max narrowly missed its entry gate. Reopen when exact image transport,
  strict integer bbox output, and bounded serving economics are available. Use
  only public checked-in fixtures until the route's data posture is known.
- **CineForge — Defer.** This is the strongest eventual value hypothesis:
  Flash-Next is explicitly optimized for lower inference cost, while Qwen3.8
  Max's exact-runtime `script-bible` answer was semantically strong but failed
  cost and latency gates by just over 2x. Reopen on an exact route with bounded
  pricing and strict `ScriptBible` output; run synthetic Open Frequency first
  and retain the existing `>=0.90`, `<=30s`, and `<= $0.01/call` gates.
- **Echo Forge — Defer.** Its structured `scene-to-soundscape-golden` lane can
  reopen for a cheap exact route, but the current two-case eligibility gate
  depends on strict schema and raw-output provenance that the release materials
  do not prove. Use public/synthetic owner-approved scenes first.
- **Storybook — Do not evaluate.** Its maintained photo/evidence lanes already
  have passing, very cheap incumbents and its production family-media boundary
  is stricter. An unqualified experimental checkpoint cannot change a current
  adoption decision; reopen only for a concrete failing golden plus an approved
  production privacy route.
- **Board Game Ingester — Defer.** The model could eventually challenge a
  broader public/licensed rulebook or asset-understanding golden, but current
  work remains package/downstream readiness and no failing model-owned lane is
  selected. Do not send private scans merely because weights are available.
- **Robo Rally — Do not evaluate.** Its maintained evals are deterministic game
  behavior and replay scenarios, not a model-selection surface; its canonical
  rules source is private.
- **Conductor — Route only.** Preserve the availability and retry triggers; the
  owning repos must run and judge any later benchmark.

## Retry trigger

Re-run Stage 1 when one of these becomes true:

1. an official managed catalog exposes an exact Flash-Next slug with price,
   context/output limits, multimodal request shape, structured-output/tool
   contract, and data policy;
2. OpenRouter exposes the exact checkpoint with at least one live endpoint and
   reproducible provider metadata; or
3. Cam approves a named owner-local serving target with a disclosed hardware,
   quantization, latency, and operating-cost boundary.

At that point, recommend only the smallest lanes whose absolute gates are
plausible from the resolved route. CineForge `script-bible`, doc-web
`image-crop-extraction`, Dossier extraction value, and Echo Forge
`scene-to-soundscape-golden` are the ordered candidates; re-inspect their live
owner state before numbering any campaign.

## 2026-08-27 follow-through — managed service available

QwenCloud now documents managed model code `qwen3.8-flash` as the production
service for the Flash-Next release. OpenRouter's public catalog independently
lists `qwen/qwen3.8-flash`, canonical snapshot
`qwen/qwen3.8-flash-20260826`, with one live Alibaba endpoint. This resolves
the launch-name mapping for this campaign: evaluate the managed production
service corresponding to Flash-Next, while recording that it has additional
production features beyond the raw `Qwen/Qwen3.8-Flash-Next` weights.

Current public contract evidence:

- text, image, and video input; text output
- 1,000,000-token context and 131,072-token maximum output
- thinking/reasoning controls, function calling, forced tool choice, and
  provider-enforced strict JSON Schema documented for the Qwen3.8-Flash series
- QwenCloud pricing of $0.15/M input, $0.47/M output, $0.016/M implicit-cache
  reads, $0.20/M explicit-cache creation, and $0.016/M explicit-cache reads
- OpenRouter pricing matching QwenCloud, with one Alibaba endpoint and
  `structured_outputs`, `response_format`, `tools`, and `tool_choice`
  advertised; endpoint ZDR remains unpublished

Official/public sources:

- <https://www.qwencloud.com/models/qwen3.8-flash>
- <https://docs.qwencloud.com/developer-guides/text-generation/structured-output>
- <https://docs.qwencloud.com/developer-guides/text-generation/function-calling>
- <https://openrouter.ai/api/v1/models>
- <https://openrouter.ai/api/v1/models/qwen/qwen3.8-flash/endpoints>

This proves **announced** and **API-listed**. Stage 1 used no owner credential,
so Cam-account **callability remains unverified**. Public metadata also does
not prove exact served identity, production-contract reliability, semantic
capability, or actual billed economics. Only public or synthetic fixtures are
authorized in the proposed campaign because the live Alibaba/OpenRouter route
does not publish ZDR status.

### Evaluate now

1. **CineForge — exact-runtime `script-bible` value screen.**
   - **Lane and decision:** begin with the synthetic Open Frequency runtime
     case under the repaired `script-bible` contract. Compare against the
     provisional `gemini-3.5-flash-lite` runtime and the maintained historical
     value reference `grok-4.1-fast-reasoning`.
   - **Why now:** Qwen3.8 Max previously produced a strong valid answer but
     missed CineForge's cost and latency gates by just over 2x. Flash-Next's
     managed service is explicitly the lower-cost, higher-throughput member of
     the family and is priced far below those failed economics.
   - **Progressive gate:** qualify exact requested/served identity, terminal
     completion, strict `ScriptBible` JSON Schema, reasoning/output behavior,
     usage, and PromptFoo parity. Run only Open Frequency first. Require
     overall `>=0.90`, latency `<=30,000 ms`, subject cost `<= $0.01`, and no
     hard assertion failure. Stop on any absolute gate; run the second corpus
     and fresh incumbent only if the first case passes.
   - **Fixtures/privacy:** synthetic Open Frequency first. Do not send a second
     corpus unless its owner eligibility is confirmed in the isolated owner
     context; no private material is authorized.
   - **Provider-spend ceiling:** **US$0.75**.

2. **doc-web — `image-crop-extraction` detector screen.**
   - **Lane and decision:** determine whether Qwen3.8 Flash can enter the crop
     detector ladder against maintained `gemini-3-flash-preview` evidence of
     `13/13`, overall `0.9703`.
   - **Why now:** Qwen3.8 Max narrowly missed this exact lane at `12/13` and
     `0.9411`; Flash-Next uses a materially new architecture, keeps native
     vision, advertises strict schema, and is much cheaper. That is a concrete
     new challenger hypothesis rather than an unchanged-family retry.
   - **Progressive gate:** prove lossless generated-image transport and strict
     integer bbox output, then PromptFoo parity and one representative case.
     Run the frozen 13-case detector only after those pass. Require `13/13`,
     overall `>=0.95`, zero schema/provider errors, and competitive latency.
     Only then run the maintained crop-validation/page-context follow-ons;
     skipped follow-ons remain not measured.
   - **Fixtures/privacy:** checked-in public detector fixtures only; no private
     books, unpublished documents, or signed assets.
   - **Provider-spend ceiling:** **US$0.75**.

3. **Dossier — C5 extraction value/default-candidate screen.**
   - **Lane and decision:** `compromise-C5-cost-optimization`, starting with an
     extraction contract probe and the three-fixture quick-smoke matrix against
     incumbent `gemini-3.1-flash-lite` and the current quality ceiling only if
     needed for the ranking claim.
   - **Why now:** C5 explicitly reopens for a materially cheaper model that can
     remain within the verified default-candidate quality window. Qwen's low
     token price, long context, and strict schema create a credible value
     challenge across Dossier's cross-domain extraction surface.
   - **Progressive gate:** qualify exact identity and the Instructor/Pydantic
     extraction contract on one synthetic case, then run the frozen quick
     smoke with cache off and concurrency one. Require entry within 5% of the
     verified quality leader, no fixture-floor or schema failures, latency
     `<=60s`, and cost `<= $0.50`. Advance to the T1 cross-domain matrix only
     after the screen passes.
   - **Fixtures/privacy:** owner-authored/owner-approved benchmark fixtures
     only (`the-mariner`, `kowalski-obituary`, and
     `thompson-oral-history`); treat any fixture whose classification is not
     confirmed in the isolated owner context as ineligible and fail closed.
   - **Provider-spend ceiling:** **US$1.00**.

**Campaign maximum: US$2.50.** Each owner stops independently at its first
absolute gate; unused budget is not authority to broaden a lane.

### Not recommended now

- **Echo Forge — Defer.** Its `scene-to-soundscape-golden` and conditional
  `soundscape-extractor-value` lanes remain relevant, but the current
  OpenRouter adapter and registry contract are part of a large uncommitted
  owner change. A fresh remote-base worktree would test stale substrate, while
  importing the active work would violate ownership/isolation. Reconsider after
  that owner change is landed or isolated for this campaign.
- **Storybook — Do not evaluate.** Its maintained photo/evidence lanes already
  pass at `1.0` with `gemini-2.5-flash-lite`, inside their latency and tiny-cost
  gates, and production family media has a stricter privacy boundary. There is
  no current failing golden or adoption decision for Qwen to change.
- **Board Game Ingester — Defer.** Its current top-level gap is downstream
  Builder/package readiness; seed routing, crop, inventory, relationship,
  matching, rules HTML, and export surfaces already pass. Reopen when a
  broader public/licensed model-owned corpus exposes a specific failure.
- **Robo Rally — Do not evaluate.** Its maintained evals are deterministic game
  behavior and replay scenarios rather than a model-selection surface, and its
  canonical rules source is private.
- **Conductor — Route only.** Conductor owns this proposal and campaign
  synthesis; the three selected owner repos must execute and judge their native
  lanes.

Cam selected evaluations 1 and 2. Evaluation 3 was excluded while Dossier is
under heavy construction; the resulting Stage 2 record follows.

## 2026-08-27 Stage 2 campaign result — evaluations 1 and 2

Cam approved CineForge and doc-web only, with Dossier explicitly excluded while
it remains under heavy construction. Each owner ran from the current remote
`main` base in an isolated worktree, used its maintained native contract, and
stopped independently at the first absolute gate. No default, deployment,
private fixture, commit, or push was authorized or performed.

### 1. CineForge — deferred at access gate

- **Owner context:** worktree
  `/Users/cam/.codex/worktrees/qwen38-flash-next-cineforge/cine-forge`, branch
  `codex/qwen38-flash-next-script-bible`, base
  `2530ca6c0910672a20594bd2c3908b4b7df43535`.
- **Resolved route:** OpenRouter `qwen/qwen3.8-flash`, sole Alibaba endpoint,
  canonical snapshot `qwen/qwen3.8-flash-20260826`.
- **Observed gate:** the native provider-enforced strict `ScriptBible` probe
  and its one allowed retry both returned pre-inference HTTP 429 with
  `limit_source=upstream_provider_shared_pool`. No response ID, served model,
  usage, cost, or semantic output existed.
- **Progressive stop:** harness parity, Open Frequency, deterministic scoring,
  Opus judging, second corpus, and fresh incumbent were not run.
- **Spend:** **US$0.00 / US$0.75**.
- **Verdict:** catalog access constrained; transport blocked before inference;
  reliability, semantic capability, latency, and subject economics not
  measured; adoption **defer**. This is provider-capacity evidence, not a model
  quality failure.
- **Owner evidence:**
  `docs/evals/attempts/031-script-bible-qwen38-flash.md` and
  `docs/evals/story-217-qwen38-flash-access-evidence.json` in the isolated
  owner worktree. Focused contract checks and the full unit suite passed
  (`2175 passed`).

### 2. doc-web — deferred at multimodal transport gate

- **Owner context:** worktree `/private/tmp/doc-web-qwen38-flash.zVx4Mk`,
  branch `codex/qwen38-flash-eval-20260827`, base
  `0864678de68246e3fe62fddd90c62585d16e17b3`.
- **Resolved route:** OpenRouter `qwen/qwen3.8-flash`, sole Alibaba endpoint,
  canonical snapshot `qwen/qwen3.8-flash-20260826`.
- **Observed gate:** after one pre-inference 429, a bounded strict-text retry
  qualified exact requested/served identity, Alibaba pinning, terminal stop,
  provider-enforced strict JSON Schema, usage, and cost in 3,043 ms. All three
  generated-image strict-bbox probes then returned the same pre-inference
  Alibaba shared-pool 429, including bounded backoff.
- **Progressive stop:** PromptFoo parity, the frozen 13-case detector, and crop
  safety follow-ons were not run because multimodal transport did not qualify.
- **Spend:** **US$0.0000678 / US$0.75**.
- **Verdict:** text strict-schema transport qualified; multimodal transport
  inconclusive and reliability-blocked; detector capability not measured;
  adoption **defer**. Repeated upstream failures are reliability evidence, not
  a semantic crop-quality score.
- **Owner evidence:**
  `docs/evals/attempts/031-qwen38-flash-evaluate-model.md` in the isolated owner
  worktree. Owner adapter checks passed `14/14`; the final focused suite passed
  `30/30`; registry and methodology checks were clean.

### Campaign closeout

- **Combined measured spend:** **US$0.0000678 / US$1.50**.
- **Credential custody:** CineForge reused its existing owner credential via
  its wrapper. doc-web received only `DOC_WEB_OPENROUTER_API_KEY` in an ignored
  mode-0600 worktree env file; Conductor removed the injected variable after
  the run and verified that no variable names remained in that file.
- **Adoption result:** no owner default changes. Retry only after materially new
  evidence that the exact Alibaba shared pool accepts the required modality and
  strict contract, or after a separately authorized access path becomes
  available. Do not rerun unchanged catalog probes or infer quality from the
  unrun semantic benchmarks.
