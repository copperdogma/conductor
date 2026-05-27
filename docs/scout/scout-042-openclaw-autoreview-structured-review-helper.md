# Scout 042 - Evaluate OpenClaw Autoreview for Structured Review Closeout

**Source**:
`https://github.com/openclaw/agent-skills/blob/main/skills/autoreview/SKILL.md`,
`https://github.com/openclaw/agent-skills/blob/main/skills/autoreview/scripts/autoreview`,
and
`https://github.com/openclaw/agent-skills/blob/main/skills/autoreview/scripts/test-review-harness`

**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

OpenClaw's `autoreview` skill is a structured code-review closeout workflow
around a bundled Python helper. Codex is the default engine, with Claude, Droid,
and Copilot also supported. The skill is meant for second-model review, review
after non-trivial code edits, and branch or PR review after fixes.

This is closely related to Scout 032 and Alignment 030, but it is not already
covered. Scout 032 adapted Peter Steinberger's `codex-review` guidance into
instruction-level `/validate` behavior and explicitly deferred helper adoption.
OpenClaw's `autoreview` is the later helper-shaped candidate that makes that
deferred question concrete.

The useful new pieces are:

- one helper path for local, branch, and commit review targets
- structured JSON output with schema validation and nonzero exit when
  accepted/actionable findings remain
- read-only review execution for Codex through `codex exec` with an output
  schema and isolated ephemeral run state
- default web search and read-only tools for dependency, docs, and security
  contract checks
- optional prompt files and datasets for review context
- heartbeat and streaming behavior for long-running reviews
- optional parallel test execution after formatting has stabilized line
  locations
- opt-in multi-reviewer panels, with the main agent still responsible for
  verifying every accepted finding
- a calibration harness with malicious and benign fixtures for security-oriented
  review behavior

The current local methodology already has the important behavioral rule: review
findings are advisory and `/validate` remains the closeout authority. The new
question is whether Cam's repos should maintain a local structured helper so
target selection, review bundle creation, schema validation, and clean exit
status are not repeatedly reimplemented by agents.

## Fit Against Current Methodology

Already covered locally:

- `/validate` may add `codex review` for non-trivial code diffs when it improves
  closeout confidence.
- `/validate` already has local, branch/PR, and commit target-selection guidance.
- Findings must be verified against real code and relevant docs before fixing.
- Accepted review-triggered fixes require focused checks and a fresh review
  signal.
- `/loop-verify` treats model and worker findings as evidence, not truth, and
  stops when the scoped verifier is clean.

New value beyond current text:

- `autoreview` turns the review signal into a structured command with an exit
  code that can be used as a repeatable closeout proof.
- The helper validates output shape before reporting success, which reduces
  ambiguity from terse or drifting model output.
- The helper can carry review-specific context via `--prompt-file` and
  `--dataset`, which fits Cam's evidence-heavy closeout style better than a
  bare review invocation.
- The helper's heartbeat and streaming rules reduce false "hung review" stops
  on larger diffs.
- The fixture harness gives a small way to test whether each engine is too
  noisy, too permissive, or appropriately calibrated for security-sensitive
  diffs.

Risks and limits:

- This is executable review infrastructure from an external repo. It should be
  vendored or reimplemented only after a code review and a small local trial.
- The helper's default Codex path enables web search and read-only tools. That
  is useful for public dependency contracts, but private-project review should
  keep data exposure and provider behavior explicit.
- The helper filters out findings whose reported location is outside the changed
  path set. That is good for diff discipline, but a local wrapper should preserve
  a way to report adjacent-file or upstream-owned findings as follow-up evidence
  rather than silently treating them as nonexistent.
- Multi-reviewer panels are useful only for high-risk or explicitly requested
  review. They should not become default token spend.
- The local Codex CLI, output-schema behavior, model flags, and sandbox support
  need to be tested in Cam's actual environments before relying on this in
  `/validate`.

## Project Relevance

- **conductor**: `Spike`. Conductor is the right owner for a bounded helper
  trial because it already owns shared `/validate` behavior and cross-project
  review policy. The spike should test the helper against one fixture and one
  real non-trivial code diff, then decide whether to add local helper guidance
  or keep the existing instruction-level `codex review` path.
- **dossier**: `Defer`. Dossier would benefit from structured review on
  behavior and intake-code diffs, but it should inherit a proven Conductor
  pattern rather than carry its own helper first.
- **storybook**: `Defer`. Useful for broad TypeScript/backend changes and
  Journey Scout runtime changes, but not until Conductor proves the helper adds
  confidence without slowing ordinary product work.
- **doc-web**: `Defer`. Potentially useful for parser/runtime changes and
  provider-boundary work. No direct repo note is warranted until the helper
  trial produces a concrete adoption shape.
- **cine-forge**: `Defer`. Useful for render-adapter and artifact-editing code
  diffs, but panels or long review loops could be wasteful for high-taste media
  work.
