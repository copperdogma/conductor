# Scout 115 — Scribe v3 diarization evaluation routing

**Current status, November17: completed public screen; retain Scribe v2.**
Scribe v3 is faster at the same decision-credit cost, but did not improve
speaker-attributed accuracy. Historical proposal and execution chronology follow;
the completed-screen section is authoritative for the current decision.

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

## Selected execution — 2026-11-17

Cam reported "Elevenlabs credit is back. Go ahead." This selects item1 only:
Storybook batch v3/v2 public-audio screen, combined US$1 maximum, including
existing owner quota verification and the disclosed acoustic/reference gates.
No live lane, Nemotron rerun, private input, account change, default activation,
commit/push or deployment. Screening-only remains the selected scope.

Removed the now-obsolete November18 credit reminder before execution. One
capable lower-cost owner worker owns the isolated Storybook execution; coordinator
reviews its evidence and updates Conductor. Worktree destination must resolve
under `/Users/cam/.codex/worktrees/scribe3-20261117/storybook`.

### Quota and reference evidence

Owner read-only subscription/user API requests returned `missing_permissions`
for the existing narrowly scoped key. Coordinator verified the already signed-in
ElevenLabs UI at `https://elevenlabs.io/app/home`, profile balance menu, on
November17: My workspace, Creator plan, total100,000 credits, remaining99,973.
No account setting, funding, permission or credential changes. This corroborates
Cam's restoration report; do not attribute any preceding credit use to this
campaign without its own receipt.

