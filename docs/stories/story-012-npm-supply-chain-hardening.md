---
title: "npm Supply-Chain Hardening"
status: "In Progress"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.2"
  - "spec:3.2"
  - "spec:4.2"
  - "spec:5.1"
  - "spec:5.2"
  - "spec:5.3"
decision_refs: []
depends_on: []
category_refs:
  - "alignment"
  - "scouting"
  - "story-prep"
tracked_projects:
  - "conductor"
  - "dossier"
  - "storybook"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 012 — npm Supply-Chain Hardening

**Priority**: High
**Status**: In Progress
**Decision Refs**: None yet
**Depends On**: None

## Goal

Turn Scout 031 into a reusable supply-chain guardrail for the tracked projects:
detect known compromised npm package/version exposure, record a small
incident-response checklist for install-time malware, and audit GitHub Actions
trust-boundary patterns that let untrusted dependency installs reach caches,
OIDC publish rights, or deploy secrets.

The Mini Shai-Hulud/TanStack incident does not currently look like a direct
tracked-repo compromise. The initial scan found TanStack Query in Storybook and
CineForge, but not the affected TanStack router/start packages or published
IOCs. The value of this story is reducing future exposure: make the cheap scan
repeatable, make workflow red flags explicit, and route any target-project
fixes through local stories/worktrees instead of blanket edits.

## Acceptance Criteria

- [x] Conductor records Scout 031 as the source analysis and links it from the
      scout index.
- [x] A reusable scanner or documented command set checks tracked project
      package manifests and lockfiles for:
      - known affected Mini Shai-Hulud/TanStack package-version pairs;
      - IOCs including `@tanstack/setup`, `router_init.js`, and the malicious
        `github:tanstack/router#79ac49eedf774dd4b0cfa308722bc463cfe5885c`
        ref;
      - future incident lists that can be extended without rewriting the
        scanner.
- [x] Conductor records a GitHub Actions audit checklist for npm supply-chain
      incidents, covering unsafe `pull_request_target`, untrusted code
      execution in base-repo context, cache writes crossing fork/base
      boundaries, lifecycle scripts during installs, broad `id-token: write`,
      and publish/deploy credentials exposed before the release gate.
- [x] The current tracked primary checkouts are scanned with the new guardrail,
      and the story records which repos were clean, which only had clean
      TanStack Query exposure, and which need target-repo follow-up.
- [x] Any project-specific fixes discovered by the audit are routed as
      target-repo inbox notes or stories; Conductor does not claim target
      remediation complete unless those repos are actually patched and
      validated.
- [x] The story includes clear incident-response guidance: if an affected
      version was installed in a credential-bearing local or CI environment,
      rotate accessible credentials and review cloud/GitHub/npm audit logs.
- [x] The story records the operating model for repeat use: when the scan runs,
      whether it is event-triggered, scheduled, skill-triggered, or all three,
      and who owns updating the incident data.
- [x] The scanner is wired into the appropriate existing workflow surfaces:
      Conductor `/security-audit dependency` and target-repo triage,
      build-story, and validate skills.
- [x] Target-repo rollout is handled explicitly before closeout: every tracked
      repo gets a self-contained scanner, incident data file, local runbook,
      local command hook, and skill/AGENTS triggers in an isolated worktree.
- [x] Conductor methodology outputs are regenerated and checked.

## Out of Scope

- Emergency credential rotation without evidence that an affected package was
  installed on a credential-bearing host.
- Blanket dependency upgrades across primary checkouts.
- Direct target-project edits from the Conductor checkout.
- Replacing repo-local security audits, dependency policies, or release
  workflows with a heavyweight central package manager.
- Treating TanStack Query as compromised when the official TanStack postmortem
  currently lists `@tanstack/query*` as confirmed clean.
- PyPI hardening unless the npm scanner reveals a concrete adjacent exposure or
  a follow-up story is created.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Implement the needed scanner, doc, skill, script, or log changes
