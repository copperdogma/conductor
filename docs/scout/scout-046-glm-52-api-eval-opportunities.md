# Scout 046 - Evaluate GLM-5.2 API Eval Opportunities

**Source**: Z.ai developer docs, Z.ai Coding Plan docs, Z.ai Hugging Face model
card, FrontierSWE, Terminal-Bench, Scale MCP-Atlas, and Vals SWE-bench pages
checked 2026-06-16.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Numbering Note

This worktree's `docs/scout.md` currently ends at Scout 043, but git refs show
Scout 044 already exists on `codex/fable-5-conductor-scout`, and prior memory
mentions a Scout 045 Browser artifact that is not present in this checkout.
This scout uses 046 to avoid an avoidable ID collision while preserving the
current worktree's existing files.

## Summary

GLM-5.2 is a real Z.ai model release, not just a social announcement. The
official docs expose `glm-5.2` for coding-agent use, `glm-5.2[1m]` as the
1M-context Claude Code suffix, and Z.ai API pricing for GLM-5.2. The Hugging
Face model card exposes open MIT weights under `zai-org/GLM-5.2` and
`zai-org/GLM-5.2-FP8`.

The product shape matters for routing:

- text input and text output only
- 1M context and 128K max output in Z.ai docs
- function calling, structured output, MCP, streaming, and context caching
- OpenAI-compatible examples for local/self-hosted serving and coding-tool use
- Z.ai API pricing of `$1.40 / 1M` input, `$0.26 / 1M` cached input, and
  `$4.40 / 1M` output

The benchmark story is strong but uneven. GLM-5.2 looks unusually credible for
long-horizon coding, repository-scale engineering, and long-context text work,
but most published score tables are still vendor/model-card reports. FrontierSWE
is the strongest independent-looking public signal found in this pass; the
official Terminal-Bench 2.1 and Scale MCP-Atlas pages checked today do not yet
show a GLM-5.2 row, so Z.ai/Hugging Face rows for those benchmarks should be
treated as self-reported until independently reproduced.

## Public Score Read

Public results checked in this pass:

- **FrontierSWE**: public leaderboard ranks GLM-5.2 third, with average rank
  `4.32` and `74%` dominance, just behind Claude Opus 4.8 and ahead of GPT-5.5
  on the page checked today.
- **Hugging Face / Z.ai model card coding table**: reports `62.1` on
  SWE-bench Pro, `48.9` on NL2Repo, `46.2` on DeepSWE, `81.0` on
  Terminal-Bench 2.1 with Terminus-2, `82.7` on Terminal-Bench 2.1 best
  reported harness, `74.4` FrontierSWE dominance, `34.3` PostTrainBench, and
  `13.0` SWE-Marathon.
- **Hugging Face / Z.ai reasoning and agentic table**: reports `40.5` HLE,
  `54.7` HLE with tools, `99.2` AIME 2026, `91.2` GPQA-Diamond, `76.8`
  MCP-Atlas public set, and `48.2` Tool-Decathlon.
- **Terminal-Bench official 2.1 page**: did not list GLM-5.2 yet; it listed
  GLM 5.1 as an older row at `58.7% +/- 2.4`.
- **Scale MCP-Atlas page**: did not list GLM-5.2 yet on the checked page; it
  listed GLM-5.1 among older public/all-task rows.
- **Vals SWE-bench Verified page**: did not list GLM-5.2 yet on the checked
  page; it listed GLM 5.1 in the model list.

Practical read: this is not a universal default-model trigger. It is a bounded
new-subject-model trigger for repos where long-context text, structured JSON,
or model-assisted code/repo work is already measured.

## Project Relevance

- **dossier**: `Spike`. Best first fit. Dossier has the clearest maintained
  model-ladder and extraction benchmark culture, plus prior OpenAI-compatible
  provider paths for xAI, Moonshot/Kimi, and Google. GLM-5.2 should be screened
  as a text-only extraction/adjudication challenger, not as a runtime default.
  Start with a Z.ai provider smoke, then a C1/C5 quick-smoke or benchmark-script
  slice that already records quality, schema validity, latency, and cost. Watch
  structured-output compatibility: GLM claims structured output/function call
  support, but Dossier should verify Instructor/raw-JSON behavior before any
  full private-document run.
- **cine-forge**: `Spike`. Good second fit. GLM-5.2's strongest public signals
  are long-horizon coding and long-context engineering, but CineForge also has
  text-heavy screenplay/script-bible/entity-discovery lanes where model rankings
  have historically inverted on full-text tasks. Evaluate only on text/script
  modules first, such as script bible, entity discovery, prompt compilation, or
  scene analysis. It is not a render, video, image, or previz provider.
