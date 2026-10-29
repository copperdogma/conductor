# Candidate ledger

This ledger deduplicates material candidates discovered by the watch. It does
not replace detailed Conductor scouts or owner-repository evidence.

## Gemini 4 Argon public release — 2026-10-13

Google's [official model entry](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)
lists stable `gemini-4-argon`; the September30–October11 trusted-tester discovery
hold is historical. All six selected owner evaluations now have exact
native inference evidence. [Scout092 decisions](../scout/scout-092-gemini4-argon-evaluation-routing.md#owner-decisions--2026-10-13)
originally prioritized Doc Web literal-reader qualification; its completed
follow-up below retains Astra.
Selected [thinking-level calibration](../scout/scout-092-argon-thinking-levels.md)
is complete: BGI high exposes a costly coverage gain; Doc Web low saves 10.96%
with poor observed latency, while high crops still fail source completeness.
No defaults change. Combined known USD 2.403345745 plus unknown USD 1.474024 =
conservative USD 3.877369745 / 35. Public/synthetic only; temporary BGI key removed.
Use [the evaluated ledger](evaluated-models.md#gemini-4-argon--scout092-2026-10-13)
for exact attempt deduplication and narrow follow-up triggers; this is no longer
an unevaluated discovery lead.

The approved [Doc Web qualification plan preparation](../scout/scout-092-docweb-literal-qualification-plan.md)
is complete. Subsequent USD 3 bounded [execution](../scout/scout-092-docweb-literal-qualification.md)
is complete: Argon missed the mandatory ambiguity hold after one exact matched
page. Retain Astra. Added known USD.468719, unknown0; cumulative conservative
exposure USD4.346088745/35. Remaining sources/repeats/live exports unmeasured.

| Provider / model | First seen | Release/access state | Evidence | Likely fit | Disposition |
| --- | --- | --- | --- | --- | --- |
| Google `gemini-3.7-flash` | 2026-08-13 | Official GA, documented API ID; direct and aggregator access were already verified in Scout 054 | [Google model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash), [Scout 054](../scout/scout-054-gemini-37-flash-deepseek-v4-pro-api-eval-routing.md) | doc-web, CineForge, Dossier maintained lanes | Existing candidate; no new recommendation today |
| DeepSeek `deepseek-v4-pro` / `-0813` | 2026-08-13 | Official GA alias update; on 2026-08-28 the current official pricing/model table documents Responses API support, though older endpoint guides still say unsupported | [DeepSeek pricing/model table](https://api-docs.deepseek.com/quick_start/pricing/), [DeepSeek GA release](https://api-docs.deepseek.com/news/news260813/), [Scout 054](../scout/scout-054-gemini-37-flash-deepseek-v4-pro-api-eval-routing.md), [evaluated-model ledger](evaluated-models.md) | CineForge and Echo Forge already attempted the exact alias; Dossier remained unrun | Already evaluated; no new recommendation. CineForge stopped on latency/value and Echo Forge was an operational reject with decision-grade capability unmeasured. Conflicting native Responses documentation is monitoring evidence only and does not satisfy the recorded strict-contract/privacy/latency/cost retry trigger |
| Z.ai `glm-5.3` | 2026-08-20 | Official model ID documented; account/API callability was not established | [Z.ai model guide](https://docs.z.ai/guides/llm/glm-5.3), [Scout 056](../scout/scout-056-glm-53-cineforge-script-bible-handoff.md) | CineForge `script_bible_v1` | Deferred: no configured native access and strict contract unproven |
| Qwen `qwen3.7-{max,plus,flash}` | 2026-08-26 | OpenRouter catalog routes exist; compact first-party pass did not establish a current launch/API contract | [OpenRouter catalog](https://openrouter.ai/api/v1/models), [Qwen Code providers](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/model-providers/) | Plausible multimodal/document/coding follow-on | Non-qualifying catalog-only lead; monitor official Model Studio release notes |
| Qwen `qwen3.8-flash` (Qwen3.8-Flash-Next production service) | 2026-08-27 | Officially announced 2026-08-26; QwenCloud documents exact API ID and OpenRouter lists an Alibaba endpoint `qwen/qwen3.8-flash` / `qwen3.8-flash-20260826` | [Qwen announcement](https://qwen.ai/blog?id=qwen3.8-flash-next), [QwenCloud model page](https://www.qwencloud.com/models/qwen3.8-flash), [OpenRouter endpoint metadata](https://openrouter.ai/api/v1/models/qwen/qwen3.8-flash/endpoints) | CineForge script-bible and doc-web multimodal/document lanes, subject to their existing gates | New qualifying lead: available now; evaluate, do not adopt yet. First candidate is CineForge; strict JSON Schema enforcement, Cam-account callability, privacy, served identity, and capability on owner fixtures remain unverified |
| Inception `mercury-2.5-preview` | 2026-09-02 | First-party model page plus exact OpenRouter model and Inception endpoint (`inception/mercury-2.5-preview-20260831`) | [Inception models](https://www.inceptionlabs.ai/models), [OpenRouter endpoint metadata](https://openrouter.ai/api/v1/models/inception/mercury-2.5-preview/endpoints), [Scout 066](../scout/scout-066-mercury-25-preview-evaluation-routing.md) | Echo Forge public/synthetic `scene-to-soundscape-golden` strict latency/value screen | **Evaluated; do not adopt.** Exact Inception-only strict transport passed and Tavern cleared latency/cost, but the low-reasoning arm failed seven maintained semantic requirements. Do not repeat unchanged; use the evaluated-model ledger retry boundary |

## Evidence discipline

The first-seen date is the date this ledger recorded the candidate, not
necessarily the provider release date. Any unlisted property—including strict
JSON Schema, forced tools, served identity, retention/training terms,
reliability, capability, economics, and adoption—is unknown unless linked
evidence says otherwise. No candidate has been adopted by this watch.


## 2026-09-07 additions and corrections

- **Google `gemini-3.8-flash` / `google/gemini-3.8-flash-20260902`:** first recorded
  here September 7; [official September 2 GA](https://ai.google.dev/gemini-api/docs/changelog)
  and [exact router endpoints](https://openrouter.ai/api/v1/models/google/gemini-3.8-flash/endpoints).
  Initially misclassified as unevaluated because the central ledger lacked the
  September 3 owner campaign. The reconciled ledger records the exact prior
  attempts; suppress unchanged evaluation framing. No new inference or adoption.
  [Full release and correction record](daily/2026-09-07.md).
- **Qwen3.8 Flash:** the August 27 recommendation above is superseded by the
  evaluated ledger's August 27 capacity stops. No new recovery evidence today.
- **Qwen3.8 Max 0902:** [Scout 068](../scout/scout-068-qwen38-max-0902-reevaluation.md)
  now records completed September 6 owner evaluation and failed grouping gate;
  suppress unchanged low-reasoning repeats.
- **Claude Sonnet 5:** already evaluated in
  [Doc Web Attempt 014](/Users/cam/Documents/Projects/doc-web/docs/evals/attempts/014-sonnet5-bounded-challenger.md)
  on June 30. Missing from the central ledger, but not a new lead; September 3
  automation-memory recommendation is corrected. Ledger maintenance remains
  with the evaluation campaign workflow.

- **IFM `IFM/K2-Horizon-375B-A23B`:** first recorded September 7, released
  [September 3](https://ifm.ai/blog/k2/). No prior exact attempt found.
  [Weights/model card](https://huggingface.co/IFM/K2-Horizon-375B-A23B) verified;
  no managed route verified and no OpenRouter catalog match. Defer CineForge
  long-context structured work until exact managed access, price and privacy
  are inspectable. Do not repeat an unchanged unavailable candidate.
- **GLM-5.3-Flash / Ox Alpha:** [Ollama's provider page](https://ollama.com/library/glm-5.3-flash)
  identifies the prior Ox Alpha preview. September 7 AutoClaw visibility is not
  a new checkpoint; no strict-contract retry proof. Suppress new-evaluation
  framing and retain Scout 059's retry boundary. Exact historical served
  response identity remains limited by the former opaque route.

## 2026-10-06 — Mistral Large 4 evaluated

**October6 owner follow-through:** Cam selected all five [Scout084 evaluations](../scout/scout-084-mistral-large4-evaluation-routing.md#owner-results--2026-10-06). Exact OpenRouter access and measured contracts qualified; retain existing models after source-faithfulness failures. Detector numerical/economic pass is qualified by logo clipping. KnownUSD0.72167835 plus unknown timeout reservations0.02448150, conservative0.74615985/USD22; no default changes; evaluation evidence landed on all five owner remote main branches. Candidate now has an evaluated-ledger entry: suppress unchanged nominations and honor task-specific retry boundaries.

### Closeout accounting correction — 2026-10-13

Pre-push review found that three original Astra071 reader receipts report 5,013
cache-write tokens each. Pricing those writes at the frozen standard USD12.5/M,
rather than the guard's USD10/M, adds USD.0125325 per call: **USD.0375975** total.
The original .198730 Astra reader total is cold-normalized; corrected actual
usage-priced total is .236327500. The 88.47% reader saving remains the original
cold comparison. Closed ledgers, manifests and archives remain unchanged.

Current cumulative known **USD2.909662245** + unknown **USD1.474024000** =
**USD4.383686245/35**. Doc Web known .931161750 + unknown .441832000 =
**USD1.372993750/15**. No new inference or verdict change.
[Landing and correction receipt](../scout/evidence/scout092-landing.json).


## 2026-10-12 — decision watch category

Decision models and typed judgment APIs are explicitly in scope, including JEV, OpenAI Decisions, Microsoft Decision, Perplexity Decider and Alibaba/Qwen decision services. Small size, derived weights and non-generative outputs do not exclude them when a maintained owner decision could change. Check the evaluated ledger and available owner evidence before nominating any exact model or endpoint; previously attempted models remain subject to their narrow retry triggers. This scope addition makes no new release, access, evaluation or adoption claim. See the [decision-source daily core](search-playbook.md#2026-10-12--explicit-decision-model-daily-core).


## 2026-10-29 — Liquid LFM3 deferred by Cam

[Scout104](../scout/scout-104-liquid-lfm3-evaluation-routing.md) closes the
access review without evaluation, downloads or provider calls. Cam does not
want local execution and lacks disk space for it. Reconsider these open-family
candidates only after meaningful relevant ranking gains and a usable hosted
route; advertised hosting alone is not proven account callability. No automatic
paid retry, local setup or new monitor is authorized. The original numbered
local proposal is withdrawn. Hosted d1.1 remains a distinct checkpoint/route,
not established equivalent to open d1-2B. Future local-model proposals should
omit prices; earlier comparison/judge ceilings were not local inference fees.
