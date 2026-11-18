# Seven-date model-watch shadow review — October 31, 2026

**Recommendation: fix and requalify before Stage C; do not integrate now.**
The finite campaign ended and launchd currently reports the job disabled and not
running. Five complete collection dates and two fail-closed quota skips account
for all seven dates. This does not meet the plan's seven usable natural-date
qualification. No extension, backfill, fresh catalog retrieval, AI scout change,
commit or push was performed for this review.

## Date accounting

All times are America/Edmonton. Near-slot receipts are consistent with natural
scheduled execution; trigger provenance is not persisted, so they cannot be
independently certified from a launchd event ID. Current launchd run count is not
a durable lifetime counter across reboots.

| October date | Recorded slot result | Weekly quota remaining | General / decisions | Packet bytes |
| --- | --- | --- | --- | --- |
| 24 | 07:45:28 quota unavailable; reserved, no collection | unavailable | — | — |
| 25 | 07:45:02 admission; complete collection | 100% | 467 / 30 | 2,972 |
| 26 | 07:45:33 quota unavailable; reserved, no collection | unavailable | — | — |
| 27 | 07:45:06 admission; complete collection | 55% | 463 / 29 | 2,964 |
| 28 | 07:45:04 admission; complete collection | 100% | 464 / 30 | 2,974 |
| 29 | 07:45:07 admission; complete collection | 78% | 457 / 32 | 3,018 |
| 30 | 07:45:06 admission; complete collection; disabled=true | 69% | 456 / 34 | 3,056 |

No date is absent, still reserved/in-progress, or recorded as a failed collection.
Additional October 26–28 late invocations recorded four `missed_window` receipts;
they did not retry the reserved date or replace its slot result. October 23 has
three outside-window invocations: the two documented startup/deployment canaries
and a later outside-window invocation with no recorded trigger identity. Keep all
three separate from scheduled collection evidence. October 31 at 00:05 recorded
`expired` and `disabled=true`. Current disabled readback independently confirms
expiry; no scheduler restart or alteration was needed.

## Quota and integrity

Each of the five run IDs has a preceding eligible quota receipt in the same tick,
with one reported weekly core window at least 55% remaining. Missing/null optional
slots were not fabricated. Both unavailable responses produced zero collection;
the durable reservation prevented same-date retries. There was no natural
below-20% or exactly-20% case. The current 21 quota and 11 shadow offline tests
pass, including below 20 blocking, exactly 20 admission, unknown-quota suppression,
conflicting usage flags, reservations and expiry. These use fake transports and
collectors, not new account reads or catalog requests.

Runtime hashes match the pinned manifest. All five snapshots report complete
coverage, canonical semantic hashes verify, full deltas recompute exactly against
the previous complete collector snapshot, packet/config identities agree, and
snapshot/delta/backlog references resolve. October 27 correctly compares with
October 25 after the skipped date; it must not be presented as a one-day delta.

## Comparison with the independent daily scout

For every complete date, both full exact-ID sets match that day's independently
saved scout catalogs. Decision rows also match completely. General rows differ
on 1 / 9 / 5 / 1 / 5 same-ID rows respectively, in pricing/cache pricing and some
completion-limit metadata. These observations were made at different times;
they do not prove parser loss or equivalence. The packet ages at the scout's
recorded report start are approximately 15.0 / 20.4 / 16.1 / 18.3 / 19.9 minutes.
Thus the proposed two-hour freshness fallback is not evidence that all prices
and limits remain current. A consumer must label observation time and refresh
volatile facts when they affect a recommendation.

Packets retain the newest 40 general slice with 416–427 explicitly omitted rows;
all 29–34 decision IDs fit. Full delta-detail omission counts are 0 / 208 / 307 / 184 /
147, with complete referenced deltas retained. Five backlog references remain;
none was automatically acknowledged or cleared by this review. Empty deltas
cannot stand in for completed semantic review.

Daily reports confirm broad discovery still matters: October 25 Clairic preview
and October 26 FLock came from native/source research; Clairic only appeared in
the saved router decision catalog on October 30. October 28 Liquid native-family
research goes beyond router IDs, October 29 Carbon remains a gated announcement,
and October 30 Joey still needs creator/owner verification. These are comparisons
to the saved reports, not new source checks or adoption verdicts. Authoritative
evaluation history and existing holds remain decisive. The two skipped dates
still had ordinary independent scout reports, so suppressing that scout on
collector failure or catalog stability would lose coverage.

## Cost, faults and next decision

Five runs made 10 public requests and retained 4,035,529 response bytes. Recorded
collector preparation totals 4,823ms (range 668–1,381ms), excluding final
serialization/fsync. Packets are 2,964–3,056 bytes. Collector model calls and
dispatches are zero. The AI scout continued its independent fetching throughout;
its reports label orchestration/retrieval unmetered. **Token savings are unmeasured.**

No scheduled collection I/O error is recorded and launchd stderr is empty. The
October 23 low-disk/replay I/O incident remains historical; no per-tick free-space
telemetry establishes disk conditions or causation during this campaign.
Two of seven quota checks were unavailable (28.6%). The wrapper discards the
reader's diagnostic reason, so timeout, access, protocol or account-response
failure cannot be distinguished retrospectively. Do not label either as low
quota or rerun it now to manufacture missing evidence.

A useful next bounded change is to preserve an allowlisted quota-unavailability
reason and phase timing, plus trigger provenance where available, while keeping
failure closed and account identifiers out of receipts. Then qualify the intended
consumer's timestamp/volatile-field refresh, missing-packet fallback, omitted
full-delta inspection and backlog contract before requesting another finite
shadow. This review authorizes none of that implementation or scheduling.
Retain the existing reusable kit and all evidence. Leave the campaign disabled.

[Machine-readable evidence and input hashes](evidence/shadow-review-2026-10-31.json)
record the comparisons and controls. The completed one-shot review follow-up is
removed after this report; no replacement monitoring loop is created.
