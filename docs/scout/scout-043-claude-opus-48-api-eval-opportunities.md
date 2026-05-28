# Scout 043 - Evaluate Claude Opus 4.8 API Eval Opportunities

**Source**: Anthropic release announcement, Claude API docs, and model overview
checked 2026-05-28.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Anthropic released Claude Opus 4.8 on 2026-05-28 as the current Opus model,
with API model id `claude-opus-4-8`. The official docs position it for complex
reasoning, long-horizon agentic coding, high-autonomy work, tool use, and
long-context tasks. The practical API facts that matter for repo evals are:
1M context on the Claude API, 128k max output, adaptive thinking, `high` effort
default, fast mode as a research preview, lower prompt-cache minimum, unchanged
regular Opus pricing versus Opus 4.7, and inherited Opus 4.7 constraints around
sampling parameters and thinking configuration.

This is a real eval trigger for repos that already have model ladders, frontier
detectors, long-context document or script tasks, persona/judgment surfaces,
or source-understanding gates. It is not a portfolio-wide model switch. Each
repo should prove quality, latency, cost, privacy posture, and API compatibility
inside its own eval harness before promoting a runtime default.

## Project Relevance

- **dossier**: `Spike`. Strong fit. Dossier explicitly reruns single-shot and
  runtime-stage evals when frontier models improve. Test Opus 4.8 through live
  model discovery, Anthropic credential health, and promptfoo compatibility,
  then run the C1 single-shot Big Fish detector and the C5 extraction,
  adjudication, and judge-stage value matrix as budget allows. Also consider a
  judge refresh because the repo still documents `claude-opus-4-6` as the
  cross-provider eval judge. Do not promote runtime defaults without registry
  evidence across quality, speed, and cost.
- **doc-web**: `Spike`. Strong fit. Opus 4.8 is a credible challenger for
  page-context extraction, crop/OCR judgment, and stronger-OCR blocked lines
  because the repo already uses promptfoo gates for multimodal document
  quality. Evaluate against maintained crop/page-context/OCR tasks and compare
  with the current OpenAI/Gemini winners. Watch Anthropic markdown-fenced JSON,
  sampling constraints, and cost on large page-image workloads.
- **cine-forge**: `Spike`. Strong fit for long-form script understanding,
  creative-direction quality, prompt compilation, character/continuity
  reasoning, and codebase-scale agentic work. It is not a render-video or image
  generation model. Start with live provider discovery/smoke, then one or two
  text or multimodal model-slot evals where the current tiered model strategy
  is still below a single-model bar.
- **storybook**: `Spike cautiously`. Strong fit for Luna persona quality,
  honesty, follow-up judgment, artifact-grounded conversation, and long
  continuity journeys. Because Storybook carries private family material, run
  synthetic/golden Luna and artifact fixtures first; do not send real private
  payloads until Anthropic paid-tier data-use and provider posture are recorded
  in the owning repo.
- **boardgame-ingester**: `Defer/spike`. Relevant for rulebook/manual
  understanding, component inventory extraction, VLM routing, and asset-to-
  inventory matching. Do not interrupt deterministic seed/package-readiness
  work. Add Opus 4.8 when the next eval story needs a frontier multimodal or
  long-context challenger, with paid calls explicitly in story scope.
- **roborally**: `Spike later`. More relevant than the recent Google/Kimi model
  notes because RoboRally's spec already has a source-rules detection path:
  rerun rules extraction/implementation when a model can take the raw private
  PDF and produce a complete rules model plus passing fixtures. Opus 4.8 is a
  plausible subject for a bounded source-derived rules spike, but only after
  the current headless scenario behavior lane has an owning story and private
  source handling is explicit.
- **echo-forge**: `Spike later`. Good fit for the structured selected-scene and
  module-room mapper lane: SceneUpdates over Sources, Source overrides, Source
  event controls, one-shot triggers, and scene/environment slots. It is not a
  reason to make provider-generated live-table audio a v0 default. Compare with
  the provider-free baseline and existing OpenAI structured-output attempt.
- **conductor**: `Adapt`. Keep this scout record and route repo-local inbox
  notes. Do not create a shared Opus 4.8 mandate.

## Repo Handoffs

- Added target-repo inbox notes for Dossier, Storybook, doc-web, CineForge,
  Board Game Ingester, RoboRally, and Echo Forge.
- No shared alignment story yet: the useful work is repo-local eval design and
  provider compatibility proof.

## Recommended Actions

1. Run first where existing eval surfaces are strongest: Dossier, doc-web, and
   CineForge.
2. Keep privacy-sensitive work bounded: Storybook synthetic/golden fixtures
   first, RoboRally private PDF only under an owning story, and Board Game
   Ingester paid calls only with explicit story scope.
3. Keep Echo Forge in the mapper lane and out of live audio generation.
4. During implementation, check current provider discovery/pricing and account
   limits instead of assuming release-page availability is enough.
5. Record prompt/API compatibility details in the target repo: `effort`,
   adaptive thinking, prompt caching, fast mode, sampling constraints, and JSON
   output handling.

## Evidence

- Anthropic release announcement:
  https://www.anthropic.com/news/claude-opus-4-8
- Claude API "What's new in Claude Opus 4.8":
  https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8
- Claude API model overview:
  https://platform.claude.com/docs/en/about-claude/models/overview

## Confidence

High that Opus 4.8 is a real eval trigger for these repos. Medium on actual
repo-level wins until each owning harness measures current credentials, pricing,
API compatibility, task quality, latency, and cost.

## Open Questions

- Which target repos currently have working Anthropic API credentials through
  their repo-local env wrappers?
- Does Opus 4.8's high-effort default alter latency/cost enough to fail any
  value-leader gates despite better quality?
- Should Dossier/doc-web/Storybook update their documented eval judge from
  `claude-opus-4-6` only after a dedicated judge-bias comparison?
