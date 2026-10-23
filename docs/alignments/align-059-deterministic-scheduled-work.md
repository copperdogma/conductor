# Alignment 059 — Optional deterministic scheduled-work reference

Date: 2026-10-23. Classification: **portable improvement**, with intentional
project-owned differences. Request: gather the best existing patterns into
Conductor so new projects can selectively copy/adapt them; consider Conductor
use too. This is canonical source preparation, not a multi-repo rollout.

## Source comparison and decision

[Scout 101](../scout/scout-101-deterministic-scheduled-work.md) contains the pinned
Bishop source and current Financial Monthly Analysis/AI Health engineering
evidence, strengths, limits and per-project relevance. No target repositories
were edited. No registry change, schedule creation, account action, live adapter,
commit or push is part of this work. Existing dirty Conductor changes were preserved.

Promoted meaning: deterministic mechanics before AI admission; exception monitor
and periodic synthesis are distinct; quiet invocations spend no model tokens
only when admission really precedes the model. Stable semantic fingerprints,
atomic state, conservative unknown-send handling, compact receipts and separate
completion/delivery evidence are reusable. Project-specific thresholds, account
access, clinical/financial authority and workflow dispositions stay local.

## Concrete source changes

- Optional `scheduled-work` module, absent from default product selection;
  preservation-safe package helper copies it to `tools/scheduled-work/`.
- One self-contained [kit/runbook](../../.agents/skills/setup-methodology/assets/scheduled-work/README.md)
  with Python collector/gate, synthetic config/input, launchd and systemd templates,
  setup/shadow procedure, adapter protocol, recovery and token accounting.
- Setup skill, kickoff/setup runbooks, product setup asset, source-library guide,
  checklist and README route projects here conditionally. No new always-loaded
  skill or general runtime dependency was added.
- Functional tests cover quiet operation, change/recovery/period identity,
  invalid/stale sources, pending state, locks, uncertain delivery and reconciliation.

The sample supports one outstanding request per job and pauses collection until
reconciled. It is a state monitor/periodic synthesis starter, not lossless intake
or a work-completion engine. No dispatch by default; unknown outcomes require
inspection before explicit retry. Existing runtimes can reuse the principles
without adopting this runner.

## Validation

Validation target: a new project can discover and selectively install a runnable
offline example that proves quiet-path behavior and recoverable dispatch, without
activating a timer, sending private data or making model calls.

Final-source checks on October 23 (Python 3.10+ stdlib, local macOS):

- `python3 -m unittest discover -s tests -p 'test_scheduled_work.py'`: 17 tests
  pass, including real subprocess/fake-adapter fault scenarios.
- `python3 -m unittest discover -s tests -p 'test_setup_package.py'`: 8 tests
  pass, including optional-only selection and an installed kit running from an
  unrelated working directory without relying on source-checkout paths.
- Source audit: all eight modules available, 105 source files; default product
  profile remains `core evidence`. The optional kit enables neither timer nor adapter.
- `make lint`, `make methodology-check`, `make skills-check`,
  `plutil -lint .../job.example.plist`, and `git diff --check`: pass. New local
  source links resolve; Linux unit files parse structurally, not runtime-tested
  on Linux. No planning-state source changed, so no graph regeneration needed.
- Disposable offline kit exercise: quiet → unchanged → threshold accepted →
  same severity unchanged → recovery accepted → recurrence accepted; periodic
  report accepted → same period unchanged → new period accepted. Five local fake
  acceptances; zero model/network calls or live schedules. Temporary copies removed.

Independent bounded review reproduced a stale-clock dispatch and an incorrect
`dispatch_attempted=false` receipt after post-dispatch persistence failure.
Both were repaired and regressions pass: freshness uses the post-collection and
pre-dispatch clock; attempt/event evidence survives receipt/state failures while
the durable reservation remains uncertain. Malformed persisted timestamps also
fail compactly. Main review removed transport commands/timing from semantic
identity so adapter installation does not retrigger the same condition; explicit
policy-version changes can request new review. Prepared observations cannot
silently expire into a send.

