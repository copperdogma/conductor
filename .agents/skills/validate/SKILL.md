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
