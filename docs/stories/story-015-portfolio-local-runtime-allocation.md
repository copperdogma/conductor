---
title: "Portfolio Local Runtime Allocation"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.2"
  - "spec:4.2"
  - "spec:5.1"
decision_refs: []
depends_on: []
category_refs:
  - "registry-routing"
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "storybook"
  - "cine-forge"
  - "echo-forge"
  - "roborally"
  - "boardgame-ingester"
  - "dossier"
  - "doc-web"
---

# Story 015 — Portfolio Local Runtime Allocation

**Priority**: High
**Status**: Done
**Decision Refs**: None yet
**Depends On**: None

## Goal

Turn Echo Forge's work-in-progress local service launcher into a portfolio
runtime contract: Conductor owns port allocation, runtime-heavy repos can start
and inspect local services safely, and future `/setup-methodology` runs teach
new repos to adopt the pattern when they grow a local web/API surface.

## Acceptance Criteria

- [x] Conductor records canonical primary ports, worktree ranges, service
  offsets, and slot-state rules in a machine-readable allocation file.
- [x] Storybook, CineForge, and Echo Forge have repo-local launch/status/stop
  surfaces that read the Conductor allocation instead of inventing ranges.
- [x] README files explain the local runtime command and reserved ranges, or
  clearly mark launchers as deferred for repos without a runtime.
- [x] The shared `/setup-methodology` skill tells future repos to add the
  Conductor-owned local runtime contract when a local web/API surface exists.
- [x] Target repo work happens in isolated worktrees and records validation
  evidence without touching dirty primary checkouts.

## Out of Scope

- Committing, pushing, or landing the rollout without explicit approval.
- Adding fake launchers to repos that do not yet have a local runtime.
- Replacing Storybook's Google-auth-safe primary `5173/3001` contract.
- Building a central daemon or global port broker.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, and decision context
- [x] Implement the needed doc, skill, script, or log changes
- [x] Update related scout or alignment memory if applicable
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: targeted repo syntax and native
        checks were run instead of Conductor `make test`
- [x] Search docs and update any related surfaces
- [x] Verify Conductor tenets:
  - [x] I1 — Meaning over text
  - [x] I2 — Distributed ownership
  - [x] I3 — Recommendation-first supervision
  - [x] I4 — Honest divergence
  - [x] I5 — Minimal overhead

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `local-dev-ports.json` — canonical Conductor-owned port allocation.
- `docs/alignments/align-032-portfolio-local-runtime-allocation.md` — durable
  alignment record and rollout plan.
- `docs/align-projects.md` — alignment index.
- `.agents/skills/setup-methodology/SKILL.md` — shared setup guidance for
  future repo-local runtime launchers.
- `docs/runbooks/setup-methodology.md` — operator-facing setup summary.
- target repo worktrees under
  `/Users/cam/.codex/worktrees/local-runtime-allocation/` — isolated rollout
  patches for README/setup/launcher surfaces.

## Notes

The inbox item came from Echo Forge's uncommitted c370 worktree. That worktree
had `scripts/local-service.mjs`, `local:*` npm scripts, health endpoints for
Registry QA and Studio, and Codex actions. A live status run showed the exact
failure class this story addresses: the c370 worktree owned app `5175` and
registry QA `4177`, while Studio `4178` was occupied by the primary checkout.

## Plan

1. Add Conductor's canonical `local-dev-ports.json` with stable primary ports,
   per-project worktree ranges, service offsets, strict-port rules, and
   `~/.codex/local-dev-ports.json` slot persistence.
2. Add Alignment 032 and update the alignment index.
3. Update shared `/setup-methodology` and setup runbook guidance so future
   repos use Conductor allocation instead of local ad hoc ranges.
4. Patch Storybook, CineForge, and Echo Forge in isolated worktrees with
   repo-local launch/status/stop surfaces reading the allocation file.
5. Patch Dossier, Doc Web, Robo Rally, and Board Game Ingester README/setup
   guidance with reserved ranges and a deferred-launcher rule.
6. Run syntax and narrow repo-native checks for changed scripts/docs, then
   report remaining validation or landing work.

## Work Log

20260515-0000 — story-created: created Story 015 from the Conductor inbox item
and Echo Forge c370 launcher pilot. Evidence: inspected
`/Users/cam/.codex/worktrees/c370/echo-forge/scripts/local-service.mjs`, status
output, npm scripts, health endpoint changes, and Codex action config. Next
step: patch Conductor allocation/setup surfaces, then isolated target repo
worktrees.

20260515-0100 — conductor-surfaces: added `local-dev-ports.json`, Alignment
032, setup-methodology/runbook guidance, and `projects.yaml` comparison
surfaces for README, environment, and local launcher files. Generated
methodology surfaces were refreshed with `make methodology-compile`.

20260515-0115 — target-rollout: created isolated worktrees under
`/Users/cam/.codex/worktrees/local-runtime-allocation/<project-key>` on branch
`codex/local-runtime-allocation`. Storybook, CineForge, and Echo Forge now have
repo-local launch/status/stop surfaces that read the Conductor allocation.
Echo Forge also carries the c370-style Codex app actions for its named local
services. Dossier, Doc Web, Robo Rally, and Board Game Ingester now document
reserved ranges and defer launchers until they have real local web/API
runtimes.

20260515-0130 — validation-evidence: setup-methodology skill copies match
Conductor byte-for-byte across all seven target worktrees. Script syntax and
dry status checks passed for Storybook, CineForge, and Echo Forge with a temp
allocation file. Repo-native checks passed for Storybook, CineForge, Echo
Forge, Robo Rally, Dossier, Doc Web, and Board Game Ingester; Dossier required
the repo virtualenv Python because the ambient `python3` lacked PyYAML.

20260516-0000 — rebase-refresh: rebased Conductor and all seven target
worktrees onto current `origin/main`; `HEAD...origin/main` is `0 0` in every
worktree. Main added its own Alignment 031 / Story 014, so this rollout moved
to Alignment 032 / Story 015. Echo Forge main already contained the local
launcher pilot, README, Codex actions, and authoring-service health endpoints;
the remaining Echo Forge diff now focuses on Conductor allocation lookup,
README allocation wording, and the shared setup-methodology copy. Re-ran
Conductor checks, target repo native checks, runtime launcher syntax checks,
and dry local-status checks with `/tmp/conductor-local-dev-ports-rebase.json`.
Storybook and CineForge regenerated methodology outputs after the rebase because
their setup-methodology text changed against current main.

20260516-0100 — target-landing: landed the target repo rollout to `main` first,
all from isolated `codex/local-runtime-allocation` worktrees. Commits:
Dossier `998db9c`, Storybook `e2348f6`, Doc Web `0000863`, CineForge
`16cb6be`, Board Game Ingester `75491af`, Robo Rally `673c979`, Echo Forge
`1a8afec`. Echo Forge needed one final rebase because its `main` moved again
during landing; validation was rerun after that rebase. Each target worktree
ended at `HEAD...origin/main` = `0 0`.

20260516-0115 — story-closeout: removed the handled Align projects item from
`inbox.md`, marked Story 015 done, and regenerated Conductor methodology
surfaces. The remaining Conductor inbox items are unrelated live capture.
