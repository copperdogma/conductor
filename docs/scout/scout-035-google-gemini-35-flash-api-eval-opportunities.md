# Scout 035 - Evaluate Gemini 3.5 Flash API Eval Opportunities

**Source**: Google Gemini API docs and Google I/O developer announcements,
checked 2026-05-19.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Google's May 19, 2026 API-side release introduces `gemini-3.5-flash` as a GA,
stable Gemini API model. The model is positioned for frontier agentic and coding
work, long-horizon tasks, sub-agent loops, multimodal input, structured output,
function calling, code execution, Search/Maps grounding, URL context, file
search, Batch, Flex, Priority, caching, and 1M input / 65k output windows.

The practical scout result is not "switch every Google lane." The release is a
real model-eval trigger for repos that already have model ladders, eval
registries, provider health checks, or current Google model slots. Promotion
should stay repo-local and evidence-gated: quality, latency, cost, privacy
posture, and prompt/API compatibility all need to clear the owning repo's
existing acceptance surface.

Two boundaries matter:

- `gemini-3.5-flash` is materially more expensive than `gemini-3-flash-preview`
  and `gemini-3.1-flash-lite`, so value-leader claims need fresh cost/latency
  evidence rather than benchmark lore.
- Gemini Omni is announced for the Gemini app, but it did not appear as a
  callable Gemini API model in the model docs checked for this scout. Treat Omni
  as not repo-actionable until a model ID and API docs exist.

## Project Relevance

- **dossier**: `Spike`. Strong fit. Dossier explicitly reruns extraction and
  value-tier evals when new frontier models arrive, and its latest Gemini
  value-leader rerun was blocked by Google credential health. Test
  `gemini-3.5-flash` through live model discovery, then the C5 stage
  extraction/adjudication matrix and, if affordable, the C1 single-shot Big Fish
  detector. Compare against `gemini-3.1-flash-lite`, `gpt-5.3-chat-latest`, and
  `chat-latest`; do not promote without registry evidence.
- **doc-web**: `Spike`. Strong fit. The new model has image/PDF input,
  structured outputs, and the media-resolution migration caveat that directly
  intersects doc-web OCR, crop, page-context, and consistency surfaces. Run a
  bounded challenger against maintained crop/page-context gates and the parked
  stronger-OCR blocker if credential and cost setup are cheap.
- **cine-forge**: `Spike`. Strong fit for text/multimodal reasoning and model
  slot evaluation, not as a render-video model. Evaluate on scene/script
  understanding, prompt compilation, role-modality reasoning, AI-previz QA, and
  model-slot cost/quality surfaces. Start with live model discovery and
  provider smoke, because CineForge already treats model catalogs as drift-prone
  runtime truth.
- **storybook**: `Spike cautiously`. Storybook has Luna persona/model evals and
  Google AI dependency experience, but user data is sensitive. Only run a
  synthetic/golden Luna challenger first. Do not send private Storybook payloads
  until paid-tier privacy/data-use posture and provider policy are recorded.
- **echo-forge**: `Spike later`. Good fit for structured selected-scene and
  module-room mapping toward SceneUpdates, Sources, event controls, and context
  slots. It is not an excuse to revive live provider audio generation; keep the
  eval in the mapper lane and compare against the provider-free baseline plus
  the existing OpenAI structured-output attempt.
- **boardgame-ingester**: `Defer/spike`. The release is relevant to the
  eval-first rulebook/image pipeline, especially source-role routing,
  rulebook-to-component inventory, and asset-to-inventory matching from
  contact-sheet/image/PDF inputs. It is not the next move if the repo is still
  closing deterministic seed package readiness, and paid model calls still need
  explicit approval in story scope.
- **roborally**: `Reject for now`. The current product truth is headless
  scenario behavior, replay, client boundaries, and deterministic bot seeds.
  Gemini 3.5 Flash may matter later for source-rule extraction or LLM bot
  policy experiments, but no maintained Google API eval surface is ready today.
- **conductor**: `Adapt`. Keep the scout memory and route repo-local inbox
  notes. Do not create a shared "new Google model" mandate.

## Repo Handoffs

- Added target-repo inbox notes for Dossier, Storybook, doc-web, CineForge,
  Board Game Ingester, and Echo Forge.
- No RoboRally note: there is no current repo-local Google API model eval
  surface.
- No shared alignment story yet: provider wiring, privacy posture, and eval
  ladders differ enough that first proof belongs inside each repo.

## Recommended Actions

1. Run first where the existing eval surface is already strongest:
   - Dossier: benchmark harness, value-tier extraction/adjudication, optional
     C1 single-shot detector.
   - doc-web: maintained crop/page-context gates and OCR blocker probe.
   - CineForge: `discover-models`, provider health, then text/multimodal
     reasoning model-slot evals.
2. Keep privacy-sensitive and product-taste work bounded:
   - Storybook: synthetic/golden Luna only until provider policy is refreshed.
   - Echo Forge: structured scene mapper only, not audio generation.
3. Defer broader Board Game Ingester use until the next eval story needs a
   model challenger for source routing, inventory, or asset matching.
4. Apply Google migration details during implementation:
   - prefer `thinking_level` over `thinking_budget`
   - remove manual sampling parameters unless a repo has measured reason to keep
     them
   - verify function-response IDs/names/counts if the repo uses tools
   - compare cost using the paid-tier prices, not free-tier availability

## Evidence

- Google's I/O developer highlight says Gemini 3.5 Flash launched on May 19,
  2026 and is aimed at fast frontier agentic workflows:
  https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
- The Gemini 3.5 Flash docs list model id `gemini-3.5-flash`, stable status,
  1M input tokens, 65k output tokens, multimodal input, structured output,
  function calling, code execution, file search, grounding, Batch, Flex,
  Priority, and the May 2026 update:
  https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash
- The "What's new" page says the model is GA/stable, recommends Interactions API
  for new agentic projects, documents `thinking_level`, and gives migration
  notes from Gemini 3 Flash Preview and Gemini 2.5:
  https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5
- The Interactions API supported-models table includes `gemini-3.5-flash` and
  the API docs say managed agents are available through Interactions:
  https://ai.google.dev/gemini-api/docs/interactions
- The pricing page lists paid standard pricing for `gemini-3.5-flash` at
  `$1.50 / 1M` input tokens and `$9.00 / 1M` output tokens, with paid-tier
  content not used to improve Google's products:
  https://ai.google.dev/gemini-api/docs/pricing
- Google's Gemini app announcement mentions Gemini Omni, but describes its
  rollout to Gemini app subscribers rather than providing an API model ID:
  https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/

## Confidence

High that `gemini-3.5-flash` is a real API eval trigger. Medium on exact
repo-level wins until each repo runs its own harness with current credentials,
pricing, prompt compatibility, and scorer behavior.

## Open Questions

- Which repos currently have working paid-tier Google API credentials after the
  earlier credential-health failures?
- Are `gemini-3.5-flash` tool/function response constraints compatible with each
  repo's current provider adapters without patching?
- Does the model win on value, not just quality, once output/thinking tokens and
  media-resolution defaults are counted?
