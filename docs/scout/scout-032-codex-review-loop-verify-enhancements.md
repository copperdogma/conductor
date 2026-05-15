# Scout 032 - Evaluate Codex Review Loop for Validate and Loop-Verify Enhancements

**Source**: `https://x.com/steipete/status/2054850632067019173?s=46&t=uFZE-MuhgWdh1YErEZzLtQ`,
`https://github.com/steipete/agent-scripts/blob/main/skills/codex-review/SKILL.md`,
and `https://github.com/steipete/agent-scripts/blob/main/skills/codex-review/scripts/codex-review`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Peter Steinberger's `codex-review` skill is a closeout workflow for running
Codex's built-in code review until there are no accepted/actionable findings
left. The tweet's important caveat is the right one: this does not replace
human architecture judgment.

This is not a replacement for Conductor's `/validate` or `/loop-verify`.
`/validate` is the essential closure checkpoint for story/task intent, checks,
artifacts, inbox cleanup, and final disposition. `/loop-verify` is a bounded
multi-shard verification loop for any scoped task, with explicit mode
selection, materiality rules, no-recursion guardrails, upstream-boundary
handling, docs/ADR behavior, and non-convergence stops. `codex-review` is
narrower than both: it turns one code-review signal into a disciplined closeout
loop for code diffs.

The useful move is selective adaptation. The external skill has strong
operational details that Conductor can borrow when a code-review signal is
useful:

- pick the right review target before running anything
- treat model review output as advisory, not authoritative
- require accepted findings to be verified against real code and relevant docs
- reject speculative, over-broad, or over-engineered fixes
- rerun focused tests and the review signal after review-triggered code edits
- stop when the final helper/review run is clean instead of chasing a nicer
  second confirmation
- report accepted and rejected findings explicitly

Those ideas belong primarily in `/validate`, because validate is Cam's essential
closeout checkpoint. `/loop-verify` should borrow only the task-agnostic
discipline: keep an accepted/rejected/follow-up finding ledger, treat model
findings as evidence rather than truth, and stop when the scoped verifier is
clean instead of chasing prettier confidence.

## Fit Against Current Validate And Loop-Verify

Already covered locally in `/validate`:

- findings-first review of the current diff before scoring closure
- validation against story acceptance criteria, tasks, workflow gates, and
  actual changed artifacts
- repo-native checks as part of the closure decision
- escalation to `/loop-verify` only when broad or high-risk validation needs a
  complete clean round

Already covered locally in `/loop-verify`:

- the coordinator chooses the loop mode, budget, materiality gate, and boundary
  before worker launch
- workers must not invoke `/loop-verify`, spawn subagents, or start nested
  loops
- docs/ADR loops default to find-only workers and main-thread fixes
- upstream-owned findings stop or split the loop instead of causing local churn
- strict-until-clean mode is reserved for explicit approval or objective
  contract-critical surfaces
- the main thread owns final synthesis and disposition

Gaps the external skill exposes for `/validate`:

- no Codex-review-specific target selection rule exists in `/validate`
- no standard accepted/rejected finding report exists for a model review signal
- no guidance says when to run a review signal in parallel with focused tests
- no explicit stop rule says a clean helper/review result is enough and should
  not be followed by extra review cycles for prettier wording

Gaps the external skill exposes for `/loop-verify`:

- the current loop reports materiality, blockers, upstream findings, and
  expansion findings, but it can be clearer that every finding should receive a
  disposition: accepted defect, rejected non-issue, or follow-up/expansion
- the existing stop rules can be sharpened so a clean scoped verifier is enough
  and the coordinator should not run extra rounds for confidence theater

## Recommendation

Adapt the idea into Conductor as an optional `codex review` closeout signal
inside `/validate`, not as a new mandatory review loop and not as a replacement
for `/validate`.

Recommended story scope:

- Add a `/validate` subsection for `codex review` on non-trivial code diffs.
- Trigger it when the user asks for a second-model review, the diff is
  broad/high-risk enough to justify another review signal, or validate is
  closing a behavior/security/API/code path where test coverage is uncertain.