- **echo-forge**: `Defer/spike`. Plausible later for the structured
  soundscape-extractor value eval because the repo already compares provider
  outputs on scene-to-structured-outline quality. Do not interrupt current
  catalog/recipe work or re-open provider-generated live-table audio. Add GLM
  only when the extractor value lane is already being refreshed.
- **doc-web**: `Defer`. GLM-5.2 is text-only, while doc-web's most active model
  pressure is multimodal crop/OCR/page-image evaluation. It may become useful
  for text-only post-OCR/table repair or born-digital long-context cleanup, but
  it should not displace the current OpenAI/Gemini/Anthropic VLM challenger
  lanes.
- **storybook**: `Reject for Luna default now; defer for upstream extraction`.
  GLM-5.2's public strengths do not target warm private family dialogue,
  voice-era persona, or privacy-sensitive memory conversation. Storybook should
  benefit through Dossier if Dossier proves an extraction win. A synthetic Luna
  challenger is possible later only after Z.ai provider privacy posture and
  Vercel/AI-SDK integration are explicit.
- **boardgame-ingester**: `Defer`. Relevant later for rulebook text extraction,
  inventory inference, and asset naming if a story is already adding a
  model-backed subject. Current eval truth is still seed package readiness, CV
  crops, and deterministic reviewed asset inventory; GLM-5.2 should not jump
  that queue.
- **roborally**: `Reject for now`. Current RoboRally value is deterministic
  rules implementation and scenario behavior. GLM-5.2 could help a future
  source-rules extraction spike, but there is no current LLM runtime/default
  lane to evaluate.
- **conductor**: `Adapt`. Keep this scout memory and recommend repo-local evals;
  do not create a shared GLM-5.2 mandate.

## Repo Handoffs

No target-repo inbox notes were added in this pass. Several likely target
checkouts are active or dirty (`dossier`, `storybook`, `cine-forge`,
`echo-forge`), and Conductor's guardrail says direct target-project changes
should happen in dedicated worktrees. If Cam approves handoff, create concise
repo-local inbox notes for Dossier and CineForge first.

## Recommended Actions

1. If doing one eval first, use **Dossier**: add a narrow Z.ai
   OpenAI-compatible provider smoke and run a cheap text-only extraction or
   adjudication challenger slice.
2. If doing a second eval, use **CineForge** on one text-heavy screenplay lane;
   do not route GLM-5.2 into previz/render/video.
3. Do not spend doc-web budget on GLM-5.2 until there is a text-only post-OCR
   or table-repair question. It is not a VLM/OCR replacement.
4. Do not evaluate Storybook Luna defaults now. Let Dossier prove or disprove
   extraction value first.
5. Before any private payload run, record Z.ai account/API privacy posture and
   whether the eval uses hosted Z.ai, GLM Coding Plan, or self-hosted MIT
   weights.

## Evidence

- Z.ai GLM-5.2 model docs:
  https://docs.z.ai/guides/llm/glm-5.2
- Z.ai pricing:
  https://docs.z.ai/guides/overview/pricing
- Z.ai quick start:
  https://docs.z.ai/guides/overview/quick-start
- Z.ai Coding Plan model-switch docs:
  https://docs.z.ai/devpack/latest-model
- Z.ai Coding Plan overview:
  https://docs.z.ai/devpack/overview
- Hugging Face model card:
  https://huggingface.co/zai-org/GLM-5.2
- Hugging Face FP8 model card:
  https://huggingface.co/zai-org/GLM-5.2-FP8
- FrontierSWE leaderboard:
  https://www.frontierswe.com/
- Terminal-Bench 2.1 leaderboard:
  https://www.tbench.ai/leaderboard/terminal-bench/2.1
- Scale MCP-Atlas leaderboard:
  https://labs.scale.com/leaderboard/mcp_atlas
- Vals SWE-bench Verified page:
  https://www.vals.ai/benchmarks/swebench

## Confidence

High that GLM-5.2 is a real, callable, open-weight, long-context text model and
a legitimate eval trigger for Dossier and CineForge. Medium on actual local
quality until each repo proves Z.ai transport, structured output, latency, cost,
and privacy posture in its own harness. Low that it should be evaluated for
Storybook chat defaults, doc-web image/OCR gates, or RoboRally's current
deterministic behavior work.

## Open Questions

- Does Cam have a Z.ai API key, and does the hosted API policy meet the privacy
  bar for any non-synthetic Dossier/CineForge payload?
- Does GLM-5.2's structured-output support work cleanly with the repo-local
  promptfoo/Instructor paths, or does it need a raw OpenAI-compatible shim?
- Is self-hosting `zai-org/GLM-5.2` or `zai-org/GLM-5.2-FP8` practical enough
  to matter locally, or should initial evaluation stay hosted?
