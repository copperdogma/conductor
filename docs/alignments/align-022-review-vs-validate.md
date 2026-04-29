# Alignment 022 - Review vs Validate

Date: 2026-04-29

## Focus

Analyze the inbox question:

> Check the `/review` skill provided by Codex vs our `/validate`. Which is
> better? Why? What could we take from `/review` if we wanted to improve our
> skill? Any reason to switch completely to review and stop using validate?
> Should we use both?

## Surfaces Compared

- Codex built-in review stance exposed in the current session instructions
- Conductor `.agents/skills/validate/SKILL.md`
- Dossier `.agents/skills/validate/SKILL.md`
- Storybook `.agents/skills/validate/SKILL.md`
- doc-web `.agents/skills/validate/SKILL.md`
- CineForge `.agents/skills/validate/SKILL.md`
- Board Game Ingester `.agents/skills/validate/SKILL.md`
- Robo Rally `.agents/skills/validate/SKILL.md`
- Echo Forge `.agents/skills/validate/SKILL.md`

No local `review/SKILL.md` was found in the active skill registry or tracked
repo skill surfaces. The comparison treats `/review` as the Codex built-in
code-review mode: findings first, severity ordered, file/line grounded, and
focused on bugs, behavioral regressions, missing tests, and concrete risks.

## Classification

Portable improvement for `/validate`, not a replacement.

## Summary Judgment

`/review` is better for one job: defect discovery in a diff. It is sharper,
more adversarial, and less likely to bury an actual bug under process
bookkeeping.

`/validate` is better for the job our projects actually use it for: deciding
whether story work is complete enough to close. It ties the diff to acceptance
criteria, workflow gates, repo-native checks, Ideal/spec/ADR fit, generated
surfaces, browser/eval evidence, close-out ownership, and the next command Cam
can approve.

Do not switch completely to `/review`. Use both concepts:

- Keep `/validate` as the story and closeout gate.
- Treat `/review` as a focused risk-finding pass inside `/validate` whenever
  there is a meaningful code diff, broad surface area, subagent work, UI/API
  behavior, security/trust-boundary risk, or unclear test coverage.

## What `/review` Does Better

- Leads with findings instead of a scorecard, so material bugs cannot hide
  behind green checks or accepted story tasks.
- Prioritizes concrete risks: bugs, regressions, missing tests, behavioral
  breaks, and line-specific defects.
- Avoids over-validating process state. It cares whether the changed code is
  wrong, not whether the story metadata is tidy.
- Has a crisp no-finding path: say no issues found and state residual test
  gaps, rather than stretching for advisory nits.
- Produces output that maps well to inline review comments and PR review
  threads.

## What `/validate` Does Better

- Knows the story contract: acceptance criteria, tasks, gates, and intended
  behavior.
- Runs and records repo-native checks instead of only reading the diff.
- Checks Ideal/spec/ADR/methodology state fit, which a generic review pass will
  not know unless prompted.
- Handles generated surfaces, eval registries, browser proof, source-artifact
  coverage, and project-specific closeout conventions.
- Separates implementation completeness from close-out bookkeeping, which is
  important for our `/mark-story-done`, `/check-in`, and `/finish-and-push`
  flow.
- Produces a disposition: `Close now`, `Keep open`, `Rescope then close`, or
  `Mark blocked`.

## Risks If We Replaced `/validate`

- Stories could close based on "no obvious bug" while acceptance criteria,
  evals, generated indexes, or workflow gates are still incomplete.
- Repo-native checks would become optional unless the reviewer remembered to
  run them.
- Cross-project methodology surfaces would drift because `/review` has no
  built-in reason to update story handoff state, eval registries, graph/state,
  or skill wrappers.
- The output would be useful for a PR but insufficient for Cam's normal
  "is this story done and what do I say yes to next?" workflow.

## What To Borrow From `/review`

Add a compact findings-first review pass to `/validate`:

- Before the acceptance-criteria table, run a defect review of the current diff:
  bugs, regressions, missing tests, changed behavior, security/trust-boundary
  risk, and operational hazards.
- Findings should be severity ordered and tied to file/line references when
  possible.
- If there are no concrete findings, say that explicitly and name any residual
  verification limits.
- For broad or high-risk validation, make this a bounded parallel packet or
  `/loop-verify` slice, but keep the main `/validate` thread as the final
  closure judge.
