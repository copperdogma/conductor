# Scout 001 — Evaluate Superpowers for Dossier-First Research Automation

**Source**: `https://github.com/obra/superpowers`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source is real and current, but it is not primarily a research-automation
system. `obra/superpowers` is a prescriptive coding-agent workflow package:
skills are installed into Codex through a symlinked skill directory, then the
repo pushes a standard engineering loop around brainstorming, explicit plans,
git worktrees, subagent execution, code review, and TDD.

That makes it a credible design-reference bundle for coding-agent ergonomics,
not a direct Dossier-first research-automation upgrade. The strongest Codex-
specific material is operational: the Codex docs show a lightweight install
path, the tool-mapping guide explains how their task-dispatch model maps onto
Codex agents, and the Codex App compatibility design records concrete worktree
and detached-HEAD handling. Those are useful workflow notes, but they do not
outrank the tracked repos' existing methodology package.

Compared with the current portfolio, the main mismatch is methodological rather
than technical. Dossier already has a richer repo-specific system around
`docs/ideal.md`, `docs/spec.md`, methodology state/graph, story ownership,
eval-first development, and deep-research tooling. Conductor also explicitly
treats the harness as distributed and recommendation-first. Superpowers is much
closer to a generic external execution style than to a missing shared research
or supervisor substrate.

## Project Relevance

- **dossier**: `Defer`. Highest relative relevance, but as a workflow
  reference, not as a Dossier research-automation layer. The potentially useful
  pieces are narrow: Codex skill-install/distribution patterns, explicit
  worktree-environment detection, and stricter subagent review loops.
- **storybook**: `Defer`. Possible future value if Storybook wants a more
  packaged Codex workflow bundle or sharper implementation-discipline guidance,
  but not as a product or runtime feature.
- **doc-web**: `Defer`. Limited current value. This does not materially improve
  document intake, OCR, or transformation confidence on its own.
- **cine-forge**: `Defer`. Possible later workflow-reference value, but it does
  not address a current CineForge product or methodology bottleneck.

## Recommendation

- Keep this at `Defer`.
- Do **not** treat Superpowers as a current cross-project sync candidate and do
  **not** frame it as Dossier-side research automation.
- Do **not** create a Conductor story or a target-repo story from this scout
  alone. There is no concrete repo-side pressure strong enough to justify a
  handoff right now.
- If a tracked repo later hits a specific workflow pain around Codex skill
  packaging, subagent review loops, or worktree behavior in managed Codex
  sessions, revisit this source as a design-reference bundle.
- If revisited, lift only the narrow ideas that fit the local methodology:
  1. Codex-native skill installation and update ergonomics
  2. explicit environment detection for managed worktrees / detached HEAD
  3. tighter implementation-review loops for code-writing tasks
- Do **not** import the package wholesale. Its strongly prescriptive
  skill-before-anything and TDD-first posture conflicts with the tracked repos'
  current eval-first, story-owned methodology.

## Confidence

- Medium-high. The repo and Codex-specific surfaces were read directly from the
  primary source, and the fit judgment is grounded in current local methodology
  docs from Conductor and Dossier, but I did not install or run Superpowers in
  a live Codex session.

## Evidence

- `https://github.com/obra/superpowers`
- `https://raw.githubusercontent.com/obra/superpowers/main/docs/README.codex.md`
- `https://raw.githubusercontent.com/obra/superpowers/main/.codex/INSTALL.md`
- `/tmp/scout-superpowers/skills/using-superpowers/SKILL.md`
- `/tmp/scout-superpowers/skills/using-git-worktrees/SKILL.md`
- `/tmp/scout-superpowers/skills/using-superpowers/references/codex-tools.md`
- `/tmp/scout-superpowers/docs/superpowers/specs/2026-03-23-codex-app-compatibility-design.md`
- Inbox note: `DOSSIER DOING NOW`
- Local methodology context:
  - `/Users/cam/Documents/Projects/dossier/AGENTS.md`
  - `/Users/cam/.codex/worktrees/7be2/conductor/docs/spec.md`
  - `/Users/cam/.codex/worktrees/7be2/conductor/docs/scout/scout-012-codex-app-plugin-surface.md`
  - `/Users/cam/.codex/worktrees/7be2/conductor/docs/scout/scout-021-operator-workflow-notes-bundle.md`

## Open Questions

- If Dossier later wants a reusable external Codex workflow bundle, is a
  plugin/package distribution path materially better than the current local
  methodology + skill-sync setup?
- Are there specific tracked-repo implementation failures that would justify
  adopting only the subagent-review or environment-detection patterns without
  importing the rest of the package?
