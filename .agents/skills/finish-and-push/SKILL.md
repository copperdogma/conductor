---
name: finish-and-push
description: Close out current Conductor work, optionally close a story if one is in scope, then run the full check-in and push-to-main flow
user-invocable: true
---

# /finish-and-push [story-number] [--cleanup]

Use this when the user wants the current Conductor work closed out, checked in,
and pushed to `main` in one pass.

This is an orchestrator. It wraps the existing leaf skills in order:

1. if a completed story is actually in scope, `/mark-story-done`
2. `/check-in`

## Bundled Permission

Invocation counts as explicit approval to:

- run `/mark-story-done`
- make narrowly scoped fixes needed to complete close-out safely
- commit intended files
- push the execution branch
- sync with latest `origin/main`
- re-run required validation
- fast-forward `main`
- push `main`

Do not ask again for those actions unless a real blocker, risk, or ambiguity
appears.

## Flow

1. Resolve the intent surface:
   - read current git context
   - determine whether the work is primarily:
     - a specific story
     - an alignment or scout artifact with clear promised outputs
     - general local repo work driven by the user request and current diff
   - if no written artifact exists, convert the user request plus current diff
     into a short explicit validation target
   - if the intent surface cannot be resolved clearly enough to judge
     completion, stop and ask

2. Validate the work against that intent surface:
   - validation is mandatory in all cases
   - if a story, scout, or alignment artifact exists, validate against it
   - if the work was small or local, validate against the explicit user intent
     plus the realized diff and current artifact quality
   - if this validation fails or remains ambiguous, stop before any close-out or
     landing step

3. If a completed story is genuinely in scope, run `/mark-story-done` first:
   - reuse that skill's workflow gates, validation requirements, story-close
     behavior, and generated backlog refresh
   - do not skip it when the current work is actually story-backed
   - if no story is in scope, skip this step entirely

4. Triage close-out issues:
   - if only minor issues remain, fix them immediately, rerun the required
     checks, and continue
   - if major gaps remain, stop before any commit/push and report the safest
     next step

5. Run `/check-in` in full landing mode:
   - reuse that skill's intent-surface audit, staging discipline,
     sync-with-main, validation, and fast-forward-only landing rules
   - pass through `--cleanup` only if the user explicitly requested it

6. Triage issues from check-in:
   - fix minor mechanical issues inline and continue
   - stop on major check-in or integration issues instead of forcing the
     landing

7. Report the outcome:
   - if successful: summarize story closure, commit/landing path, validation
     results, and whether `main` was pushed and cleanup was performed
   - if stopped: list blockers, what you already checked or fixed, and the
     recommended next step

## Minor vs Major

Treat these as **minor** unless they reveal a larger underlying problem:

- missing workflow-gate checkbox or stale story status row
- stale generated planning surfaces resolved by `make methodology-compile`
- missing or incomplete `CHANGELOG.md` entry
- generated skill wrapper drift fixed by `scripts/sync-agent-skills.sh`
- small doc or metadata mismatch caused by the current work
- narrow lint/test failure with an obvious, low-risk local fix
- missing re-run of a required check after a small patch

Treat these as **major** and stop before commit/push:

- unmet acceptance criteria or unchecked substantive tasks when a written plan
  is in scope
- missing alignment or scout memory updates when the current work depends on
  those artifacts being the source of truth
- inability to state a clear validation target for non-story work
- failing tests or lint with unclear root cause or broad blast radius
- unrelated, risky, or suspicious git changes in the landing set
- secrets, credentials, large artifacts, or accidental generated output
- integration conflicts that are not purely mechanical
- anything that requires architecture changes, scope renegotiation, or user
  judgment about what should land

## Guardrails

- Never require a story when the current work was intentionally small, local, or
  otherwise not story-backed
- Never bypass `/mark-story-done` when the current work is actually a completed
  story
- Never skip validation just because the work was small, local, or not planned
  in a story
- Never push partial work just because only a small issue remains
- After every inline fix, rerun the minimum required validation before
  continuing
- Never weaken the guardrails from `/mark-story-done` or `/check-in`
- Never land onto `main` without the fast-forward-only rule
- If you stop, explain whether the issue is minor-but-blocked or major and why
