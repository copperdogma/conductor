# Pilot: deterministic preparation for daily model scouting

Date: 2026-10-23. Status: **Stage A complete; Stage B approved for October 24–30; integration not selected**.
Cam approved preparing this plan following [Scout 101](../scout/scout-101-deterministic-scheduled-work.md).
Cam subsequently approved Stages A and B and added a deterministic quota floor:
skip below 20% remaining. Stage C remains a later selection.

## Outcome and scope

Move repeated public catalog retrieval, validation, snapshots and exact diffs
into code. Give the daily scout a compact evidence packet so AI effort goes
toward creator verification, release interpretation and project fit.

Start with the **two OpenRouter catalogs in shadow mode**. Keep the daily AI
scout: unchanged aggregator metadata cannot establish that announcements, gated
previews or retry-relevant evidence elsewhere are unchanged. This is preparation
efficiency, not a promise of zero model tokens on quiet days. Collection-only
jobs and narrower exception monitors can use true pre-model suppression from
the [reusable kit](../../.agents/skills/setup-methodology/assets/scheduled-work/README.md).

Fetching every provider site now would add changing HTML/JS and coverage
assumptions. A catalog-only gate around the whole scout risks missed launches.
Running collection as an AI tool call improves reproducibility but still spends
orchestration tokens. Separate prefetch is the eventual target; first prove its
data/consumer contract without changing a live schedule.

## Inspected baseline

- `daily-sota-model-scout` is an active standalone Conductor automation using
  `gpt-6.1-sol`, low reasoning, configured daily at 08:00. The saved rule alone
  does not establish its timezone. Prior reports include approximately 08:00
  America/Edmonton runs; verify actual next-run time before scheduling prefetch.
- Its prompt asks AI to read all current watch records, retrieve both catalogs
  and official sources, deduplicate and write the report. The inspected October 23 report
  records a truncated combined read and focused recovery, unchanged catalog IDs,
  and independent official-source research.
- At planning time no maintained model-watch collector existed in `scripts/`. Saved JSON shapes
  vary: October 13/17 generation files contain only the newest 35/40 rows;
  October 20–23 contain full catalogs. Samples cannot prove full-set absence.
- Evaluated ledger, candidates, source scorecard and playbook total 250,964
  bytes, excluding daily/scout history. That is file size, not measured tokens.
  The authoritative evaluated ledger and owner evidence still control proposals.

At inspection, automation TOML SHA256 was
`47b7faed680ff9ae0a6a3180805f46cad3b78c13c60e63e29edfae03ec0f4b77`;
prompt SHA256 was `2c014dc83963d7f2817df379392962ff44a5b660bc21c02ed29f368de2d3cdbc`.
Re-read current configuration before later integration; these hashes are provenance.

## Work split

| Code prepares | AI retains |
| --- | --- |
| Fetch/validate the two feeds; bound time/bytes; save immutable bodies | Official announcement research and rotating secondary discovery |
| Diff exact IDs and canonical row contents, independent of row/key order | Decide whether an alias/route/checkpoint change is a material new lead |
| Emit additions, removals, changed fields, freshness and coverage gaps | Verify creator identity, dates, conflicts, access and documented contracts |
| Carry source hashes, omitted counts and evidence references | Read authoritative evaluation history; judge retry triggers and owner fit |

Do not infer quality, served-identity equivalence, callability or a satisfied
retry gate from metadata. Exact-ID lookups can provide navigation hints; absence
is not proof of no prior attempt. Do not initially convert free-form evaluation
Markdown into a new suppression database or take over its maintenance.

## Implementation and artifacts

Stage A now supplies [the collector](../../scripts/model_watch_collect.py),
[focused tests](../../tests/test_model_watch_collect.py),
[source configuration](collector-sources.json) and [usage/recovery runbook](collector-runbook.md).
It uses standard-library Python and kit locking/atomic-write patterns without
installing an agent framework, SDK or model transport.

