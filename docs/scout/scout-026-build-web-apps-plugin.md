# Scout 026 - Evaluate Build Web Apps Plugin for Tracked App Workflows

**Source**: Codex inbox note plus local plugin bundle at
`/Users/cam/.codex/.tmp/plugins/plugins/build-web-apps`
**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Reviewed the OpenAI Build Web Apps plugin bundle, its included skills, the
official Codex plugin/skill/browser documentation, current Codex use-case
guidance for front-end work, and the tracked repos' existing UI/frontend
surfaces on 2026-04-29.

The plugin is real and useful, but its right role here is selective
augmentation, not replacement. Its strongest contribution is the
`frontend-app-builder` workflow: start visually led web work from a complete
Image Gen concept, treat the accepted concept as a production design spec,
extract a small design system, implement faithfully, then verify the browser
render against the concept with `view_image`, desktop/mobile checks, and a
written fidelity ledger.

That is a good fit for greenfield web apps, dashboards, games, creative sites,
landing pages, public marketing surfaces, and substantial redesigns where the
visual concept should be the spec. It is a poor default for narrow UI fixes,
dense operational workspaces, authenticated product flows, story-local runtime
repairs, or cases where an existing repo-specific design system and product
truth surface already own the answer.

The plugin also bundles useful specialty references:

- `react-best-practices` for React/Next performance patterns.
- `shadcn-best-practices` for registry/component usage and component
  composition.
- `stripe-best-practices` for payment and billing integration decisions.
- `supabase-postgres-best-practices` for Postgres/Supabase performance and
  schema guidance.

Those should be used as task-specific references, not portfolio-wide defaults.
They do not replace existing repo validation, product identity, UI-scout, or
visual-inspection skills.

The installation-unit detail matters: Build Web Apps should be enabled once as a
user-level Codex plugin, not copied or vendored into each web repo. After the
follow-up discussion, `build-web-apps@openai-curated` is enabled in the current
`~/.codex/config.toml`, so its bundled skills can be discovered by Codex across
threads when their metadata matches the task. Browser Use is installed
separately and remains the browser-operation substrate.

## Project Relevance

- **conductor**: `Adapt`. Record the scout and use the plugin as a reference
  when future cross-project UI methodology questions appear. Do not turn
  Conductor into a canonical frontend skill source. If repeated pressure
  appears, the honest next vehicle is an alignment pass, not a direct sync.
- **storybook**: `Adapt cautiously`. Storybook already has a warm,
  product-specific `frontend-design` skill, `ui-scout`, authenticated browser
  smoke patterns, and `visual-inspect-loop`. Do not replace those. Borrow the
  complete-concept, design-system-extraction, and fidelity-ledger pieces for
  major redesigns or public/marketing surfaces. Browser/IAB is insufficient for
  many Storybook flows because local verification often requires seeded
  sessions, cookies, Postgres, media, and authenticated state.
- **cine-forge**: `Adapt cautiously`. CineForge already has a strong
  design-in-browser workflow, shadcn/ui stack, representative-state rule, and
  browser verification contract. Use Build Web Apps ideas for visually led
  surfaces, generated visual assets, and shadcn composition help, but do not let
  a static generated concept override representative project/API/driver states
  or the current high-taste interactive feedback loop.
- **echo-forge**: `Adapt`. Echo Forge is a React/Vite/PWA UI app and can use the
  concept-first path for larger table-panel, scene, or mixer surface design.
  Keep the local live-table identity: dense, calm, large touch targets, global
  controls visible, and no decorative marketing treatment on operational views.
  Browser/IAB is a good fit for unauthenticated local Vite screens.
- **doc-web**: `Defer`. The current pressure is document conversion,
  source-faithfulness, and visual artifact inspection, where
  `visual-inspect-loop` is the better existing tool. Build Web Apps may become
  useful if doc-web grows a substantial editor/review UI, but that is not the
  current bottleneck.
- **dossier**: `Defer`. Current Dossier pressure is text/entity extraction,
  graph/eval truth, and doc-web runtime freshness, not rich frontend work.
  Postgres/Supabase guidance may be useful later for a concrete database
  performance task, but this plugin should not create a UI methodology lane.
- **boardgame-ingester**: `Defer with future fit`. The repo owns visual
  artifacts and crop/golden quality, but not a primary web app yet. If an
  inspector or golden-review UI lands, the concept-first and game/asset guidance
  could help; until then, `visual-inspect-loop` is more relevant.
- **roborally**: `Spike later`. The plugin's game-surface and generated sprite
  guidance will be useful when the project starts a visual client, but Robo
  Rally is intentionally headless first. Authoritative game truth must stay in
  headless logic, not in generated UI or asset state.

## Recommendation

- Keep this scout as `Adapt`.
- Keep Build Web Apps installed/enabled once at the Codex user level for Cam's
  environment. Do not install or vendor a copy into every tracked repo.
- Do not replace repo-local `frontend-design`, `ui-scout`,
  `visual-inspect-loop`, `webapp-testing`, or `/validate` skills with Build Web
  Apps.
- Do not add the Build Web Apps plugin as a repo-scoped default marketplace
  dependency yet. The repo boundary should stay product rules and validation,
  not plugin distribution.
