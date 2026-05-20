# Alignment 038 - Harness Navigation and Context-Debt Review

**Date**: 2026-05-20
**Classification**: Portable review rule with local adaptation
**Source**: [Scout 039](../scout/scout-039-claude-code-large-codebase-practices.md)
**Story**: [Story 020](../stories/story-020-harness-navigation-context-debt-review.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Focus

Evaluate Scout 039's Claude large-codebase guidance against the current
distributed harness before adopting anything new.

The user constraint is the controlling rule: inspect each repo first, document
what already exists and how it works, then adopt only changes with high
expected value. "Might be useful" is a reject or defer signal because every new
instruction, tool, hook, checklist, or file adds carrying cost.

Surfaces compared:

- `AGENTS.md`, README, setup checklist, setup runbook, state, scout, and
  alignment docs where present
- `.agents/skills` and `.claude` / `.cursor` / `skills` compatibility links
- `.codex/environments/environment.toml`, `scripts/codex-setup`, local runtime
  scripts, Makefile, package scripts, and repo-native validation commands
- `.gitignore` coverage for dependency folders, build outputs, media/input
  folders, runtime logs, caches, benchmark outputs, and generated command dirs
- codebase-improvement, story, scout, and setup notes that already mention
  root-instruction size, stale process, wrong-file edits, or context overhead
- primary checkout status and `origin/main` where the primary checkout was
  behind or actively dirty

No target repo files were edited during this inventory.

## Inventory Summary

| Project | Existing harness/navigation surfaces | Generated/noise/runtime coverage | Review decision |
| --- | --- | --- | --- |
| Conductor | 113-line `AGENTS.md`; 18 skills; scout/alignment/story methodology; `.codex` setup hook; Makefile methodology and skill checks. | Minimal `.gitignore`; few generated surfaces. | No target change. Conductor already owns recommendation-first comparison. |
| Dossier | 366-line `AGENTS.md`; 31 local skills, 32 on `origin/main`; README, build map, setup docs, runbooks, Makefile, pyproject; compat links. | `.gitignore` covers Python envs, caches, output/logs/tmp/runtime, evals, tests corpus, input, generated commands. | Defer root slimming. Local scout evidence says generic short AGENTS is the wrong tradeoff while scaffolding remains active. |
| Storybook | 419-line `AGENTS.md`; 36 local skills, 37 on `origin/main`; archived build-map redirect, long setup runbook, local-service and local-dev port surfaces, package scripts. | `.gitignore` covers node deps, builds, coverage, logs, runtime, voice eval output, backups, input PDFs, generated commands. | Defer root review until a local setup/methodology refresh or observed agent confusion. Size alone is not enough. |
| Doc Web | 478-line `AGENTS.md`; 28 skills; README with many fixture recipes; build map, setup docs, Makefile, pyproject. | `.gitignore` covers input/output, venv/build, debug/elements JSONL, Playwright MCP, local settings, generated commands. | Defer. There is a long-doc smell, but the one wrong-module note found is specific to patch-file support, not a repeated navigation failure. |
| CineForge | 709-line `AGENTS.md`; 38 local skills, 39 on `origin/main`; large build-map, setup docs, local-service, package/Makefile/pyproject. | `.gitignore` covers Python/Node deps, builds, reports, envs, input/output/logs/tmp, generated promptfoo packets, tests corpus, browser artifacts. | Adopt existing owner only. Story 103 already owns AGENTS runbook extraction and the latest codebase-improvement report calls it out. Do not create parallel work. |
| Board Game Ingester | 123-line `AGENTS.md`; 29 skills on `origin/main`; setup docs and Makefile; compact repo map. | `.gitignore` covers Python env/caches, output with benchmark exceptions, cache, PSD templates, generated commands. | Reject new navigation work. Current surface is compact enough. |
| Robo Rally | 66-line `AGENTS.md`; 31 skills on `origin/main`; setup docs, package scenario scripts, methodology checks. | `.gitignore` covers node deps, build artifacts, private input, runtime, logs, generated commands. | Reject new navigation work. Current surface is small and headless scenario truth is already obvious. |
| Echo Forge | 263-line `AGENTS.md` on `origin/main`; 38 skills on `origin/main`; rich `.codex` run actions, local-service, registry/catalog scripts. | `.gitignore` covers node deps, envs, builds, coverage/logs, input, tmp, campaign-protected inputs. | Defer. Current active checkout is dirty Story 053 work; origin baseline is moderate and already has runtime/action surfaces. |

Primary checkout state was intentionally treated as part of the inventory.
Dossier, Storybook, CineForge, and Robo Rally primary checkouts were behind
`origin/main`; Storybook had an untracked GEDCOM file; CineForge had a local
deploy-log edit; Board Game Ingester and Echo Forge were on active story
branches. Any future target changes should start from refreshed isolated
worktrees.

## Candidate Scoring

| Candidate | Decision | Expected-value note |
| --- | --- | --- |
| Add a portfolio-wide LSP/code-intelligence requirement | Reject | The inventory did not find repeated wrong-symbol, wrong-module, or search-noise failures that local docs and `rg` cannot handle. Benefit is speculative; overhead includes setup, maintenance, and false confidence. Reversible, but not worth adding now. Confidence: high. |
| Add a new generated-file exclusion checklist or ignore layer across repos | Defer | Existing `.gitignore` coverage is already substantial and repo-specific. No current evidence shows agents repeatedly reading dependency or media artifacts because of missing shared ignore guidance. Benefit plausible, overhead moderate. Confidence: medium. |
| Extract CineForge root AGENTS procedural detail into runbooks | Adopt existing owner | There is concrete evidence: 709-line `AGENTS.md`, a 2026-05-19 codebase-improvement report naming the issue, and draft Story 103 already scoped to a 300-line target. Benefit is direct context reduction; overhead is bounded because the repo already owns the story. Confidence: high. |
| Slim Dossier, Storybook, and Doc Web root instructions now | Defer | These files are long, but they encode local safety/product/test constraints. Dossier has explicit local evidence that generic shortening is the wrong tradeoff right now. Storybook and Doc Web should be reviewed only when a local refresh or observed confusion creates a concrete failure mode. Confidence: medium. |
| Add more path-command tables/build maps everywhere | Reject for now | Most repos already expose README, Makefile, package, setup, build-map, or local-service command surfaces. Adding more tables without a failing workflow increases documentation drift. Confidence: high. |
| Make EV-overhead scoring a Conductor scout/alignment rule | Adopt in this record | The main failure mode is over-adopting external agent advice. A lightweight recorded rule costs almost nothing and keeps future scouting honest without changing target repos. Confidence: high. |
| Create target repo stories immediately | Reject | Only CineForge has clear local ownership already; creating duplicate target stories would add coordination overhead. Other repos need a local trigger first. Confidence: high. |

## Recommendation

Do not roll out a new tool, hook, LSP layer, ignore standard, or root-instruction
rewrite across the portfolio.

Record the portable rule instead:

> External coding-agent practice scouts must inventory existing repo surfaces
> before recommending adoption. A candidate must name the observed or likely
> failure mode, concrete benefit, added overhead, reversibility, and confidence.
> Low-confidence "might help" additions default to reject or defer.

The only high expected value target action found is to preserve and, when
CineForge hygiene is next, prioritize CineForge's existing Story 103 AGENTS
runbook extraction rather than creating parallel Conductor work.

## Practical Impact

Cam gets the value from the Claude large-codebase article without importing its
tooling stack. The portfolio keeps its existing repo-local harness, avoids
speculative methodology sprawl, and has one concrete high-value target to
consider when CineForge context debt becomes the active lane.
