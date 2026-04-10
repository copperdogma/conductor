# Scout 020 — Evaluate Storybook Realtime Agent Platform Bundle

**Source**: announcement bundle + official docs
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The bundle is real and current, not just ambient vendor hype. `Twitter
Scraper` confirmed the referenced announcement trail spans 2026-02-12
(`Responses` WebSockets "landing in GA soon") and 2026-02-23 (OpenAI
Developers announcing WebSockets in the Responses API and Justin Uberti
announcing `gpt-realtime-1.5`). The current official docs are materially
stronger than those announcement fragments: OpenAI's Voice Agents guide now
documents browser `WebRTC` plus `WebSocket` transport, the Realtime
server-controls guide documents attaching a backend `WebSocket` to the same
session via `call_id`, and the current `gpt-realtime-mini` model page exposes a
cost-efficient realtime model over `WebRTC`, `WebSocket`, or `SIP`. LiveKit's
current OpenAI docs also show a real wrapper surface around the Responses API,
not just rumor.

That means Storybook's older February 2026 voice-evaluation context is stale as
written. ADR-005 still frames OpenAI Realtime as effectively eliminated, while
the live Storybook runtime has already moved somewhere else entirely: a thinner
pipeline around Deepgram streaming input, shared backend conversation
orchestration from Story 075, and ElevenLabs TTS via `/api/voice/tts`. I did
not find a current OpenAI Realtime, `WebRTC`, or LiveKit runtime path in the
shipped Storybook code.

The core blocker also did not disappear. The current official
`gpt-realtime-mini` page still lists a `32,000` token context window, which is
the same continuity pressure ADR-005 worried about for long storytelling. More
importantly, I did not find a live Storybook story, inbox item, or current bug
showing that today's voice latency, interruption handling, or transport shape
is painful enough to justify reopening the whole substrate now. This is worth
preserving as a dated future decision note for Storybook, not as an active
Conductor work line.

## Project Relevance

- **dossier**: Low direct relevance. This is a product/runtime decision for
  Storybook rather than a reusable Dossier or Conductor methodology seam.
- **storybook**: Highest relevance. Storybook is the only tracked repo with a
  real voice product surface and an older ADR that now overstates the case
  against revisiting realtime options.
- **doc-web**: Low relevance. `doc-web`'s active seams are document intake,
  OCR, and evidence handling, not live conversational transport.
- **cine-forge**: Low current relevance. This may matter later if CineForge
  grows live voice or realtime collaboration surfaces, but that is not the
  current frontier.

## Recommendation

- Defer at the Conductor level and hand the note off to Storybook's inbox.
- Do **not** create a Conductor story or a Storybook implementation story from
  this scout alone.
- Treat the source bundle's main value as a decision correction:
  - OpenAI Realtime is more mature and better documented than ADR-005 assumed.
  - Storybook's actual shipped runtime is no longer on the older S2S-vendor
    path that ADR-005 and Story 024 emphasized.
  - The continuity objection is still live enough that "switch now" would be
    premature.
- If Storybook reopens the voice substrate later, the first honest step is a
  narrow ADR refresh against current product pain:
  1. confirm a real measured pressure such as reply latency, interruption
     quality, or browser transport complexity
  2. compare today's pipeline against one current realtime candidate
  3. decide whether the gain is really transport-level or just better
     turn-taking / voice-output handling
- Treat LiveKit as an optional orchestration wrapper if Storybook ever wants a
  managed voice-agent session layer. Do not treat it as a prerequisite for
  revisiting the decision.

## Confidence

- Medium-high. The external bundle is now verified against primary vendor docs
  and the Storybook fit judgment is grounded in the current Storybook docs and
  runtime, but I did not run a live latency benchmark or prototype a realtime
  branch.

## Evidence

- `https://x.com/openaidevs/status/2026025368650690932?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://x.com/juberti/status/2026038008240337101?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://x.com/stevendcoffey/status/2022011371362431060?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://platform.openai.com/docs/guides/voice-agents`
- `https://platform.openai.com/docs/guides/realtime-server-controls`
- `https://developers.openai.com/api/docs/models/gpt-realtime-mini`
- `https://docs.livekit.io/agents/models/llm/openai/`
- Storybook local evidence:
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/decisions/adr-005-speech-voice/adr.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/stories/story-075-conversation-runtime-architecture-streamlining.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/routes/voice.ts`
  - `/Users/cam/Documents/Projects/Storybook/storybook/packages/frontend/src/hooks/useVoiceCapture.ts`
- Inbox notes already hinting at future voice-provider pressure:
  - `try Gemini 3.1 Flash Live for Luna?`
  - `MAYBE try Mistral TTS for Luna?`

## Open Questions

- Does current Storybook use actually show recurring voice pain severe enough to
  justify reopening ADR-005, or is the real remaining work still within the
  existing pipeline?
- If Storybook does revisit this later, is the first comparison really
  OpenAI Realtime vs pipeline, or should it first measure whether interruption
  quality and turn-taking can be fixed without a substrate switch?
- Should Storybook correct ADR-005's wording now, or wait until a fresh
  voice-architecture story is actually active?
