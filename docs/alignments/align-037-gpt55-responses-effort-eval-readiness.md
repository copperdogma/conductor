# Alignment 037 — GPT-5.5 Responses Effort Eval Readiness

**Focus**: Carry Dossier's new eval-only OpenAI Responses reasoning-effort pattern into the tracked repos that may need model-value evals.
**Source Project**: dossier
**Target Projects**: storybook, doc-web, cine-forge, boardgame-ingester, roborally, echo-forge

## Surfaces Compared

- Dossier commit `7456021` (`Evaluate GPT-5.5 reasoning effort`)
- Dossier `evals/providers/openai_responses_cost_provider.py`
- Dossier `evals/gpt55-responses-effort-smoke.yaml`
- Dossier `docs/stories/story-152-gpt55-responses-reasoning-effort-benchmark.md`
- Dossier `docs/evals/registry.yaml`
- Target repo `docs/evals/README.md`
- Target repo `.agents/skills/create-eval/SKILL.md` where present
- Target repo `.agents/skills/improve-eval/SKILL.md`
- Existing target Responses provider surfaces in Storybook, doc-web, and CineForge

## Key Differences

- Dossier added the newest portable substrate: a tiny Promptfoo custom provider
  that calls the OpenAI Responses API, accepts `reasoning.effort`, records
  cached/reasoning token metadata, estimates cost, and keeps the run eval-only.
- doc-web already had measured GPT-5.5 Responses results and a custom
  `chat-latest` Responses helper, but that helper did not take effort config or
  report cached/reasoning token metadata.
- Storybook already had a local OpenAI Responses provider with `reasoningEffort`
  support for Luna synthetic evals, but its token usage report did not surface
  cached/reasoning details.
- CineForge already had a Promptfoo Responses provider with
  `reasoning_effort`; it reported reasoning tokens but not cached input tokens.
- Board Game Ingester, Robo Rally, and Echo Forge have eval registry guidance,
  but no repo-specific rule telling future eval work to prefer a bounded
  reasoning-effort sweep over an opaque one-model retest.

## Classification

- **Intentional adaptation**: Do not copy Dossier's exact Mariner promptfoo
  config into other repos. Each repo's eval subject, runner, provider privacy,
  and runtime-default gates are local.
- **Portable improvement**: Add shared eval workflow guidance for bounded
  `low` / `medium` / `high` effort sweeps, and record quality, latency, cost,
  cached-input tokens, reasoning tokens, and "do not retry" outcomes before
  any runtime/default promotion.
- **Portable improvement**: Where a repo already owns an OpenAI Responses
  provider, surface the token metadata needed to compare effort tiers honestly.
- **Methodology conflict**: None found. The improvement strengthens existing
  eval-ladder and cost/latency discipline rather than changing target product
  behavior.
- **Unclear drift**: Whether Echo Forge should add a dedicated custom Responses
  provider is still open. Its current promptfoo task can use provider config
  guidance first; add code only when a concrete eval needs it.

## Execution

Target edits were made in isolated worktrees from `origin/main`, not in primary
checkouts:

| Project | Worktree | Branch | Base | Changes |
|---|---|---|---|---|
| Storybook | `/Users/cam/.codex/worktrees/gpt55-effort-readiness/storybook` | `codex/gpt55-effort-eval-readiness` | `0328dd8` | Added effort-sweep guidance to create/improve eval docs and eval README; added cached/reasoning token details to `packages/backend/src/ai/evals/openai-responses-provider.mjs`. |
| doc-web | `/Users/cam/.codex/worktrees/gpt55-effort-readiness/doc-web` | `codex/gpt55-effort-eval-readiness` | `37ef4af` | Added effort-sweep guidance to improve-eval docs and eval README; extended `benchmarks/providers/openai_chat_latest_responses.py` to accept effort/verbosity config and report cached/reasoning token details. |
| CineForge | `/Users/cam/.codex/worktrees/gpt55-effort-readiness/cine-forge` | `codex/gpt55-effort-eval-readiness` | `2a39893` | Added effort-sweep guidance to create/improve eval docs and eval README; added cached prompt token reporting to `benchmarks/providers/openai_responses_provider.py`. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/gpt55-effort-readiness/boardgame-ingester` | `codex/gpt55-effort-eval-readiness` | `d3d5142` | Added effort-sweep guidance to improve-eval docs and eval README. |
| Robo Rally | `/Users/cam/.codex/worktrees/gpt55-effort-readiness/roborally` | `codex/gpt55-effort-eval-readiness` | `40b82fe` | Added effort-sweep guidance to create/improve eval docs and eval README. |
| Echo Forge | `/Users/cam/.codex/worktrees/gpt55-effort-readiness/echo-forge` | `codex/gpt55-effort-eval-readiness` | `5bec49b` | Added effort-sweep guidance to create/improve eval docs and eval README. |

## Validation

- Storybook: `node --check packages/backend/src/ai/evals/openai-responses-provider.mjs`, `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`, and `git diff --check` passed.
- doc-web: `python3 -m py_compile benchmarks/providers/openai_chat_latest_responses.py`, `make skills-check`, `make methodology-check`, and `git diff --check` passed.
- CineForge: `python3 -m py_compile benchmarks/providers/openai_responses_provider.py`, `./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, and `git diff --check` passed. Existing methodology warnings remain unrelated: architecture audit domains and UI scout freshness.
- Board Game Ingester: `make skills-check`, `make methodology-check`, and `git diff --check` passed.
- Robo Rally: `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed.
- Echo Forge: `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. Existing `No Ideal requirements parsed` warning remains unrelated.

## Recommendation

- **dossier**: Keep local. Its Story 152 result is the source evidence and
  should not imply runtime Responses migration or broader GPT-5.5 reruns.
- **storybook**: Sync now. It already had a synthetic OpenAI Responses provider;
  the metadata and guidance make future effort-tier evals clearer.
- **doc-web**: Sync now. It already relies on GPT-5.5 Responses for a maintained
  page-context gate, so effort/metadata readiness is directly useful.
- **cine-forge**: Sync now. Its benchmark provider already accepts effort; the
  missing cached-token metadata was a small gap.
- **boardgame-ingester**: Sync partially. Guidance only; no provider code until
  a concrete model-backed eval needs it.
- **roborally**: Sync partially. Guidance only; current evals are behavior-first
  and should not grow a promptfoo/provider dependency prematurely.
- **echo-forge**: Sync partially. Guidance only for now; add provider code only
  when the soundscape extractor eval actually needs effort/cost metadata beyond
  built-in promptfoo support.

## Human Decision Needed

- Commit/push the six target worktree branches when Cam wants this readiness
  rollout landed. No primary target checkout was edited.