- Skip it for docs-only scout/alignment/inbox/generated-index work, tiny
  obvious patches, and product/taste validation.
- Keep the main coordinator responsible for target selection:
  - dirty local work: `codex review --uncommitted`
  - branch or PR work: `git fetch origin`, then `codex review --base` against
    the PR base or `origin/main`
  - single committed change: `codex review --commit HEAD`
- Warn that a clean `--uncommitted` review on a clean tree only proves there is
  no local patch.
- Treat review findings as advisory. Verify each finding before fixing it,
  reject speculative or over-broad items, and prefer small fixes at the right
  ownership boundary.
- If a review-triggered fix changes code, rerun the narrow affected tests and
  the review signal. Stop when the final review/helper run exits clean with no
  accepted/actionable findings.
- Report the command used, tests run, accepted findings, rejected findings with
  short reasons, and the final clean or consciously-rejected state.
- Add only task-agnostic finding-disposition and clean-stop wording to
  `/loop-verify`.

Do not import the external helper wholesale yet. A later story can decide
whether a small local helper is worth maintaining after the instruction-level
behavior is proven useful.

## Project Relevance

- **conductor**: `Adapt`. This belongs first in Conductor's shared `/validate`
  skill, with a smaller general finding-disposition refinement in
  `/loop-verify`.
- **dossier**: `Defer`. It can benefit only after Conductor has a validated
  portable wording update; no direct repo note is needed now.
- **storybook**: `Defer`. Same as Dossier. The review signal may help on
  broad TypeScript/backend diffs, but the routed change should come through a
  methodology rollout rather than a Storybook-only story.
- **doc-web**: `Defer`. Potentially useful for code closeout, but not a direct
  doc-web product story.
- **cine-forge**: `Defer`. Potentially useful for high-risk code closeout, but
  should inherit the Conductor pattern if adopted.
- **boardgame-ingester**: `Defer`. Potentially useful on parser/runtime code
  diffs, but not a direct product need.
- **roborally**: `Defer`. Potentially useful on scenario-engine diffs, but not
  worth a repo-local fork of the workflow.
- **echo-forge**: `Defer`. Potentially useful on UI/control changes, but the
  right route is shared loop-verify wording first.

## Rejected Adaptations

- Do not require Codex review on every patch. That would add token burn and
  latency to low-risk work.
- Do not make `/loop-verify` a story-closure or code-review-only loop.
- Do not let a loop-verify worker spawn a subagent to filter Codex review
  output. That conflicts with the current no-recursion worker contract.
- Do not treat the external helper's grep for `[P0]` through `[P3]` as a stable
  parser contract for all future Codex CLI output.
- Do not use `--full-access` as a default. It is only appropriate when the
  review run hits sandbox or permission limits and the surrounding task already
  justifies that execution mode.
- Do not push merely to make review easier. Push remains controlled by the
  user's explicit check-in or ship request.

## Evidence

- The X post says the skill runs Codex review in a loop until no issues remain
  and explicitly says human architecture judgment is still required.
- The GitHub skill treats review output as advisory and requires real-code
  verification before accepting findings.
- The skill chooses different review commands for dirty local work, branch/PR
  work, and a single committed change.
- The skill allows tests and review to run in parallel after formatting, but
  requires rerunning both affected tests and review when either path changes
  code.
- The helper auto-selects local dirty review first, otherwise PR/base review,
  and reports clean only when the selected review exits clean with no accepted
  findings.
- Replies retrieval through the Twitter connector failed with a URL-metadata
  error, so this scout relies on the original tweet plus the linked public
  GitHub skill and helper source.

## Confidence

High. The source is clear, and the local comparison is constrained by recent
Conductor alignments that already define what `/loop-verify` should and should
not become.

## Open Questions

- Whether the current Codex CLI review output is stable enough to support a
  helper-level parser in Cam's environments. The first adaptation should stay
  instruction-level unless a follow-up story proves helper maintenance is worth
  it.
