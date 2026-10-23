# Model-watch collector: offline pilot runbook

The [pilot plan](deterministic-pilot-plan.md) separates offline implementation,
scheduled shadowing and integration. This command implements Stage A only:
catalog preparation with **zero model calls and no dispatch or scheduling**.
It does not change the existing daily scout, judge model quality, complete
semantic review, recommend evaluations or write the evaluation/candidate ledgers.

## Replay without network

From the Conductor checkout, with Python 3.10+ on macOS/Linux:

```bash
python3 scripts/model_watch_collect.py replay \
  --state-root /Users/cam/.local/state/conductor/model-watch-replay \
  --snapshots docs/model-watch/daily/2026-10-20-catalogs.json \
              docs/model-watch/daily/2026-10-21-catalogs.json \
              docs/model-watch/daily/2026-10-22-catalogs.json \
              docs/model-watch/daily/2026-10-23-catalogs.json
```

Snapshots are consumed in the supplied order. Each gets a new immutable run and
one compact stdout JSON receipt. They are read without rewriting the originals.
October 13/17 generation samples are also recognized, but yield `sample_only`
and partial status; they never advance a complete general-catalog baseline.
Replay source timestamps remain unknown if the source file omitted them. Run
preparation time is not a reconstructed historical observation time.

For reproducible comparisons use a fresh replay root: the first complete
snapshot initializes the baseline and emits no mass “new model” claim; later
ones compare against that feed's last complete snapshot. Repeating a command
uses its saved baseline and adds new runs; it does not overwrite old evidence.
Do not mix replay, collection or a different config identity in one state root.

## Manual public collection

The Stage A approval covers one bounded collection run against the two feeds:

```bash
python3 scripts/model_watch_collect.py collect \
  --state-root /Users/cam/.local/state/conductor/model-watch-pilot
```

This makes unauthenticated GETs to the two exact feeds in
[collector-sources.json](collector-sources.json). No environment file, API key,
browser cookie or provider account is loaded. The HTTP client disables inherited
proxy settings and refuses redirects; a changed URL or compression contract
requires inspection. Identity encoding avoids unbounded decompression. Pagination
can follow only the same catalog path/origin and the original output modality.
An access failure does not authorize credential provisioning or inference.

The source config is versioned. Its limits can be reduced for offline fault
tests, never increased above the code's ceilings. A changed canonical config
requires a separate state root or an explicit future migration; reformatting the
same JSON does not change identity. Defaults are 15 seconds per HTTP open/read
operation, 90 seconds per run with POSIX timer/deadline checks, one retry for a
transient GET-open failure, eight pages, 8 MiB decoded body per feed and 32 MiB
written per run. Mid-body read/schema/auth failures fail visibly; they are not
silently retried. The collector itself does not install a timer; the finite
Stage B wrapper below owns scheduled admission.

## Inspect the result

| File | Meaning |
| --- | --- |
| `state.json` | Single atomic commit manifest: source/config identity, mode, latest run, last complete snapshot per feed, accumulated review references |
| `last-attempt.json` | `in_progress` before work, then its outcome/error; interruption remains visible instead of leaving old success as current; inspect stdout/exit status if disk writes fail |
| `runs/RUN_ID/snapshot.json` | Complete normalized rows or explicit sample coverage, HTTP receipts, source/collector hashes, observed/validation/change times |
| `runs/RUN_ID/delta.json` | Full exact-ID additions/removals and same-ID changed field paths, with the actual baseline run IDs |
| `runs/RUN_ID/packet.json` | At most 8 KiB, source status, selected IDs, omitted counts and full evidence references |
| `runs/RUN_ID/receipt.json` | Per-run operational counts/bytes/preparation time; model calls and dispatches are zero |
| `runs/RUN_ID/*-page-NNN.json` | Bounded decoded HTTP200 bodies, including malformed JSON retained for inspection; 304 uses the hash-verified prior complete snapshot |
| `runs/RUN_ID/replay-input.json` | Exact saved replay input and source hash; replay can include a different legacy wrapper |

`complete` means both feeds passed the known coverage/schema checks. It is not
semantic review, first-party release verification or proof the public catalog is
globally authoritative. `partial`/`unavailable` keep usable evidence and gaps
visible. Exit 0 covers complete runs and overlap; exit 2 covers partial,
unavailable and errors. Repeated overlap needs investigation. No result wakes AI.

