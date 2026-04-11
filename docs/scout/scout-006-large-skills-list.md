# Scout 006 — Evaluate the Large Skills List for Portable Additions

**Source**: `https://x.com/zodchiii/status/2034924354337714642`
**Status**: Reject
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source is a curated social recommendation list rather than a methodology or
product artifact, so the real question is not "which skills are popular?" but
"does this list expose a missing capability the tracked repos do not already
cover?"

The answer is no.

The list clusters around seven recommendations:

1. `frontend-design`
2. `simplify`
3. `browser-use` / `agent-browser`
4. `shannon` (security)
5. `test-driven-development`
6. `Composio / Connect`
7. `antigravity awesome-skills`

After comparing those against the current portfolio, none of them justifies a
new shared skill adoption line.

- `frontend-design` was already handled more honestly in Scout 007: selective
  UI-guidance adaptation for Storybook and CineForge, not a broad portfolio
  skill sync.
- `simplify` overlaps with the repos' existing cleanup and hygiene lanes, which
  are already more repo-aware than a generic post-build simplifier.
- `browser-use` overlaps with the existing browser-automation and verification
  workflow already carried in the local methodology and the current Codex tool
  surface.
- `shannon` overlaps with Conductor's existing `security-audit` lane, and its
  active pentesting posture is too heavy to import casually as ambient workflow.
- `test-driven-development` does not outrank the portfolio's stronger
  repo-native validation contracts: eval-first, promptfoo, artifact inspection,
  browser verification, and integration-heavy checks where applicable.
- `Composio / Connect` would add a generic OAuth/integration layer without a
  measured repo-side need for cross-SaaS action automation.
- `antigravity awesome-skills` is breadth, not leverage. It is the exact shape
  of list-induced scope creep Conductor should resist.

The only durable lesson worth keeping is methodological, not functional:
external skill bundles are useful as selective idea mines, but most should be
rejected unless they close a real repeated workflow gap. That lesson is already
compatible with the tracked repos' existing local-skill strategy.

## Project Relevance

- **dossier**: `Reject`. Dossier already has repo-local eval improvement,
  promptfoo benchmarking, and codebase-improvement scouting. The list does not
  expose a missing Dossier skill category that outranks those local surfaces.
- **storybook**: `Reject`. The only meaningful overlap, `frontend-design`, was
  already captured more precisely in Scout 007, while generic TDD and browser
  skills are weaker than Storybook's current promptfoo plus runtime/browser
  verification loop.
- **doc-web**: `Reject`. doc-web already has stronger repo-native eval and
  artifact-validation discipline than anything in this list besides the already
  generic browser/integration suggestions.
- **cine-forge**: `Reject`. CineForge already carries promptfoo, browser
  verification, and cleanup-scanning lanes. No source item shows a sharper
  CineForge-side gap than those existing workflows.

## Recommendation

- Reject this as a shared external skill-adoption line.
- Do **not** create a Conductor story and do **not** hand this off to any
  target-project inbox.
- Do **not** import breadth bundles or marketplace starter packs into the
  tracked repos merely because they are popular.
- Keep three narrow lessons only:
  1. evaluate skill lists by repeated-workflow leverage, not by popularity
  2. invoke important skills explicitly instead of relying on vague trigger
     matching
  3. when a workflow keeps being re-explained locally, build the repo-native
     skill instead of installing a broad external bundle
- If this general question resurfaces later, the honest follow-up is a targeted
  gap hunt against one repo's actual repeated friction, not another marketplace
  browsing pass.

## Confidence

- Medium-high. The source itself is lightweight, but the reject decision is
  grounded in current local methodology surfaces plus prior scout memory for
  overlapping external skill bundles.

## Evidence

- `https://x.com/zodchiii/status/2034924354337714642`
- Twitter Scraper fallback note:
  - the X connector resolved tweet `2034924354337714642` but only exposed the
    short-link shell, so content extraction fell back to a public mirror of the
    same list
- `https://www.reddit.com/r/claude/comments/1s51b5u/the_claude_code_skills_actually_worth_installing/`
- Overlap and prior-scout context:
  - `/Users/cam/.codex/worktrees/5cf1/conductor/docs/scout/scout-001-superpowers-dossier-research-automation.md`
  - `/Users/cam/.codex/worktrees/5cf1/conductor/docs/scout/scout-007-openai-delightful-frontends.md`
  - `/Users/cam/.codex/worktrees/5cf1/conductor/docs/scout/scout-014-agent-skills-test-consolidation-hard-cut.md`
  - `/Users/cam/.codex/worktrees/5cf1/conductor/.agents/skills/security-audit/SKILL.md`
  - `/Users/cam/Documents/Projects/dossier/AGENTS.md`
  - `/Users/cam/Documents/Projects/dossier/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/AGENTS.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/doc-web/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/.agents/skills/codebase-improvement-scout/SKILL.md`
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`
  - `/Users/cam/Documents/Projects/cine-forge/.agents/skills/codebase-improvement-scout/SKILL.md`

## Open Questions

- If a future scout finds a genuinely missing skill lane, should Conductor land
  it as a repo-native skill template, an alignment pass, or a single target-
  repo story instead of another marketplace import?