- **boardgame-ingester**: `Defer`. Potentially useful for ingestion/runtime
  code diffs; lower immediate leverage.
- **roborally**: `Defer`. Potentially useful for scenario-engine changes, but
  too much process for the current project size unless a risky code diff
  appears.
- **echo-forge**: `Defer`. Useful for UI/control/runtime code diffs, especially
  when live browser verification already shows risk. Any adoption should avoid
  disturbing active primary checkout work.

## Recommendation

Spike `autoreview` as a Conductor-owned optional closeout helper, not as a
blanket skill import.

Spike result on 2026-05-27: helper mechanics and Codex fixture calibration
passed, but helper adoption should still defer until the first approved
non-trivial real code-diff closeout. The local trial proved the helper can run
through Codex, validate structured output, catch a malicious fixture, and avoid
false positives on a benign security-sensitive fixture. It did not prove
real-repo diff value because the only substantial tracked code diff found was
unrelated active Echo Forge primary-checkout work, which should not be used as
supervisor-spike material.

Recommended follow-up scope:

1. Run the helper on one real non-trivial branch or local diff where
   `/validate` would already justify a review signal.
2. Compare results against the existing manual `codex review` guidance:
   target selection, finding quality, runtime, false positives, output
   stability, and final-report ergonomics.
3. If the helper earns its keep, add Conductor guidance for an optional
   structured-review helper inside `/validate`; then create a normal alignment
   rollout only if the behavior should travel to tracked repos.

Do not add inbox notes to target projects yet. The only honest current owner is
Conductor; target projects should receive this only after a successful helper
trial produces a small, portable adoption contract.

## Rejected Adaptations

- Do not import the `autoreview` skill into every tracked repo now.
- Do not require structured review for docs-only scout/alignment work, generated
  index updates, tiny obvious patches, or product/taste validation.
- Do not make review panels the default. Use them only when requested or when
  risk justifies the extra cost.
- Do not let `/loop-verify` workers invoke `autoreview`, `codex review`, or
  other nested review panels.
- Do not push a branch just to make review easier.
- Do not treat a clean helper run as proof that the task is complete. It proves
  only that the selected review target has no accepted/actionable review
  findings.
- Do not allow the changed-path filter to hide valid adjacent-surface findings;
  route those as follow-up or expansion evidence.

## Evidence

- The upstream skill says Codex is the default and recommended reviewer, and it
  triggers on second-model review requests, non-trivial code edits, and local or
  PR branch review after fixes.
- The skill contract keeps findings advisory, requires real-code verification,
  reruns focused tests and review after review-triggered fixes, and stops after
  the helper exits clean.
- The helper chooses dirty local review first, otherwise current PR base when
  available, otherwise `origin/main` for non-main branches, with explicit commit
  review for landed or pushed work.
- The helper builds local, branch, or commit diff bundles and validates
  reviewer output against a strict findings schema before printing a report.
- The Codex path runs `codex exec` with read-only sandboxing, an output schema,
  output capture, optional model reasoning effort, and web search unless
  disabled.
- The helper supports prompt files, datasets, JSON output, human-output files,
  parallel test commands, engine panels, per-engine model/thinking settings, and
  streaming/heartbeat status.
- The helper exits nonzero when accepted/actionable findings remain or parallel
  tests fail, and prints a clean line only when no accepted/actionable findings
  are reported.
- The companion harness creates malicious and benign temporary git fixtures so
  engines can be calibrated against concrete security findings and false
  positives.
- Local spike evidence on 2026-05-27 used upstream blob SHAs
  `78fd688641f39bf0319ed211cbc546b671267db2`,
  `653f75c455a916bf57d18a635d227713fbd94bcd`, and
  `58105bc558986d44d84652d969ba18daa377a75e`; Codex CLI was
  `codex-cli 0.133.0`.
- The malicious fixture produced three concrete P1 findings and the benign
  fixture exited clean with no accepted/actionable findings.
- No target checkout was modified. The first real tracked-repo diff trial was
  deferred because the only substantial code diff found was unrelated active
  Echo Forge primary-checkout work.

## Confidence

High that the source is relevant and distinct from the existing instruction-only
review rollout. High that the helper can run locally with Codex on controlled
fixtures. Medium-low on immediate adoption value until it is run on one real
repo code diff that already warrants review.

## Open Questions

- Does the current local Codex CLI behavior stay stable across normal app
  updates, especially the exact `exec`, output-schema, sandbox, and streaming
  flags the helper depends on?
- Should a local version preserve the changed-path filter exactly, or report
  out-of-scope findings separately as follow-up evidence?
- Is the helper best kept as a Conductor-only utility, or should it eventually
  travel to every repo that carries `/validate`?
- What runtime threshold makes the helper worth using over manual
  findings-first review plus targeted tests?
