# Scout 031 — Evaluate Mini Shai-Hulud npm Supply-Chain Risk

**Source**: `https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised`
**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge, boardgame-ingester, roborally, echo-forge

## Summary

Aikido reported a renewed Mini Shai-Hulud npm campaign on 2026-05-12. The
official TanStack postmortem and GitHub advisory confirm that, on 2026-05-11
between 19:20 and 19:26 UTC, 84 malicious versions across 42 `@tanstack/*`
packages were published through a chained GitHub Actions compromise: unsafe
`pull_request_target` execution, cross-boundary Actions cache poisoning, and
OIDC token extraction from the release runner.

The direct tracked-repo exposure appears low from the initial scan. The primary
tracked projects did not contain the affected TanStack router/start packages,
the malicious `@tanstack/setup` optional dependency, the malicious git ref, or
`router_init.js`. Storybook and CineForge do use `@tanstack/react-query` /
`@tanstack/query-core`; TanStack's postmortem lists the `@tanstack/query*`
family as confirmed clean.

The reusable lesson is still important: the practical risk is not only bad
package versions. It is install-time credential theft plus release-workflow
trust-boundary collapse when CI caches, lifecycle scripts, OIDC publish rights,
and deploy secrets share the same execution path.

## Project Relevance

- **conductor**: High relevance as supervisor work. Conductor should prepare a
  small cross-project guardrail story instead of doing opportunistic primary
  checkout edits.
- **storybook**: Relevant because the frontend uses TanStack Query, though not
  affected versions. Needs lockfile/IOC scan coverage and GitHub Actions
  workflow audit guidance.
- **cine-forge**: Same relevance as Storybook: TanStack Query is present, but
  the affected router/start packages were not found.
- **dossier**: No direct package exposure found in the initial scan, but it
  should benefit from the shared CI/dependency guardrail if it has Node or
  release workflows.
- **doc-web**: No direct package exposure found in the initial scan; include in
  the workflow/cache/OIDC audit because it owns external intake and package
  surfaces.
- **boardgame-ingester**: No direct package exposure found in the initial scan;
  include in the lightweight lockfile/CI audit because it consumes generated
  package artifacts.
- **roborally**: No direct package exposure found in the initial scan; low
  urgency, but include in the same cheap scanner if it has npm lockfiles.
- **echo-forge**: No direct package exposure found in the initial scan; include
  because it has active frontend/tooling work and credential-bearing provider
  workflows.

## Recommendation

Adapt this into a Conductor story for a reusable npm supply-chain hardening
pass. The right next move is not emergency credential rotation based on current
evidence. It is a small guardrail package:

- scan tracked lockfiles/manifests for the known compromised package/version
  pairs and IOCs from this incident;
- audit GitHub Actions workflows for `pull_request_target` jobs that execute
  fork-controlled code, cache writes crossing fork/base boundaries, broad
  `id-token: write`, and publish/deploy secrets available to install/build
  steps;
- document install discipline for incidents: frozen lockfiles, clean reinstalls
  when exposure is found, and temporary lifecycle-script controls for audit
  jobs;
- route any target-repo fixes through isolated worktrees/stories instead of
  direct primary-checkout churn.

Story 012 implemented the first reusable scanner and checklist. The first
scanner run across Conductor plus the tracked primary checkouts found zero
affected-version hits, zero dependency leads, zero IOC hits, and zero risky
workflow combinations. It reported only clean TanStack Query exposure in
Storybook and CineForge.

## Evidence

- Aikido report: `https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised`
- TanStack postmortem: `https://tanstack.com/blog/npm-supply-chain-compromise-postmortem`
- TanStack GitHub advisory: `https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx`
- Initial local scan on 2026-05-12:
  - Storybook primary checkout: `@tanstack/react-query@5.90.21` and
    `@tanstack/query-core@5.90.20` present.
  - CineForge primary checkout: `@tanstack/react-query@5.90.21` and
    `@tanstack/query-core@5.90.20` present.
  - No primary tracked checkout hit for affected router/start packages,
    `@tanstack/setup`, `router_init.js`, or
    `github:tanstack/router#79ac49eedf774dd4b0cfa308722bc463cfe5885c`.
  - No obvious primary tracked checkout workflow hit for
    `pull_request_target`, `id-token: write`, `actions/cache`, npm/pnpm
    publish, or trusted-publisher terms.
- Story 012 scanner run on 2026-05-12:
  `python3 scripts/npm_supply_chain_scan.py` reported `affected hits: 0`,
  `dependency leads: 0`, `ioc hits: 0`, and
  `risky workflow combinations: 0` across Conductor, Dossier, Storybook, Doc
  Web, CineForge, Board Game Ingester, Robo Rally, and Echo Forge.

## Open Questions

- Should the guardrail live as a Conductor-owned scanner/runbook first, or as
  repo-local validation snippets after the Conductor proof exists?
- Should this hardening story also capture Python/PyPI compromise checks for
  the reported Mistral/Lightning/Guardrails-adjacent packages, or should that be
  a second story if Python exposure appears?