Skill-creator's `quick_validate.py` could not run with system Python (missing
PyYAML); isolated `uv run --with pyyaml` ran it and rejected the pre-existing
`user-invocable` frontmatter key, which is used throughout this repo. That
compatibility limit was preserved rather than rewriting unrelated metadata.
The repo's own skill-surface check passes. No generic product suite or paid
evaluation was needed; evidence is scoped to this tooling and setup consumption.

### Strategy checkpoint

One-off `/loop-review`: **continue to this bounded handoff, then stop**. The
actual consumer is a new project's setup agent: disposable installation and
offline execution now demonstrate that connected handoff. The established
alternative is reusing a project's existing collector/scheduler with only the
guide; that remains the preferred route for mature projects. A tiny optional
starter is justified for projects without those mechanics and is cheaper than
an always-running AI orchestration loop. Reuse the Apple/systemd/idempotency
source comparison from Scout101; no new uncertain mechanism needs research.
Finish verified reference material; defer live pilots, task-engine generalization
and downstream rollout. No extra framework, schedule or acceptance gates added.
Independent reviewer used inherited parent configuration; served identity and
review token attribution were not independently available.

## Practical effect and possible next step

Projects can reuse tested mechanics and avoid spending an AI turn to perform
routine collection or ask whether anything changed. Conductor can apply the same
pattern to prefetch/dedup source facts for daily model scouting, retaining AI for
semantic research and adoption decisions. A single shadow pilot with measured
output equivalence and token use is the next optional step; it is not enabled here.

## Pilot planning follow-through — October 23

Cam approved preparing a Conductor daily-model-scout pilot plan. The
[concrete plan](../model-watch/deterministic-pilot-plan.md) names a two-feed
offline collector/replay stage, a later finite seven-day scheduled shadow and
optional integration into the existing scout. Current automation configuration,
sample/full historical snapshot differences and public GET feasibility were
inspected without changing the live job. Broad announcement discovery remains
AI-owned; unchanged catalogs cannot gate the entire scout. No implementation,
schedule change or token-savings result is claimed. Next proposed approval is
only the offline collector/config/focused tests and one bounded public collection.

Planning validation: `make lint`, `make methodology-check`, `git diff --check`
and local link/anchor checks pass. Live automation TOML hash still matches the
inspected baseline; evaluated-ledger hash matches the October 23 daily receipt.
Proposed implementation files remain absent. A bounded independent review found
no material plan gaps. No code tests were rerun for this documentation-only step;
the reusable kit's previous focused test evidence remains applicable to its
unchanged implementation, not to the unbuilt pilot.

## Stage A implementation — October 23

Cam approved the offline collector/replay stage. The
[collector runbook](../model-watch/collector-runbook.md) and
[execution evidence](../model-watch/evidence/stage-a-2026-10-23.json) now record
24 focused passing tests, complete/sample replay and exactly one public
collection (two GETs, 468/30 rows, 2,990-byte packet). Independent review's four
demonstrated reliability gaps were fixed with regressions; tested code hashes
match the retained artifacts. Repo lint/graph/diff checks pass. Source history,
evaluation/candidate/scorecard/playbook and automation hashes are unchanged.

Conductor can now perform this catalog preparation without a model. The daily
AI scout still owns broad discovery, creator verification and recommendations;
no live integration, schedule, commit or push was performed. Actual token savings
and seven-day natural delivery remain unmeasured. Metadata churn, especially
benchmark changes, is visible rather than misclassified as new releases.

## Stage B installation — October 23

