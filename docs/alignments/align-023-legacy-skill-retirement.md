# Alignment 023 - Legacy Skill Retirement

**Date:** 2026-04-29

## Focus

Inventory custom project skills before removing the old
`advice-for-past-self` context-reset helper, and identify any other custom
skills whose original purpose is now covered by current Codex context
compression, repo methodology, or stronger shared skills.

## Surfaces Compared

- Conductor `docs/ideal.md`, `docs/spec.md`,
  `docs/methodology/state.yaml`, `docs/methodology/graph.json`,
  `projects.yaml`, `inbox.md`, `docs/align-projects.md`, and
  `docs/scout.md`.
- `.agents/skills/*/SKILL.md` across Conductor and every tracked project:
  Dossier, Storybook, doc-web, CineForge, Board Game Ingester, Robo Rally,
  and Echo Forge.
- Legacy wrappers for the candidate skills in doc-web and Board Game Ingester.
- Existing issue-log data under `ai-work/issues` for skills that claimed to be
  durable memory.

The inventory found 221 `SKILL.md` files across Conductor plus the tracked
project skill surfaces.

## Findings

`advice-for-past-self` exists only in doc-web and Board Game Ingester. Its
premise is explicitly obsolete: it assumes the user will reset the chat, destroy
all context, and revert all code. Current Codex behavior preserves useful state
through automatic context compression, and the repo workflow now has story
logs, validation, and alignment memory for durable handoff.

`you-pick` also exists only in doc-web and Board Game Ingester. It asks the
agent to choose and start work from a hard-coded project-context list. That is
now weaker and riskier than the current `/triage` flow because it bypasses
Ideal/spec/state/graph, story worthiness, inbox routing, eval pressure, and the
yes-ready approval handoff.

`improve` exists only in doc-web and Board Game Ingester. Its instructions are
good generic engineering advice, but the behavior is now split more cleanly
across `/triage`, `/triage-health`, `/codebase-improvement-scout`,
`/improve-eval`, `/visual-inspect-loop`, and `/validate`. Keeping the broad
name makes it easy to invoke a stale, methodology-unaware analysis pass.

`fix-difficult-issue` exists only in doc-web and Board Game Ingester. It is
partly legacy because it says "the log is your memory" and assumes context will
be lost between sessions. It is not as clearly disposable as
`advice-for-past-self`, because it also provides a durable issue-log structure.
The only issue-log file found in this pass is doc-web
`ai-work/issues/onward-full-run-audit-reconciliation.md`, and its current state
is `Resolved` with no active issue.

The candidate skills all have generated Gemini wrappers in both affected repos:

- `.gemini/commands/advice-for-past-self.toml`
- `.gemini/commands/you-pick.toml`
- `.gemini/commands/improve.toml`
- `.gemini/commands/fix-difficult-issue.toml`

Both repos use `scripts/sync-agent-skills.sh` to regenerate wrappers from
`.agents/skills`, so removals should delete the canonical skill directories and
then rerun the sync script rather than hand-editing generated wrappers only.

## Classification

| Skill | Projects | Classification | Recommendation |
| --- | --- | --- | --- |
| `advice-for-past-self` | doc-web, Board Game Ingester | Obsolete legacy context-reset helper | Remove now. |
| `you-pick` | doc-web, Board Game Ingester | Obsolete pre-methodology autonomy prompt | Remove now with `advice-for-past-self` unless Cam wants a narrower deletion only. |
| `improve` | doc-web, Board Game Ingester | Redundant generic improvement prompt | Remove now or fold into `codebase-improvement-scout`; no unique current behavior found. |
| `fix-difficult-issue` | doc-web, Board Game Ingester | Legacy durable issue-log lane with one resolved doc-web artifact | Do not remove blindly. Either archive/migrate the resolved issue log first, or intentionally retire the skill while leaving historical `ai-work/issues` untouched. |
| `improve-skill` | Dossier, Storybook, CineForge, Robo Rally, Echo Forge | Still-useful retrospective lane | Keep. It improves skill/process instructions after a real interaction; it is not a context-reset helper. |
| `loop-verify` | Conductor plus all tracked projects | Still-useful delegated verification lane | Keep. It encodes bounded subagent review/fix rounds, not automatic context compression. |
| `create-cross-cli-skill` | All tracked product repos | Still-useful cross-CLI wrapper lane | Keep. It owns project-local skill and wrapper creation across Codex, Claude, Cursor, and Gemini. |
| `frontend-design` / `webapp-testing` | UI-capable repos | Still-useful cross-CLI local guidance | Keep. Codex has browser/frontend guidance, but these skills preserve local product expectations and support other CLIs. |

## Recommended Action

Create isolated target-repo worktrees for doc-web and Board Game Ingester, then
remove:

- `.agents/skills/advice-for-past-self/`
- `.agents/skills/you-pick/`
- `.agents/skills/improve/`

Run each repo's `./scripts/sync-agent-skills.sh` so stale Gemini wrappers are
removed, then validate with:

- doc-web: `./scripts/sync-agent-skills.sh --check`, `make methodology-check`,
  `git diff --check`
- Board Game Ingester: `./scripts/sync-agent-skills.sh --check`,
  `make methodology-check`, `make lint`, `git diff --check`

Handle `fix-difficult-issue` as a separate decision in the same story or a
follow-up:

- If Cam wants a clean retirement pass, remove it too after confirming the
  resolved doc-web issue log can remain as historical evidence.
- If Cam still wants a durable debug-log command, rewrite it later as a
  story-integrated debugging lane instead of a context-loss workaround.

## Human Judgment

The only judgment call is whether to include `fix-difficult-issue` in the first
deletion pass. The other three candidate skills have no current unique purpose
under the Ideal-first triage/story/eval workflow.

## Practical Impact

Removing the three clear candidates would cut stale command choices from
doc-web and Board Game Ingester and reduce the chance that an agent starts work
from old hard-coded context instead of current methodology evidence.

Keeping `fix-difficult-issue` out of the first automatic deletion avoids losing
a durable debugging pattern before deciding whether its one resolved issue-log
artifact should be archived, ignored as history, or folded into story memory.

## Result

Implemented the approved first deletion pass in isolated target-repo worktrees:

| Project | Worktree | Branch | Base | Result |
| --- | --- | --- | --- | --- |
| doc-web | `/Users/cam/.codex/worktrees/legacy-skill-retirement/doc-web` | `codex/legacy-skill-retirement` | `origin/main` at `efaa296` | Removed `advice-for-past-self`, `you-pick`, and `improve`, then regenerated wrappers. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/legacy-skill-retirement/boardgame-ingester` | `codex/legacy-skill-retirement` | `origin/main` at `6d35def` | Removed `advice-for-past-self`, `you-pick`, and `improve`, then regenerated wrappers. |

Each target repo deleted these files:

- `.agents/skills/advice-for-past-self/SKILL.md`
- `.agents/skills/improve/SKILL.md`
- `.agents/skills/you-pick/SKILL.md`
- `.gemini/commands/advice-for-past-self.toml`
- `.gemini/commands/improve.toml`
- `.gemini/commands/you-pick.toml`

Validation passed:

- doc-web: `./scripts/sync-agent-skills.sh --check` reported 23 skills and 23
  Gemini wrappers, `make methodology-check`, and `git diff --check`
- Board Game Ingester: `./scripts/sync-agent-skills.sh --check` reported 25
  skills and 25 Gemini wrappers, `make methodology-check`, `make lint`, and
  `git diff --check`

No commits or pushes were made. `fix-difficult-issue` was intentionally left in
place for a separate decision.
