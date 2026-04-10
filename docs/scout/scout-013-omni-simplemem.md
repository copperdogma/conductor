# Scout 013 — Evaluate Omni-SimpleMem for Long-Lived Agent Memory

**Source**: `https://arxiv.org/abs/2604.01007`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The primary source is real and current: `Omni-SimpleMem: Autoresearch-Guided
Discovery of Lifelong Multimodal Agent Memory` (`arXiv:2604.01007v2`, revised
2026-04-02) reports strong benchmark gains from an autoresearch-discovered
memory stack built around selective ingestion, multimodal atomic units, hybrid
dense+sparse+graph retrieval, and progressive token-budgeted expansion. The
implementation-side repo now lives in `aiming-lab/SimpleMem`, which packages
both text memory and the newer Omni-SimpleMem multimodal path.

That makes this a credible design-reference bundle, not tweet noise. But after
comparing it with the tracked repos, it still does not justify a direct
architecture pivot. Storybook already accepted a much thinner fast-lane memory
shape in ADR-015 and ADR-018: per-turn RAG, a small session-scoped working
memory buffer, and minimal session state. Omni-SimpleMem, Memary, and the MCP
memory server are all useful references, but they are materially heavier or
more generic than the current honest next step.

The strongest reusable lesson from the broader source bundle is operational, not
benchmark-driven: memory must be inspectable, clearly enabled, and visibly
separated into short-lived working state versus durable reviewed memory. That
fits Storybook better than importing a new external memory subsystem.

## Project Relevance

- **dossier**: Low current relevance. This is not a shared-supervisor memory
  method that obviously belongs in Conductor or Dossier methodology first.
- **storybook**: Highest relevance. Storybook is the one tracked repo that
  already committed to fast-lane memory architecture and still has live memory
  discoverability/continuity pressure.
- **doc-web**: No current relevance. `doc-web`'s active memory issues are
  methodology memory and OCR proof surfaces, not agent-session recall.
- **cine-forge**: Low current relevance. CineForge may eventually want stronger
  long-lived creative memory, but that is not the live bottleneck surfaced in
  its current stories or inbox.

## Recommendation

- Defer at the Conductor level and hand the outcome to Storybook's inbox.
- Do **not** create a Conductor story and do **not** recommend replacing
  Storybook's accepted ADR-015/ADR-018 memory direction with Omni-SimpleMem,
  Memary, or the MCP memory server.
- If Storybook revisits memory architecture later, the honest next step is:
  1. verify or ship the thin local session-memory lane already promised by
     ADR-015/ADR-018
  2. improve memory discoverability / inspectability if operators still cannot
     tell what memory is active
  3. only then benchmark external stacks against Storybook-specific continuity
     tasks instead of importing them from LoCoMo or Mem-Gallery hype
- Treat the official MCP memory server as a tiny developer-tool reference, not
  a product-memory candidate. It is useful for showing an inspectable local
  entity/relation/observation surface, but it is too primitive for Storybook's
  provenance and UX bar.
- Treat Memary as another design reference, not a drop-in fit. Its graph-heavy
  agent stack, database assumptions, and older model/runtime posture are much
  heavier than Storybook's current thin-memory needs.

## Confidence

- Medium-high. The paper and repos are real and the fit-to-Storybook judgment is
  grounded in primary sources plus Storybook's own accepted ADRs, but I did not
  run local benchmark code from the external memory repos.

## Evidence

- `https://arxiv.org/abs/2604.01007`
- `https://arxiv.org/html/2604.01007v2`
- `https://github.com/aiming-lab/SimpleMem`
- `https://raw.githubusercontent.com/kingjulio8238/Memary/main/README.md`
- `https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/memory/README.md`
- `https://belimad.substack.com/p/dreaming-how-openclaw-learns-to-remember`
- Inbox note: `might be good for Storybook if we can poach some ideas`
- `Twitter Scraper` result for 2026-01-27 tweet `2016192932685230374`, where
  Alex Volkov says OpenClaw memory was "not enabled by default" and onboarding
  did not guide users through it. That is a product/discoverability lesson more
  than an architecture win.

## Open Questions

- Does Storybook already have enough shipped thin-session state to satisfy the
  ADR-015/ADR-018 promise, or is there still a concrete local gap worth turning
  into a Storybook story?
- If Storybook does benchmark an external memory stack later, what is the
  smallest honest eval surface: continuity across returning conversations,
  grounded recall of people/facts, or question timing during live chat?
- How visible is Storybook's current memory behavior to operators and users, and
  is discoverability now the bigger problem than retrieval quality?
