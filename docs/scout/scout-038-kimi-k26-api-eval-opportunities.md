# Scout 038 - Evaluate Kimi K2.6 API Eval Opportunities

**Source**: Moonshot/Kimi docs, Kimi K2.6 technical blog, Hugging Face model
card, Kimi Vendor Verifier notes, Fireworks/Together provider pages, and
OpenRouter endpoint metadata checked 2026-05-20.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Kimi K2.6 is Moonshot AI's April 2026 open-weight, native multimodal agentic
model. The official docs position `kimi-k2.6` as the current most capable Kimi
API model, with text/image/video input, thinking and non-thinking modes, tool
use, JSON/structured output, automatic context caching, and a 256K context
window. The Hugging Face model card lists a 1T-parameter MoE architecture with
32B activated parameters and a MoonViT vision encoder.

The model is credible enough to evaluate. It is not credible enough to promote
by benchmark claims alone. Moonshot explicitly recommends reproducing official
benchmarks through the official API and using Kimi Vendor Verifier for
third-party providers, because third-party deployments can lose quality through
decoding, quantization, KV-cache, tool-call, or vision preprocessing
differences.

Provider recommendation: use direct Moonshot API as the baseline provider for
the first eval. It is the canonical quality target, supports the full model
surface, and is priced at `$0.95 / 1M` input, `$0.16 / 1M` cached input, and
`$4.00 / 1M` output on the Kimi API platform. Use Fireworks as the first
alternate provider if throughput or dedicated/on-demand deployment matters; its
published K2.6 serverless pricing matches Moonshot's token prices and it offers
on-demand deployments. Use OpenRouter only for quick smoke/routing experiments
or explicitly pinned-provider comparisons, not as the acceptance baseline.
Together is available but currently more expensive on published serverless
pricing (`$1.20 / 1M` input, `$0.20 / 1M` cached input, `$4.50 / 1M` output)
with no clear advantage for the first eval.

## Provider Notes

- **Moonshot direct API**: `https://api.moonshot.ai/v1`, model `kimi-k2.6`.
  Best first eval path. It is the official API, OpenAI-compatible, supports the
  documented K2.6 thinking and multimodal behavior, and Kimi's data-security FAQ
  says API input/output is not used to train or improve Kimi models.
- **Fireworks**: good second provider. Its model page lists Kimi K2.6 as ready,
  available through serverless API, fine-tuning, and on-demand dedicated GPU
  deployments; published standard serverless pricing is `$0.95 / $0.16 /
  $4.00` per 1M input/cached input/output tokens.
- **OpenRouter**: useful for provider discovery and smoke tests. Current
  endpoint metadata showed many providers, including cheaper and quantized
  routes, but also varied statuses, quantization tags, max completion limits,
  and no implicit caching flag. Treat it as a router, not the model-quality
  source of truth.
- **Together**: available and easy if existing Together credits matter, but its
  current published pricing is higher than Moonshot/Fireworks for the same
  model.

## Eval Cautions

- Do not manually set sampling params unless the adapter knows Kimi's K2.6
  constraints. Official docs say thinking mode uses fixed temperature/top-p
  behavior and incompatible values error.
- Tool use needs adapter attention. With thinking enabled, `tool_choice` must
  stay `auto` or `none`, and multi-step tool calls need the assistant
  `reasoning_content` preserved in context.
- Kimi's official `$web_search` tool is temporarily incompatible with K2.6
  thinking mode. Disable thinking or avoid built-in web search in evals.
- Video input is a direct-official-API feature first. The Hugging Face model
  card warns that third-party vLLM/SGLang deployments do not yet support video
  chat.
- Third-party routes should be checked with Kimi Vendor Verifier or equivalent
  local golden prompts before any quality conclusion is attributed to the model.

## Project Relevance

- **doc-web**: `Spike`. Strong fit. K2.6's vision, long context, structured
  output, and official token-estimation path make it worth a bounded challenger
  run against maintained crop/page-context/OCR gates. Use Moonshot direct first,
  synthetic or non-sensitive fixtures only, and compare against the maintained
  OpenAI/Gemini winners on quality, latency, and cost.