The packet shows newest general IDs and decision references even on empty
deltas. It excludes raw descriptions and response bodies from initial context.
Omitted rows/delta details point to full artifacts: inspect them when relevant;
an empty ID delta does not clear earlier review references. Review backlog is
retained in the manifest and has no automatic completion/acknowledgement in this
pilot. Evaluated-model history and existing holds remain independently decisive.

## Failure and recovery

- Do not reset state to clear corruption or switch modes. Preserve the root,
  inspect the error and restore verified state or select a fresh explicit root.
- A malformed/truncated body, duplicate ID, changing pagination total, missing
  page, wrong modality or empty catalog cannot become unchanged. Good per-feed
  baselines advance only after the new immutable run is complete and the single
  state manifest is replaced.
- ETag/Last-Modified are optional. A 304 is accepted only for an intact complete
  cached single-page body when a conditional validator was actually sent; a
  first-page validator cannot cover a merged catalog.
  New successful validation time does not imply new content or a new release.
- Write interruption can leave `.staging-*` or a complete unreferenced run.
  Referenced snapshots remain hash-checked. Do not promote an orphan as the latest
  good state by guessing; retain it for inspection and rerun only within the
  authorized collection budget. Old run files are never edited in place.
- State must be outside the checkout, at an explicit absolute nonsymlink root.
  New files are owner-only; protect permissions of any existing directory.
  No secrets belong here. State under any detected Git checkout and symlinked
  state contents are refused. A shared worktree
  should not acquire its own hidden scheduler/state fork.
- The collector reserves room against a 448 MiB state ceiling and 10,000-file
  bound, then stops rather than deleting evidence. Staging/orphan files count.
  No evidence-deletion timer is installed. Keep campaign evidence until review;
  the Stage B expiry stops collection without deleting it.

## Focused validation

```bash
python3 -m unittest discover -s tests -p 'test_model_watch_collect.py'
make lint
make methodology-check
git diff --check
```

Tests use real saved catalogs plus synthetic offline HTTP/state faults. They do
not query a provider or start a scheduler. Source snapshots and the evaluated
ledger must remain unchanged. Full replay and one manual collection are separate
evidence from a natural scheduled tick; token savings remain unmeasured until
normal-scout integration and comparable telemetry are available.

## Research decisions

