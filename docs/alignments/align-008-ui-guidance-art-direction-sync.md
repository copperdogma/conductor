# Alignment 008 — UI Guidance Art Direction Sync

**Date**: 2026-04-10
**Focus**: Compare Storybook and CineForge UI-development guidance against the
OpenAI front-end skill patterns captured in Scout 007 and decide what should
sync
**Source Project**: Baseline across `storybook` and `cine-forge`, with Scout
007 as the external reference
**Target Projects**: `storybook`, `cine-forge`, `dossier`, `doc-web`

## Surfaces Compared

- Conductor [Scout 007 — Evaluate OpenAI Frontend Guidance for UI Skill Upgrades](../scout/scout-007-openai-delightful-frontends.md)
- Storybook `AGENTS.md`
- Storybook `docs/runbooks/browser-automation.md`
- CineForge `AGENTS.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the goal is to align useful methodology meaning, not to force exact
  text identity.
- Alignment 006 already settled that `ui-scout` is a real methodology lane for
  Storybook and CineForge only. This pass is narrower: front-end build guidance
  for those UI-heavy repos.
- Scout 007 closed with `Adapt`, not `Adopt`: the OpenAI source is useful, but
  only as selective carry-through for UI-heavy repos.
- No narrower Conductor decision record was found for front-end prompt
  discipline, art-direction rules, or UI-specific reasoning defaults.

## Key Differences

- Storybook and CineForge already share the core UI build substrate:
  - `shadcn/ui` plus CSS-variable design tokens
  - design-in-browser theme showcase workflow
  - screenshot-verified build loops with browser tooling
  - `v0.dev` as an exploration aid rather than a production surface
- CineForge currently has the fuller internal workflow package in `AGENTS.md`:
  multi-step setup, visual-identity bootstrap, screenshot-verified loop,
  checkpoint timing, and mandatory reuse directives.
- Storybook has the same core principles, but currently expresses them as a
  concise bullet list rather than a full UI workflow with pre-build framing or
  composition rules.
- The OpenAI front-end skill adds a distinct layer that neither repo currently
  states explicitly:
  - low/medium reasoning as the default for front-end work
  - visual references / mood boards as a first-class input
  - pre-build `visual thesis`, `content plan`, and `interaction thesis`
  - stronger composition-first rules such as poster-like first viewport,
    cardless defaults, hero-content budget, and meaningful motion
  - grounding design work in real copy and product context rather than generic
    placeholder messaging
- Some OpenAI guidance is not universally portable:
  - full-bleed hero and promotional-surface rules fit marketing or visually led
    pages, not routine product workspaces
  - Storybook and CineForge both also need app-surface guidance where utility
    copy, dense workspace layouts, and restrained chrome remain correct
- Dossier and doc-web currently lack a corresponding UI methodology lane, so
  adding this guidance there would be structure-first busywork rather than a
  pressure-driven improvement.

## Classification

- **Portable improvement**: add explicit art-direction and prompting discipline
  to Storybook and CineForge UI guidance without changing their stack:
  reasoning defaults, reference/mood-board usage, pre-build framing, and
  composition-first constraints for visually led work.
- **Intentional adaptation**: keep CineForge's fuller workflow mechanics and
  reuse directives, keep Storybook's product/app-specific design-token
  guidance, and avoid applying marketing-surface rules to ordinary operational
  workspaces.
- **Methodology conflict**: none if the OpenAI guidance is treated as a
  selective layer on top of the existing token/theme/screenshot workflow rather
  than as a replacement.
- **Unclear drift**: Storybook may simply be missing the fuller AGENTS-level UI
  workflow articulation that CineForge already has, but the current evidence
  does not prove whether that omission is intentional minimalism or just
  documentation lag.

## Recommendation

- **storybook**: Sync partially. Keep Storybook's design-token, theme-route,
  and screenshot-loop guidance, but add the missing front-end prompting layer:
  low/medium reasoning default, real-content framing, mood-board/reference
  prompts, and explicit composition-first / cardless rules where the task is
  visually led.
- **cine-forge**: Sync partially. Keep CineForge as the internal reference for
  the fuller UI workflow, but add the same missing art-direction layer from
  Scout 007, especially `visual thesis`, `content plan`, `interaction thesis`,
  and reasoning-default guidance.
- **dossier**: Keep local. No active UI methodology lane exists, so do not
  install UI-specific guidance just for parity.
- **doc-web**: Keep local. No active UI lane or repeated front-end prompting
  pressure justifies this sync yet.

## Human Decision Needed

- None for the classification pass itself.
- If execution is desired, the narrow scope is: update Storybook and
  CineForge AGENTS-level UI guidance only. Do not broaden this into
  `setup-methodology`, Dossier, or doc-web unless separate UI pressure appears.

## Result

- Prepared dedicated target-repo worktrees on branches:
  - Storybook:
    `/Users/cam/.codex/worktrees/ui-guidance-art-direction-sync/storybook`
    on `codex/ui-guidance-art-direction-sync-storybook`
  - CineForge:
    `/Users/cam/.codex/worktrees/ui-guidance-art-direction-sync/cine-forge`
    on `codex/ui-guidance-art-direction-sync-cine-forge`
- Applied the selective UI-guidance carry-through in each target repo:
  - Storybook: updated `AGENTS.md` to add art-direction framing, reference
    usage, front-end reasoning defaults, composition-first guidance, and
    real-content grounding on top of the existing token/theme/screenshot loop
  - CineForge: updated `AGENTS.md` with the same art-direction layer while
    keeping CineForge's fuller UI workflow structure intact; refreshed the
    generated `docs/build-map.md` during methodology compile
- Verified the target patches with repo-local checks:
  - Storybook: `pnpm methodology:check`
  - CineForge: `pnpm methodology:compile` and `pnpm methodology:check`
- Landed the validated target branches onto remote `main`:
  - Storybook: `54b837f` (`Refine UI art direction guidance`)
  - CineForge: `11a1bf0` (`Refine UI art direction guidance`)

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  line is the alignment record plus the landed target-repo updates.
- Dossier and doc-web remain intentionally local for this slice unless future
  UI methodology pressure appears there.
