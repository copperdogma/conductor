# Candidate ledger

This ledger deduplicates material candidates discovered by the watch. It does
not replace detailed Conductor scouts or owner-repository evidence.

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
