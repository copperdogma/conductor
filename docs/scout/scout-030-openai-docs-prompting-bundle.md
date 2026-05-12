# Scout 030 - Evaluate OpenAI Docs and Prompting Bundle for Tracked Workflows

**Source**: Conductor inbox bundle:
`https://developers.openai.com/learn/docs-mcp`,
`https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide`,
`https://developers.openai.com/api/docs/guides/prompt-guidance?model=gpt-5.5`,
`https://github.com/openai/skills/tree/main/skills/.curated/openai-docs`, and
`https://github.com/openai/skills/blob/main/skills/.system/openai-docs/references/upgrade-guide.md`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Reviewed the official OpenAI docs/prompting bundle on 2026-05-12.

The useful move is not to copy the OpenAI skill or rewrite every project prompt
immediately. The useful move is to make OpenAI-product work more current and
less speculative:

- use the OpenAI Docs MCP as the preferred retrieval path for OpenAI API,
  Codex, Apps SDK, Agents SDK, model, and prompt-upgrade questions
- treat the OpenAI Docs skill as a reference workflow for model-selection,
  model-upgrade, and prompt-upgrade tasks
- use GPT-5.5 guidance as a prompt-shaping reference when a repo is actually
  moving a model or prompt, especially around outcome-first instructions,
  reasoning-effort choice, preambles, `phase`, output shape, retrieval budgets,
  and validation rules
- keep upgrades narrow: model string and directly related prompt surfaces first,
  with repo evals or realistic spot checks before changing defaults

This is a strong cross-project reference bundle because several tracked repos
periodically touch OpenAI model slugs, prompt templates, Responses workflows,
structured outputs, or Codex-facing methodology text. It should become a
Conductor scout memory and a future alignment/story-prep input, not raw inbox
pressure.

## Project Relevance

- **conductor**: `Adapt`. Use this scout when routing future OpenAI model,
  prompt, skill, plugin, or docs-MCP notes. Do not make Conductor the canonical
  copy of OpenAI guidance; keep it as a routing and comparison surface.
- **dossier**: `Adapt`. Strong fit for benchmark/model refreshes, Responses
  workflow checks, structured extraction prompts, and prompt-upgrade gating.
  Preserve Dossier's measured benchmark discipline before promoting defaults.
- **storybook**: `Adapt`. Useful for prompt/model changes in storytelling,
  agentic workflow, or structured-output surfaces. Adoption should go through
  Storybook's eval and product-quality gates, not a blanket prompt cleanup.
- **doc-web**: `Adapt`. Useful for maintained OpenAI-provider checks, prompt
  refreshes, extraction/HTML pipeline prompts, and docs lookup during runtime
  upgrades. Keep doc-web's source-faithfulness and artifact contracts as the
  acceptance gate.
- **cine-forge**: `Adapt`. Useful for AI pipeline prompt upgrades, provider
  capability routing, and long-running Responses/tool-heavy flows. Do not
  promote new defaults without measured quality, latency, cost, and artifact
  checks.
- **boardgame-ingester**: `Adapt cautiously`. Useful if OpenAI-backed
  rulebook/component extraction or prompt templates become active; otherwise
  keep as reference memory.
- **roborally**: `Defer`. RoboRally is headless-first and not currently driven
  by OpenAI prompt/model pressure. Revisit when AI opponent or UI-agent work
  introduces real OpenAI integration choices.
- **echo-forge**: `Adapt`. Useful for structured scene-outline and soundscape
  prompt work, especially when comparing model quality or moving model slugs.
  Keep live-table behavior and eval/golden evidence as the proof surface.

## Recommendation

- Keep this scout as `Adapt`.
- Do not create immediate repo-local inbox notes for every tracked project.
- Do not roll out a blanket OpenAI Docs MCP or `openai-docs` skill rule across
  all repo `AGENTS.md` files yet.
- Story 011 / Alignment 028 generalize the durable part of this scout: fresh
  upstream docs are an active dependency for drift-prone provider/component
  work, while local Ideal/spec/evals remain the adoption gate.
- Use the bundle as the default reference when an OpenAI-related task appears:
  1. verify current OpenAI guidance from official docs first
  2. preserve explicit target models when the user names them
  3. keep model/prompt upgrades narrow and behavior-preserving
  4. leave historical docs, eval baselines, fixtures, examples, and fallback
     paths unchanged unless explicitly in scope
  5. require repo-native validation before default promotion
- Create a future Conductor alignment or story only when a concrete OpenAI
  model/prompt change needs to be propagated across multiple tracked repos.

## Evidence

- OpenAI's Docs MCP page says the hosted MCP provides read-only search and page
  content for OpenAI developer docs, is documentation-only, and can be added to
  Codex as `openaiDeveloperDocs`.
- That page also recommends adding repo instructions so agents use the OpenAI
  developer documentation MCP for OpenAI API, ChatGPT Apps SDK, and Codex work.
- The GPT-5.5 prompt guidance says shorter, outcome-first prompts often work
  better than process-heavy prompt stacks, and that low/medium reasoning should
  be re-evaluated before escalating.
- The same guidance keeps preambles, `phase` handling, and assistant-item
  replay important for tool-heavy Responses workflows, and calls out explicit
  personality, retrieval budgets, and validation rules for customer-facing and
  agentic UX.
- The Codex prompting guide documents how `AGENTS.md` files are discovered and
  injected from `~/.codex` through the repo root to the current directory, which
  matches why repo-local prompt and methodology instructions should stay
  explicit and scoped.
- The OpenAI `openai-docs` skill defines OpenAI docs as the source of truth for
  OpenAI questions, model selection, model migration, and prompt-upgrade
  guidance.
- The OpenAI upgrade-guide reference keeps GPT-5.5 upgrades narrow: update
  active model strings and directly related prompts, preserve explicit targets,
  avoid broad SDK/tooling/provider migrations, and validate with existing tests,
  spot checks, or eval suites.
- Existing Conductor memory already covers adjacent OpenAI workflow sources:
  Scout 023 for general Codex use cases and Scout 026 for the Build Web Apps
  plugin. This scout is narrower: OpenAI docs retrieval, prompt/model upgrade
  posture, and skill-guided upgrade workflow.

## Confidence

High. The sources are official OpenAI documentation and the recommendation is
conservative: adapt as a reference and routing rule, but wait for concrete
repo-local pressure before changing prompts or defaults.

## Open Questions

- Should Conductor later add a small OpenAI-docs lookup rule to shared skill
  guidance, or is the current user-level docs skill enough?
- Which repo will next need a measured OpenAI model/prompt refresh: Dossier,
  doc-web, CineForge, Storybook, or Echo Forge?
- Should a future model-release routing story include a standard compatibility
  checklist derived from this scout?
