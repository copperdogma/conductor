# Deterministic scheduled work

Use a normal executable for recurring mechanics. Invoke AI after collection,
validation and a decision made in code. This optional starter is for projects
that actually have recurring work; copying it does not install a schedule.
Python 3.10+, macOS/Linux, standard library only. The sample is newly written
from the reviewed patterns; it contains synthetic inputs and no account wiring.

## Choose the work shape

| Shape | Deterministic phase | AI phase |
| --- | --- | --- |
| Collection only | Fetch, normalize, reconcile, persist, advance verified cursor | None |
| Exception monitor | Collect, check freshness, compare stable signals and thresholds | Only on meaningful new/escalated conditions, or configured recovery |
| Periodic synthesis | Collect and validate an immutable period bundle, compute totals/deltas | One bounded synthesis per period/revision, even without anomalies |
| Work queue | Collect stable item IDs and full relevant content; track ready/waiting/done separately | While actionable work remains; dispatch receipt never completes the task |

The bundled runner implements **state-change monitoring** and **period/revision
synthesis admission**. It is not a durable task engine or lossless event-stream
consumer. A task that remains ready must not disappear merely because its hash
was sent once. Use project-owned dispositions/cursors for those shapes.

```text
OS timer → bounded collector → validated durable snapshot → deterministic gate
                                                        ├─ quiet → receipt only
                                                        └─ ready → durable request
                                                                  → explicit adapter → AI
```

Scheduling an AI chat and asking it to run the gate still spends invocation and
context tokens on quiet checks. Put the script before model admission. An
existing runtime hook can also gate admission, but prove that the real scheduled
delivery path hits it. A hook that falls back to AI on errors is an efficiency
optimization, not an enforced spending cap.

## Smallest useful setup

1. Inventory recurring work: cadence, source, deterministic operations, judgment
   needed, acceptable delay, privacy boundary, and owner of the final output.
2. Prefer an existing maintained collector over a new framework. Keep account
   access, thresholds, workflow authority, and provider choice in the project.
3. Choose collection-only, monitor, synthesis, or queue behavior explicitly.
4. Define source identity, cursor, time window/timezone, stable signal, freshness,
   and what constitutes new work. Use full relevant content when changes matter.
5. Run offline fault cases, then shadow the collector/gate without a dispatcher.
6. Wire the selected scheduler to the executable. Add an adapter only when the
   destination, data, spending limit, and permitted side effects are established.
7. Observe natural ticks, including quiet and actionable cases. Keep installation,
   manual execution, natural dispatch, AI completion, and notification delivery
   as separate evidence.

## Offline quick start

Copy this directory to a project's `tools/scheduled-work/` or select the optional
`scheduled-work` setup module. Work in a disposable copy for the demo. From the
copied directory:

```bash
python3 scheduled_job.py run --config job.example.json --state-dir .state/demo
```

The default input is below threshold: `decision=quiet`, then `unchanged`.
Change `sample-input.json` to `{"unresolved_count": 3, "period": "2026-10"}`
and run again. The result is `pending_adapter`; the durable request is in
`.state/demo/state.json`. Repeating cannot send anything: no dispatcher is set.

For a fully local fake acceptance adapter create `accept_local.py`:

```python
import json, sys
from pathlib import Path
request = json.load(sys.stdin)
Path("accepted-event.txt").write_text(request["event_id"] + "\n")
```

Copy `job.example.json` to `job.local.json` and set its `dispatcher` to
`["python3", "accept_local.py"]`. Use that config on subsequent runs. One
prepared event is accepted; a repeat is unchanged. Changing input to 0 yields
one recovery request. Changing back to 3 yields a new incident ID. This demo
does not call AI or contact a service. Delete only the disposable demo directory
when finished; production state is not disposable.

For synthesis, set `mode` to `report`. The collector must emit an explicit
`period`, such as `2026-10` or `2026-10-23@America/Edmonton`. A new period is
admitted even when its signal is identical. Changed signals in the same period
are a new revision; projects that permit only one publication per period must
add their own publication ledger. Never infer the report period from file mtime.

## Collector and adapter contracts

Commands are argv arrays, executed with no shell, relative to the config file's
directory. Use absolute interpreter/executable paths for production. The runner
locks before collection, invokes each command once with a timeout, and suppresses
child stdout/stderr from operational receipts. The collector emits one JSON
object to stdout, at most 16 KB:

```json
{
  "observed_at": "2026-10-23T12:00:00+00:00",
  "status": "attention",
  "signal": {"threshold_exceeded": true},
  "summary": "Minimized explanation of a meaningful condition.",
  "period": "2026-10"
}
```

