# Alignment 029 — npm Supply-Chain Hardening

**Date**: 2026-05-12
**Focus**: Convert the Mini Shai-Hulud/TanStack incident into a reusable,
self-contained per-repo guardrail for lockfile scanning and CI trust-boundary
review.

## Source

Primary inputs:

- Scout 031 on the 2026-05 Mini Shai-Hulud/TanStack npm compromise.
- TanStack's postmortem and GitHub advisory for affected package/version data.
- Conductor's operating rule that target-project changes should be prepared and
  routed before broad synchronization.

## Classification

Portable improvement with a small local scanner and checklist in each tracked
repo.

This should not become a central package manager, a permanent emergency lane, or
a blanket dependency-update program. The repeated risk is narrower: incident
reports arrive with known package/version indicators, and the tracked projects
need a fast way to separate direct exposure from clean related package usage and
workflow-hardening follow-up.

The target repos are intentionally self-contained. They should not need to know
where Conductor lives or call back into Conductor to answer whether their own
checkout is exposed.

## Decision

Each tracked repo should own a local first-pass supply-chain incident scan:

- keep incident indicators in a small machine-readable data file;
- scan local manifests and lockfiles without installing dependencies;
- distinguish affected package/version hits from clean related packages;
- report GitHub Actions combinations that let untrusted installs reach caches,
  OIDC, publish, deploy, or secret-bearing jobs;
- route repo-specific remediation through that repo's normal story/worktree
  flow.

Conductor remains the supervisor for rollout and drift detection. It may keep a
fleet-scan convenience over `projects.yaml`, but that is monitoring only. The
distributed repo-local scanner is the canonical answer inside each target repo.

## Checklist

When reviewing a new npm incident:

- update the repo-local `docs/security/npm-supply-chain-incidents.json` from
  first-party incident sources;
- run the repo-local `make supply-chain-scan`, `npm run supply-chain:scan`, or
  `python3 scripts/npm_supply_chain_scan.py`;
- treat lockfile affected-version hits and IOC hits as exposure evidence;
- treat `package.json` range-only hits as investigation leads;
- inspect workflows for `pull_request_target`, cross-boundary cache use,
  dependency installs, `id-token: write`, npm publish, deploy credentials, and
  lifecycle-script behavior;
- rotate credentials only when evidence shows an affected install could have
  run where credentials were available.

## Practical Impact

Cam gets a repeatable answer to "are we hit?" without turning every dependency
incident into manual searching. The tracked projects keep their self-contained
operating model, and Conductor can still compare rollout/drift without becoming
a runtime dependency.
