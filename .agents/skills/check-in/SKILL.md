---
name: check-in
description: Verify current work against the best available intent surface and, when explicitly requested, commit and push validated changes safely
user-invocable: true
---

# /check-in [--audit-only] [--cleanup]

Use this when the user wants the current work checked for completeness and, if
it is honestly done, committed and pushed.

Unless `--audit-only` is present, invocation counts as explicit approval to:

- make narrowly scoped fixes needed to complete close-out safely
- commit intended files
- push the execution branch
- sync with latest `origin/main`
- re-run required validation
- fast-forward `main`
- push `main`

Do not ask again for those actions unless a real blocker, risk, or ambiguity
appears.

## Intent Surface

Use the strongest available scope in this order:

1. active story
2. active alignment or scout entry
3. explicit user request plus the current diff
4. if the local work came from another repo's story or supervisor artifact, read
   that source too

There is always an intent surface. If no written artifact exists, convert the
user request plus the current diff into a short explicit statement of what this
work was trying to accomplish, then validate against that. If you cannot name
the intended outcome clearly enough to judge completion, stop and report the
missing context instead of guessing.

## Steps

1. Inspect git context:
   - `git branch --show-current`
   - `git status --short`
   - `git diff --stat`
   - `git diff`
   - `git diff --staged`
   - `git fetch origin main`

2. Read the intent surface and audit completion:
   - story work: acceptance criteria, tasks, workflow gates
   - alignment or scout work: promised outputs, follow-up artifacts, and any
     stated recommendation or decision surface
   - general repo work: the user's high-level goal, the realized diff, and any
     obvious generated surfaces that should have changed
   - flag:
     - missing outputs
     - stale generated files
     - unrelated changes
     - secrets or build artifacts
     - anything not freshly verified
   - name the validation target in one sentence before deciding the work is
     complete

3. Classify issues before landing:
   - treat these as **minor** unless they reveal a larger problem:
     - missing workflow-gate checkbox or stale story status row
     - stale generated planning surfaces fixed by `make methodology-compile`
     - missing or incomplete `CHANGELOG.md` entry
     - generated skill wrapper drift fixed by `scripts/sync-agent-skills.sh`
     - small doc or metadata mismatch caused by the current work
     - narrow lint/test failure with an obvious, low-risk local fix
     - missing re-run of a required check after a small patch
   - treat these as **major** and stop before commit/push:
     - unmet acceptance criteria or unchecked substantive tasks
     - missing story, alignment, or scout memory updates required by scope
     - failing tests or lint with unclear root cause or broad blast radius
     - unrelated, risky, or suspicious git changes in the landing set
     - secrets, credentials, large artifacts, or accidental generated output
     - integration conflicts that are not purely mechanical
     - anything that requires a methodology decision, scope renegotiation, or
       user judgment about what should land

4. Fix minor issues inline and rerun the minimum required validation:
   - if an issue is minor and local, fix it now, refresh any generated surfaces,
     and rerun the affected checks before continuing
   - if a fix starts widening scope or touching unsettled behavior, reclassify
     it as major and stop

5. Run fresh validation for the touched surface:
   - validation is mandatory, even for small local work
   - `make methodology-check`
   - `make lint`
   - `make skills-check` if skill files changed
   - `make test` if scripts or repo checks changed
   - if story, alignment, scout, or registry changes should affect generated
     backlog surfaces, run `make methodology-compile` before the final
     `make methodology-check`
   - inspect the actual changed artifacts and verify they satisfy the resolved
     intent surface, not just the repo checks

6. Decide whether the work is closeable:
   - if any required artifact, validation step, quality bar, or high-level goal
     is still partial, stop and report exactly what blocks check-in
   - if a story is in scope and is fully complete, close it with
     `/mark-story-done` before committing
   - if the user asked for audit only, stop here with one clear closure
     recommendation

7. Commit and push safely:
   - stage only the intended files
   - draft a commit message that matches the completed work
   - if the current branch is not `main`, commit there, push the branch, sync it
     with `origin/main` if needed, validate again if integration changed files,
     then fast-forward `main`
   - if the current branch is `main` and `origin/main` is already an ancestor of
     `HEAD`, commit locally and push `main` only after checks pass
   - if the current branch is `main` and integration with `origin/main` is
     required, create a temporary `codex/checkin-<timestamp>` branch, resolve
     there, validate, then fast-forward `main`

8. Report:
   - which intent surface was used
   - the explicit validation target
   - whether the work was complete or blocked
   - which checks passed
   - whether a story was closed
   - branch, commit, and push result
   - whether cleanup was performed

## Guardrails

- Never commit or push without explicit user request.
- Never hide remaining gaps just to get a clean commit.
- Never push partial work just because only a small issue remains.
- Never treat passing repo checks alone as sufficient validation when the actual
  changed artifacts still do not satisfy the intended outcome.
- Never stage unrelated files or use `git add .`.
- Never push `main` before fresh validation on the exact tip being landed.
- Never resolve integration conflicts directly on `main`.
- After every inline fix, rerun the minimum required validation before
  continuing.
- If confidence depends on a check you did not run, stop and say it is not
  freshly verified.
