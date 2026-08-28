# Search playbook

## Daily core

1. Read `evaluated-models.md`, `source-scorecard.md`, the most recent daily
   report, `candidates.md`, and recent model scouts before searching. Match each
   lead against canonical IDs, aliases, and dated checkpoints before proposing
   owner work. An existing match suppresses a new-eval recommendation.
2. Check first-party release notes, model catalogs, API references, pricing,
   and official announcement accounts for OpenAI, Anthropic, Google/DeepMind,
   xAI, DeepSeek, Alibaba/Qwen, Moonshot/Kimi, Z.ai/GLM, Mistral, and MiniMax.
   For Qwen, check both the Qwen release blog and the matching QwenCloud model
   page: the former can name the open-weight release while the latter can
   establish the managed API ID, price, limits, and documented features.
3. Query OpenRouter's public `GET https://openrouter.ai/api/v1/models` for
   model IDs, routing, modalities, token limits, and advertised parameters.
   Treat it as discovery/access metadata only.
4. Rotate one small secondary slice: API release-note search, a credible
   technical-news/launch tracker, a model hub, a leaderboard, or an official
   account. Verify any material lead at a primary source.

## Search patterns

- `site:<provider-domain> "August" "2026" model API release`
- `<provider> API changelog latest model`
- `site:openrouter.ai <exact model family>`
- provider-specific model catalog and pricing endpoints documented in the
  relevant source; do not authenticate or call inference for discovery.

Use Twitter Scraper for X URLs/accounts and YouTube Transcripts for YouTube
sources when those connectors are available. Otherwise prefer official web
pages over search snippets.

## Cadence and failure handling

Check the core daily; rotate 2–4 secondary sources and replace low-yield,
redundant sources only after recorded evidence. Search results can lag primary
pages; a vendor benchmark proves neither quality in a maintained lane nor
production contract. Catalog `supported_parameters`, a generic JSON mode, or
HTTP success does not prove strict JSON Schema, enforced tools, served identity,
privacy, reliability, or callability for Cam's account/region.

Provider documentation can also lag or disagree across pages after a release.
When a release note, pricing table, and endpoint reference disagree, record the
exact conflict, use the newest model-specific API table only as documentation
evidence, and require an owner-side contract probe before treating the route as
callable or strict-contract qualified.

For an already evaluated model, a newly documented endpoint, price, feature, or
aggregator route is a monitoring update, not a new evaluation recommendation.
Recommend a clearly labeled re-evaluation only when current evidence satisfies
the exact retry condition recorded in `evaluated-models.md`. Documentation or
metadata does not by itself satisfy a callability, strict-contract, privacy,
reliability, latency, cost, or capability trigger.
