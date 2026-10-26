# Storybook quota-burn pilot — October 25–26, 2026

## Outcome

The one-project round delivered Story053's voice-action capture repair, committed
and independently verified on remote main at
[d32c2dfe](https://github.com/copperdogma/storybook/commit/d32c2dfe4a0ab3120a81be8d887f9252a7d7c0fd).
Voice recordings saved before their matching chat request now preserve the
selected question/discussion action through durable storage and both transports.
Retries remain bound to original targets and source revisions; semantic target
authority remains server-owned. Ordinary audio and empty archives cannot initiate
a discussion action. This fixes a reproduced API/PostgreSQL failure rather than
adding speculative hardening.

## Evidence and limits

Owner committed evidence in `docs/reports/voice-action-capture-20261026/README.md`
records 127 affected API/PostgreSQL regressions and related command/Scribe checks,
plus 1,827 backend, 379 frontend, 56 shared and 8 native release-suite checks,
with 12 conditional skips. Typecheck, lint and build pass. Four React/IndexedDB
browser cases cover manual/automatic send, question/discussion, changed UI target,
reload and original metadata delivery, with zero page errors. Provider transport
was intercepted; physical microphone/echo and speech-model acceptance were not
proved. Unchanged historical Dossier smoke evidence was reused; no new paid
provider calls were claimed. The supervisor read the committed evidence and
change summary; it did not rerun these owner tests.

`git ls-remote origin main` independently matched the full candidate SHA.
The primary checkout retains only its pre-existing dirty `docs/deploy-log.md`;
its SHA256 still matches the round baseline. The supervisor created no Storybook
worktree and performed no deployment or cleanup. The owner's dependency-install
preflight initially exhausted disk; it recovered using the existing source-path
option with pin/hash checks, with no product-code installer workaround.

## Round control

Only Storybook was enrolled. Astra/ultra dispatch was accepted. Cam subsequently
confirmed the chat was on Standard speed; the requested Fast setting had not been
applied. Native messaging exposes no speed field and computer use could not
control Codex. The skill now requires verified Fast before launch, with a manual
setting/confirmation step when necessary. Persistent goal creation failed with a
transaction-depth error; the old goal remained paused. The active turn did useful
work, but a durable automatic triage loop was never established. Do not describe
this as a fully successful goal-loop pilot.

At 00:08 MDT on October 26 the announced quota reset arrived before the
20%-remaining reserve was reached. The supervisor latched closeout rather than
carrying the old pre-reset round into a new allowance. No reserve crossing was
observed, and project-exclusive quota consumption was not measured. The latched
round was not restarted. Raw quota snapshots and chat identifiers remain local.

The owner initially planned production deployment based on an older fulfilled
request. The supervisor clarified the burn's scope. The owner subsequently
checked the saved conversation and asked Cam for fresh release approval,
acknowledging that release48 had already fulfilled the earlier request. The
validated repair is pushed. Cam then explicitly requested shutting Storybook down
at a good checkpoint. The owner confirmed idle, a paused loop goal, no active
delegates or temporary servers/candidate build, preserved evidence and unchanged
dirty deployment-log edits. Production remains release 48; the pending new
deployment will not start. Closeout records are pushed at
[eab55d80](https://github.com/copperdogma/storybook/commit/eab55d80bbe13b48fb8a36631a7948353e48abe5).
The app confirmed this finite monitor was deleted. No new round is enabled.

## Next readiness

The voice-action defect is closed. JS021 correction phaseC still needs separately
authorized paid work; Story197 approval/holdout and Story175 infrastructure gates
remain unmet, and diarization stays deferred. Before another quota-burn round,
fix or verify the persistent-goal lifecycle and verify speed independently. Keep
the same per-round slate approval and owner-triage workflow.