The problem class is bounded HTTP collection with partial-snapshot and crash
recovery, not model selection. Reuse standard HTTP and POSIX mechanisms:
[OpenRouter's source contract](https://openrouter.ai/docs/api/api-reference/models/list-all-models-and-their-properties),
[Python urllib](https://docs.python.org/3/library/urllib.request.html) and
[Python interval timers](https://docs.python.org/3/library/signal.html#signal.setitimer).
The API's declared totals/next links establish the completeness checks; local
replay demonstrates the legacy sample distinction. Socket timeouts alone do not
bound a whole drip-fed response, so CLI execution also uses a POSIX wall timer.
Signals are main-thread/POSIX behavior, not a portable Windows implementation or
an unconditional guarantee over arbitrary stalled C/kernel work. No transport
fallback, private scheduler-store editing or AI launch is needed for Stage A.

## Seven-day shadow and quota floor

Cam approved a finite script-only shadow on October 23. It collects at **07:45
America/Edmonton, October 24–30, 2026**, through a user launchd agent. A delayed
wake can collect through 08:00 on that date; later starts record `missed_window`.
No retries, backfill or automatic extension. The last selected day disables the
job; an October 31 00:05 entry and RunAtLoad expiry check cover missed final ticks.
Calendar entries lack a year, so the runtime's full-date check is authoritative.
An expired invocation cannot read quota or collect even if disabling fails.

Files:

- Wrapper: [model_watch_shadow.py](../../scripts/model_watch_shadow.py).
- Native status reader: [codex_quota.py](../../scripts/codex_quota.py).
- Campaign: `/Users/cam/.local/state/conductor/model-watch-shadow-20261024/`.
- LaunchAgent: `/Users/cam/Library/LaunchAgents/com.copperdogma.conductor.model-watch-shadow.plist`.
- Install evidence: [Stage B receipt](evidence/stage-b-2026-10-23.json).

The campaign contains `campaign.json`, a hash-pinned four-file `runtime/`,
`days.json` durable reservations, `last-tick.json`, up to 256 immutable `ticks/`
receipts, launchd logs and the collector's bounded `collector/` evidence. Runtime
copies prevent active checkout changes and launchd Documents-access restrictions
from changing the experiment. Stop/rebuild explicitly to adopt changed source.
The default collector source configuration and its 448 MiB state ceiling apply.

**Admission:** before any catalog GET, use `codex app-server` only for initialize
and `account/rateLimits/read`. It reads native account status; it starts no chat,
turn or inference and does not read/copy auth files. The reader bounds elapsed
time and response bytes, terminates/reaps the child, and saves only sanitized
remaining percentages. Any reported 300-minute or 10080-minute core window below
20% blocks collection. Exactly 20% permits it. Missing/null optional slots are not fabricated;
a valid weekly-only response suffices. Malformed/unavailable status, a denied
ordinary-usage flag or no assessable core window skips. Slots can rotate, so
duration identifies the window. No reset, paid-credit fallback or quota retry.

Reservations precede quota reads, including skips and interrupted attempts.
Repeated invocation on that date becomes `duplicate_day`; uncollected dates
remain missing evidence. Hash/timezone drift or damaged campaign state fails
closed and disables the job. Failures and skips
remain local and quiet. The existing daily AI scout's schedule/prompt is unchanged;
it still performs its ordinary independent discovery and catalog retrieval.
Stage C consumption and any quota policy for that AI automation require separate
integration work. No new AI job is created to inspect these receipts.

Inspect local status without quota or network access:

```bash
python3 scripts/model_watch_shadow.py status \
  --campaign /Users/cam/.local/state/conductor/model-watch-shadow-20261024
launchctl print gui/501/com.copperdogma.conductor.model-watch-shadow
```

Stop early (retain evidence):

```bash
launchctl disable gui/501/com.copperdogma.conductor.model-watch-shadow
launchctl bootout gui/501 /Users/cam/Library/LaunchAgents/com.copperdogma.conductor.model-watch-shadow.plist
```

Do not re-enable or kickstart after expiry to imply a natural tick. A manual
canary is installation evidence only; seven scheduled dates have not occurred at
installation. Review missing/skipped dates and compare fresh complete packets
with the normal reports before selecting integration. Token savings are still
unmeasured during this parallel shadow.

Focused offline checks:

```bash
python3 -m unittest tests.test_codex_quota tests.test_model_watch_shadow tests.test_model_watch_collect
```

Research: native status transport adapts the engineering-only AI Health quota
reader (source hash in installation evidence). The supported
[Codex app-server API](https://learn.chatgpt.com/docs/app-server) exposes
`account/rateLimits/read`. Apple's
[scheduled jobs guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html)
and [launchd.plist manual](https://github.com/apple-oss-distributions/launchd/blob/main/man/launchd.plist.5)
establish calendar arrays, sleep coalescing and RunAtLoad behavior. Actual
scheduled delivery, quota availability under launchd and comparison quality
remain to be observed; a manual transport check does not prove those outcomes.

Installation limitation: one repeated historical-replay test encountered an
`OSError`; the earlier combined run, a bounded four-replay diagnostic and the
same CLI test on rerun passed unchanged. The cause was not established. The host
had roughly 200 MiB free at the final check. No cleanup was performed. A write
failure cannot become a successful packet; inspect the attempt/launchd receipt
and preserve a failed or reserved date instead of automatically retrying it.

Cam approved the post-window review. A single-date follow-up named
`Review model-watch shadow` returns to this chat on October 31, 2026, at
09:00 America/Edmonton (the app may apply a few minutes of scheduling jitter).
It reviews existing local evidence and daily reports, records gaps and an
integration recommendation, then pauses itself. It adds no daily AI polling,
campaign extension or Stage C implementation. The saved nominal time was
verified through readback; the heartbeat rule uses UTC. Keep this Mac and the
app available for the local review. See the Stage B evidence's
`post_window_review` record for its identity and configuration hashes.

Close-out validation fixed conflicting ordinary-usage flags: an explicit denial
at either supported response location blocks work. The updated pinned runtime
passed a second manual launchd canary before the date window. All 81 focused kit,
package, collector, quota and shadow tests pass; see
[the close-out receipt](evidence/closeout-2026-10-23.json). The original 53-test
installation result and I/O limitation above remain historical evidence. The
schedule, quota threshold, existing AI scout and review time are unchanged.
