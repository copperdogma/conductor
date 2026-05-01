# Scout 028 — Evaluate Grok 4.3 API Eval Opportunities

**Source**: xAI API docs and current public benchmark/pricing snapshots,
checked 2026-05-01.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

xAI now documents Grok 4.3 as the recommended chat/API model under the model id
`grok-4.3`, and the API docs say access still depends on team/account
availability. Artificial Analysis currently reports Grok 4.3 at about
`$1.25 / 1M` input tokens and `$2.50 / 1M` output tokens, with text and image
input, text output, a 1M-token context window, high speed, and competitive
reasoning/intelligence scores.

That makes the old "Grok 4.3 is not available in API yet" rejection stale. It
does not make Grok 4.3 a default anywhere. The right move is bounded repo-local
evals where the project already has model-selection, provider, or benchmark
surfaces. The most urgent matches are Storybook and CineForge, but Dossier,
doc-web, Echo Forge, and Board Game Ingester also have narrower eval-trigger
shapes.

One important privacy boundary remains: xAI's API security FAQ says API inputs
and outputs are not trained on without explicit permission, but standard API
requests/responses are stored for 30 days unless the team has enterprise Zero
Data Retention. Any repo using sensitive private payloads needs that checked
before live evaluation on real data.

## Project Relevance

- **storybook**: `Spike`. Storybook has a live conversational model path,
  prompt/eval surfaces, cost tracking, and very sensitive user data. Grok 4.3
  should be evaluated only on synthetic/golden Luna transcripts first, compared
  against the current Claude-family chat baseline for tone, continuity, refusal
  behavior, latency, and cost. Provider privacy/ZDR evidence must be handled
  before real private life-story payloads are sent.
- **cine-forge**: `Spike`. Strong fit. CineForge already has model-slot,
  cost-quality, scene understanding, prompt compilation, and xAI media-provider
  surfaces. Grok 4.3 should be separated from the existing xAI image-generation
  inbox item and tested as a text/image reasoning model against the current
  scene/script/prompt-compilation lanes before any default changes.
- **dossier**: `Spike`. Strong benchmark fit. Dossier explicitly treats a
  new subject model as a retry trigger for extraction and compromise evals.
  Grok 4.3 should enter only through live model discovery, provider wiring, and
  the smallest current benchmark surface with cost/latency gates intact.
- **doc-web**: `Spike`. Moderate fit. The text+image capability and price make
  Grok 4.3 worth a bounded challenger run for VLM crop/OCR surfaces if xAI
  credentials and provider adapters are cheap to wire. It should be compared
  against the maintained Gemini/OpenAI winners, not added to default configs by
  availability alone.
- **echo-forge**: `Spike later`. The repo has an explicit "new model/provider"
  retry trigger for the scene-to-soundscape structured-output eval. A one-off
  Grok 4.3 live outline attempt is useful once xAI access can be wired, but it
  should stay in the mapper/eval lane and not revive default live audio
  generation.
- **boardgame-ingester**: `Defer/spike later`. The project has rulebook,
  inventory, VLM/image, and package eval surfaces, so Grok 4.3 may become a
  useful LLM/VLM subject once the current deterministic seed work needs a
  broader model challenger. It is not the next move while the repo is still
  closing seed package readiness and rulebook review gaps.
- **roborally**: `Reject for now`. Robo Rally's current AI pressure is the
  build process and behavior-proof loop, not an API model runtime. No inbox
  handoff is warranted until there is a concrete LLM-powered bot, rules-ingest,
  or game-eval story.
- **conductor**: `Adapt`. Conductor should keep this as scout memory and route
  repo-local inbox notes rather than creating a shared model-eval mandate.

## Repo Handoffs

- Added target-repo inbox notes for Storybook, CineForge, Dossier, doc-web,
  Echo Forge, and Board Game Ingester.
- No Robo Rally note: there is no current repo-local Grok/API eval surface.
- No shared alignment story yet: each repo's eval harness and privacy/provider
  posture differs enough that the first pass should stay repo-local.

## Recommended Actions

1. Start with Storybook and CineForge.
   - Storybook: synthetic/golden Luna transcript eval first; privacy/ZDR check
     before real user content; compare against current Claude-family chat lane.
   - CineForge: run a bounded scene/script/prompt-compilation challenger pass;
     keep separate from xAI image-generation support.
2. Then pick the narrowest model-trigger repo:
   - Dossier if the goal is extraction/model-quality pressure.
   - doc-web if the goal is text+image VLM crop/OCR pressure.
   - Echo Forge if the goal is cheap structured-output outline quality.
3. Do not promote defaults from public benchmark lore. Promotion requires the
   repo's maintained eval registry to show quality, latency, and cost wins.

## Evidence

- xAI's model docs list Grok 4.3 and recommend `grok-4.3` for API callers:
  https://docs.x.ai/developers/models
- xAI's text API docs state the Responses API is the preferred API path and
  require API key/model access to be enabled:
  https://docs.x.ai/developers/model-capabilities/text/generate-text
- xAI's security FAQ says standard API requests/responses are retained for 30
  days and ZDR is enterprise-only:
  https://docs.x.ai/developers/faq/security
- Artificial Analysis reports current Grok 4.3 price/performance and modality
  data:
  https://artificialanalysis.ai/models/grok-4-3

## Confidence

High that Grok 4.3 is now a real API evaluation trigger. Medium on exact
repo-level leverage until each project confirms credential access, provider
adapter shape, structured-output behavior, and privacy posture in its own
runner.

## Open Questions

- Does Cam's xAI team/account already have `grok-4.3` enabled, or only
  console-visible documentation?
- Does the available xAI API path support the structured-output and image-input
  shapes each repo needs without a custom adapter?
- Is enterprise ZDR available for the projects that would otherwise send
  private family, document, or creative payloads?
