# Scout 115 — Scribe v3 diarization evaluation routing

2026-11-16 (America/Edmonton). Stage 1 complete; selection pending. No
authenticated discovery, inference, credential inspection, target edits,
worktrees, account changes, commits or pushes. USD0. Existing dirty work preserved.

## Verified provider surface

Source supplied by Cam: https://x.com/elevenlabs/status/2120217467100541396
Twitter Scraper search for ElevenLabs Scribe3 returned no posts; direct X fetch
returned403. Used first-party release, API reference and model documentation.

- [Release](https://elevenlabs.io/blog/scribe-v3): announced November9;
  provider reports12% lower batch diarization error overall and17% lower with
  three or more speakers versus v2. Its16-language meeting/call dataset was
  internal at announcement, with future open release promised. These are provider
  claims, not independent Storybook results; FLEURS single-speaker WER cannot
  establish diarization quality.
- [Models](https://elevenlabs.io/docs/overview/models/),
  [changelog](https://elevenlabs.io/docs/changelog/2026/11/9): native
  `scribe_v3` (canonical identifier `elevenlabs/scribe_v3`) and
  `scribe_v3_live` (`elevenlabs/scribe_v3_live`) announced and API-listed.
  **Access: unverified** for both. No exact prior attempt found in central ledger.
- [Batch API](https://elevenlabs.io/docs/api-reference/speech-to-text/convert):
  POST `https://api.elevenlabs.io/v1/speech-to-text`, multipart audio/video input,
  JSON transcript/words/speaker_id/start/end output, `diarize=true`, up to32
  speakers, word/character timestamps. Existing v2 request shape supported.
  Number formatting and secondary languages added; no tool-calling, reasoning
  effort or arbitrary strict-schema interface applies to this ASR lane.
- [Realtime API](https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime):
  WSS `wss://api.elevenlabs.io/v1/speech-to-text/realtime`, exact
  `scribe_v3_live`, `diarize=true`. Draft labels can change; final
  `diarized_transcript` follows committed text and `speakers_merged` revises
  prior IDs. Cannot combine diarization with background-audio filtering.
  Live is a distinct transport/consumer evaluation, not covered by batch results.
- [API pricing](https://elevenlabs.io/pricing/api): listed v3/v2 batch
  USD0.20/audio-hour and v3 Live USD0.22/hour, excluding tax. Actual owner plan,
  quota and effective credit billing require qualification. No discounts assumed.
- Batch API defaults `enable_logging=true`; `false` requests enterprise-only
  zero retention. Realtime can explicitly warn that requested ZRM was not
  applied. No account-level ZDR, residency or training opt-out verified.
  Public licensed audio only; standard retention/training eligibility remains
  account-dependent. Preserve stricter owner controls, never silently disable
  them or change account settings to make an evaluation work.

## Current owner evidence and practical decision

Storybook executable
`packages/backend/src/services/audio-processing-providers.ts` still requests
`scribe_v2`, `diarize=true`, then uses `routes/voice/scribe-format.ts`.
The replacement boundary is saved-audio transcription, not Dossier extraction,
identity inference, live capture or Luna TTS. Better attribution could reduce
putting a relative's words under another speaker; the size of that improvement
is currently unmeasured. Same published base rate makes quality the main reason
to test; no measured latency or whole-workflow savings are claimed.

Read current owner AGENTS, relevant Ideal/spec/state, registry and:

- `docs/stories/story-201-batch-diarization-provider-evaluation.md`
- `docs/reports/story201-deepinfra-weekly-20261111.md`
- `docs/reports/artifacts/story201-preflight-20261028/corpus-manifest.json`
- `docs/evals/registry.yaml`: `story201-batch-diarization-qualification`
- `docs/stories/story-136-live-multi-speaker-just-listen-diarization.md`

All owner paths above are relative to
`/Users/cam/Documents/Projects/Storybook/storybook`.

Important correction to older context: DeepInfra's November11 native canary
**passed** labels/timings (103 words, four speakers). The matched Scribe v2
request failed HTTP401 `quota_exceeded`, zero credits. This is an access/billing
stop, not model quality. The owner paused and deleted its weekly monitor.
Do not retry inference until quota restoration or an explicitly authorized
eligible funded credential is evidenced. This proposal does not fund an account,
resume the Nemotron wallet, or restart monitoring.

## Stable proposal — one recommended lane, prerequisite explicit

1. **Storybook batch Scribe v3 versus current Scribe v2 — screening only,
   US$1 total maximum; prepare now, inference conditional on restored access.**
   Selection authorizes isolated owner preparation, read-only quota verification
   using the existing owner credential and bounded execution only if sufficient
   existing quota is verified. If still empty, complete offline preparation and
   report the exact access prerequisite; do not issue a known-failing ASR probe.
   No funding, subscription, automatic top-up or alternate credential selection.

   Reuse the owner Story201 public CC BY4.0 AMI packet (~33.6min per arm), exact
   audio hashes and pinned MeetEval0.4.3 scorer. Finish acoustic/reference and
   scoring-normalization gates before decision calls; do not misrepresent source
   annotations or prior source-hash audit as newly hand-checked acoustic truth.
   If independent acoustic adjudication cannot be satisfied, stop at contract
   qualification and report quality unmeasured rather than fabricate a baseline.

   Start one fresh matched60s no-hints contract pair, then the frozen same-input
   packet. Use automatic speaker count, word timestamps, faithful raw transcript,
   no keyterms/entity/edit surcharges and provider default diarization threshold.
   Match all applicable controls; no thinking setting exists, no threshold sweep.
   Preserve original responses and raw audio, treat speaker IDs as recording-local
   acoustic labels only. No private family/production recordings.

   Score cpWER primarily, tcpWER where valid, ordinary WER, speaker confusion,
   fillers/name errors, missed/extra speech and silence hallucinations; report
   per-clip, macro and micro results, latency and effective cost. Predeclare
   >=10% relative aggregate cpWER improvement, no >2 percentage-point absolute
   WER regression in represented conditions, no fabricated silence speech or
   identity claims. These are owner provisional screening bars, not an automatic
   production adoption gate. Stop a valid failing arm; repair harness defects
   offline using saved answers when possible. Do not rerun valid failures to win.

   Reserve conservatively at USD0.40/hour plus20% cushion pending actual account
   billing. 67.2min paired packet costs about USD0.538 with cushion; two60s
   canaries about USD0.016, leaving bounded recovery headroom under US$1.
   Cap all billed subject duration at90min at that reservation rate (~USD0.72),
   total known plus unknown exposure <=US$1. No paid judges/synthesis. If actual
   billing is higher, reduce only predeclared nonessential coverage before calls
   or pause; never exceed the cap or omit failures from accounting. Existing
   Story201 Nemotron spending/reservations remain separately preserved.

   This is explicitly a public meeting screen. It lacks representative family,
   two-person/noisy and5–8-speaker coverage; no production adoption claim or patch
   is promised from this packet. A win identifies the exact missing independent
   quality/consumer gates for a later bounded adoption selection. Existing
   formatter replay can be checked offline; no default activation or product
   writes are selected.

Combined proposed cap US$1. No spending approved by this Stage1 record.

## Task decision table

| Owner / boundary | Incumbent | Candidate / evidence | Disposition / next action |
|---|---|---|---|
| Storybook saved-audio words and attribution | Scribe v2 native batch | Scribe v3; public docs only, access/quality unverified | Recommend conditional public screen above; selection and quota prerequisite outstanding |
| Storybook live Just Listen | Deepgram Nova-3; diarization Story136 future | Scribe v3 Live; docs only | Defer; no implicit reprioritization of future story or live transport/UX replacement |
| Echo Forge live GM narration | No maintained ASR comparator found | Scribe v3 Live; capability fit only | Defer until owner maintains audio fixtures/scorer and a live consumer decision |

## All registered owner dispositions

A bounded lower-cost read-only delegate inspected the ten non-Storybook repos;
coordinator inspected Storybook and checked its actual provider/owner evidence.

| Registered repo | Disposition | Concrete reason |
|---|---|---|
| Storybook | Evaluate now: conditional preparation/screen above | Current batch job and public packet; paid inference blocked until access restored |
| Dossier | Do not evaluate | Consumes transcript text/JSONL; no owned acoustic transcription boundary |
| Doc Web | Do not evaluate | Maintained transcription is document OCR, not speech recognition |
| CineForge | Defer | Audio/media references plausible, but no maintained ASR/diarization job, eligible benchmark or incumbent found |
| Board Game Ingester | Do not evaluate | Document/image/component intake; no speech lane |
| Robo Rally | Do not evaluate | Game engine; audio output is not speech recognition |
| Echo Forge | Defer | Push-to-talk GM narration planned; maintained comparisons use typed scene text, not acoustic fixtures |
| Ultima IV Web | Do not evaluate | Game audio effects/timing, no ASR consumer |
| Financial Hub | Do not evaluate | Financial document/report workflow, no maintained speech lane |
| Financial Monthly Analysis | Do not evaluate | Statement/transaction source intake, no maintained speech lane |
| VLC Thumbs | Do not evaluate | Playback thumbnails/bookmarks, no maintained transcription/attribution job |

Echo evidence: `docs/spec.md` push-to-talk/live-table sections and
`docs/evals/attempts/20261024-harness-integrity.md`; live speech interaction is
a product direction, not proof of an existing ASR benchmark. Root checked
Story136's explicit future-story restriction. Retain current models everywhere
pending measured evidence. No worktrees were created, so no cleanup inventory.

## Validation

Documentation-only: checked provider claims against linked primary sources,
owner request/formatter boundary, quota report, public manifest, registry,
prior-attempt ledger and future-story status. No product suites or paid calls.
