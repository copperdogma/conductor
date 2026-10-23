# Scout 101 — Deterministic scheduled work before AI

Date: 2026-10-23. Decision: **Adapt into Conductor's optional setup library**.
Scope: infrastructure inspection and source preparation, not live scheduler
changes or a cross-project rollout. User request is the authority for this work.

## Finding and decision

The useful general pattern is scheduler → deterministic collection/validation →
durable evidence → code-based admission → bounded judgment or synthesis.
Collection-only needs no model; monitoring wakes one only for meaningful work;
a periodic report can still invoke AI every period after mechanics are complete.
Success-message suppression alone does not avoid inference if an AI turn already
launched the script.

Adopt source-specific collectors, stable IDs/cursors, atomic state, minimized
bundles, explicit thresholds, reservation/dedup and actual scheduler evidence.
Adapt those into a new domain-free sample, rather than copying live private
scripts/configuration. Keep source review, dispatch acceptance, task completion
and user notification as distinct states. Keep domain authority local.

Canonical resource: [scheduled-work kit](../../.agents/skills/setup-methodology/assets/scheduled-work/README.md).
Package integration and validation: [Alignment 059](../alignments/align-059-deterministic-scheduled-work.md).
Private source references below are engineering pointers, not included in the
portable module. No patient records, financial transactions, account IDs,
credentials, personal prompts or live scheduler definitions were copied.

## Sources and evidence strength

### Bishop

