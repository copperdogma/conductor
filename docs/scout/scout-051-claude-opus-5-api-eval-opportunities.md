# Scout 051 - Evaluate Claude Opus 5 API Eval Opportunities

**Source**: Anthropic model docs and authenticated Anthropic/OpenRouter API
checks performed 2026-07-24.
**Status**: Spike
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Claude Opus 5 is not announcement-only. It is visible and callable today:

- Anthropic's authenticated Models API returned `claude-opus-5`, display name
  `Claude Opus 5`, created `2026-07-24`.
- A native Anthropic Messages request returned HTTP 200, served-model
  `claude-opus-5`, terminal `end_turn`, valid usage, and `API_OK`.
- OpenRouter's public catalog exposes `anthropic/claude-opus-5` at
  `$5/M` input and `$25/M` output. An authenticated request returned HTTP 200,
  provider `Anthropic`, served model `anthropic/claude-opus-5`, terminal
  `stop`, valid usage, and `API_OK`.

The native API is the best first eval route because it proves Anthropic's own
contract and served identity. OpenRouter is a confirmed fallback or parity
route, not a reason to obscure the native result.

Anthropic documents a 1M context window, 128k maximum output, adaptive thinking
on by default, `low` through `max` effort, multimodal input, and regular pricing
unchanged from Opus 4.8 at `$5/M` input and `$25/M` output. It is also listed for
AWS, Google Cloud, and Microsoft Foundry. Anthropic positions the largest gains
in deep reasoning, long-horizon agents, code review, vision, long context, and
multi-agent coordination.

The default-thinking change matters to existing harnesses. A deliberately tiny
16-token native probe spent the entire output budget on thinking and returned
`max_tokens` with no visible text. Repeating with `output_config.effort=low`
and 256 output tokens returned `API_OK`. Repo evals must therefore set effort
and output budget deliberately, capture thinking usage, and not misclassify
budget exhaustion as model quality.

## Recommended Eval Order

### 1. Dossier - evaluate now

**Decision**: `Spike`, highest priority.

Dossier has the broadest decision-bearing provider-native model workflow:
structured extraction, adjudication, judging, relationship/projection quality,
and a benchmark-only raw Anthropic Messages path. Opus 5 is a better practical
ceiling challenger than Fable 5 for routine evaluation because it is half
Fable's price and does not carry Fable's documented 30-day-retention-only
constraint.

Start with access/native/strict-schema/harness-parity qualification, then the
smallest maintained runtime quick-smoke against current defaults. Progress to
broader extraction/adjudication/judge gates only if it clears the early quality,
latency, cost, privacy, and safety gates. Compare at a predeclared effort level;
do not give Opus 5 an unbounded `max` run against ordinary incumbent settings.

### 2. doc-web - evaluate now

**Decision**: `Spike`, second priority.

Opus 5's vision claim and the repo's already maintained Anthropic Messages
adapter make this the cleanest multimodal hard-gate test. Run the maintained
`image-crop-extraction` detector first against Gemini 3 Flash. Only if it clears
that prerequisite should it enter the `crop-page-level-deletion-gate` against
the GPT-5.5 validator. The prior Sonnet 5 result (`5/13` detector and `20/22`
page context) is not predictive of a claimed step-change Opus release, but it
does make the progressive stop rule important.

Before scoring, update or override the adapter so Opus 5's default thinking,
effort, output budget, strict task schema, finish reason, and served model are
all explicit. Use public/approved fixtures until provider retention is recorded
for this exact route.

### 3. CineForge - bounded follow-on

**Decision**: `Spike after the first two`, medium priority.

Opus 5 is plausibly useful for full-script understanding, world/bible
construction, continuity reasoning, and ordered-frame or QA judgment. The best
first lane is a maintained text/vision decision surface with a current quality
gap, not the expensive full Big Fish pipeline. Qualify strict structured output
and run one representative full-script or ordered-frame gate against the
current Gemini/Kimi evidence. Stop if the early result cannot meet the repo's
latency and cost budget; adaptive thinking can make a long pipeline especially
expensive.

### 4. Storybook - defer unless a live product decision reopens

**Decision**: `Defer`.

Opus models have historically been strong on Storybook's identity-sensitive
document work, but the narrowed C3 identity gate already passes and its registry
says the next action is implementation simplification, not another model sweep.
Do not spend merely to refresh the model name. Reopen Opus 5 only for a current
Luna/artifact-grounded conversation decision, a richer ambiguous-identity
fixture, or a material architecture change. Start with synthetic/golden
fixtures because the repo contains private family material.

## Other Tracked Repos

- **Board Game Ingester**: `Defer`. Revisit when a maintained long-context
  rulebook/component eval has a model-owned quality gap.
- **RoboRally**: `Defer`. The private source PDF and rules-model path need an
  owning story and explicit payload approval before a frontier call.
- **Echo Forge**: `Defer`. Opus 5 is not an audio model; only reconsider it for
  a maintained structured mapper or planning gate.
- **Conductor**: `Adapt`. Preserve the route and staged recommendation; do not
  create a shared model default.

## Recommendation

Authorize two owning-repo evaluations now, in order:

1. Dossier provider-native runtime quick-smoke.
2. doc-web progressive crop detector, then page-context only on a detector pass.

Keep CineForge as the first bounded follow-on. Do not route Storybook or the
other tracked repos until a concrete maintained decision surface reopens.

No target-repo inbox or story was created in this scout pass. That handoff
should follow Cam's approval of the proposed order so recommendation does not
turn into ambient work pressure.

## Evidence

- Anthropic model overview:
  https://platform.claude.com/docs/en/about-claude/models/overview
- Anthropic "What's new in Claude Opus 5":
  https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5
- Anthropic Models API:
  `GET https://api.anthropic.com/v1/models`
- Anthropic Messages API:
  `POST https://api.anthropic.com/v1/messages`
- OpenRouter Models API:
  `GET https://openrouter.ai/api/v1/models`
- OpenRouter Chat Completions:
  `POST https://openrouter.ai/api/v1/chat/completions`

## Confidence and Open Questions

**Confidence**: High on native Anthropic and OpenRouter availability and on the
first two repo priorities. Medium on CineForge leverage until a narrow owning
surface is selected. Low that Storybook needs another model run without a new
product or architecture trigger.

Open questions for owning-repo execution:

- Does each repo have its own approved Anthropic credential and retention
  posture, rather than relying on a credential visible only in this session?
- Does strict structured output pass natively and through the repo adapter with
  thinking enabled?
- Which `effort` level is fair against each maintained incumbent, and how much
  output headroom is required to avoid hidden thinking-budget truncation?
- Does Opus 5 clear hard quality gates at a cost/latency point that could
  actually change a maintained default?
