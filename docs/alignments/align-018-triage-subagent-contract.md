# Alignment 018 — Triage Subagent Contract

Date: 2026-04-28

## Focus

Make unscoped `/triage` explicit enough that a cautious runtime treats it as
authorization for contracted subagent fan-out.

The previous rollout said lane packets may be parallelized when the environment
and user instructions allow it. In practice, that left room for a higher-level
runtime guard to conclude that `/triage` did not explicitly request subagents.

## Classification

Portable improvement.

## Decision

Tracked repos should phrase unscoped `/triage` as a contracted fan-out command:

- invoking unscoped `/triage` is explicit authorization to use the runtime's
  subagent/delegation tool for neutral lane packets when it is available and
  safe for the current checkout
- the main thread keeps the north star: Ideal/spec/state synthesis, direct fact
  script execution, top-three ranking, and the final recommendation
- subagents gather lane evidence; they do not decide the repo-wide answer
- if subagents are unavailable, unsafe for the checkout, or the user asks not to
  use them, triage runs the same lane-packet contracts sequentially and states
  that fallback in the response

This preserves the loop-verify finding that one truth change must be propagated
through the top-level triage skill and companion runbook together.

## Updated Worktrees

- Storybook — `/Users/cam/.codex/worktrees/triage-orchestration/storybook`
- Dossier — `/Users/cam/.codex/worktrees/triage-orchestration-rollout/dossier`
- doc-web — `/Users/cam/.codex/worktrees/triage-orchestration-rollout/doc-web`
- CineForge — `/Users/cam/.codex/worktrees/triage-orchestration-rollout/cine-forge`
- Board Game Ingester — `/Users/cam/.codex/worktrees/triage-orchestration-rollout/boardgame-ingester`
- Robo Rally — `/Users/cam/.codex/worktrees/triage-orchestration-rollout/roborally`
- Echo Forge — `/Users/cam/.codex/worktrees/triage-orchestration-rollout/echo-forge`
- Conductor — `/Users/cam/Documents/Projects/conductor`

## Validation

- Storybook: `bash scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`, `git diff --check`
- Dossier: `./scripts/sync-agent-skills.sh --check`, `PYTHON='uv run --frozen python' make methodology-check`, `git diff --check`
- doc-web: `./scripts/sync-agent-skills.sh --check`, `make methodology-check`, `git diff --check`
- CineForge: `./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, `git diff --check`
- Board Game Ingester: `./scripts/sync-agent-skills.sh --check`, `make methodology-check`, `git diff --check`
- Robo Rally: `npm run skills:check`, `npm run methodology:check`, `git diff --check`
- Echo Forge: `npm run skills:check`, `npm run methodology:check`, `git diff --check`
- Conductor: `make skills-check`, `make methodology-check`, `git diff --check`

All checks passed. CineForge still reports its existing architecture/UI freshness
warnings, and Dossier still reports existing non-local ADR / legacy metadata
warnings.
