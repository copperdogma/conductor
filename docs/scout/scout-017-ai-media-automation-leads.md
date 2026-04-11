# Scout 017 — Evaluate AI Media Automation Leads for CineForge and Storybook

**Source**: multiple inbox items
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

This bundle does not resolve to one coherent "AI media automation" product
direction. It splits into three different shapes:

- a productized marketing-video agent (`HeyGen Video Agent`)
- a research-style multimodal orchestration paper (`MultiMedia-Agent`)
- a narrow open video-editing model plus a generic orchestration shell
  (`Netflix VOID`, `OpenClaw`, and the linked OpenClaw + Seedance + Premiere
  demo tweet)

That matters because CineForge's current product truth is narrower and more
honest than "make any media workflow autonomous." CineForge already knows its
main bottleneck: operator-facing previz must be real AI-generated motion, and
current models are still too slow to satisfy the `<= 6000 ms` runtime target.
The local evals already show that quality is plausible while runtime remains
blocked.

Against that backdrop, none of the external leads justifies a new shared
substrate or immediate story:

- **HeyGen** is real, but it is optimized for fast branded explainers,
  onboarding, sales, and UGC-style avatar videos. That is a useful commercial
  workflow, not a strong fit for CineForge's film-planning, storyboard,
  animatic, and previz lane.
- **MultiMedia-Agent** is conceptually aligned with the idea that media work
  requires planning plus multiple tools, but it remains a paper-level system.
  It is valuable as architecture inspiration, not as a ready operational lane.
- **Netflix VOID** is the most concrete technical artifact in the bundle. It is
  a specialized model for interaction-aware video object deletion, which makes
  it interesting as a future post-generation editing reference. But that is a
  narrower later-stage editing capability, not the current CineForge bottleneck.
- **OpenClaw** is a capable self-hosted orchestration shell with built-in
  video-generation tools and background tasks, and the tweet demonstrates that
  an agent can chain model generation with editor automation. But that still
  does not solve CineForge's current core problem: picking and validating a
  genuinely useful, fast-enough AI-previz lane.

So the honest outcome is `Defer`, with one CineForge-side future note and no
portfolio-wide adoption pressure.

## Project Relevance

- **dossier**: `Reject`. No meaningful direct fit. The bundle is about media
  generation/editing orchestration, not provenance-rich document/entity work.
- **storybook**: `Defer`. Some future internal marketing or onboarding-video
  workflows could borrow ideas from HeyGen or generic media orchestration, but
  there is no current Storybook product pressure strong enough to justify a
  repo-side handoff.
- **doc-web**: `Reject`. No current fit beyond very abstract multimodal
  workflow inspiration.
- **cine-forge**: `Defer`. Highest real relevance, but only as a future design-
  reference bundle for two narrow cases:
  1. post-generation video editing / cleanup operations
  2. orchestration of long-running external media jobs once CineForge's own
     eval-backed AI-previz lane is already clearer

## Recommendation

- Keep this at `Defer`.
- Do **not** create a Conductor story or a target-project story from this scout
  alone.
- Route one concise future note to CineForge only.
- Do **not** treat HeyGen as a CineForge substrate candidate. It is a polished
  marketing-video agent, not a film-planning or previz system.
- Do **not** treat the OpenClaw + Seedance + Premiere demo as proof that
  CineForge should pivot to an editor-driving agent shell. The demo proves
  orchestration is possible; it does not answer the current product question of
  which AI-previz lane is fast and useful enough.
- If revisited later, borrow only the narrow ideas that match a real CineForge
  story:
  1. interaction-aware post-generation video editing (`VOID`)
  2. background-task / provider-failover orchestration for long-running media
     generation (`OpenClaw`)
  3. multi-tool plan/execute structures for complex multimodal jobs
     (`MultiMedia-Agent`)
- Keep the current priority on CineForge's own eval-backed previz and render-
  adapter truth instead of importing another media-agent layer.

## Confidence

- Medium-high. The source-shape judgment is grounded in primary sources from
  HeyGen, OpenClaw, Netflix/VOID, and arXiv plus current CineForge spec/eval
  surfaces. I did not run any of the external systems live.

## Evidence

- `https://huggingface.co/netflix`
- `https://x.com/ehuanglu/status/2035286532857205088?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- `https://huggingface.co/netflix/void-model`
- `https://www.heygen.com/agent`
- `https://arxiv.org/abs/2601.03250`
- `https://docs.openclaw.ai/`
- `https://docs.openclaw.ai/tools/video-generation`
- Inbox notes: `HeyGen video agent`, `multimedia content agent`, and
  `image-generation launch analysis follow-up`
- Local overlap evidence:
  - `/Users/cam/Documents/Projects/cine-forge/docs/spec.md`
  - `/Users/cam/Documents/Projects/cine-forge/docs/evals/registry.yaml`
  - `/Users/cam/Documents/Projects/cine-forge/docs/inbox.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/docs/spec.md`

## Open Questions

- If CineForge later needs post-generation cleanup or deletion tools, is
  interaction-aware editing like `VOID` the right first narrow spike?
- If long-running external media jobs become normal in CineForge, should the
  orchestration live inside CineForge's own task/runtime substrate or in an
  external gateway shell like OpenClaw?
