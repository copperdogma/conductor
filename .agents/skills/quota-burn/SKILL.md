---
name: quota-burn
description: Run a selected multi-project Codex quota round, screen for valuable work, monitor remaining quota, and drain at 20% through validation, commit, push, and an evidence-based summary.
---

# Quota burn

Spend expiring included quota on useful project outcomes. Success is validated,
landed work, not token consumption. Support `review`, `start`, `monitor`, and
`finish`; infer the mode from Cam's request. Canonical source lives here in
Conductor; do not roll this supervisor skill into product repos.

## Activation boundary

Creating, editing, discussing, or reviewing this skill does not enable a quota
round or authorize monitoring current project work. A request to run/burn quota
first prepares a suggested project list. Wait for Cam's `yes` or refined-list
approval before activating the round, creating its monitor, or messaging workers.
Enroll only the participants selected for that round; recent activity and inclusion in
a portfolio review do not enroll a chat. Until then, create no monitor and send
no start, stop, or closeout messages. A historical round record is not activation.

Once enabled, the coordinator owns watching quota for that round and telling
its participants to finish when any reported core window reaches 20% remaining.
Follow through on validation, scoped commit/push and the aggregate round summary.

## Review and select

Select on two separate questions: does Cam still want this project advanced,
and does it currently have useful work ready? Cam owns the first; evidence and
the project's triage own the second. Do not equate incomplete, large backlog,
old age, or recent activity with personal priority.

Maintain a lightweight eligible pool from Cam's explicit selections: eligible,
parked, or undecided. Keep it with quota-round records, separate from managed
project membership in `projects.yaml`. A project can remain managed while being
parked for quota rounds. When establishing the pool, present a compact inventory
for Cam to mark once; use recency and previous choices only as suggested defaults.
Do not silently enroll older/undecided projects. Remember exclusions within the
round records until Cam changes them; avoid repeating the full preference pass
on every run. This is portfolio configuration, not permission to start a round.

The published pool contains only the approved entries; unlisted projects default
to parked. Resolve `repo_directory` against the current app project inventory or
Cam's selected Projects root, then verify the actual local triage path. Keep
unnecessary private inventory, raw chat text and account identifiers out of public
configuration. Active-round participant IDs belong only to an authorized round.

On each request to run a round, read `docs/quota-burn/project-pool.json`, cheaply
screen the eligible pool and return a short
ranked slate with evidence of meaningful ready work and blockers. Reuse recent
round results; inspect only enough changed owner evidence to assess readiness.
Do not run thirty exhaustive audits or thirty triage loops just to select a few
projects. If a readiness judgment needs owner triage, use that project's actual
skill in read-only recommendation mode, without creating a loop goal. Keep
blocked/low-yield projects out until their recorded re-entry condition changes.
Show the proposed names and a short reason for each, plus important deferrals.
Explicitly invite `yes` to approve the displayed list or edits to refine it.
Eligibility is not round approval; a generic request to run the skill does not
skip this selection checkpoint. A `yes` approves only the most recently displayed
slate, with any explicit edits applied; ask only if those edits are ambiguous.
Cam can select the slate or override it; once the round starts, each owner's
triage goal chooses the actual work as described below.

Use existing project chats via `list_threads`/`read_thread`, then inspect the
owning backlog, current state, and relevant changes. Do not count delegates as
separate projects. Read-only local rollout history can fill gaps when chat tools
fail; record that fallback. Keep thread titles verbatim when naming chats.

For each candidate identify a concrete next outcome, evidence of need, readiness,
expected user benefit, dependencies, and a stopping point. Prefer known defects,
unfinished product milestones, and decision-bearing qualification over repeated
scanning, extra bookkeeping, or speculative hardening. A large backlog alone does
not prove immediate readiness. Rank as priority, bounded task, or standby, and
record what would change that rank. Stop a project when only human, external,
spend-approval, or excluded work remains. Never invent work to use quota.

Review the recent round separately from future readiness. Establish actual user
start/stop messages and local dates; separate prior work, burst implementation,
later closeout, and deployment. Verify claims against owner evidence/changes.
Do not infer quota efficiency from commit count, test count, generated lines, or
cached token totals. Report unavailable cost attribution honestly.

Once Cam approves the displayed slate or refined subset, proceed without another
launch confirmation. Reviewing a portfolio does not authorize resuming its chats.
Use existing owner chats; create new chats only when explicitly requested.

## Start a round

Require the activation above and record the actual start instruction and selected
participants. Do not treat a request to build this skill as that instruction.

Read fresh account quota first. Prefer `get_usage_limits`; use
`rateLimitsByLimitId.codex` when supplied, otherwise legacy `rateLimits`. Identify
core five-hour/weekly windows by duration (300/10080 minutes), not slot order.
Remaining is `100 - usedPercent`. Null or missing is unavailable, never zero.
Any reported core window at **20% remaining or lower** begins draining. The
existing `scripts/codex_quota.py` admission rule permits exactly 20%; this skill
intentionally stops there. `scripts/quota_burn_gate.py` implements this rule
without changing other scheduled jobs. Never consume resets or buy credits.

Create a durable round record under `docs/quota-burn/`, with unique round ID,
phase, start time/time zone, exact participant chat/host IDs and repo/worktree,
approved outcome and constraints, baseline commit and dirty-state ownership,
requested model/reasoning/speed, actual settings if observable, quota snapshots,
monitor ID, and delivery/closeout status. Keep `active-round.json` as the active
record; preserve completed records separately before replacing it. Exclude
private source material and credentials. Keep one writer per repo Git state.

