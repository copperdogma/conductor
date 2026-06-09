# Scout 044 - Evaluate Claude Fable 5 API Eval Opportunities

**Source**: Anthropic release announcement, Claude API model overview,
pricing page, and migration guide checked 2026-06-09.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Anthropic released Claude Fable 5 on 2026-06-09 with the API model ID
`claude-fable-5`. The official docs position it as Anthropic's strongest
widely released model for demanding reasoning and long-horizon agentic work.
It has a 1M-token context window, 128k max output, always-on adaptive thinking,
and the same broad Messages API shape as Opus 4.8, but with Fable-specific
thinking/refusal behavior and higher pricing.

The practical cost fact dominates the routing decision: Fable 5 is $10 / MTok
input and $50 / MTok output, twice Opus 4.8's $5 / MTok input and $25 / MTok
output. Prompt-cache hits are still much cheaper than fresh input, but this is
not a model to trial as a high-volume default unless it deletes enough
pipeline complexity or crosses a quality gate that cheaper frontier models
cannot cross.

This is a real eval trigger, not a portfolio-wide model switch. Treat it as a
ceiling model for hard, maintained eval lanes where one of these could be true:

- a single stronger call might beat a multi-stage pipeline
- a blocked semantic, OCR, or long-context gate might move
- a once-per-project creative/deep-analysis pass could justify high per-run cost
- an evaluator/judge role needs the strongest available reasoning

Do not use it for routine chat, volume extraction, UI copy, ordinary agent
workers, mechanical validation, or any lane where the current winner is already
cheap, fast, and good enough.

## Project Relevance

- **dossier**: `Spike` and the best first fit. Dossier has the most mature
  benchmark/default-promotion discipline, and its hardest questions are exactly
  where Fable might matter: long-prose/entity graph extraction, relationship
  overproduction suppression, identity continuity, and single-shot ceiling
  probes. The first useful run should be a benchmark-only ceiling pass, not a
  runtime default proposal. Candidate lanes: C1 Big Fish/single-shot detector,
  W8-style long-prose architecture repeat, or a narrow extraction/adjudication
  quick-smoke where Opus 4.8 and cheaper models left classified model-wrong
  gaps. Guardrail: no default promotion unless registry evidence clears
  quality, latency, and cost against the current Dossier defaults.
- **doc-web**: `Spike` with cost controls. Fable is plausible for the hardest
  image/document understanding seams: page-context crop deletion, crop
  validation, and blocked handwritten OCR screens. It should be tested only as
  a ceiling or failed-case rerun, because page-image workloads can burn tokens
  quickly and the repo already has cheaper working crop validators. Candidate
  lanes: `crop-page-level-deletion-gate`, a bounded handwritten OCR screen, or
  one failed crop/page-context case set. Guardrail: use the existing
  Anthropic-direct provider pattern and record full image-token cost.
- **cine-forge**: `Defer` unless a specific high-value creative/script lane is
  active. Fable may be useful for character depth, scene analysis, script bible,
  or creative-direction quality where one expensive once-per-project result is
  acceptable. But Opus 4.8 already proved "strong challenger, not default" on
  maintained lanes, and CineForge's defaults are explicitly value-selected.
  Candidate lane if approved: one `character-extraction` or `script-bible`
  model-slot pass. Guardrail: it must beat both quality target and cost story,
  not merely feel smarter.
- **echo-forge**: `Defer/spike later`. The scene-to-soundscape mapper has an
  explicit new-flagship retry trigger, so Fable is a legitimate future
  challenger for structured selected-scene outlines. It is not relevant to live
  audio generation, catalog matching, or the current local matcher substrate.
  Candidate lane: `scene-to-soundscape-golden` only if mapper quality is the
  active bottleneck. Guardrail: compare to GPT-5.4 Mini's value-winning
  baseline and keep Fable as an oracle/ceiling unless it materially improves
  table-facing quality.
- **storybook**: `Reject for chat default; defer for narrow synthetic ceiling
  tests`. Evaluating Fable as Luna's normal chat model would be wasteful:
  Storybook's chat lane is high-volume, privacy-sensitive, latency-sensitive,
  and already tracks per-turn cost tightly. Fable could be considered only for
  synthetic/golden artifact-understanding or Journey Scout-style ceiling
  questions after the owning upstream Dossier/doc-web lanes are ruled out.
- **boardgame-ingester**: `Defer`. The repo has AI-first eval scaffolding and
  may eventually benefit from a strong multimodal/long-context rulebook model,
  but the current evidence points at product/eval substrate and deterministic
  crop/package readiness before expensive frontier calls. Revisit once a
  concrete LLM subject lane exists for rulebook inventory extraction or
  asset-to-inventory matching.
- **roborally**: `Reject for now`. The current repo shape is scenario and eval
  scaffold work, not a maintained model-comparison lane. Fable should not be
  introduced until there is a specific source-rules extraction or opponent
  reasoning eval where a model is the actual bottleneck.
- **conductor**: `Adapt`. Keep this scout and use it to route follow-up inbox
  notes only for repos with concrete lanes. Do not create a shared Fable policy.

## Ranking

1. **Dossier** - highest expected value. It has hard semantic extraction
   problems, benchmark infrastructure, and enough cost discipline to keep the
   trial honest.
2. **doc-web** - second, but only on small hard-document/OCR slices because
   image-token costs can swamp the value.
3. **CineForge** - third if Cam wants a once-per-project creative/script
   ceiling comparison; otherwise defer.
4. **Echo Forge** - legitimate future mapper challenger, not current default
   work.
5. **Board Game Ingester** - plausible later, premature now.
6. **Storybook** - no chat-default eval; only narrow synthetic ceiling tests.
7. **RoboRally** - no current fit.

## Recommended Actions

1. If doing one paid eval first, do **Dossier** with `claude-fable-5` as a
   benchmark-only ceiling model.
2. If doing a second, do **doc-web** on a tiny failed-case document/OCR slice.
3. Do not run a Storybook Luna chat default comparison.
4. Do not append target-repo inbox notes until Cam approves the handoff list;
   target repos should each receive one short note naming candidate, lane,
   baseline, and cost/privacy guardrail.

## Evidence

- Anthropic release announcement:
  https://www.anthropic.com/news/claude-fable-5-mythos-5
- Claude model overview:
  https://platform.claude.com/docs/en/about-claude/models/overview
- Claude pricing:
  https://platform.claude.com/docs/en/about-claude/pricing
- Opus 4.8 to Fable 5 migration guide:
  https://platform.claude.com/docs/en/about-claude/models/migration-guide

## Confidence

High that Fable 5 is a real callable API model and a valid ceiling-model eval
trigger. Medium on repo-level wins until the target harnesses measure quality,
latency, refusal behavior, and cost with live credentials. Low that it should
become any high-volume runtime default soon.

## Open Questions

- Which target repos currently have working Anthropic API keys in their
  repo-local env wrappers?
- Does promptfoo's built-in Anthropic provider still send any parameters that
  Fable rejects, or can the existing Opus 4.8 direct-provider shims be reused?
- Does always-on adaptive thinking inflate visible-output budget or latency
  enough to fail existing target gates?
- Do safety/refusal stop reasons need explicit handling in any eval runner
  before the first paid run?
