# Alignment 014 — Browser Testing Tool Choice Sync

**Date**: 2026-04-20
**Focus**: Decide whether the new Computer Use guidance should sync across the
tracked repos, and if so where
**Source Project**: Baseline across `storybook` and `cine-forge`, with recent
Computer Use and Playwright usage evidence from Storybook plus Conductor Scout
023
**Target Projects**: `storybook`, `cine-forge`, `dossier`, `doc-web`

## Surfaces Compared

- Conductor [Scout 023 — Evaluate OpenAI Codex Use Cases for Cross-Project Workflow Ideas](../scout/scout-023-openai-codex-use-cases.md)
- Storybook `AGENTS.md`
- Storybook `docs/runbooks/browser-automation.md`
- CineForge `AGENTS.md`
- CineForge `docs/runbooks/browser-automation-and-mcp.md`
- Dossier methodology notes around Story 078
- doc-web `testdata/README.md`

## Decision Context

- Scout 023 already recorded `QA an app with computer use` as a real current
  Codex use case, but explicitly as a selective reference rather than a
  portfolio-wide sync trigger.
- Storybook and CineForge both already have real browser-verification surfaces:
  interactive app UIs, screenshot-driven loops, and browser-tool runbooks.
- Dossier explicitly says it has no browser automation or screenshot surface.
- doc-web's maintained website lane is a checked-in static HTML seam, not live
  browser automation or URL-driven product testing.

## Key Differences

- Storybook already states `Vitest + Playwright` as its test stack and already
  documents a real-browser `computer` lane for Google OAuth pages where
  DOM-native extension tools do not work.
- CineForge already documents a richer browser-tool environment split across
  Playwright MCP, Claude-in-Chrome controls, and fallback operational recovery.
- Neither repo currently states the tool-choice rule explicitly enough:
  - Playwright is better when the main question is behavior, determinism, and
    repeatable validation.
  - Computer Use is better when the main question is visual judgment, native
    prompts, OAuth/account chooser flows, or blocked automation paths.
- Dossier and doc-web do not have enough browser-testing pressure to justify
  importing this guidance for parity alone.

## Classification

- **Portable improvement**: add a short explicit rule in Storybook and
  CineForge that says when to prefer Playwright, when to prefer Computer Use,
  and when to use both together.
- **Intentional adaptation**: keep the guidance only in repos with active
  browser-validation surfaces. Do not create fake portfolio drift by copying it
  into Dossier or doc-web.
- **Methodology conflict**: none, as long as Computer Use is framed as a
  complement to Playwright rather than a replacement for deterministic browser
  testing.
- **Unclear drift**: none after the selective-sync rule is made explicit.

## Recommendation

- **storybook**: Sync now. Update `AGENTS.md` and the browser automation
  runbook so the repo names the difference between Playwright and Computer Use,
  with special emphasis on visual judgment and OAuth-style real-browser flows.
- **cine-forge**: Sync now. Update `AGENTS.md` and the browser automation/MCP
  runbook with the same decision rule, adapted to CineForge's broader browser
  tooling matrix.
- **dossier**: Keep local. No browser automation surface exists, so this would
  be methodology noise.
- **doc-web**: Keep local. The maintained web-page lane remains a static
  checked-HTML surface, not a browser-automation lane.

## Human Decision Needed

- None for the selective-sync decision itself.
- If later one of the non-UI repos gains an honest browser-testing lane, rerun
  this alignment instead of copying the current wording forward by default.

## Result

- Prepared dedicated target-repo worktrees on branches:
  - Storybook:
    `/Users/cam/.codex/worktrees/storybook-computer-use`
    on `codex/computer-use-guidance-20260420`
  - CineForge:
    `/Users/cam/.codex/worktrees/cineforge-computer-use`
    on `codex/computer-use-guidance-20260420`
- Applied local-only documentation updates in those worktrees:
  - Storybook `AGENTS.md`
  - Storybook `docs/runbooks/browser-automation.md`
  - CineForge `AGENTS.md`
  - CineForge `docs/runbooks/browser-automation-and-mcp.md`
- No Dossier or doc-web files were changed.

## Follow-Up

- If Cam wants these changes landed, the next step is repo-local verification
  plus intentional commit/push in the two target worktrees.
- Conductor now has a durable record for why this sync applied only to
  Storybook and CineForge.