Bounded research on reference validity checked the
[AMI transcription process](https://groups.inf.ed.ac.uk/ami/corpus/transcription.shtml):
source human transcribers listened/transcribed, a second pass reviewed segments
and uncertainty, and channel IDs distinguish speakers. Word timings are forced
aligned. Thus the published manual archive is a valid human-reference basis for
exploratory benchmarking, but it is not a fresh local listening audit of our
derived clips. The owner November11 audit and this selected proposal retained
that latter gate as open. Preserve the distinction; do not silently claim it
has passed from an XML/hash review. Existing
[MeetEval](https://github.com/fgnt/meeteval) scoring techniques remain the selected
standard tools, with local known-case checks before use.

### Reference selection clarified by Cam

On November17, Cam explicitly selected "Yes—use AMI’s human-reviewed references
(Recommended)" in response to the concrete choice between published-reference
quality screening and contract-only execution. The question disclosed that the
new local listening audit cannot be performed with available tools, that AMI's
source references were already human-transcribed/reviewed, and that results
would explicitly retain this limitation. The same combined US$1 cap applies;
no new wallet, adoption, private-data or live scope. This supersedes the earlier
contract-only stop for absence of a fresh local listening audit. Original plan
and November11 reference limitations remain preserved above.

## Completed public screening — 2026-11-17

**Retain Scribe v2 for Storybook saved-audio transcription.** Scribe v3 is
callable and contract-compatible, but missed the predeclared >=10% relative
speaker-attributed transcription improvement. This completes the selected public
screen, not production/family-audio qualification. No further paid round follows
automatically.

Three frozen AMI decision recordings, about33.1min and3,309 normalized reference
words, were scored using the approved published human-reviewed references and
MeetEval0.4.3. Exact native/default `scribe_v3` was fresh; exact same-day
`scribe_v2` outputs from the separately resuming original Story201/Nemotron
comparison were reused after independent input/settings/raw-response verification.
This preserves Cam's recorded no-repeat-baseline instruction and avoids three
duplicate POSTs. This is same-input/same-day, not all-fresh paired dispatch.
Our selected fresh matched60s canaries remain separate development evidence.
No hints, model effort controls or parameter tuning were tested.

| Decision metric | Scribe v2 | Scribe v3 |
|---|---:|---:|
| Word-weighted cpWER, lower better | 637/3,309 =19.2505% | 653/3,309 =19.7341% |
| Clip-macro cpWER | 14.2614% | 16.5213% |
| Word-weighted tcpWER,2s collar | 19.8247% | 20.1571% |
| Chronologically flattened WER | 12.3905% | 13.3877% |
| Mean decision request wall time | 12.5463s | 6.6967s |
| Provider-reported decision credits | 877 | 877 |

V3's micro cpWER was2.51% relatively worse, although mean latency was46.6%
lower. Its three clip cpWERs were12.15%,15.98%,21.43% versus
v2's11.60%,9.20%,21.98%. The long clip slightly favored v3; both models emitted
only two speaker IDs for its four-speaker reference. All per-clip ordinary-WER
regressions stayed below2 percentage points. Both15s zero-PCM controls returned
no invented lexical speech. Native canaries and formatter replay passed for
both. cpWER measures joint word/speaker errors, not pure time-based diarization
error rate; flattened WER is overlap-order-sensitive and tcpWER uses source
forced-aligned times.

### Layered verdict and limits

- Access/transport: qualified on the existing native owner key. Missing
  account-read permissions did not prevent ASR; signed-in UI verified quota.
  Native responses did not independently attest an immutable served revision;
  requested model IDs and direct route are retained.
- Reliability: successful bounded requests and silence controls; no broad
  concurrency/reliability qualification.
- Capability: no demonstrated v3 quality win on this frozen screen; retain v2.
- Economics: same decision credits, v3 faster; actual USD charges unreported.
  Current campaign used973 new credits and retained US$0.336 maximum exposure,
  below US$1. The877 reused baseline credits and their dollar accounting belong
  to the separate original campaign, not this wallet. Unknown charges are not
  silently converted into actual settled USD costs.
- Adoption: retain incumbent. Storybook live diarization and Echo Forge speech
  evaluation remain deferred. Other registered projects remain unchanged.
  Reopen only for a material model/route change, a new representative maintained
  task/corpus, or explicit fresh selection; no unchanged automatic rerun.

The25min long recording contributes76.6% of reference words; both macro and
micro are reported. One run per model/decision clip, no fresh local listening
audit, no private interviews or representative noisy/two-person/five-to-eight-
speaker corpus, and no training-set independence claim. No production/default,
identity or canonical transcript changes.

### Evidence, review and custody

Owner: Storybook. Retained worktree
`/Users/cam/.codex/worktrees/scribe3-20261117/storybook`, branch
`codex/scribe3-20261117-storybook`, base
`4c9483179944461c20081b39d3bf4544ff9b023b`. Retain uncommitted for evidence and
reproduction; no removal/landing selected. Primary checkout remains untouched
by this campaign. Original Story201 work remains separately attributed.

[Owner report](https://github.com/copperdogma/storybook/blob/a1829c7914d6a2ef12d82f79a4987c1e0699e569/docs/reports/story201-scribe3-public-screen-20261117.md),
[frozen plan](https://github.com/copperdogma/storybook/blob/a1829c7914d6a2ef12d82f79a4987c1e0699e569/docs/reports/artifacts/story201-scribe3-20261117/plan.json),
[scores](https://github.com/copperdogma/storybook/blob/a1829c7914d6a2ef12d82f79a4987c1e0699e569/docs/reports/artifacts/story201-scribe3-20261117/decision-scores.json),
[cost ledger](https://github.com/copperdogma/storybook/blob/a1829c7914d6a2ef12d82f79a4987c1e0699e569/docs/reports/artifacts/story201-scribe3-20261117/spend-ledger.json),
[custody manifest](https://github.com/copperdogma/storybook/blob/a1829c7914d6a2ef12d82f79a4987c1e0699e569/docs/reports/artifacts/story201-scribe3-20261117/custody-manifest.json).
Exact-baseline reuse amendment, original receipts, copied native responses,
normalization/scorer freeze, archive/audio/reference hashes, code identity,
formatter replay and provider-free checks live alongside those artifacts.

Coordinator independently reviewed dispatch/scoring code, recalculated637/3309
and653/3309, credit sums and means, and verified every current response and
receipt fixture hash. Score artifact SHA256:
`698c63cca85f0d91f193c90c9bb30fcc2e5843e5170e61462cca4e9be88c00a3`.
Owner's focused privacy4 and methodology12 checks and known-case scorer/integrity
checks passed. No product suite, runtime edit, commit, push or deployment.

Final owner validation also passed methodology compile/check, privacy-manifest
coverage, full offline score replay, report-link/JSON/hash checks and whitespace.
An unrelated pre-existing global privacy review expiry was recorded, not changed
or represented as a newly passing global gate. Owner registry ID
`story201-scribe3-public-screening`, attempt
`story201-scribe3-public-screen-20261117`; Story201 worklog and generated views
retain this independent screen. All11 new inference POSTs terminated; no retry,
active dispatch lock or further provider work remains. No `.env` or key was
copied, so no temporary credential removal was needed.

Final custody-manifest SHA256
`153abcd7b0962e14e698c806c635309910fa55c0c49379f418a1dc6cdbf5289d`;
ledger SHA256
`bf58142a3f2cd5848741483cb6adb13f724845362577353656919b9b08b6ab2f`.
Final recommendation across selected owners: retain Storybook Scribe v2;
no other owner was selected for execution. No further run recommended now.

## Accepted recommendation and publication — 2026-11-17

Cam accepted retaining Scribe v2 and requested check-in/push. This authorizes
publication of the completed screening evidence, not a runtime switch or a new
evaluation. Storybook's unrelated, still-unlanded Nemotron story and in-progress
campaign records are excluded; only the exact public AMI preparation dependencies
required by this screen accompany its report, independent registry entry,
native responses and reproducible scorer. No story-wide completion claim.

Conductor publication includes only this scout, its current index/ledger/inbox
entries and a scoped changelog. Prepared against current remote main in an
isolated worktree to preserve the shared checkout's unrelated changes.
Documentation validation: `make lint`, `make methodology-check`, reviewed
task-only diff, local evidence links and whitespace pass. Reuse the owner
unchanged provider-free/scorer checks; no new provider calls or product suites.

| Worktree | Owner / branch | Custody |
|---|---|---|
| `/Users/cam/.codex/worktrees/scribe3-20261117/storybook` | Storybook / `codex/scribe3-20261117-storybook` | Retained for public media/request evidence and excluded historical work; no cleanup selected |
| `/Users/cam/.codex/worktrees/scribe3-closeout-20261117/conductor` | Conductor / `codex/scribe3-closeout-20261117` | Retained integration checkout; no cleanup selected |

The original primary checkouts and unrelated staged/untracked changes remain
untouched. Scribe v2 remains the configured transcription/diarization provider;
no deployment is part of this publication.

### Owner publication identity

Storybook evidence candidate `a1829c7914d6a2ef12d82f79a4987c1e0699e569` is based on
`4c9483179944461c20081b39d3bf4544ff9b023b`. Final portability fixes changed only
three derived reused-baseline witness paths to repo-relative paths; the native
responses, decision score artifact and spend ledger are unchanged. Final custody
manifest SHA256 `40debf6d1cdb245eeed5c5dbc0d48822bb0af6c8070d1ea0d089d672f8d07025`
supersedes the earlier custody snapshot above. Historical raw receipts remain
preserved. Root reviewed the candidate's task-only path list and verified
unchanged score/spend identities. Owner staged62-file allowlist, safe credential
scan, methodology consistency, full offline score byte replay and Ruff passed.
Historical byte-frozen dispatch ESLint used its documented no-explicit-any
exception; no production lint rule or runtime source was changed.

Permanent owner report and artifact links above point to this exact commit.

Storybook task branch and remote main were independently verified at
`a1829c7914d6a2ef12d82f79a4987c1e0699e569`; publication was a fast-forward from
`4c9483179944461c20081b39d3bf4544ff9b023b`. Retained original media/request bytes
and the excluded Story201 snapshot under the owning worktree's ignored
`tmp/scribe3-reviewed-unlanded-story201/` custody surface. No account, provider,
runtime or deployment changes occurred during closeout. Conductor supervisor
publication follows the owner landing; its commit identity is supplied by Git.