- **cine-forge**: `Spike`. Strong fit for scene/script understanding, prompt
  compilation, coding-driven UI/design, and long-horizon agentic coding. Do not
  treat it as a render model. Start with provider smoke plus one text/image
  reasoning or prompt-compiler eval.
- **dossier**: `Spike cautiously`. Strong candidate for extraction and
  adjudication model ladders, but private document payloads raise privacy and
  retention questions. First run should use synthetic/golden fixtures and direct
  Moonshot only.
- **storybook**: `Spike cautiously`. Possible challenger for Luna/persona and
  long-context continuity work, but only on synthetic/golden transcripts until
  provider privacy posture is accepted for real family material.
- **boardgame-ingester**: `Defer/spike`. Relevant later for rulebook/PDF/image
  reasoning and component inventory extraction, but not worth pulling ahead of
  deterministic seed and scenario readiness work unless a current story needs a
  new model challenger.
- **echo-forge**: `Defer/spike`. Useful later for structured scene mapping and
  source-control reasoning, not for audio generation. Current asset-catalog and
  local UI work does not need a new provider-first lane.
- **roborally**: `Reject for now`. The current product truth is deterministic
  headless behavior and scenario proof, not an LLM runtime.
- **conductor**: `Adapt`. Keep this scout memory and recommend repo-local evals;
  do not create a shared model-switch mandate.

## Recommended Actions

1. Treat Kimi K2.6 as a real eval trigger, not a default-model trigger.
2. Start with one direct-Moonshot eval in the repo whose maintained harness gives
   the fastest useful signal:
   - doc-web if the goal is VLM/document quality.
   - cine-forge if the goal is coding/design/prompt compilation.
   - dossier if the goal is extraction/adjudication quality.
3. If Moonshot-direct passes a local golden, run the same prompts through
   Fireworks and one pinned OpenRouter route to separate model quality from
   provider quality.
4. Do not send private user/family/project payloads until the owning repo records
   provider privacy posture and the eval fixture scope.

## Evidence

- Kimi K2.6 technical blog and benchmark table:
  https://www.kimi.com/blog/kimi-k2-6
- Kimi K2.6 API quickstart and parameter constraints:
  https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart
- Kimi API model/pricing overview:
  https://platform.moonshot.ai/
- Kimi chat-completion API reference:
  https://platform.kimi.ai/docs/api/chat
- Kimi API data-security FAQ:
  https://www.kimi.com/help/kimi-api/api-data-security
- Kimi Vendor Verifier:
  https://www.kimi.com/blog/kimi-vendor-verifier
- Hugging Face model card:
  https://huggingface.co/moonshotai/Kimi-K2.6
- Fireworks Kimi K2.6 model page and pricing:
  https://fireworks.ai/models/fireworks/kimi-k2p6
  https://docs.fireworks.ai/serverless/pricing
- Together Kimi K2.6 model page and pricing:
  https://www.together.ai/models/kimi-k26
  https://www.together.ai/pricing
- OpenRouter Kimi K2.6 endpoint/provider metadata:
  https://openrouter.ai/moonshotai/kimi-k2.6
  https://openrouter.ai/api/v1/models/moonshotai/kimi-k2.6/endpoints

## Confidence

High that Kimi K2.6 is a real eval candidate for coding, vision, structured
output, and long-context agentic tasks. Medium on provider choice after
Moonshot-direct, because third-party K2.6 deployments differ materially and need
local quality checks rather than public reputation.

## Open Questions

- Does Cam already have a Moonshot API key or should the first smoke use an
  existing OpenRouter account with the Moonshot provider pinned?
- Which repo has the cheapest currently maintained eval surface for a first
  direct-Moonshot challenger run?
- Do any target repos require zero-retention or enterprise handling before real
  non-synthetic payloads are sent?
