# Alignment 021 - Triage Story Sizing Calibration

Date: 2026-04-29

## Focus

Route the inbox item about Robo Rally triage creating stories that were too
small, then compare whether the same story-sizing guidance should carry across
tracked triage skills.

The user-tested wording that helped was blunt: if triage usually suggests
stories that can be finished in a few minutes, expand scope toward about an
hour of AI work when that logically makes sense. The portable improvement is
the sizing heuristic, not the exact sentence.

## Surfaces Compared

- Conductor `.agents/skills/triage/SKILL.md`
- Dossier `.agents/skills/triage/SKILL.md`
- Storybook `.agents/skills/triage/SKILL.md`
- doc-web `.agents/skills/triage/SKILL.md`
- CineForge `.agents/skills/triage/SKILL.md`
- Board Game Ingester `.agents/skills/triage/SKILL.md`
- Robo Rally `.agents/skills/triage/SKILL.md`
- Echo Forge `.agents/skills/triage/SKILL.md`
- Alignment 012, which already added a same-line anti-fragmentation guardrail
  to the older product-repo set

## Classification

Portable improvement with repo-local wording.

The existing anti-fragmentation guardrail prevents new story shells when the
work is really a continuation of the same line. This follow-up addresses a
different failure mode: triage can choose the right vehicle, `create a story`,
but still size the story as a few-minute seed with poor work-to-overhead ratio.

## Decision

Carry the Robo Rally lesson across every tracked triage skill that creates or
recommends stories:

- Do not default to the smallest commandable step.
- Treat a few-minute story as suspicious when adjacent work shares the same
  problem line, subsystem, validation boundary, artifact contract, or
  user/operator-facing proof surface.
- Use roughly one focused AI hour of implementation plus validation as a
  calibration floor when coherent bundling is honest.
- Let larger milestones stay larger when that is the smallest coherent
  capability step.
- Keep tiny stories when they isolate a real high-risk unknown, unblock, or
  indivisible proof boundary.
- Treat the hour as a heuristic, not a quota, and do not pad scope just to hit
  a clock.

## Per-Repo Recommendation

| Repo | Recommendation | Reason |
| --- | --- | --- |
| Robo Rally | Source/update in place | Robo Rally already had the strongest "milestone stories, not micro-stories" language. Replace the too-literal `2-6 hour` phrasing with the calibrated one-hour heuristic plus explicit exceptions. |
| Dossier | Sync partially | Existing triage has same-line consolidation, but not the story-size calibration that prevents few-minute story shells after `create a story` remains the right vehicle. |
| Storybook | Sync partially | Existing triage treats story shells as packaging context, but should also teach the minimum useful work-package size when a new story is warranted. |
| doc-web | Sync partially | Existing anti-fragmentation review is strong, but the follow-up sizing heuristic helps prevent tiny artifact-chain story increments. |
| CineForge | Sync partially | Existing wording says not to fragment into tiny story shells; add the hour-as-heuristic calibration for media/runtime milestones. |
| Board Game Ingester | Sync partially | Existing fixture/eval/artifact boundary guidance should gain the practical sizing floor because visual/eval work can otherwise become a long string of tiny probes. |
| Echo Forge | Sync partially | Existing wording says a good story should advance table experience or execution truth; add the calibrated floor for coherent table/audio workflow milestones. |
| Conductor | Sync local supervisor guidance | Conductor routes inbox items and recommends/create stories across projects, so it should use the same sizing rule when packaging supervisor work. |

## Implementation

Target repo edits used isolated worktrees from `origin/main`:

`/Users/cam/.codex/worktrees/triage-story-sizing-calibration/<project-key>`

Branch:

`codex/triage-story-sizing-calibration`

| Repo | Worktree | Base | Result |
| --- | --- | --- | --- |
| Dossier | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/dossier` | `f5bf1c3` | Added few-minute-story calibration and explicit tiny-story exceptions. |
| Storybook | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/storybook` | `f8938b9` | Added the same sizing heuristic next to story-shell packaging guidance. |
| doc-web | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/doc-web` | `e224844` | Added artifact-chain sizing calibration after anti-fragmentation review. |
| CineForge | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/cine-forge` | `61c13d4` | Added runtime/media milestone sizing calibration. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/boardgame-ingester` | `866e524` | Added fixture/eval/artifact sizing calibration and guardrail reminder. |
| Robo Rally | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/roborally` | `d4eb374` | Replaced the literal `2-6 hour` guidance with the one-hour calibration heuristic, larger-milestone allowance, and tiny-story exceptions. |
| Echo Forge | `/Users/cam/.codex/worktrees/triage-story-sizing-calibration/echo-forge` | `08f7f08` | Added table/execution milestone sizing calibration. |
| Conductor | `/Users/cam/Documents/Projects/conductor` | `3fbf38a` | Added the same sizing rule to supervisor inbox/story routing guidance. |

Ran `./scripts/sync-agent-skills.sh` in every touched repo. Only
`.agents/skills/triage/SKILL.md` changed in each target because existing
wrappers did not need content updates.

## Validation

Checks that passed:

- Conductor: `./scripts/sync-agent-skills.sh --check`,
  `PYTHONDONTWRITEBYTECODE=1 make methodology-compile`,
  `PYTHONDONTWRITEBYTECODE=1 make methodology-check`, `make lint`,
  `git diff --check`
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

- Dossier's default `make methodology-check` in this isolated worktree used a
  system Python without `PyYAML`, so the validated command uses the repo's
  locked `uv` environment. The check passed and reported the repo's existing
  legacy metadata/non-local ADR warnings.
- CineForge `npm run methodology:check` still reports existing architecture
  audit and UI-scout freshness warnings, exits successfully, and the warnings
  are unrelated to this triage wording change.
- Storybook was rebased onto the current `origin/main` tip before commit. Its
  first push was rejected because `main` moved again; the branch was rebased
  onto `f8938b9` and the listed Storybook checks were rerun after the final
  rebase.

## Follow-Up

No Conductor story was created. This alignment is the durable routing record,
and the change intentionally avoids adding more story overhead to a
story-overhead fix.
