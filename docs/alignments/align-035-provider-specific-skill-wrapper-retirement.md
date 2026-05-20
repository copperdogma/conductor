# Alignment 035 - Provider-Specific Skill Wrapper Retirement

**Date**: 2026-05-19
**Classification**: Portable improvement
**Source**: [Scout 037](../scout/scout-037-google-antigravity-skills-and-cli.md)
**Story**: [Story 017](../stories/story-017-retire-provider-specific-skill-wrappers.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Decision

Treat `.agents/skills/<name>/SKILL.md` as the canonical repo skill package
across Conductor and the tracked repos.

Provider-specific surfaces are no longer part of required skill sync when the
provider can discover standard Agent Skills directly. They are one of two
explicitly separate compatibility categories:

- **Compatibility links**: cheap symlinks such as `.claude/skills`,
  `.cursor/skills`, or `skills` pointing back to `.agents/skills` where a tool
  still benefits from them. Do not add `.gemini/skills` by default because
  current Gemini CLI already reads `.agents/skills` and reports duplicate
  conflicts when both paths exist.
- **Command aliases**: generated slash-command shims such as
  `.gemini/commands/*.toml`. These may exist when a repo wants typed
  slash-command UX, but they are not proof that skills are synced.

Do not create provider-specific skill variants unless a concrete tool still
requires a distinct format. The default skill-creation and setup workflow should
write standard `SKILL.md` packages and then refresh compatibility links.

## Rationale

Scout 037 found that Google Antigravity and Gemini CLI now support standard
`SKILL.md` skills under `.agents/skills`. The old generated Gemini command
wrapper layer was useful when Google-specific discovery needed a separate
surface, but it now creates drift-prone generated files and extra validation
noise without improving the canonical skill package.

This also matches Conductor's core tenets:

- canonicalize meaning, not provider-specific text
- preserve repo-local adaptation when a repo proves it needs command aliases
- recommend and record the cross-project contract before rolling changes
- keep methodology overhead small enough to remove work rather than create it

## Contract

`scripts/sync-agent-skills.sh` should default to this proof:

- canonical skill folders exist under `.agents/skills`
- compatibility links point back to `.agents/skills`
- `make skills-check` validates the canonical skill package and links
- command aliases are optional and checked only through an explicit alias mode

Skill-creation guidance should use the same split:

- create or edit `.agents/skills/<name>/SKILL.md`
- use `scripts/`, `references/`, `assets/`, and templates inside that skill
  package when useful
- run the repo's skill-surface check
- generate provider-specific aliases only when the repo intentionally keeps
  them for UX compatibility

## Rollout Plan

Conductor goes first:

- remove `.gemini/commands/*.toml` from the required tracked surface
- update `scripts/sync-agent-skills.sh`
- update setup, learning-candidate, setup-checklist, runbook, and repo-check
  wording
- attempt one Google-side skill discovery smoke after workspace trust is
  handled, or record the exact trust/install blocker

Then roll the semantic contract to target repos in isolated worktrees:

- inventory each repo's current `scripts/sync-agent-skills.sh`, package
  scripts, setup-methodology skill, setup checklist/runbooks, and generated
  command wrappers
- patch only the surfaces that exist locally
- preserve optional command aliases where local evidence says they are still
  needed
- validate with each repo's native skill/methodology checks and
  `git diff --check`

## Stop Conditions

- Do not edit target primary checkouts.
- Do not delete command aliases from a repo that proves it still depends on
  typed slash-command UX.
- Do not invent a local skill-creator surface in repos that do not have one.
- Do not call the rollout complete until target repos have applied patches or a
  precise deferred reason.
- Do not make Conductor a canonical shared harness repository.

## Rollout Evidence

Story 017 build applied the contract in Conductor and seven isolated target
worktrees. No target primary checkout was edited.

| Project | Worktree branch base | Canonical skills | Removed required aliases | Evidence |
| --- | --- | ---: | ---: | --- |
| conductor | `7cf737e` on `codex/retire-provider-specific-skill-wrappers` | 17 | 17 | `gemini --skip-trust skills list` found all workspace skills from `.agents/skills`; default `make skills-check` passed. |
| dossier | `17fc8ca` on `codex/skill-wrapper-retirement-20260519` | 31 | 31 | `make skills-check`, `make methodology-compile`, `make methodology-check`, `make triage-facts-check`, and `git diff --check` passed using the Dossier venv. Existing legacy/non-local methodology warnings remain unrelated. |
| storybook | `8239ef7` on `codex/skill-wrapper-retirement-20260519` | 36 | 36 | `pnpm methodology:compile`, `scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`, `pnpm triage:facts:check`, and `git diff --check` passed. |
| doc-web | `ba94d4b` on `codex/skill-wrapper-retirement-20260519` | 27 | 27 | `make skills-check`, `make methodology-compile`, `make methodology-check`, `make triage-facts-check`, `make lint`, and `git diff --check` passed. |
| cine-forge | `f11bfee` on `codex/skill-wrapper-retirement-20260519` | 38 | 37 | `make skills-check`, `make triage-facts-check`, `npm run methodology:compile`, `npm run methodology:check`, and `git diff --check` passed. Existing architecture-audit and UI-scout freshness warnings remain unrelated. |
| boardgame-ingester | `343d3a2` on `codex/skill-wrapper-retirement-20260519` | 28 | 28 | `make skills-check`, `make methodology-compile`, `make methodology-check`, `make triage-facts-check`, `make lint`, and `git diff --check` passed. |
| roborally | `1f184e4` on `codex/skill-wrapper-retirement-20260519` | 30 | 30 | `npm run methodology:compile`, `npm run methodology:check`, `npm run skills:check`, `npm run triage-facts:check`, and `git diff --check` passed. |
| echo-forge | `e21ad1b` on `codex/skill-wrapper-retirement-20260519` | 37 | 37 | `npm run methodology:compile`, `npm run methodology:check`, `npm run skills:check`, direct text and JSON `node scripts/triage-facts.mjs` smokes, and `git diff --check` passed. Configured `npm run triage-facts:check` is blocked in this worktree because `vitest` is not installed. Existing `No Ideal requirements parsed` methodology warning remains unrelated. |

The target patches all keep `.agents/skills/<name>/SKILL.md` canonical, refresh
`.claude/skills`, `.cursor/skills`, and `skills` compatibility links, ignore
`.gemini/commands/` as generated optional alias output, and update local
triage/fact surfaces so absent command aliases no longer count as skill drift.

Validation follow-up tightened the Conductor implementation after `/loop-verify`
and `codex review` found closeout gaps: default skill checks now validate
compatibility-link targets, optional alias checks validate alias names and
content, and doc-web's methodology active-surface list includes its
`create-cross-cli-skill` skill. The targeted Conductor and doc-web checks
passed after those fixes.

A final strict confirmation pass found no remaining Story 017 material issue.
One expanded Dossier unit probe exposed an unchanged main-branch test drift:
`python -m pytest tests/test_triage_facts.py tests/unit/test_methodology_graph.py
-q` fails because `tests/unit/test_methodology_graph.py` still expects the old
W8 retry triggers while the current generator and `docs/methodology/graph.json`
use the newer `materially-new-local-helper` /
`seed-pass-reuse-with-quality-preservation` triggers. Those files have no
Story 017 diff against `origin/main`, so the failure is recorded as a
pre-existing Dossier follow-up rather than a blocker to this rollout.

Finish-and-push landed the linked target repo updates on `main`: Dossier
`6f309fd`, Storybook `e295fa3`, doc-web `99450a3`, CineForge `0b5ae05`, Board
Game Ingester `b822102`, Robo Rally `a0d8029`, and Echo Forge `7766b8e`.
