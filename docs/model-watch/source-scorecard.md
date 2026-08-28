# Source scorecard

Baseline created 2026-08-26. Yield records qualifying leads, not routine
announcements. Cost is public-metadata search cost; this watch uses no paid
inference.

| Source | Role / cadence | Yield and uniqueness | Reliability / friction | Last checked | Last useful | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| OpenAI product/API release notes | Core daily | No new general-purpose model; August GPT-5.6 pricing remained economics-only | First-party; low friction | 2026-08-27 | 2026-07-09 | Keep |
| Anthropic news/model docs | Core daily | No August general-purpose API release; text-watermarking is policy, not a model lead | First-party; low friction | 2026-08-27 | 2026-07-24 | Keep |
| Google Gemini API changelog/model pages | Core daily | Reconfirmed prior Gemini 3.7 Flash GA; no material change | First-party, exact capability docs | 2026-08-27 | 2026-08-13 | Keep |
| xAI news/docs | Core daily | Grok 4.6 platform expansion only; existing model/route | First-party; low friction | 2026-08-27 | 2026-08-12 | Keep |
| DeepSeek API docs | Core daily | Current V4 Pro pricing table now lists Responses API support; older endpoint pages still contradict it, and the exact alias already has owner evaluation attempts | First-party but release pages can lag each other; documentation does not satisfy the recorded owner retry gates | 2026-08-28 | 2026-08-28 | Keep for monitoring; do not recommend a repeat from documentation alone |
| Qwen/Alibaba docs | Core daily | Unique qualifying Qwen3.8-Flash-Next launch and current managed `qwen3.8-flash` page found | First-party model page and launch post; medium friction | 2026-08-27 | 2026-08-27 | Promote to daily direct QwenCloud model/release pages |
| Moonshot/Kimi and Z.ai/GLM docs | Core daily | No new material lead surfaced | First-party but search indexing is uneven | 2026-08-27 | 2026-08-20 | Keep |
| Mistral news/docs | Core daily | Infrastructure/regional-inference update, not a new general-purpose challenger | First-party; low friction | 2026-08-27 | 2026-06-23 | Rotate |
| MiniMax official surfaces | Core daily | Music/video releases and prior M3 references only; no newly released maintained-lane challenger | Sparse indexed docs; medium friction | 2026-08-27 | — | Rotate |
| OpenRouter public catalog | Core daily access discovery | Independently exposed the new Alibaba `qwen/qwen3.8-flash` endpoint, with pricing/limits and public endpoint metadata | Useful access metadata; cannot prove strict contracts/privacy/quality | 2026-08-27 | 2026-08-27 | Keep |
| General web/API release-note search | Secondary, rotating | Found and primary-verified the Qwen release; otherwise no unique qualifying lead | Fast but noisy and index-lagged | 2026-08-27 | 2026-08-27 | Keep, rotate queries |

## Strategy changes

- **2026-08-26:** Baseline added. Keep the compact first-party core and
  OpenRouter catalog; rotate Qwen, Mistral, and MiniMax depth because today's
  discovery yield was low or non-qualifying. No source was retired because this
  is the first scored run.
- **2026-08-27:** Promoted direct QwenCloud model/release pages from rotating
  depth to the daily core: they supplied the primary identity, price, limits,
  and feature evidence for a newly available model, while OpenRouter supplied
  independently useful route metadata. Retain Mistral and MiniMax as rotating
  depth because today's result was non-qualifying.
- **2026-08-28:** Added a documentation-conflict rule for DeepSeek: the current
  V4 Pro pricing/model table lists Responses support, while cached endpoint and
  guide pages still exclude it. The evaluated-model ledger shows the exact
  alias already reached CineForge and Echo Forge owner attempts. Keep the direct
  docs in the core as monitoring evidence, but do not recommend re-evaluation
  unless current evidence satisfies the recorded strict-contract, privacy,
  latency, and cost trigger; documentation alone does not.