Cam selected the finite seven-day shadow and required a deterministic quota
floor. Installed the script-only launchd campaign for October 24–30 at 07:45
America/Edmonton, before the existing scout's 08:00 nominal/07:57:11 current
jittered next start. No new AI automation. The native account-status endpoint
is read before collection: any reported five-hour/weekly window below 20%
remaining blocks, exactly 20% permits, and unavailable/malformed quota skips.
A valid weekly-only response is assessed without inventing another window.

The wrapper copies four pinned runtime files outside Documents/Git, checks
their hashes and host timezone, reserves each date before quota/network work,
and disables on final date/expiry or broken campaign state. No backfill,
automatic retry or extension. launchd has no calendar-year key, so a full-date
runtime guard prevents later annual triggers from collecting even if disable
fails. Evidence is retained rather than deleted.

[Stage B evidence](../model-watch/evidence/stage-b-2026-10-23.json) records
installation, 53 focused offline tests, native quota preflight, plist/launchd
readback and unchanged protected hashes. Startup ran once from the installed
runtime, exited 0 and recorded `outside_window` on October 23 with no collector
state, day reservation, catalog GET or model call. This is a startup canary,
not a natural scheduled collection. Independent review prompted a regression
for damaged/missing campaign state disabling the known job.
One repeated historical replay had an I/O error and then passed unchanged;
the runbook/evidence retain that limitation and the observed low disk space.

Conductor now prepares future shadow packets without an AI orchestration turn
and avoids work below Cam's quota floor. Existing daily AI scouting remains
unchanged; it still fetches independently during the comparison period. Seven
natural dates, launchd quota access, packet/report comparison and measured token
savings remain unproven. Review after October 30 before selecting Stage C;
do not silently extend a missing/skipped sample. No commit or push.

### Post-window review follow-up

Cam approved the recommended review. Created the single-date heartbeat
`review-model-watch-shadow` in this chat for October 31, 2026, at 09:00
America/Edmonton, with a finite expiry that excludes later dates. Readback
verified the nominal local time; heartbeat rules use UTC. The prompt reviews
the seven dates, quota admission, failures, packet/report agreement and actual
metrics, records a recommendation, and then pauses. No recurring daily AI
checks, collection restart, Stage C integration, commit or push is authorized.
Existing daily scout configuration still matches its protected hash. At setup
the shadow remains loaded with only its successful October 23 startup canary;
natural collection and the review are still future work.

## Scoped close-out — October 23

Cam explicitly requested validation, fixes, check-in and push. Prepared the
candidate in an isolated worktree from current remote main, preserving the stale
shared checkout and its unrelated changes. Only this reference/pilot, necessary
public replay fixtures and its setup/index/inbox hunks are included. Existing
remote methodology, model-watch ledgers and other campaign records are retained.

All 81 focused tests pass: 17 kit, 8 package/installation, 24 collector, 21 quota
and 11 shadow. Package audit, lint, methodology/skill checks, plist checks,
changed-document links and diff checks pass. No generic product suite or paid
evaluation was needed. The earlier replay I/O error was not reproduced with
the current candidate; its historical limitation remains recorded. Public
replay fixtures are included unchanged so a clean checkout can run the tests.

Independent review found that a top-level `ordinaryUsageAllowed=true` could
override a selected bucket's explicit false. Both supported locations are now
validated independently; either false blocks. Three additional tests cover
conflicting flags, optional null and malformed bucket flags. Updated the pinned
runtime under its campaign lock, retaining the previous code/manifest locally.
A second launchd invocation verified the updated runtime exits cleanly before
the date window, with no quota read, reservation, catalog fetch or model call.
Both launchd invocations are manual/startup canaries; natural collection remains
unobserved. Dates, 20% floor, schedule, AI scout and October 31 review are unchanged.

[Close-out evidence](../model-watch/evidence/closeout-2026-10-23.json) binds the
checks to file identities and the remote integration base. Exact pushed commit
and remote verification belong to the final handoff. The isolated worktree is
retained; no cleanup of other worktrees or user files was performed.
