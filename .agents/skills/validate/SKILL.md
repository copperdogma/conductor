---
name: validate
description: Validate Conductor work against its story and current diff
user-invocable: true
---

# /validate [story-number]

Validate Conductor work with fresh current-pass evidence.

## Steps

1. Review all local changes:
   - `git status --short`
   - `git diff --stat`
   - `git diff`
   - `git ls-files --others --exclude-standard`
2. If a story is in scope, validate against:
   - acceptance criteria
   - tasks
   - workflow gates
3. Re-run the honest checks for the touched surface:
   - `make methodology-check`
   - `make lint`
   - `make skills-check` if skill files changed
   - `make test` if scripts or repo checks changed

3b. Optional parallel validation:
   - Use bounded validation packets only when they will materially improve
     confidence, such as changed-file review, story acceptance review,
     check/test execution, or holistic Ideal/spec/architecture review.
   - Scope each packet to explicit files, commands, or criteria. Each packet
     must return fresh evidence from the current diff and must not decide the
     final disposition.
   - The main thread keeps Conductor's final synthesis: acceptance status,
     Ideal/spec fit, closure recommendation, impact note, and yes-ready next
     step.
   - Do not use subagents for routine small validations where direct review is
     cheaper and equally trustworthy.
   - If subagents are unavailable, unsafe for the checkout, or explicitly
     disabled by the user, run the same validation sequentially and note the
     fallback in the report.
   - Escalate to `/loop-verify` when the diff is broad or high-risk, material
     fixes keep appearing during validation, the work is a cross-repo rollout,
     or one complete clean parallel round is important before closure.
4. Inspect the actual outputs:
   - updated story
   - updated log entry
   - updated generated graph/index when relevant
5. Produce a report with:
   - Met / Partial / Unmet
   - concrete remaining gaps
   - a short plain-language impact note: what improved for Cam or the target
     projects, or what practical risk got smaller
   - one clear closure recommendation
   - one recommended next step phrased so a bare `yes` can approve it

## Closure recommendations

- `Close now`
- `Keep open`
- `Rescope then close`
- `Mark blocked`

## Guardrails

- Fresh evidence only.
- Do not count close-out bookkeeping as an implementation failure by itself.
- End with one recommended disposition and a yes-ready next step when an honest
  next move exists.
