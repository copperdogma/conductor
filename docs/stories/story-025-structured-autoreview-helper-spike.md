---
title: "Structured Autoreview Helper Spike"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I3"
  - "I5"
spec_refs:
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.2"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "scouting"
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "conductor"
---

# Story 025 — Structured Autoreview Helper Spike

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Turn Scout 042's `autoreview` recommendation into a bounded Conductor spike.

The point is to answer the adoption question with local evidence: does the
OpenClaw structured review helper improve Cam's existing `/validate` closeout
process enough to justify maintaining helper-level guidance, or is the current
instruction-level `codex review` path still the right amount of process?

This story should prove mechanics and decision quality before any repo-wide
rollout. Target projects should not get inbox notes, stories, or helper installs
unless the spike produces a small, portable adoption contract.

## Acceptance Criteria

- [x] Upstream `autoreview` source version is recorded with enough detail to
      make the spike reproducible.
- [x] The helper's execution and privacy assumptions are reviewed before any
      local run.
- [x] Local CLI compatibility is tested without mutating the Conductor checkout.
- [x] A fixture or controlled diff run tests structured output, exit semantics,
      and finding quality against at least one concrete code-review scenario.
- [x] If no suitable real non-trivial tracked-repo code diff is available for
      the second half of the spike, the blocker is recorded instead of faking
      adoption proof from a docs-only diff.
- [x] The story records a decision: adopt helper guidance, defer until a real
      code diff, or reject helper adoption.
- [x] No target project checkout is modified.

## Out of Scope

- Importing `autoreview` into every tracked repo.
- Replacing `/validate` with a helper.
- Running review panels by default.
- Running nested review from `/loop-verify` workers.
- Pushing or committing solely to make review easier.
- Modifying target project checkouts during the spike.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Create Scout 042 and add it to the scout index
- [x] Record upstream source SHAs or current source identity
- [x] Review helper execution and data-exposure assumptions
- [x] Test helper CLI compatibility and dry-run behavior locally
- [x] Run the fixture or a controlled local code-review scenario
- [x] Decide whether helper guidance is warranted now
- [x] Update Scout 042 and related alignment/story memory with the result
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test` not required because no
        repo scripts or checks changed
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/stories/story-024-structured-autoreview-helper-spike.md` — spike plan,
  work log, evidence, and final decision.
- `docs/scout/scout-042-openclaw-autoreview-structured-review-helper.md` —
  scout result update after the spike.
- `docs/scout.md` — already updated with Scout 042.
- No alignment log is required for this pass because the spike does not change
  shared methodology yet.

## Notes

- Triggered by Cam's approval to proceed after Scout 042 classified
  `autoreview` as worth a bounded Conductor spike, not a blanket rollout.
- Current `/validate` already has instruction-level `codex review` guidance.
  The spike must prove helper-level value beyond what is already documented.
- A real tracked-repo code-diff trial is preferred, but only if a suitable
  non-trivial diff exists and can be reviewed read-only without disturbing a
  live primary checkout.
- Spike result: fixture behavior is promising, but real-diff proof is still
  missing. Do not add helper guidance to `/validate` yet.

## Plan

1. Pin the upstream source identity for the skill, helper, and fixture harness.
2. Inspect helper behavior for local writes, network/model exposure, review
   target selection, sandbox mode, output schema, and exit status.
3. Copy the upstream helper/harness into a temporary directory only and run
   `--help` / `--dry-run` style checks first.
4. If the local Codex CLI supports the helper path, run a bounded fixture or
   controlled code-review scenario with Codex only.
5. Record whether the helper improves target selection, review structure,
   final-report evidence, and false-positive handling enough to justify local
   `/validate` helper guidance.
6. Update the story and Scout 042 with the decision, run Conductor methodology
   checks, and leave target projects untouched.

Autonomy: Go after approval. Cam already approved the bounded spike; pause only
if the helper would need target-repo writes, credential changes, a broad
provider/model decision, or more than a bounded fixture-style review run.

## Work Log

20260527-1244 — story-created: created from Cam's approval to proceed with the
Scout 042 structured autoreview helper spike. Scope is Conductor-only evidence;
no target project checkout edits are approved.

20260527-1247 — upstream-and-cli-checked: recorded current upstream blob SHAs:
`SKILL.md` `78fd688641f39bf0319ed211cbc546b671267db2`, helper
`653f75c455a916bf57d18a635d227713fbd94bcd`, and test harness
`58105bc558986d44d84652d969ba18daa377a75e`. Local Codex CLI is
`codex-cli 0.133.0` at `/Applications/Codex.app/Contents/Resources/codex`.
`codex exec --help` exposes `--ephemeral`, `--sandbox read-only`,
`--output-schema`, `--output-last-message`, `--json`, and `-C/--cd`, matching
the helper's expected Codex path. The helper also accepts `--help` and local
`--dry-run`; on this detached Conductor worktree it selects `local`, reports
`engine: codex`, and can disable web search for dry-run checks.

20260527-1250 — helper-assumptions-reviewed: the helper writes temp schema and
output files, can write requested `--output` / `--json-output` files, reads
local/branch/commit diffs, includes untracked text files in local bundles, and
can call review engines with read-only tools plus web search by default. The
important local guardrails are: use it only when model exposure of the diff is
acceptable, prefer `--no-web-search` for private code unless upstream lookup is
needed, preserve follow-up handling for out-of-scope findings, and avoid panels
unless explicitly justified.

20260527-1252 — fixture-calibration-passed: copied the upstream helper and
harness into `/tmp/conductor-autoreview-spike-20260527` only. `python3 -m
py_compile` passed. The malicious Codex fixture found three concrete P1
findings: path traversal, command injection via shell interpolation, and public
password exposure. Because the harness expected findings, the command exited 0.
The benign Codex fixture exited 0 clean, with no accepted/actionable findings,
and specifically recognized the safe child-path validation, `execFile` use, and
owner-gated password-adjacent state.

20260527-1254 — real-diff-trial-deferred: read-only tracked-project status
sweep found no suitable isolated non-trivial code diff for the second half of
the spike. Echo Forge has a substantial active primary-checkout code/assets
diff, but it is unrelated live product work; using it as supervisor-spike
material would violate the intent to keep target workspaces quiet and isolated.
Storybook has only an untracked GEDCOM input and CineForge has a docs deploy
log change. Decision: do not adopt helper guidance into `/validate` yet. Keep
`autoreview` as fixture-proven and run the first real-diff trial only when a
future approved code closeout already warrants a review signal.

20260527-1258 — validation-complete: regenerated methodology surfaces with
`make methodology-compile`; `make methodology-check`, `make lint`, `make
skills-check`, `git diff --check`, and a trailing-whitespace scan of the touched
scout/story files passed. Current-pass review found no material issues: the
story records the real-diff blocker instead of overstating adoption proof, Scout
042 now reflects fixture-passed/real-diff-deferred status, and no target project
checkout was modified. `make test` was not required because no Conductor script
or repo-check code changed.

20260527-1300 — story-closed: marked Story 025 done after validation. The
durable outcome is not a `/validate` helper rollout; it is a fixture-proven
candidate with real-diff adoption deferred until a future approved code closeout
already warrants review.
