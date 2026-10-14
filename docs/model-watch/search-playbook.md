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


## 2026-09-07 retrieval refinements

- Use the current month in searches (for example September 2026), but inspect
  official release dates; freshly crawled pages can describe old checkpoints.
- If the central ledger has no exact match, search existing owner attempt
  records before declaring a first evaluation. Sonnet 5's June attempt was
  absent centrally. Record gaps as corrections without editing this watch's
  read-only evaluated ledger.
- If web retrieval of a public catalog endpoint fails, one unauthenticated
  direct HTTP GET may recover the metadata; record both outcomes.
- Rotate Artificial Analysis release discovery, then verify at exact official
  model cards. Prefer those cards over Hugging Face's noisy global recency feed.
- Monitor exact K2 Horizon managed-route appearance; do not repeat its open-weight
  announcement or incur hosting/setup work while access remains unchanged.


## 2026-10-12 — explicit decision-model daily core

Cam added decision models as a first-class watch category. Existing owner evaluations are tracked, but prior general-purpose-only search did not guarantee daily decision-source coverage. This scope update supersedes earlier specialist/small/derived exclusions for decision models with plausible maintained-lane fit.

Check a compact daily core alongside general-purpose sources:

| Source | Retrieval / purpose |
| --- | --- |
| [TypeSafe models](https://docs.typesafe.ai/models) | JEV pinned versions, moving aliases, native System One contracts and releases |
| [OpenAI Decisions](https://developers.openai.com/api/docs/guides/decisions) | Official Docs MCP first; supported exact models, native endpoint and release changes |
| [Microsoft Foundry Decision docs](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision), [announcement](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/) | Exact Microsoft checkpoints, deployments and typed contracts |
| [Perplexity Decisions](https://docs.perplexity.ai/api-reference/decisions-post), [Decider creator card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b) | Hosted versus open checkpoint/revision, endpoint-specific terms and new releases |
| [Qwen decision API](https://docs.qwencloud.com/api-reference/decision-model-api), [release notes](https://docs.qwencloud.com/changelog/models) | Decision service identities and material contract/access changes |
| [OpenRouter decision catalog](https://openrouter.ai/api/v1/models?output_modalities=decisions), [API discovery](https://openrouter.ai/skills/) | Public decision metadata separately from generation catalog; discover successors and providers |

Follow current source links to successor cards/catalogs rather than assuming these recorded checkpoints stay latest. General generation-catalog absence does not imply decision-model absence. Keep model ID, served revision, deployment and endpoint/configuration separate; protocol similarity does not prove shared weights. A new endpoint on an already evaluated model is a possible endpoint/configuration re-evaluation subject to its recorded gate, not a first evaluation.

Track Noul/predicate, finite Choice, ordered Score, probabilities/calibration, abstention, text/image eligibility, fallback behavior, actual task latency/cost and endpoint-specific retention/privacy. Typed confidence is not correctness; generic chat ZDR does not prove Decisions coverage. Strongest existing owner fits: Storybook routing/confirmation, Doc Web consistency/uncertainty review and Echo control-intent; Board Game orientation only for eligible image contracts. Preserve owner-specific gates and no unchanged repeat recommendations. No paid probes or owner changes in the watch.