- [x] Update related scout and alignment memory if applicable
- [x] Decide and implement the operating cadence/skill hook for recurring use
- [x] Complete or explicitly hand off target-repo rollout/pointer work
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check` not required; covered by
        `make test`
  - [x] If scripts or repo checks changed: `make test`
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [ ] Validation complete or explicitly skipped by user
- [ ] Story marked done via `/mark-story-done`

## Files to Modify

- `docs/scout/scout-031-mini-shai-hulud-npm-supply-chain.md` — source scout
  and initial exposure analysis.
- `docs/scout.md` — scout index entry.
- `docs/stories/story-012-npm-supply-chain-hardening.md` — story source of
  truth.
- `scripts/npm_supply_chain_scan.py` — reusable incident IOC/lockfile scan.
- `docs/security/npm-supply-chain-incidents.json` — machine-readable incident
  package/version and IOC data.
- `docs/runbooks/npm-supply-chain-hardening.md` — operator checklist and
  incident-response guidance.
- `docs/alignments/align-029-npm-supply-chain-hardening.md` and
  `docs/align-projects.md` — portable workflow hardening decision.
- `Makefile` — convenience target for the scan.
- Generated methodology surfaces after compile:
  `docs/stories.md` and `docs/methodology/graph.json`.

## Notes

- Scout 031 source bundle:
  - Aikido report:
    `https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised`
  - TanStack postmortem:
    `https://tanstack.com/blog/npm-supply-chain-compromise-postmortem`
  - GitHub advisory:
    `https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx`
- Initial 2026-05-12 evidence:
  - Storybook and CineForge use `@tanstack/react-query` /
    `@tanstack/query-core`.
  - Official TanStack postmortem says `@tanstack/query*` is confirmed clean.
  - No primary tracked checkout hit for affected router/start packages,
    `@tanstack/setup`, `router_init.js`, or the malicious TanStack git ref.
  - No obvious primary tracked checkout workflow hit for `pull_request_target`,
    broad `id-token: write`, `actions/cache`, npm/pnpm publish, or
    trusted-publisher terms.
- Practical risk model:
  - lockfiles answer whether a known bad version was installable;
  - CI logs answer whether it actually ran in a credential-bearing environment;
  - workflow audit answers whether future install-time malware can reach cache,
    OIDC, publish, or deploy boundaries.

## Plan

Implemented `/build-story` shape:

1. Added a tiny machine-readable incident IOC list and scanner script for npm
   manifests/lockfiles across `projects.yaml`.
2. Ran the scanner against tracked primary checkouts and recorded the result in
   this story's work log.
3. Added a short GitHub Actions supply-chain checklist as an alignment record.
4. Audited tracked primary checkout workflows using the checklist and routed no
   concrete target-repo follow-ups.
5. Regenerated Conductor methodology outputs and ran checks:
   - `make methodology-compile`
   - `make methodology-check`
   - `make lint`
   - `make test`
   - `git diff --check`

## Work Log

20260512-0000 — `/create-story` from Scout 031 follow-up: created this story
after Cam approved turning the Mini Shai-Hulud/TanStack incident review into a
Conductor hardening work item. Initial evidence says no direct tracked-repo
compromise, but enough future-risk surface exists to justify a small reusable
scanner and workflow checklist. Next step: `/build-story 012`.

20260512-2056 — Higher-effort pre-build review: story shape is still correct,
but the implementation should use extensible incident data rather than
hard-coded scanner strings, and the GitHub Actions trust-boundary guidance
should be recorded as alignment memory because it is a portable methodology
rule. Files to change: scanner script, incident data, runbook, alignment log,
Makefile target, and this story. Risks: false positives from text lockfile
matching and scope creep into direct target-repo remediation. Expected
evidence: scanner output across `projects.yaml`, methodology compile/check,
lint, test, and diff whitespace check. Fresh upstream evidence already captured
from the Aikido report, TanStack postmortem, and GitHub advisory.

20260512-2110 — `/build-story 012` implementation: added
`docs/security/npm-supply-chain-incidents.json`,
`scripts/npm_supply_chain_scan.py`, `make supply-chain-scan`,
`docs/runbooks/npm-supply-chain-hardening.md`, and Alignment 029. Updated Scout
031 with the built scanner evidence. The scanner checks Conductor plus
`projects.yaml` primary checkouts for affected package/version pairs, incident
IOCs, clean related TanStack Query packages, and GitHub Actions workflow
signals.

Scanner evidence from `python3 scripts/npm_supply_chain_scan.py`:

- Conductor, Dossier, Doc Web, Board Game Ingester, Robo Rally, and Echo Forge:
  no npm incident indicators or workflow flags.