GitHub connector read of [copperdogma/openclaw-bishop](https://github.com/copperdogma/openclaw-bishop),
default `master`, pinned inspected commit
`ddeb060a05198c5613a207d0b22d1e3eb450929a` (commit date July 27, 2026).
Repository pushed-at metadata is later; it does not establish changed source or
current live deployment. Repo is private and has no license metadata. This pass
inspected engineering code/docs via the authorized connection, not the live host.

- [gather_morning_reports.sh](https://github.com/copperdogma/openclaw-bishop/blob/ddeb060a05198c5613a207d0b22d1e3eb450929a/scripts/caretaker/gather_morning_reports.sh)
  builds a bundle from local artifacts and delivery-ledger pointers for later
  synthesis. Portable: gathering and summary preparation in code. Caution:
  existence of a `latest` file is not freshness, completeness or delivery proof.
- [healthcheck.sh](https://github.com/copperdogma/openclaw-bishop/blob/ddeb060a05198c5613a207d0b22d1e3eb450929a/scripts/caretaker/healthcheck.sh#L1099)
  supports dry-run/alert-only delivery. Portable: write evidence every time,
  suppress routine success delivery. Its health thresholds/account access and
  auto-remediation permissions remain local; alert-only delivery is not proof
  that a model wasn't invoked upstream.
- [report_meta_monitor.py](https://github.com/copperdogma/openclaw-bishop/blob/ddeb060a05198c5613a207d0b22d1e3eb450929a/scripts/report_meta_monitor.py)
  emits deterministic OK/WARN/FAIL findings, report artifacts and a ledger.
  It also has legacy assumptions/fallbacks. Do not promote cron-success as proof
  of actual email receipt or treat stale historical exceptions as permanent policy.
- [durable-automation story](https://github.com/copperdogma/openclaw-bishop/blob/ddeb060a05198c5613a207d0b22d1e3eb450929a/stories/20260403-story-redesign-top-risk-cron-jobs-for-durable-automation.md)
  documents moving mechanics out of large prompts, bounded tool permissions and
  lighter context. Some recorded wrappers still used `small` AI turns to run a
  script. The historical `run_morning_supervisor.sh` named there is absent from
  the inspected tree; do not claim that specific wrapper is currently available.
- [SQLite migration incident](https://github.com/copperdogma/openclaw-bishop/blob/ddeb060a05198c5613a207d0b22d1e3eb450929a/stories/20260610-story-fix-cron-watchdog-sqlite-run-detection.md)
  records false missing-run alarms after scheduler storage changed. Current
  [watchdog](https://github.com/copperdogma/openclaw-bishop/blob/ddeb060a05198c5613a207d0b22d1e3eb450929a/scripts/caretaker/cron_watchdog_force_morning_reports.sh#L45)
  checks SQLite then legacy JSONL. Portable lesson: version/read the authoritative
  run source and test migration. Do not copy hardcoded host/job IDs, forced reruns,
  direct store edits, or messaging/remediation as setup defaults.

Confidence: high in inspected code/recorded architecture; current scheduler
installation and end-to-end token savings were not checked on Bishop's host.

### Financial Monthly Analysis

Read-only checkout: `/Users/cam/Documents/Projects/financial-monthly-analysis`,
HEAD `da0462921d14855d72064dfc67fc6ccb9602db56`, divergent `main` with substantial
local changes. Relevant owner-refresh/collector code inspected was clean;
some runbooks are locally modified. Findings include those working-copy docs.
No source financial records were read; no collectors or finance tests were run.

- [TD refresh runbook](/Users/cam/Documents/Projects/financial-monthly-analysis/docs/runbooks/td-refresh.md:41)
  and [td_refresh.py](/Users/cam/Documents/Projects/financial-monthly-analysis/src/sure_assist/td_refresh.py:302):
  sealed inputs, digest-derived run IDs, strict account binding, overlap checks,
  staged/atomic writes, integrity-checked rollback and repeat-build rehearsal.
  This is owner-assisted acquisition, not unattended bank access.
- [insights.py](/Users/cam/Documents/Projects/financial-monthly-analysis/src/sure_assist/insights.py:194):
  deterministic relative-plus-absolute thresholds against prior-period medians.
  Promote the threshold shape, not financial constants.
- [owner_refresh.py](/Users/cam/Documents/Projects/financial-monthly-analysis/src/sure_assist/owner_refresh.py:385):
  deterministic aggregation and minimization precede AI; bind review reuse to
  the summary and current authoritative-state digest, reserve before outbound
  dispatch, and fail closed on previously reserved unknown outcomes.
  [Tests](/Users/cam/Documents/Projects/financial-monthly-analysis/tests/sure_assist/test_owner_refresh.py:405)
  cover unknown outcomes not silently repeating; inspected, not rerun here.
- [Runtime runbook](/Users/cam/Documents/Projects/financial-monthly-analysis/docs/runbooks/sure-candidate-runtime.md:185):
  network-free page rendering, explicit owner refresh, bounded outbound work.
  [Monthly report runbook](/Users/cam/Documents/Projects/financial-monthly-analysis/docs/runbooks/monthly-report.md:155)
  preserves source/hash/version and semantic-review gates before publication.

Important limit: no maintained scheduler definition was found in repo inventory;
this is a collection/synthesis exemplar, not a demonstrated scheduled monitor.
A new current-state digest can still trigger AI review with no anomalies. That
is valid for requested synthesis, but does not implement exception-only admission.
Financial Hub owns end-user analysis/reporting; reuse preparation mechanics
without moving that product authority back into the acquisition project.

### AI Health

Read-only checkout: `/Users/cam/Documents/Medical/Cam/AI Health`, HEAD
`a9cc0584a61742fc5bad75acd98668320e4e88d3`, with substantial local changes.
Engineering source/evidence only; no clinical/family records or credentials.
No collectors or accounts mutated. A read-only engineering audit was run.

- [healthbot_gmail_runner.py](</Users/cam/Documents/Medical/Cam/AI Health/scripts/healthbot_gmail_runner.py:28>)
  and its maintained launchd definition run deterministic collection without a
  shell/model wake. Source capture/attachment verification precedes external
  message mutation in [healthbot_intake.py](</Users/cam/Documents/Medical/Cam/AI Health/scripts/healthbot_intake.py:399>).
  Promote stable IDs, resumable phases, atomic capture and verified acknowledgement;
  preserve owner-specific access and source permissions.
- [stewardship_preflight.py](</Users/cam/Documents/Medical/Cam/AI Health/scripts/stewardship_preflight.py:235>)
  emits WORK/WAIT plus a bounded packet, joining actual ready tasks, due dates
  and source changes. Full relevant-content fingerprints prevent nested changes
  being hidden. Unchanged ready tasks remain WORK; waiting/done dispositions need
  evidence and reopen on relevant change/due date. This is richer than the starter's
  state-change monitor and should remain project-owned until needed elsewhere.
- [stewardship_prompt_gate.py](</Users/cam/Documents/Medical/Cam/AI Health/scripts/stewardship_prompt_gate.py:44>)
  identifies exact scheduled prompt/session/cwd before doing quota/source work.
  WORK enriches the existing turn; WAIT blocks model admission. Unrelated/direct
  requests pass through. Preflight errors fall back to the original investigation
  prompt: this preserves operational visibility but is not a hard spending cap.
- [check_sources.py](</Users/cam/Documents/Medical/Cam/AI Health/scripts/check_sources.py:149>)
  caches file signatures/hashes with periodic full verification; observed and
  reviewed baselines remain separate. Inaccessible/partial scans are unavailable,
  never unchanged. Signature cache assumptions must remain explicit.
- [Day-one natural-run evidence](</Users/cam/Documents/Medical/Cam/AI Health/analysis/stewardship-gate-validation/2026-10-23.md:7>)
  supersedes the earlier `no_live_hook_evidence` finding: 17 native receipts
  correlated to actual turns; 11 WAITs had zero assistant/tool items, six WORKs
  reached the thread, with one upstream capacity failure later recovered.
  Seven-day proof continues through October 29. This demonstrates quiet-path
  admission, not measured aggregate token savings or natural low-quota blocking.
- Fresh read-only `python3 -B scripts/stewardship_gate_audit.py` returned PASS
  on October 23: installed-hook/config checks true; 18 native-form events in
  the audit's rolling window. This later snapshot is distinct from the 17-turn
  correlated sample. `launchctl print` also reported healthbot 104 runs, hourly
  interval, last exit 0; configured state/readback alone cannot prove output quality.

The October 23 evidence also caught a real schedule-timezone mismatch. Carry
explicit time windows and verify actual ticks; schedule readback is not delivery.
Port mechanics without patient content, clinical thresholds, private prompts,
hardcoded paths, or assumptions about a particular hook/app version.

## Bounded primary-source research

Problem class: reliable scheduled admission, duplicate delivery, missed ticks
and crash/unknown-outcome recovery. Standard schedulers and idempotency tokens
fit; a bespoke always-running agent loop adds little value here.

- [Apple timed jobs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html):
  launchd calendar scheduling and sleep/off distinctions; local host man page and
  actual tick remain the applicability test.
- [systemd timers](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html):
  calendar activation, persistence and jitter. Persistent catch-up is not replay
  of every missed interval; OS/user manager availability still matters.
- [AWS idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/):
  caller intent tokens and receiver cooperation for safe retries. The starter
  keeps an unknown send uncertain instead of claiming exactly-once execution.

Decision: use standard OS timer examples plus a small POSIX Python collector/gate;
leave live transports project-owned. Offline tests/disposable installation prove
the generic mechanics; no natural Conductor schedule is claimed.

## Portfolio relevance and next routes

| Owner | Decision and concrete next route |
| --- | --- |
| Conductor | Adapt now as optional setup reference (this work). Candidate later: one shadow deterministic prefetch/change bundle for daily model scouting, compared with current output and cost. |
| Financial Monthly Analysis | Keep source acquisition and explicit synthesis local. Future selected work could add deterministic cadence/admission without unattended bank authorization or taking Financial Hub's analysis role. |
| AI Health (user-named source; not enrolled in registry) | Keep richer dispositions/hooks local. Continue its existing seven-day validation; no extra schedule/rewrite needed from this scout. |
| Financial Hub | Defer adoption until a concrete recurring report/monitor is chosen; it owns end-user finance analysis/reporting. |
| Dossier, Storybook, Doc Web, CineForge | Optional reference for future ingestion/maintenance jobs; runtime admission semantics not audited here. No immediate rollout recommendation. |
| Board Game Ingester, Robo Rally, Echo Forge, Ultima IV Web, VLC Thumbs | Defer until a recurring operational need appears; batch determinism alone does not require a timer. No runtime inspected in this pass. |

This is source-library preparation, not rollout target selection. Registry
membership is unchanged. An actual cross-project rollout would first run the
managed-project check and use dedicated owner worktrees/stories.

Remaining uncertainty: project-specific dispatch adapters, current Bishop
deployment, long-term AI Health hook reliability, representative token/cost
baselines, and which Conductor routine warrants a first live pilot. No token
percentage, unattended source access, deployed scheduler or downstream adoption
is claimed by this package.
