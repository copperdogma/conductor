# Scout 053 - Evaluate Grok 4.6 API Eval Opportunities

**Source**: Official xAI launch, model, release-note, and privacy documentation,
plus authenticated direct-API probes, checked 2026-08-12.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
canmore-town-council, boardgame-ingester, roborally, echo-forge

## Summary

Grok 4.6 is available now through the direct xAI API as `grok-4.6`. The current
xAI account returned HTTP 200 for the exact model lookup, a Responses request
completed with exactly `API_OK`, and a strict JSON Schema request completed with
`{"status":"API_OK","accessible":true}`. This is proven callable access, not
just catalog or launch-page availability.

xAI documents a 500,000-token context window, text and image input, text output,
no text output limit, Responses and Chat Completions support, function calling,
web/X search, code execution, and low/medium/high/xhigh reasoning. Short-context
pricing is unchanged from Grok 4.5 at $2/M input, $0.50/M cached input, and $6/M
output; prompts above 200,000 tokens are billed at $4/M, $1/M, and $12/M.

The release is a credible eval trigger because xAI specifically claims gains on
long-running agents, knowledge work, coding, and visual/interactive tasks over
Grok 4.5. It is not an adoption trigger. Grok 4.5 was already unsafe or
uncompetitive on important CineForge and doc-web lanes, and earlier Grok runs
were too slow for Dossier and Storybook. Grok 4.6 should be tested only where a
maintained repo-local gate can determine whether those exact failures improved.

The live response header was `x-zero-data-retention: false`. xAI's current
privacy documentation says standard API inputs and outputs are retained for 30
days unless team-level ZDR is active. Initial evals must therefore use
synthetic, public, or explicitly approved fixtures.

## Prioritized Project Relevance

1. **dossier**: `Spike first`. Dossier already has direct xAI transport,
   discovery, cost capture, structured-output benchmarks, and disciplined
   promotion gates. Run the smallest public/synthetic extraction screen first,
   including the medium screenplay case that timed out on Grok 4.3. Expand only
   if 4.6 clears schema reliability, catastrophic-run, latency, cost, and
   entity/relationship quality gates. This is the best test of xAI's claimed
   long-horizon knowledge-work improvement.
2. **cine-forge**: `Spike second`. CineForge has the cleanest direct Grok 4.5
   to 4.6 comparison. Start with the current maintained script-bible decision
   lane and its quality, 30-second latency, and $0.01/call gates. Expand to the
   remaining scene extraction, scene enrichment, QA, and six-anchor video lanes
   only if that first result is healthy or the owning agent needs the full 4.5
   comparison. The deciding question is whether 4.6 preserves 4.5's strong
   enrichment and script-bible scores while fixing the known-good QA false
   rejection, invented errors, weak visual reads, and latency/value misses. Do
   not change defaults from vendor benchmark claims.
3. **doc-web**: `Spike third, progressive gate`. Re-run the exact 13-case
   maintained crop detector that Grok 4.5 failed at 11/13 and 0.7667. Only if
   Grok 4.6 clears the existing detector prerequisite should the owning repo
   spend on the materially different 22-case page-context deletion gate. This
   tests the claimed visual improvement without pretending the 500k context
   window proves document fidelity.
4. **canmore-town-council**: `Defer behind an owning eval`. Public council data
   and knowledge-work claims make a future provenance-scored challenger
   plausible, but the repo already has an unrouted Kimi K3 retrieval-answer
   comparison note. Establish that maintained citation/attribution lane before
   adding a second frontier model candidate.
5. **storybook**: `Reject for this wave`. Grok 4.3 tied the Claude synthetic
   persona score while taking roughly eight times longer and exposing thinking,
   and Storybook's private-data posture makes the live non-ZDR account a poor
   fit. Grok 4.6 is a costly frontier model, not a credible fast chat-default
   challenger without a specific failing golden that cheaper incumbents cannot
   solve.
6. **echo-forge**: `Defer`. The relevant model surface is narrow structured
   scene mapping, not audio generation. There is no current evidence that a
   Grok 4.6 run would answer a decision that stronger first-wave repos cannot.
7. **boardgame-ingester**: `Defer`. The repo has visual and rules-ingest goldens,
   but current deterministic package-readiness work does not justify another
   paid frontier subject without a selected failing model-owned lane.
8. **roborally**: `Reject`. There is no current decision-bearing API-model lane.
9. **conductor**: `Adapt`. Record and route the decision; do not run target-repo
   benchmarks or create a portfolio-wide default mandate.

## Recommended Actions

1. Gate Dossier on a small public/synthetic extraction screen before any larger
   document matrix.
2. Ask CineForge to run its current maintained script-bible decision lane
   against `grok-4.6`, expanding only when the first result justifies it.
3. Gate doc-web on the 13-case detector before the 22-case page-context suite.
4. Keep all three runs direct-xAI, uncached where the owning harness requires
   freshness, with exact served-model, reasoning, latency, token, cost, schema,
   and ZDR evidence recorded.
5. Do not send private Storybook/family content or change any runtime default.

No target-repo handoff was written during this recommendation pass. The owning
repo agents should execute and interpret their benchmarks after Cam approves
the shortlist.

## Evidence

- xAI release notes document the August 12 API release and pricing tiers:
  https://docs.x.ai/developers/release-notes
- xAI's Grok 4.6 overview documents the exact model ID, API shapes, modalities,
  500k context, reasoning levels, tools, and partner availability:
  https://docs.x.ai/developers/grok-4-6
- xAI's launch post describes the intended 4.5-to-4.6 improvements and
  self-reported evaluation results:
  https://x.ai/news/grok-4-6
- xAI's API security FAQ documents default 30-day retention and the response
  header used to verify ZDR status:
  https://docs.x.ai/developers/faq/security
- Authenticated direct xAI evidence on 2026-08-12: exact-model lookup HTTP 200;
  model `grok-4.6`; context 500,000; Responses HTTP 200 with exact `API_OK`;
  strict-schema HTTP 200 with schema-valid access confirmation; both inference
  responses reported `x-zero-data-retention: false`.
- CineForge's Grok 4.5 decision and five-lane results:
  `/Users/cam/Documents/Projects/cine-forge/docs/stories/story-207-grok-45-model-slot-eval-refresh.md`
- doc-web's maintained Grok 4.5 detector failure and progressive stop:
  `/Users/cam/Documents/Projects/doc-web/docs/evals/attempts/019-grok45-evaluate-model-skill-pilot.md`
- Dossier's prior xAI extraction and latency evidence:
  `/Users/cam/Documents/Projects/dossier/docs/stories/story-143-grok-43-xai-benchmark-trigger.md`
- Storybook's prior persona, latency, and visible-thinking result:
  `/Users/cam/Documents/Projects/Storybook/storybook/docs/stories/story-129-grok-4-3-luna-persona-challenger-eval.md`

## Confidence

High that Grok 4.6 is directly callable and that CineForge, Dossier, and
doc-web are the only immediate decision-bearing fits. Medium on whether 4.6
fixes their prior Grok failure classes until the owning repos run current
maintained evals.

## Open Questions

- Does Grok 4.6 eliminate CineForge's known-good QA false rejection and visual
  hallucinations without losing its script-bible and enrichment quality?
- Does it complete Dossier's medium/long fixtures within the operational gate?
- Does the claimed visual improvement clear doc-web's source-backed crop gate?
- Should the xAI team enable ZDR before any later evaluation using sensitive
  project data?