- Let Codex discover and choose the globally installed plugin when the active
  task is a good shape: greenfield frontend app, visually led redesign, landing
  page, dashboard, browser game, or generated-asset-heavy website.
- When using it in tracked repos, combine it with repo-local rules:
  - first read local Ideal/spec/ADR/AGENTS guidance
  - preserve product identity and existing design-system tokens
  - use Image Gen concepts only when visual concepting is actually helpful
  - keep true app text and controls code-native
  - use Browser/IAB first only for unauthenticated local/file/public pages
  - fall back to Playwright, Computer Use, or repo-specific browser runbooks
    when auth, cookies, real browser profiles, or representative product state
    are required
  - keep final acceptance tied to repo-native checks and product evidence
- Borrow these ideas into future repo-local skill work when a concrete story or
  alignment pass warrants it:
  - complete-surface concept before implementation for large visual builds
  - design-system extraction from the accepted concept
  - explicit allowed above-the-fold copy list
  - generated standalone assets when brand/product imagery must be coherent
  - Browser/IAB-first verification where its auth limitations do not apply
  - `view_image` comparison of accepted concept and implementation screenshot
  - fidelity ledger with at least five concrete comparison points
  - hard stop on browser-default control typography, invented copy, clipped
    content, generic placeholder assets, and visible concept drift
- The first practical test should be a bounded pilot on the next eligible
  greenfield or redesign task, not an immediate cross-repo skill rollout or
  repo-by-repo plugin installation. After that pilot, Conductor can decide
  whether an alignment pass should add a small "consider Build Web Apps for
  substantial visually led work" note to Storybook, CineForge, and Echo Forge
  frontend guidance.

## Evidence

- Local plugin manifest says Build Web Apps is a coding plugin for
  frontend-focused web apps with generated assets, browser testing, shadcn/ui,
  Stripe, and Supabase/Postgres guidance.
- Local plugin README lists five skills: `frontend-app-builder`,
  `react-best-practices`, `shadcn-best-practices`, `stripe-best-practices`, and
  `supabase-best-practices`.
- `frontend-app-builder` requires Image Gen concepts by default for substantial
  visual work, complete-surface design before coding, exact implementation of
  the accepted concept, design-system extraction before implementation, and
  Browser/IAB-first verification.
- `frontend-app-builder` blocks final handoff until the accepted concept and
  latest browser screenshot are inspected with `view_image` and judged for
  agency-signoff fidelity.
- The concept briefing reference emphasizes concrete product content,
  complete-surface concepts, code-native app UI, separable generated assets,
  no header-only crops, no default card grids, no invented hero labels, and
  fidelity comparison against the accepted concept.
- Official Codex docs say plugins bundle skills, app integrations, and MCP
  servers into reusable Codex workflows, while skills are the authoring format
  for reusable workflows and plugins are the installable distribution unit.
- Official Codex customization docs say skill metadata is visible for discovery,
  Codex can choose skills implicitly when a task matches their descriptions, and
  user-level skills are appropriate for workflows wanted across repos.
- Official Build plugins docs say to start with a local skill when still
  iterating on one repo or personal workflow, and build a plugin when sharing a
  stable workflow, bundling app integrations/MCP config, or publishing.
- Official in-app browser docs say Browser Use can operate local development
  servers and file-backed previews, inspect rendered state, take screenshots,
  and verify fixes, but the in-app browser does not support authentication
  flows, signed-in pages, regular browser profiles, cookies, extensions, or
  existing tabs.
- Official Codex frontend-design use-case docs recommend translating
  screenshots and briefs into code that matches the repo's design system, using
  browser visual checks, and iterating until the UI matches references.
- Local tracked repo evidence:
  - Storybook: React/Vite/shadcn/Tailwind, local `frontend-design`, `ui-scout`,
    `webapp-testing`, authenticated browser smoke patterns, and
    `visual-inspect-loop`.
  - CineForge: React/Vite/shadcn/Tailwind, design-in-browser workflow,
    representative UI state rule, browser verification contract.
  - Echo Forge: React/Vite/PWA, local `frontend-design`, `ui-scout`, and
    `webapp-testing`.
  - doc-web, boardgame-ingester, and roborally: stronger relevance to visual
    artifact/client work than to immediate web-app-builder adoption.
  - Dossier: no current UI-scout/product frontend pressure.
- Existing Conductor records already cover adjacent ideas:
  - Scout 007 adapted OpenAI frontend guidance selectively.
  - Scout 012 deferred Codex plugins as a general product opportunity.
  - Alignment 008 carried art-direction guidance into UI-heavy repos.
  - Alignment 020 rolled out `visual-inspect-loop` where visual proof is
    already first-class.

## Confidence

High for the recommendation not to replace local skills. The local plugin
bundle and official docs are explicit about the plugin/skill shape, and the
tracked repos already have product-specific UI, browser, and visual-inspection
contracts. Medium-high for the exact adoption timing because the best proof is
one real pilot on the next eligible frontend task.

## Open Questions

- Which upcoming task is the right low-risk pilot: an Echo Forge table-panel
  redesign, a Storybook public/marketing surface, a CineForge visual workflow
  view, or a future Robo Rally client screen?
- Should Conductor create a later alignment pass after one pilot to update
  repo-local `frontend-design` skills, or is this scout enough as a reference?
- How should generated-concept approval work in default mode when the user has
  not asked to review concepts first?
