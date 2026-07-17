# Scout 047 - Evaluate Kimi K3 API Eval Opportunities

**Source**: Kimi API model list, Kimi K3 quickstart, Kimi API pricing and
data-security docs, plus OpenRouter model/provider pages checked 2026-07-16.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, canmore-town-council, storybook,
echo-forge, doc-web, alain-lessard-book

## Summary

Kimi K3 is a real callable Moonshot API release, not an app-only announcement.
The direct API exposes model id `kimi-k3` at `https://api.moonshot.ai/v1`.
Moonshot describes it as a 2.8T-parameter multimodal model with a 1M-token
context window for software engineering, knowledge work, and deep reasoning.
The documented API surface includes native image/video input, strict JSON
Schema output, required custom tool calls, dynamic tool loading, automatic
context caching, and up to 1M completion tokens.

This is a launch-day eval trigger, not an adoption decision. K3 costs
`$3.00 / 1M` uncached input, `$0.30 / 1M` cached input, and `$15.00 / 1M`
output. It is always in thinking mode, currently accepts only `max` reasoning
effort, and fixes sampling parameters. Those constraints make transport
compatibility, reasoning-token consumption, latency, and schema completion as
important as answer quality in local evals.

Provider recommendation: use Moonshot direct for the first eval. Working
repo-local Moonshot credentials were confirmed to list `kimi-k3` on launch day.
OpenRouter did not yet expose a dedicated K3 model; its Moonshot provider page
still listed K2-family models, and its `moonshot/kimi-k3` page reported the
model unavailable. Do not use the floating `kimi-latest` route as K3 evidence.

## API And Eval Cautions

- K3 always thinks. Use top-level `reasoning_effort="max"`; do not reuse the
  K2.x `thinking` parameter or assume a non-thinking cost/latency path exists.
- Preserve the complete assistant message, including reasoning content, across
  multi-turn and tool-call loops.
- Strict structured output is documented with `json_schema` and
  `strict: true`, but each repo must still prove its own Instructor, Promptfoo,
  or raw OpenAI-compatible adapter path.
- K3 fixes temperature, top-p, penalties, and `n`; omit those parameters rather
  than sending repo defaults that the API may reject.
- Public image URLs are not accepted. Vision evals must use base64 or uploaded
  `ms://` file ids.
- Moonshot says its official web-search tool is being updated and is not
  recommended for production use in the near term. Do not include web search
  in the acceptance lane.
- Kimi's API security documentation says API inputs and outputs are not used to
  train or improve its models. Privacy-sensitive repos should still begin with
  synthetic or approved golden fixtures and record the provider posture before
  sending real family or civic material.

## Project Relevance

- **dossier**: `Spike first`. This is the strongest maintained eval seam. Add
  K3 to live discovery and pricing, prove raw and strict-schema compatibility,
  then run the existing C5 extraction/adjudication/judge quick-smoke against
  current defaults and the recorded K2.6 result. The baseline to beat is the
  current per-stage winner on quality, schema completion, latency, and cost.
  K3 is especially relevant because K2.6 previously failed a structured judge
  path after reasoning consumed the completion budget; K3's strict schema may
  fix that transport failure, while always-on max reasoning may make it worse.
- **canmore-town-council**: `Spike second`. Use a small, provenance-scored
  cross-meeting/cross-document question set over already-public council
  material. Compare with the current retrieval-plus-answer path on citation
  correctness, document/page/video attribution, unsupported claims, latency,
  and cost. The 1M window is only a win if it preserves provenance rather than
  replacing retrieval with a persuasive context dump.
- **storybook**: `Defer to a narrow ceiling check`. Do not evaluate K3 as the
  chat default. If Dossier's K3 transport passes, run only the existing
  synthetic/golden Story 016 or identity/promotion-safety fixtures through the
  Dossier-owned extraction lane. The baseline is the current Dossier runtime
  default plus Storybook trust gates; real family payloads stay out of the
  launch-day eval.
- **echo-forge**: `Defer/spike`. K3 is relevant only to the maintained
  scene-to-structured-outline or registry-repair eval, not audio generation.
  Compare against the provider-free baseline and current structured-output
  winner when that lane is next refreshed. Do not interrupt current asset and
  sound-library work for a provider-first benchmark.
- **doc-web**: `Defer`. K3 vision and long context are technically relevant,
  but the current bottleneck is provenance-aware OCR/document workflow quality,
  not raw context size. Revisit only if Dossier establishes clean K3 transport
  and a hard page-context fixture remains unsolved.
- **alain-lessard-book**: `Reject for now`. The maintained doc-web generation
  and companion-document workflow matters more than adding another hosted
  model. K3 does not justify bypassing that pipeline.
- **conductor**: `Adapt`. Preserve the access and routing decision here; do not
  create a shared model mandate or benchmark K3 inside the supervisor repo.

## Repo Handoffs

- Route an immediate eval note to Dossier.
- Route a bounded public-corpus eval note to Canmore Town Council.
- Keep Storybook and Echo Forge as explicit follow-ons gated on the Dossier
  transport result; do not open broad default-model work.
- No handoff for doc-web or Alain Lessard Book.

## Recommended Actions

1. Hand the first evaluation to Dossier's owning agent: discovery, pricing,
   strict JSON/raw transport probes, then the smallest C5 comparison that can
   produce an adopt/do-not-adopt result. Conductor does not run that eval.
2. If Dossier reports clean transport, hand Canmore's small provenance-scored
   public-corpus slice to Canmore's owning agent. Do not test a giant context
   dump without a retrieval baseline.
3. Only after Dossier produces a credible result, decide whether Storybook's
   synthetic trust fixtures or Echo Forge's extractor lane would add new
   information.
4. Keep K3 off runtime defaults until local evidence beats current winners on
   quality and survives cost, latency, privacy, and provenance gates.

## Evidence

- Kimi K3 API quickstart and constraints:
  https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
- Kimi API model list:
  https://platform.kimi.ai/docs/models
- Kimi API platform pricing summary:
  https://platform.kimi.ai/
- Kimi API data processing and security:
  https://www.kimi.com/help/kimi-api/api-data-security
- OpenRouter Moonshot provider page:
  https://openrouter.ai/provider/moonshotai
- OpenRouter unavailable K3 page checked on launch day:
  https://openrouter.ai/moonshot/kimi-k3

## Confidence

High that K3 is callable through Moonshot direct and materially different
enough to trigger a Dossier transport/value eval. Medium that its 1M context
will help Canmore once provenance and retrieval baselines are enforced. Low
that it should be considered for Storybook chat, Echo Forge audio, doc-web's
current OCR workflow, or any production default before local benchmarks.

## Open Questions

- Does K3 complete Dossier's strict judge schema before max reasoning consumes
  the output budget?
- Does automatic caching make repeated long-context Canmore questions
  economical enough to compete with retrieval?
- When OpenRouter adds a dedicated K3 slug, does any pinned route preserve the
  direct API's structured-output and 1M-context behavior closely enough to be a
  useful secondary transport?