Requested settings are **maximum-strength available model, maximum reasoning,
and Fast speed**. The current model/reasoning target is GPT-6 Astra with `ultra`.
Fast is required for quota-burn launches; do not launch on Standard or substitute
Ultrafast without Cam requesting it. Recheck available choices and verify the
actual speed for every selected chat before dispatching its loop goal. A prose
request to the worker does not configure speed, and selecting Astra/ultra does
not establish Fast.

Neither `create_thread` nor `send_message_to_thread` currently exposes a speed
argument. Use a supported per-chat control if available. If speed cannot be set
or observed through available tools, tell Cam before launch and wait for Cam to
set Fast and explicitly confirm it for that chat. Do not silently preserve an
unverified speed or start first and mention the limitation afterward. Keep the
model/reasoning/speed choices separate; reverify speed if a settings change can
reset it. Do not change global defaults or modify hidden application databases.
Record requested speed `fast`, observed/confirmed speed, and verification source
separately. Availability source: [official Speed documentation](https://learn.chatgpt.com/docs/agent-configuration/speed).

Send `gpt-6-astra` and thinking `ultra` with authorized worker messages only after
the launch settings are verified. When Cam explicitly requests a new chat,
`create_thread` also accepts model and thinking; this skill alone does not
authorize creating extra chats.

Before launching, install/verify a thread heartbeat using `automation_update`
with destination `thread` and this chat as target. Start at a two-minute cadence;
this is a polling interval, not a guaranteed hard stop. When observed burn rate
could exhaust the reserve before the next check plus closeout, reduce concurrency
or drain early. Keep the app running for local scheduling. Confirm creation from
the tool result; a saved prompt alone is not an active monitor. Inspect existing
automation records and update the round's monitor rather than duplicating it.

Verify each selected project has its own triage skill and use its actual path
in the launch message. If missing, report that project as unready rather than
substituting a generic scan or silently installing a skill.

Send a succinct goal-setting instruction, with the round ID as coordination
context:

> Set a goal to do this in a loop: use [$triage](ABSOLUTE_PROJECT_TRIAGE_SKILL_PATH),
> do the work it recommends, then use the triage skill again. Keep going until
> I tell you to finish up.

The owner must actually set this as its persistent goal using the available
goal tool, not merely acknowledge it or run one triage pass. Record confirmation
of the goal in the round record. Do not invent a token budget. Let the project's
triage skill select work each iteration; supervisor readiness suggestions are
context, not a replacement task list. Follow the project's implementation and
validation workflow before returning to triage. If no meaningful authorized work
remains, checkpoint and report that instead of manufacturing another iteration.

Keep additional launch context brief: scoped closeout/commit/push is authorized
when told to finish; preserve unrelated work and existing deployment/provider
spend boundaries. Recheck quota between substantive chunks and before delegation.
Product owners obey their local skills/contracts. New supervisor worktrees follow
Conductor's approved root and custody rules; no blanket cleanup.

## Monitor and drain

Before polling or messaging, confirm this is an explicitly enabled round with
the selected participants. If no round is enabled, do no monitoring; remove any
obsolete monitor using the available automation tool.

The heartbeat prompt must reference this skill and the exact round record, carry
Cam's explicit authorization to message its listed participants, and instruct
quiet operation until a meaningful change, failure, closeout, or needed action.
It must not start/resume projects, add participants, or migrate to a new reset.

Read fresh quota before broad project inspection. Save observation time and
window/reset identity. Session telemetry is useful historical evidence but not
a substitute for fresh quota without a disclosed freshness check. If quota is
unavailable, do not launch more work; checkpoint/finish active participants and
report one actionable monitoring failure. Do not spin on repeated failures.

At the first threshold crossing, explicit finish, monitoring failure, or reserve
prediction, latch phase `draining` in the record **before dispatch**. Reset or
quota recovery cannot undo draining. Inspect participant state before messaging:
already completed/stopped work needs no new prompt; an unfinished closeout may
receive a closeout-only prompt. Do not resume a stopped triage goal.

Send each active participant, without model escalation that wastes the reserve:

> The round is draining. Stop selecting new work and wind down owned delegates.
> End the triage loop; do not invoke triage again to select another task.
> Finish the current bounded change to a coherent checkpoint; validate against
> your repo's acceptance requirements, reusing still-applicable evidence. Commit
> and push only scoped, validated work, preserving unrelated dirty/index work and
> respecting branch/review/CI policy. Verify the remote destination. If blocked,
> preserve evidence and report the blocker; do not falsely close the story or
> force a push. Then stop and summarize work since the round baseline: user
> benefit, actual changes, validation and limits, commit/remote status, remaining
> work/blockers, and retained worktrees. No new features, deployment, paid calls,
> resets, credit purchase, or cleanup beyond prior authorization.

Persist per-chat dispatch intent, delivery result, and terminal evidence. Treat
unknown delivery as uncertain: inspect the destination for the round ID before
retrying. Use compact `wait_threads` snapshots with cursors to follow closeout;
read details only when needed. Do not repeatedly prompt finished workers. A
heartbeat can return between checks; its durable state carries pending work.

## Finish and report

Verify each participant as landed, validated-but-unlanded, or blocked, with
commit/destination and evidence. Owner reports are claims until corroborated by
actual changes, receipts or remote verification. Keep partial failures explicit.
Summarize the whole round by project, distinguishing product advancement,
reliability fixes, and supporting investigation. Update readiness rankings and
next bounded tasks so the next round starts intelligently. Include worktree
custody only for worktrees this round created or used; no speculative deletion.

Save the report and terminal state, then pause the heartbeat using its returned
ID once every participant is terminal or has a clearly reported blocker and no
assistant-owned closeout remains. Report scheduling or delivery failures rather
than claiming monitoring works. Do not keep a dormant burn loop alive forever or
restart it after a reset. A later round requires Cam's new start instruction.