`status` is `ok` or `attention`; errors must exit nonzero, never emit `ok`.
`observed_at` is when the source was actually checked, not when a stale cache was
rewritten. The source must be no older than `max_age_seconds` or over 60 seconds
in the future. Summary is capped at 2,000 characters. `signal` contains only
semantic fields worth another AI request; observation time and summary prose
are excluded from the fingerprint. The example deliberately bins queue counts
at a threshold, so 3→4 does not produce another alert. For escalation, use stable
severity bands and hysteresis (different enter/clear thresholds), and persist
debounce counters across ticks. IDs/content belong in signals if their changes
require action. A deterministic summary can still be privacy-sensitive.

Bump the config's `policy_version` when collector/threshold semantics change and
need fresh review. The key includes job, mode, policy version, status, signal and
report period. Dispatcher commands and timing settings are excluded: installing
an adapter or rotating its executable must not re-notify the same condition.

Include cursor/window, source freshness, omitted counts, evidence references,
policy/collector version and source digest where they affect judgment. Large
evidence stays in project-controlled storage. Review what the adapter may send;
do not send a whole database, raw inbox, account config or secret to a model.

A dispatcher reads the request JSON on stdin. It must return 0 **only after
durable acceptance by the intended destination**. This means queued, not task
completed, reviewed, emailed or published. It must retain the supplied `event_id`
as an idempotency key. Before real use add a project-owned adapter with an exact
destination, minimized context, bounded model/tool budget and explicit authority.
No live thread/model transport is bundled. Prefer a durable local queue as the
acceptance boundary; separately track downstream completion/failure.

Add a deterministic quota/budget admission check when a project needs one. Read
account status without starting an AI turn; check every reported relevant window
before the guarded work, with a short timeout. For a 20% remaining floor, `<20`
skips and exactly 20 permits. Validate finite percentages, identify windows by
their documented duration/identity, and never treat an unavailable reading as
zero usage or unlimited capacity. Save only the decision and needed percentages,
not account identifiers or raw status. A quota skip should stay quiet and follow
an explicit retry/reservation policy. This starter does not bundle an account
transport; the owning project must choose the endpoint and guarded scope.

Before invocation the runner stores `uncertain` atomically. Nonzero exit,
timeout, or crash remains uncertain and is never automatically dispatched again.
A crash before the actual send can therefore require reconciliation too. This
conservative choice avoids an unknown billable outcome silently repeating.
If a destination supports idempotent delivery, the project can add bounded
backoff/jitter after demonstrating that contract. A hash alone cannot provide
exactly-once remote execution; the receiver must cooperate. See [AWS's primary
reference on idempotent requests](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).

## State and recovery runbook

Use a private ignored state directory **per job**, outside versioned source and
shared worktree output. State uses an OS lock and atomic replace with file and
directory fsync. New state files are owner-only; tighten existing directory
permissions yourself. Store secrets through the project's existing mechanism.
The example's `.gitignore` covers only the bundled `.state/`; ignore/protect any
other chosen location explicitly. Never store credentials in argv or receipts.

| Observation | Action |
| --- | --- |
| `quiet` / `unchanged` | Zero dispatcher calls. Inspect compact receipt if needed. |
| `pending_adapter` | Request persisted, no dispatch. Intentional in shadow mode; alert if production expected a consumer. |
| `accepted` | Verify destination accepted the event; downstream completion is a separate check. |
| `delivery_uncertain` | Inspect destination by event ID before any retry. |
| `error` / `configuration_or_state_error` | Repair freshness, input, collector or state; never classify this as quiet. |
| `overlap` | Another invocation holds the lock. Repeated overlap or stale completion needs operator attention. |

Receipts are `latest.json` plus `ledger.jsonl`; the authoritative pending request
and last accepted signal are in `state.json`. Exit 2 is an operational failure;
exit 0 also includes intentional shadow waiting and lock overlap. An independent
non-AI watchdog should monitor receipt age, failure codes, outstanding-request
age, disk/credential problems and expected AI completion. The same stopped timer
cannot reliably report its own absence. Source success, run success, admission,
dispatch acceptance, model completion and notification delivery are different.

After evidence-based reconciliation, use the **current exact event ID**:

```bash
# Destination proves it already accepted the event:
python3 scheduled_job.py ack --config job.local.json --state-dir /private/job-state --event-id EVENT_ID
# Destination proves it did not accept it, or its idempotency contract makes replay safe:
python3 scheduled_job.py retry --config job.local.json --state-dir /private/job-state --event-id EVENT_ID
# Explicitly abandon a stale/superseded request without advancing the accepted baseline:
python3 scheduled_job.py discard --config job.local.json --state-dir /private/job-state --event-id EVENT_ID
```

`retry` only makes the saved request eligible on the next run; it does not send.
Prepared observations are freshness-checked before dispatch. `discard` allows a
fresh collection next time. Keep the reconciliation evidence in the owning
project. Never use `ack` just to clear an error or imply completed review.

