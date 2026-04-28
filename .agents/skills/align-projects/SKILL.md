---
name: align-projects
description: Compare infrastructure surfaces across tracked projects and recommend what should sync
user-invocable: true
---

# /align-projects [optional focus]

Use this to compare shared-ish infrastructure surfaces across the tracked projects.

## Typical surfaces

- `AGENTS.md`
- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology-ideal-spec-compromise.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `docs/build-map.md`
- `docs/setup-checklist.md`
- `docs/runbooks/setup-methodology.md`
- `docs/scout.md`
- `docs/scout/`
- `docs/decisions/`
- `.agents/skills/`
- story templates
- skill sync tooling
- setup or methodology docs

## Steps

1. Read `projects.yaml` to identify the projects and comparison surfaces.
2. Choose the relevant surface area for this pass.
3. Compare the source and target projects.
4. Classify each important difference:
   - intentional adaptation
   - portable improvement
   - methodology conflict
   - unclear drift
5. Recommend per project:
   - sync now
   - sync partially
   - keep local
   - ask for a decision
6. Write an alignment entry under `docs/alignments/`.
7. Update `docs/align-projects.md`.
8. If warranted, create follow-up stories.

## Target-repo edit isolation

Alignment comparison may read from each project's primary checkout, but
alignment execution should not edit a tracked project's active checkout by
default. Assume each primary checkout may be serving current product work,
local validation, or another agent.

When an approved alignment pass needs target-project edits:

- inspect each target repo's current branch and `git status --short --branch`
  before deciding where to work
- create a dedicated worktree per target repo under
  `/Users/cam/.codex/worktrees/<task>/<project-key>` unless Cam explicitly asks
  to work in place
- create a task branch with the `codex/` prefix from `origin/main` unless the
  user names a different base branch
- keep one branch/worktree per target repo for cross-repo rollouts
- do not modify dirty primary checkouts, switch their branches, or clean their
  untracked files as part of supervisor work
- record the target worktree path, branch, base, and validation commands in the
  alignment entry when execution follows the recommendation
- still require explicit approval before committing, pushing, or landing target
  repo changes

Work in a primary checkout only when the user explicitly asks to continue that
checkout's current branch/work, and first confirm the local branch, status, and
which existing changes are in scope.

## Output shape

- surfaces compared
- key differences
- classification of those differences
- recommended next action by project
- what still needs human judgment

## Guardrails

- Do not force exact textual identity.
- Do not treat local product-specific adaptation as accidental drift by default.
- When methodology intent truly conflicts, surface it clearly and ask whether it should converge.
- Do not step on tracked project workspaces. Use isolated task worktrees for
  target-repo edits unless Cam explicitly requests in-place work.
