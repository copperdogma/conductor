# Runbook: npm Supply-Chain Hardening

Use this when an npm compromise, suspicious package release, or install-time
malware report may affect Conductor or the tracked projects.

## Quick Scan

Run the Conductor fleet scanner from this checkout:

```bash
make supply-chain-scan
```

The Conductor target reads `projects.yaml`, includes the Conductor checkout, and
checks package manifests, lockfiles, and GitHub Actions workflows against
`docs/security/npm-supply-chain-incidents.json`.

Run the same scanner against only the current checkout:

```bash
python3 scripts/npm_supply_chain_scan.py
```

Use strict mode when the scan should fail on a known affected package/version or
IOC:

```bash
python3 scripts/npm_supply_chain_scan.py --strict
```

Tracked repos should not depend on Conductor at runtime. Each tracked repo that
receives the rollout has its own copy of the scanner, incident data, runbook,
and local command hook.

## Operating Model

- Event-triggered: run the local repo scanner when triaging an
  npm/package/dependency/CI supply-chain incident.
- Change-triggered: run the local repo scanner before and after dependency
  upgrades, lockfile refreshes, package-manager script changes, `.github`
  workflow changes, publish/deploy job changes, cache changes, and OIDC/token
  permission changes.
- Validation-triggered: run the local repo scanner when validating a story or
  diff that touched any of those surfaces.
- Supervisor sweep: Conductor may run `make supply-chain-scan` periodically or
  after updating incident data to compare tracked repos, but that is a
  monitoring convenience, not a runtime dependency for the target repos.
- Incident data owner: whichever repo is running the scan must update its local
  `docs/security/npm-supply-chain-incidents.json` from first-party incident
  sources before treating a clean scan as evidence for a new incident.

## What Counts As Evidence

- A package name plus affected version in a lockfile is exposure evidence.
- An affected package name in `package.json` without the affected lockfile
  version is a dependency lead, not proof that malware ran.
- An IOC such as a malicious optional dependency, file name, or git ref is
  exposure evidence until disproven.
- A clean related package note, such as TanStack Query in the 2026-05 incident,
  is not an incident finding when official incident sources say that package
  family was clean.
- CI logs and local shell history are needed to prove whether an affected
  install actually executed in a credential-bearing environment.

## GitHub Actions Checklist

Flag workflows that combine untrusted code or dependency installs with
privileged repo context:

- `pull_request_target` plus checkout or execution of fork-controlled code.
- `pull_request_target` plus dependency install, build, test, or cache writes.
- `actions/cache` keys that can be poisoned from untrusted branches and reused
  by privileged jobs.
- `id-token: write` available in jobs that run dependency installs before a
  tightly scoped release step.
- npm publish, package provenance, cloud deploy, or SSH credentials exposed to
  install/build/test jobs instead of only to the final release step.
- Lifecycle scripts allowed during audit-only dependency checks when
  `--ignore-scripts` would be sufficient.

## Response Rule

If a scan finds an affected version or IOC in a credential-bearing local or CI
environment:

1. stop installs from that lockfile or cache;
2. remove `node_modules` and package-manager caches for the affected checkout;
3. rotate credentials available to the install environment;
4. review GitHub, npm, cloud, and provider audit logs for the exposure window;
5. route repo-specific fixes through that repo's own story or an isolated
   worktree.

Do not claim target-project remediation complete from Conductor unless the
target repo was actually patched and validated.