This starter permits one outstanding request and pauses collection until it is
resolved. It coalesces state changes between accepted snapshots. If collection
must continue, or every inbox event matters, use a separate durable collector
and transactional outbox/SQLite queue with item IDs, cursors, bounded retention
and explicit dispositions. Do not turn this single-snapshot demo into a claim
of lossless intake. Do not reset state to force a report: it can repeat calls.

## Scheduler templates

Only one scheduler should own each job. Replace every `/ABSOLUTE/` placeholder,
create private log/state directories, use the project's maintained environment,
and validate syntax before installation. The templates never install themselves.
Do not edit the live scheduler's database as a generic setup technique.

| Host | Example | Semantics to verify on the actual host |
| --- | --- | --- |
| macOS | `job.example.plist` | Calendar minute 10 each hour, local system timezone. Logged-in LaunchAgent; absolute paths. No `KeepAlive` retry loop. |
| Linux | `job.example.service` + `.timer` | Hourly local time, up to 60s jitter, bounded service; user service needs an active user manager. |
| Existing orchestrator | Call the executable directly | Verify it does not instantiate an AI turn before running the command. |

macOS: lint the customized file with `plutil -lint path.plist`, then explicitly
install/manage it using the owning project's launchd runbook. Inspect
`launchctl print gui/$(id -u)/LABEL` and actual receipts. Calendar jobs missed
during sleep can run on wake; powered-off time has different behavior. Verify
the host's current man page and actual tick. [Apple's scheduling documentation](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html)
explains those distinctions.

Linux: validate customized units with `systemd-analyze verify`, install under
the appropriate user/system manager, and inspect `systemctl --user list-timers`
plus `journalctl --user -u NAME.service`. `Persistent=true` catches a missed
calendar activation; it does not replay every missed interval. Jitter spreads
load. [systemd's timer reference](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
defines these options. Choose owner permissions and lifecycle before enabling.

Neither sample embeds timezone conversion: calendar schedules use the host's
timezone. The collector must calculate report windows in an explicit zone and
test DST/clock changes. Confirm interpreter PATH under the actual timer, sleep,
reboot/logout, source outage, token expiry, lock contention and missed ticks.

## Best practices to carry forward

- **Finish mechanics before AI:** pagination, caching/conditional HTTP requests,
  stable IDs, dedup, normalization, exact arithmetic, reconciliation, source
  completeness, schema checks and report aggregation belong in code.
- **Keep source and review state separate:** observing a change, collecting it,
  sending it, reviewing it and resolving it are separate transitions. Capture
  and verify durable evidence before mutating a source mailbox or cursor.
- **Fail visibly:** unavailable, partial, stale and malformed are not unchanged.
  Decide locally whether an error should alert a human, enqueue AI diagnosis,
  or stop. The starter fails without invoking AI.
- **Bound the work:** time, pages, bytes, retry count, payload, tool permissions,
  inference attempts and spend. Collector subprocesses must bound their own
  output and avoid background children; production supervisor must reap process
  groups. This simple runner bounds memory reads, not temporary-file disk growth.
- **Separate delivery policy:** one notification owner, stable incident/period
  identity, dedup, recovery/escalation rules and cooldown. Repeated errors can
  be quiet to the user only while still recorded and covered by escalation.
- **Keep source/config stable:** runtime state, cursors, audit logs, generated
  reports and credentials stay separate from reviewed job definitions.
- **Use existing schedulers and storage:** a shell script or Python command is
  enough for many jobs. Add a queue/database only when the real failure or
  concurrency contract warrants it. Avoid installing a model to launch a script.

## Verification and token accounting

Before live enablement, exercise unchanged/threshold/escalation/recovery,
same-content next-period reports, stale/partial/invalid sources, duplicate IDs,
collector failure, overlap, corrupt state, restart, unknown delivery and late
acknowledgement. Test actual dispatch with a local fake before a real adapter.
Then inspect natural scheduler evidence; a manual canary is not a natural tick.

Track scheduled ticks, quiet ticks, gate errors, prepared requests, dispatch
attempts, accepted requests, completed AI runs, delivery success, input/output
tokens and monetary cost where available. Record collector/gate elapsed time
and bundle size. Compare against a measured representative baseline including
bootstrap/context overhead; don't turn a skipped-dispatch count into a fabricated
token-savings percentage. Report jobs may call AI every period yet save tokens
by doing collection and aggregation without a model.

For Conductor, daily model scouting could prefetch official source changes and
prepare a deduplicated candidate bundle; weekly project checks could emit only
changed actionable facts. Semantic release research and adoption judgment still
need AI. Start with one shadow job and compare usefulness/cost before migrating
any existing automation. Setup reference alone does not enable that adoption.