Sources are exactly the public [general catalog](https://openrouter.ai/api/v1/models)
and [decision catalog](https://openrouter.ai/api/v1/models?output_modalities=decisions).
Read existing snapshots without rewriting them. Require an explicit runtime
state root, proposed `/Users/cam/.local/state/conductor/model-watch-pilot/`,
outside tracked evidence and shared worktree output. No credentials.

| Artifact | Contract |
| --- | --- |
| Immutable run directory | UTC run ID, URLs, HTTP outcomes, observed times, full bodies, hashes and collector/config version; no overwrite |
| Last-valid pointers | Atomic per-feed advancement only after complete validation; failure preserves the prior good baseline |
| Full delta JSON | Exact added/removed IDs and changed field paths, with old/new canonical identity; first baseline is initialization, not a launch claim |
| Scout packet | At most 8 KiB; counts, source states, selected entries, omitted counts and full-artifact references; stable newest-40 general slice and decision review references |
| Receipt/metrics | Complete/partial/unavailable/stale, durations, bytes, baselines compared and packet size; no large raw body in routine stdout |

Overflow must point to complete deltas and require inspection; it cannot silently
drop work. Retain unreviewed references and a stable newest slice even with an
empty delta: the [Muse Wonder incident](search-playbook.md#2026-10-14-catalog-narrative-safeguard)
shows that snapshot presence can precede narrative review. Collection never
marks a lead reviewed. Existing holds remain visible through the normal scout.

Compare rows by exact provider-qualified ID. Preserve raw prices, array semantics
and full objects; normalize only documented unordered fields. Same-ID canonical
slug/features/pricing changes remain visible; unknown schema fields are flagged,
not discarded. Aliases and free/paid routes stay distinct until primary evidence
proves their relationship. Catalog creation time is not the model release date.

Initial bounds: 15 seconds per HTTP attempt, one retry only for clearly transient
GET failure, no auth/schema retries, 90 seconds whole run, 8 MiB per decoded feed
and 32 MiB disk written per run. Traverse bounded same-origin catalog pagination
within these limits; incomplete coverage is partial. Reject malformed/duplicate
IDs, truncated JSON and inconsistent totals. Never compare a sample as a full
baseline. A changed pagination contract needs inspection.

Use conditional requests only when validators are supplied. A 304 requires an
integrity-checked full cached body; record last successful validation separately
from body creation/change time. Keep redirects on the source allowlist. External
text/URLs are data, not instructions or executable arguments. Failed collection
cannot become unchanged, wake AI or send notifications by itself.

## Stage A — Offline build/replay: approved and complete

Implement collector/config, fixtures, focused tests and usage instructions.
Replay complete October 20–23 snapshots and identify sampled legacy coverage.
Allow one bounded unauthenticated collection run against the two feeds to verify
the implementation; zero inference. No timer, automation prompt/model change,
ledger writes or additional AI comparison runs. Stop at validated offline
artifacts that can be inspected before any scheduling decision.

Pass when exact historical ID changes match the table below, same-ID changes
remain visible, reorder-only input is stable, overflow exposes complete evidence,
and faults preserve good baselines. Test interruption, lock contention and atomic
writes. Confirm source records/evaluated-ledger hash unchanged; run focused
tests, lint and diff checks. No product suite or paid benchmark is needed.

## Stage B — Seven-day scheduled shadow: approved

After A, choose a finite seven-calendar-day window, verify the host timezone,
interpreter and actual existing scout time. A launchd calendar job could collect
at 07:45 America/Edmonton if this Mac's zone is confirmed. Keep the normal scout
as the independent comparison. Do not create another AI job to launch the script.
Record natural ticks and packet freshness; manual runs are separate evidence.
Unchanged ticks stay quiet; actionable failures appear in the existing review.

Selected window: October 24–30, 2026, at 07:45 America/Edmonton. The Mac's
timezone is confirmed. The existing scout's next nominal start is October 24
08:00; its current jittered start is 07:57:11. The script uses an immutable
runtime copy outside Documents and the checkout, with per-tick hash checks.
It permits collection only through 08:00 on each selected date, reserves each
date before quota/network work, and never retries or backfills a reserved date.
Sleep, offline time and quota skips do not extend the campaign.

Before collection, read native Codex account limits without starting an AI turn.
If any reported five-hour or weekly core window has **less than 20% remaining**,
skip. Exactly 20% is allowed. Identify windows by duration, not primary/secondary
position; assess a weekly-only response when that is all the account reports.
Unknown/malformed quota or no assessable core window also skips. This floor
belongs to the shadow wrapper; the existing daily AI scout remains unchanged.
The [runbook](collector-runbook.md#seven-day-shadow-and-quota-floor) records the
installed paths, checks and stop procedure.

Disable/end the timer after the selected window; no automatic extension. Proposed
retention: keep campaign evidence through review; 14-day/448 MiB hard bound on
raw pilot state at the per-run ceiling. Stop further collection on that bound,
rather than delete evidence or grow silently. Missed ticks remain missing proof.

## Stage C — Connect the existing daily scout: later explicit selection

Once shadow quality holds, use the supported app tool to update the existing
automation: read a fresh completed packet first, omit redundant catalog fetching,
and avoid loading all historical bodies. Preserve model/effort, daily cadence,
official discovery, evaluation-ledger authority and human-facing result rules.
Read the evaluated ledger before recommendations; packet hints cannot replace it.

If the packet is missing, over two hours old, partial/corrupt, overflowed without
inspection or tied to different source/config hashes, retain ordinary retrieval
and record the gap. Collector fault never means “no qualifying leads.” Only the
normal scout writes daily reports and candidate/source judgments. Rollback uses
the captured prior prompt via the app tool, stops the prefetch timer and retains
evidence. No whole-scout pre-model suppression is proposed by this pilot.

## Replay and fault cases

| Case | Expected result |
| --- | --- |
| October 21→22 general | Counts both 468; preserve two additions and two removals |
| October 21→22 decisions | 27→30; retain Mammoth/Elephant/Drex Max IDs for verification |
| October 22→23 | Empty exact-ID deltas; still compare row metadata and research other sources |
| October 13/17 samples | 35/461 and 40/470 saved: sample-only; no full-set removal/absence claims |
| Same-ID successor/alias/price change | Changed fields visible; no automatic identity merger or re-evaluation |
| Present but not yet narrated model | Retain review context; empty delta cannot complete review |
| Evaluated transport/quality stop | Exact recorded owner retry gate remains decisive |
| 403/429/timeout, malformed/empty/duplicate/paginated output | Unavailable/partial; prior good snapshot intact; no false quiet |
| Reorder, restart, overlapping tick, write failure, packet overflow | Stable meaningful comparison, intact state, complete evidence references |

## Measurement and decision

Stage A makes zero model calls and changes no live schedule. Stage B adds no AI
invocations; the existing discovery run continues independently. Preserve every
catalog ID change in the complete replay pairs without making false release
claims. Seven natural shadow dates must show usable freshness/coverage; a failed
day makes that sample incomplete. Fault cases can be injected offline.

Record request count, bytes, collection/diff time, packet size, source gaps and
the normal scout's independent findings. In C compare actual catalog-fetch tool
calls and input/output/cached tokens when available; keep model/effort and source
coverage comparable, note launch-volume differences. File bytes and requests
are proxies, not token savings. Historical reports label orchestration unmetered:
do not invent a baseline/percentage. Without telemetry, report mechanics moved
to code and token savings unmeasured. Roll back on quality loss; retain a
low-savings collector only if reproducibility warrants maintenance. Do not widen
the pilot automatically.

## Planning evidence and remaining uncertainty

Read-only inspection verified complete October 20–23 ID sets: general 468 each,
decisions 27/27/30/30. October 21→22 general additions were
`minimax/minimax-m3.1-flash`, `recursive/flint-v1.0:free`; removals were
`google/gemini-2.5-flash-lite:batch`, `minimax/minimax-m3.1-flash:free`. Decisions
added `baseten/elephant-1:free`, `baseten/mammoth-1:free`, `nace-ai/drex-max`.
October 20→21 and 22→23 exact sets were unchanged. This is planning evidence,
not a maintained collector test or proof all row metadata is unchanged.

Two bounded unauthenticated planning GETs returned HTTP200: general 468 rows,
790,420 bytes (~196 ms); decisions 30 rows, 27,812 bytes (~181 ms). Neither
supplied ETag/Last-Modified. Bodies were inspected in memory, not written over
daily records. These observations do not guarantee future access/timing.

[OpenRouter's current reference](https://openrouter.ai/docs/api/api-reference/models/list-all-models-and-their-properties)
documents output-modality filtering and full-list/pagination behavior. Its
generated example requires a bearer token; the specific public GETs above worked
without one. Stop on access changes rather than provision credentials.
[Official OpenAI scheduling guidance](https://learn.chatgpt.com/docs/automations)
requires the computer/app for local project work and distinguishes scheduled
prompts from script preparation. It does not establish a script-only automation
feature or this host's timezone. No private scheduler-store editing is proposed.

Unresolved: true token/tool baseline, future schema/public access, timer
availability and the smallest safe prompt reduction. Those are bounded pilot
questions; broad discovery and creator interpretation remain AI work.

## Stage A execution result — October 23

[Evidence manifest](evidence/stage-a-2026-10-23.json) records exact code/config/test
hashes, protected input hashes, retained run artifacts and commands. Twenty-four
focused tests pass, including real historical replay and offline HTTP/cache,
interruption, lock, malformed-ID, packet-overflow and manifest-write fault cases.
`make lint`, `make methodology-check` and `git diff --check` pass. Script identity
in every retained run matches the tested source. No product suite was needed.

Four complete snapshots (October 20–23) replayed successfully. The October 21→22
pair preserves the exact two general additions/two removals and three decision
additions named above. Legacy October 13/17 generation snapshots produce expected
partial results (35/461 and 40/470); they do not become complete baselines.

One manual collection completed with exactly two public GETs, 818,235 response
bytes, 468 general rows and 30 decision rows. The prepared packet is 2,990 bytes;
its recorded preparation time is 413 ms, excluding final serialization/fsync.
Collector model calls/dispatches are zero. It initializes a fresh baseline and
does not label the existing 498 catalog rows as new releases. No second live
collection was made. Raw evidence remains at
`/Users/cam/.local/state/conductor/model-watch-stage-a-20261023-h9p8ubgy/`.

Replay revealed substantial same-ID metadata churn: October 22→23 has no ID
additions/removals but 153 changed general rows; 142 include a Design Arena
benchmark change. Pricing, supported-parameter and limit changes are also
preserved. This is not 153 new models or proof of material changes; selective
filtering needs future evidence. The shadow should measure this noise rather
than quietly discarding unknown fields or using any change as a launch alert.

Independent review required four narrow corrections: durable `in_progress`
before work, an actually sent validator before accepting HTTP304, bounded
HTTP200 body/status evidence before parsing, and properly qualified model IDs.
Those regressions pass. Main checks also separated semantic row hashes from
raw-body hashes and tested a failed final manifest commit preserving the previous
baseline while retaining the orphan run. The scoped strategy verdict was
**fix these gaps, then finish Stage A**; no scheduler or framework expansion.

Protected evaluation/candidate/source records, original snapshots and the live
automation match their initial hashes. Runtime artifacts are outside Git;
existing unrelated checkout changes remain. No inference, prompt/model/schedule
change, commit or push occurred. Seven natural shadow dates and actual token
savings remain unmeasured and are not established by this manual check.