- Storybook: clean TanStack Query exposure only:
  `@tanstack/react-query` declared as `^5`, with lockfile
  `@tanstack/react-query@5.90.21` and `@tanstack/query-core@5.90.20`;
  `.github/workflows/db-backup.yml` uses secrets but has no npm install,
  cache, `pull_request_target`, `id-token: write`, or publish combination.
- CineForge: clean TanStack Query exposure only:
  `@tanstack/react-query@5.90.21` and `@tanstack/query-core@5.90.20` in both
  npm and pnpm lock surfaces.
- Summary: affected hits `0`, dependency leads `0`, IOC hits `0`, risky
  workflow combinations `0`.

Build check evidence:

- `python3 -m py_compile scripts/npm_supply_chain_scan.py`
- `make supply-chain-scan`
- `python3 scripts/npm_supply_chain_scan.py --json` parsed with
  `python3 -m json.tool`
- `make methodology-compile`
- `make methodology-check`
- `make lint`
- `make test`
- `git diff --check`

Build result: complete. No target-project remediation was routed because the
scan found no affected package/version hits, no IOCs, and no risky npm
supply-chain workflow combinations. Next step: `/validate 012`.

20260513-0000 — Post-build scope correction from Cam: the central scanner was
not rolled out into the other repos. It only reads the tracked primary
checkouts from Conductor. Before this story can close, decide and document the
operating model for repeat use, wire the scan into an existing workflow surface
or cadence, and either roll out repo-local pointers/hooks through isolated
target-repo worktrees or create explicit target-repo handoffs explaining why
Conductor remains the central owner.

20260513-0025 — Distributed rollout redesign: corrected the operating model to
avoid a runtime dependency from target repos back to Conductor. The scanner is
now designed to run as a single-repo local tool by default, while Conductor's
`make supply-chain-scan` remains a fleet-monitoring convenience over
`projects.yaml`. Target rollout uses isolated worktrees and gives each tracked
repo its own:

- `scripts/npm_supply_chain_scan.py`
- `docs/security/npm-supply-chain-incidents.json`
- `docs/runbooks/npm-supply-chain-hardening.md`
- local command hook: `make supply-chain-scan` or `npm run supply-chain:scan`
- AGENTS guidance and triage/build-story/validate skill triggers

Run model:

- Event-triggered: supply-chain incident triage.
- Change-triggered: dependency upgrades, lockfile/package-manager script
  changes, workflow/publish/deploy/cache/OIDC changes.
- Validation-triggered: story or diff touches those surfaces.
- Supervisor cadence: Conductor can run a weekly fleet sweep, but target repos
  remain self-contained and do not call Conductor.

Target worktree evidence so far:

- Local scanner and strict JSON scans passed in Dossier, Storybook, Doc Web,
  CineForge, Board Game Ingester, Robo Rally, and Echo Forge.
- Local command hooks passed:
  - `make supply-chain-scan`: Dossier, Doc Web, CineForge, Board Game Ingester.
  - `npm run supply-chain:scan`: Storybook, Robo Rally, Echo Forge.
- Skill/methodology checks passed with repo-native commands. Dossier needed the
  primary checkout virtualenv Python, and Storybook/CineForge/Echo Forge
  regenerated methodology outputs because their graph checks include
  time/freshness surfaces.

Next step: commit and push the target-repo rollout branches, then update this
story with commit/push evidence and run Conductor closeout checks.

20260513-0412 — Target rollout branches committed and pushed. Each target repo
now has the self-contained scanner, incident data, runbook, local command hook,
AGENTS guidance, and triage/build-story/validate skill triggers on
`codex/npm-supply-chain-hardening`:

- Dossier: `7556c74`
- Storybook: `8dc5b05`
- Doc Web: `de2e982`
- CineForge: `c36ed94`
- Board Game Ingester: `a23a8d4`
- Robo Rally: `2eccc86`
- Echo Forge: `a0f7f02`

Validation evidence before push:

- strict local scanner runs passed in all seven target worktrees;
- JSON scanner output parsed in all seven target worktrees;
- local command hooks passed in all seven target worktrees;
- repo-native methodology and skill checks passed in all seven target
  worktrees, with only existing/generated freshness warnings in the repos that
  already expose those checks.
