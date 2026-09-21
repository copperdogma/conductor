# Inbox

Use this file as the capture surface for cross-project work. Notes can be raw.
Triage is responsible for turning them into stories, scout missions, ADRs, or
explicit rejections.

## General

- 2026-09-21: Approved final review and landing of Echo Story071. Requested
  relative re-evaluation of other JEV tests affected by overly strict gates.
  Storybook is the sole other tested owner; new synthetic paired screen capped
  at US$1, preserving old evidence and product behavior. Routed to Scout072.

- 2026-09-19: Research JEV against current project classification opportunities.
  Routed to [Scout 072](docs/scout/scout-072-jev-classification-opportunities.md).
  Storybook correction intent is the first bounded comparison; Echo Forge needs
  a new cue-classification baseline. Dossier/Doc Web/Scrypted remain scoped eval
  proposals. Bishop, unified updater and Labor/Zero excluded by Cam for now.
  Approved Storybook screen completed22 pairs before adapter-contract stop:
  19 correct JEV projections,3 fallbacks; incumbent22/22. US$0.08689611/$1.
  Only4.1% estimated full-workflow savings; no adoption. Evidence and isolated
  benchmark changes retained; temporary key removed. Subsequent approved Echo
  Forge offline eval construction adds38 synthetic cases and component baselines
  in a separate owner worktree. Approved live dev screen then stopped after8
  matched cases on GPT control-policy mismatch; JEV abstention/latency also miss
  targets. Spend US$0.005804382/$1; key removed, no adoption.
  Approved offline v2 separates control intent from new-sound presence:24
  development cases,19 distinct utterances,5 active/empty-state pairs. Original
  v1 evidence stays frozen. Subsequent approved v2 live screen:6matched pairs,
  JEV6/6 vs GPT5/6, stopped on GPT maintenance-only music false positive.
  US$0.004907424/$1;18cases unrun, JEVp95 475ms, no adoption. Temporarykey
  removed; no runtime changes. Approved diagnostic completion then finished
  remaining18pairs forUS$0.014816976. Stitched24: JEV15exact vsGPT14,
  macroF1 .6389vs.7434, soundFP0/15vs2/15; JEV misses more real cues.
  No fullcue adoption. Approved offline control-intent eval now has48 fresh
  independently reviewed synthetic cases and two frozen deterministic baselines.
  Lexical reference catches1/20 controls with3/22 false positives; AI quality
  initially unmeasured, US$0 offline spend. Subsequently approved48pair native
  comparison completed: JEV31/48exact,15/20recall,1/22FP,14clearabstentions;
  GPT36/48exact,19/20recall,5/22FP. Neither meets ambiguity/latency targets.
  US$0.016273332/$1; no adoption, key removed. Further paid work needs
  representative fresh usage cases/stronger deterministic comparison. Existing
  runtime is a different action contract.
  Cam corrected the decision rule: rank useful relative improvements instead
  of rejecting every model against aspirational absolute gates. Explicitly
  approved broader comparison of prior promising models; Astra, Gemini 3.8,
  Grok 4.6 and Terra plus fresh JEV/Mini anchors completed the frozen48:
  Grok46/48 (quality winner,zero false activations), Gemini44/48 (recommended
  interactive balance), Terra/Astra42, Mini36, JEV30. All288 unique calls cost
  US$0.437034082/$5. Gemini+Terra agreement projects45/48; JEV→Gemini is cheaper
  but drops to42/48. TypeSafe key removed; no runtime changes or commits.
  Historical measurements remain intact; relative recommendations supersede
  earlier blanket rejection against aspirational gates.
  Cam approved implementing the Gemini control-intent path with Grok as the
  accuracy-focused option. Owner implementation is isolated in
  `/Users/cam/.codex/worktrees/echo-control-intent-runtime-20260920`, based on
  current Echo Forge HEAD `cc3c77798`; the older eval worktree stays frozen.
  Scope: explicit PTT submission, server-held provider keys, persisted model
  selection, semantic routing with deterministic execution and review on
  ambiguity/failure. No commit, push or deployment requested.
  Implementation is now build-complete in that worktree: Gemini default/Grok
  option, bounded server route, persisted choice and cancellation/manual-review
  behavior. Verification: 134 App + 348 non-App + 5 server tests, typecheck, lint,
  build and mocked browser smoke. Node test discovery was corrected; final
  evidence reuses unchanged passing App shards with corrected other runners.
  Story071 subsequently validated, marked Done and landed on remote main at
  `518046e` on 2026-09-21. Final review fixed an autoplay cancellation race;
  30 affected tests and packaging preflight pass. No deployment.

- 2026-09-19: Evaluate the models deferred from Dossier while development was
  active, one at a time. Routed to [Alignment 047](docs/alignments/align-047-dossier-model-catchup.md);
  the applicable historical queue and exclusions are reconciled there.
  Follow-through approved: resolve the ordinary benchmark contradictions in the
  same isolated owner worktree, preserving the original model evidence.
  Subsequent direct-runtime audit corrected the ordinary-lane scope; approved
  standalone Dossier semantic benchmark was built and tested as owner Story170 in
  its own worktree, with no consumer coupling. The subsequently authorized
  serial comparison is complete:17 callable models screened, no cheaper
  replacement established, US$3.66071209916 conservative accounted cost.

- Idea: add state machine specs (if it makes sense) to story planning. Apparnetly this very much helps vibe coded app quality. Let's research and discuss.

- 20260506: Scout this: https://claude.com/blog/new-in-claude-managed-agents
  - Looks similar to a lot of stuff we do but we may be able to use some of its hardness/code/ideas in our projects.

- HTML docs/views where it makes sense: This is kind of cool: https://x.com/trq212/status/2052809885763747935
  - I'm imaginging moving our core management docs over to something like this. If it's just text, like the ideal.md, it could be an html file with a nicer presentation. Instead of referecing docs via paths or notation in markdown we could just hyperlink to them. And some things that are data-heavy like the stories.md file or the like could be done in a better format for AI to worth with (like json) with an HTML view available for humans to look at, which would be much easier to understand. The stories could also be linked a lot better with hyperlinks plus there are a ton of broken-link tools and the like we could use for linting to make sure nothing goes astray.
  - I'd be worried about the cruft it would create. It's not usually just html, it's css, svg, image files, js, etc, etc. Maybe it doesn't matter because it's written and maintaned by AI and the benefits may outweigh the costs.
  - A lot of this could be stitched together in a project dashboard, linking to the ideal and spec, showing the active and upcoming stories, perhaps showing the pipeline runs or latest evals if applicable, etc.
