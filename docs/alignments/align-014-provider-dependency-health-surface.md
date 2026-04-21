# Alignment 014 — Provider Dependency Health Surface

**Date**: 2026-04-20
**Focus**: Evaluate CineForge's new provider dependency health and credential
readiness surface and whether the same operator-facing pattern should sync into
other tracked repos
**Source Project**: `cine-forge`
**Target Projects**: `storybook`, `dossier`, `doc-web`

## Surfaces Compared

- CineForge `docs/stories/story-179-provider-dependency-health-and-credential-readiness.md`
- CineForge `src/cine_forge/api/routers/health.py`
- CineForge `src/cine_forge/schemas/provider_health.py`
- CineForge `src/cine_forge/services/provider_dependency_health.py`
- CineForge `.agents/skills/deploy/SKILL.md`
- CineForge `docs/deployment.md`
- Storybook `packages/backend/src/index.ts`
- Storybook `docs/decisions/adr-014-ai-operated-deployment/adr.md`
- Storybook `.agents/skills/deploy/SKILL.md`
- Dossier `src/dossier/runtime_preflight.py`
- Dossier `docs/output-schema.md`
- doc-web `doc_web/cli.py`
- doc-web `docs/dossier-doc-web-handoff.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the goal is to carry over useful supervisory meaning, not to force
  textual identity.
- CineForge Story 179 explicitly scoped the new surface as a fast operational
  truth layer below the real post-rollout product gate. It also explicitly kept
  machine liveness separate from provider readiness.
- Storybook ADR-014 does not govern Conductor directly, but its D8 decision is
  a real target-repo constraint: Storybook's `/health` must stay DB-only and
  must not treat external provider outages as machine death.
- No narrower Conductor decision record already covers cross-project provider
  dependency health semantics.

## Key Differences

- CineForge now has a dedicated cached dependency-health surface at
  `/api/health/dependencies`, while `/api/health` stays app-local. The service
  probes the currently required Anthropic, Google, and OpenAI runtime paths
  with cheap model-access checks and reports `ok`, `missing`,
  `auth_failed`, `permission_failed`, `quota_failed`, `rate_limited`, or
  `unknown`.
- CineForge also promoted that surface into its live deployment contract:
  deploy now checks `/api/health/dependencies?refresh=1`, and
  `docs/deployment.md` treats it as the fast provider-readiness signal that
  sits underneath the representative post-rollout eval.
- Storybook already separates machine liveness from broader app startup truth
  in one way: `/health` checks Postgres only, while startup preflight covers
  media storage and the pinned Dossier runtime. But Storybook still lacks an
  explicit operator-facing dependency-readiness probe for its external AI
  provider and credential surfaces, so a deploy can still look healthy before a
  first real provider-backed action proves otherwise.
- Dossier already owns the same problem at a different boundary. Its
  `runtime_preflight` contract resolves provider credentials, records
  `credential_names_checked` and `credential_name_used`, and can mark a
  provider path `incompatible` after a bounded compatibility probe. That is a
  package/runtime contract, not a web-app health surface.
- doc-web also already has a machine-readable preflight boundary, but it is a
  pinned-consumer/runtime contract (`doc-web contract --json`), not a deployed
  operator-health problem. The current repo truth does not justify a live
  dependency-health endpoint there.

## Classification

- **Portable improvement**: separate machine liveness from dependency
  readiness; expose cheap bounded probes for the real shipped dependency path;
  and teach deployment verification to query that readiness surface explicitly
  instead of inferring it from a generic health route.
- **Intentional adaptation**: keep Dossier and doc-web on their current
  package/runtime preflight surfaces rather than forcing them into web-style
  health semantics. Keep Storybook's `/health` DB-only per ADR-014 D8.
- **Methodology conflict**: any attempt to fold external dependency failures
  into Storybook's existing `/health` would directly conflict with its accepted
  deployment model. The conflict disappears if the new readiness truth is kept
  separate.
- **Unclear drift**: Storybook currently has a real fast-readiness gap between
  "app is up" and "provider-backed path is actually callable." That gap is now
  better understood because CineForge has a concrete narrow pattern for closing
  it without making machine health dishonest.

## Recommendation

- **storybook**: Sync partially. Preserve `/health` exactly as the DB-only
  machine signal, but add a separate dependency-readiness surface or equivalent
  deploy-time probe for Storybook's provider-backed runtime path. The portable
  value is the split between liveness and provider readiness, not CineForge's
  exact endpoint shape or provider list.
- **dossier**: Keep local. Dossier's current CLI/runtime preflight already owns
  credential and compatibility truth more honestly than an HTTP health route
  would, because the repo is primarily consumed as a runtime/library boundary.
- **doc-web**: Keep local. The current machine-readable contract preflight is
  the right seam. There is no comparable deployed-app dependency-health
  pressure here yet.

## Human Decision Needed

- For Storybook only: should the fast external-dependency truth live behind a
  dedicated HTTP route similar to CineForge's `/health/dependencies`, or behind
  a narrower CLI/pre-deploy probe that the deploy skill runs explicitly?
- For Storybook only: which dependencies belong in the first shipped readiness
  surface? Likely candidates are the provider-backed AI path and any other
  external dependency that can make first-use fail after `/health` still says
  the app is alive.

## Result

- Completed the comparison pass and recorded the decision in Conductor
  alignment memory.
- A target-repo story was created, built, validated, and landed in Storybook
  after this comparison pass.
- The original Conductor inbox note is now fully routed into durable alignment
  memory instead of remaining as raw backlog pressure.

## Follow-Up

- Recommend Storybook story-prep only. The next honest move is to turn this
  alignment result into a small Storybook execution story that adds a separate
  dependency-readiness check while preserving ADR-014 D8.
- No Dossier or doc-web follow-up is warranted from this pass.

## Status Update

- Later on 2026-04-20, the recommended Storybook follow-up was created,
  renumbered to avoid a live Story 098 collision, and landed from an isolated
  Storybook worktree as
  `docs/stories/story-104-provider-dependency-readiness-surface.md`.
- The approved default package matches this alignment's recommendation:
  preserve `/health` as DB-only, add a separate dependency-readiness surface,
  scope the first cut to Anthropic plus Google AI runtime dependencies, and
  keep voice/OAuth plus startup-preflight-owned dependencies out of that first
  slice.
- Storybook `main` now carries the split health contract: `/health` stays
  DB-only, while `/health/dependencies` reports bounded provider readiness for
  the first shipped Anthropic plus Google AI runtime path.