- Preserve `/validate`'s story, Ideal/spec/ADR, repo-check, browser/eval, and
  closeout sections after the findings.

## Recommendation

Keep `/validate` as the primary skill.

Improve it by adding an explicit "review-mode findings pass" to the top of the
validation report and to the optional parallel-validation packet list. Do this
as a cross-repo validate-skill rollout only if Cam wants the behavior
everywhere. The change should be small: do not replace the validation template,
do not remove grades/dispositions where repos rely on them, and do not turn
every validation into a heavyweight audit.

## Current Status

Implemented locally in Conductor and isolated target-repo worktrees.

Target repo edits used isolated worktrees from `origin/main`:

`/Users/cam/.codex/worktrees/validate-findings-first/<project-key>`

Branch:

`codex/validate-findings-first`

Each `/validate` skill now includes:

- a findings-first review pass before acceptance/closure scoring
- explicit review for concrete bugs, behavioral regressions, missing tests,
  security/trust-boundary risks, and operational hazards
- severity-ordered findings with file/line grounding where possible
- an explicit no-material-findings path with residual verification limits
- review-mode defect finding as a valid optional parallel-validation packet

| Repo | Worktree | Base | Result |
| --- | --- | --- | --- |
| Conductor | `/Users/cam/Documents/Projects/conductor` | `443339a` | Added the findings-first pass to the supervisor `/validate` closure gate. |
| Dossier | `/Users/cam/.codex/worktrees/validate-findings-first/dossier` | `11828d0` | Added the findings-first pass while preserving Dossier's local test, ruff, ADR, and spec-compromise gates. |
| Storybook | `/Users/cam/.codex/worktrees/validate-findings-first/storybook` | `b534609` | Added the findings-first pass while preserving Storybook's typecheck, test, lint, build, browser, eval, and skill-sync gates. |
| doc-web | `/Users/cam/.codex/worktrees/validate-findings-first/doc-web` | `3c2b558` | Added the findings-first pass to the graded diff-analysis style validate skill. |
| CineForge | `/Users/cam/.codex/worktrees/validate-findings-first/cine-forge` | `abed869` | Added the findings-first pass while preserving backend, UI, browser, eval, methodology, and skill-sync gates. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/validate-findings-first/boardgame-ingester` | `4dfecfe` | Added the findings-first pass to the graded diff-analysis style validate skill. |
| Robo Rally | `/Users/cam/.codex/worktrees/validate-findings-first/roborally` | `23980fa` | Added the findings-first pass while preserving methodology, skills, scenario, eval, runtime, and source-artifact coverage gates. |
| Echo Forge | `/Users/cam/.codex/worktrees/validate-findings-first/echo-forge` | `dd8f3de` | Added the findings-first pass while preserving typecheck, test, lint, build, browser, eval, and skill-sync gates. |

Ran `./scripts/sync-agent-skills.sh` in every touched repo. Only
`.agents/skills/validate/SKILL.md` changed in each repo; existing generated
wrappers remained current.

## Validation

Checks that passed:

- Conductor: `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
  `PYTHONDONTWRITEBYTECODE=1 make methodology-check`,
  `PYTHONDONTWRITEBYTECODE=1 make lint`,
  `./scripts/sync-agent-skills.sh --check`, `git diff --check`
- Dossier: `./scripts/sync-agent-skills.sh --check`,
  `PYTHON='uv run --frozen python' make methodology-check`,
  `git diff --check`
- Storybook: `./scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, `git diff --check`
- doc-web: `./scripts/sync-agent-skills.sh --check`,
  `make methodology-check`, `git diff --check`
- CineForge: `./scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, `git diff --check`
- Board Game Ingester: `./scripts/sync-agent-skills.sh --check`,
  `make methodology-check`, `make lint`, `git diff --check`
- Robo Rally: `npm run validate`
- Echo Forge: `./scripts/sync-agent-skills.sh --check`,
  `npm run methodology:check`, `git diff --check`

Validation notes:

- Dossier used the repo's locked `uv` environment for `PyYAML`. The command
  passed and reported existing legacy metadata/non-local ADR warnings.
- CineForge `npm run methodology:check` still reports existing architecture
  audit and UI-scout freshness warnings, exits successfully, and the warnings
  are unrelated to this validate-skill wording change.

## Follow-Up

Recommended next action after validation:

Check in and push the Conductor analysis plus target-repo validate-skill
updates if validation remains clean.
