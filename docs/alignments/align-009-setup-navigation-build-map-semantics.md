# Alignment 009 — Setup Navigation Build-Map Semantics

**Date**: 2026-04-11
**Focus**: Compare the operator-facing setup/navigation surface after the
state/graph migrations and decide what `docs/build-map.md` should mean across
the tracked repos
**Source Project**: Baseline across `dossier`, `storybook`, `doc-web`, and `cine-forge`
**Target Projects**: `dossier`, `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- Dossier `AGENTS.md`, `docs/build-map.md`, `docs/setup-checklist.md`,
  `docs/runbooks/setup-methodology.md`
- Storybook `AGENTS.md`, `docs/build-map.md`, `docs/setup-checklist.md`,
  `docs/runbooks/setup-methodology.md`
- doc-web `AGENTS.md`, `docs/build-map.md`, `docs/setup-checklist.md`,
  `docs/runbooks/setup-methodology.md`
- CineForge `AGENTS.md`, `docs/build-map.md`, `docs/setup-checklist.md`,
  `docs/runbooks/setup-methodology.md`
- Dossier Story 095 and CineForge Story 145 as the strongest local evidence for
  the post-migration role of `docs/build-map.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the goal is to align the meaning of the setup/navigation surface,
  not to force one textual package everywhere.
- Alignment 001 already identified Dossier's old build-map-first methodology as
  a real conflict. That conflict is now closed locally: Dossier Story 095
  explicitly demoted `docs/build-map.md` to a supporting archived redirect.
- CineForge Story 145 made a different but explicit local choice: keep
  `docs/build-map.md` as a generated dashboard view compiled from
  `docs/methodology/state.yaml` and `docs/methodology/graph.json`.
- No narrower Conductor decision record was found for whether post-migration
  repos should archive `docs/build-map.md`, keep it as a generated dashboard,
  or drop the path entirely. The settled shared rule is only that mutable
  planning authority lives in state/graph, not in a hand-authored build map.

## Key Differences

- Dossier, Storybook, and doc-web all retired the hand-authored build map as a
  mutable planning authority, but they do not teach that demotion equally
  clearly:
  - Dossier says so explicitly in `AGENTS.md`, `docs/build-map.md`, and the
    setup runbook/checklist.
  - doc-web says so explicitly in `AGENTS.md` and `docs/build-map.md`, but its
    setup runbook/checklist do not repeat the archived-role guidance.
  - Storybook's `docs/build-map.md` is archived, but the current AGENTS/setup
    navigation surface largely omits what that path now means.
- CineForge intentionally keeps `docs/build-map.md` as a generated
  human-readable dashboard. Its AGENTS, checklist, and runbook all say the
  file is derived from state/graph and is not the writable authority.
- Setup checklists now serve two different operator meanings:
  - Storybook, doc-web, and CineForge read like current package-state snapshots
    with completed checklist items.
  - Dossier still reads like an in-progress working copy, with core
    state/graph migration items left unchecked even though the migration story,
    AGENTS surface, and runbook already present that package as landed.
- Runbook style also differs:
  - Dossier and CineForge use procedural bootstrap guides with explicit steps,
    boundaries, and troubleshooting.
  - Storybook and doc-web use more conceptual front-door explanations of the
    methodology package.
- Repo-specific setup overlays remain intentionally different:
  - doc-web keeps the coverage matrix in the core hierarchy
  - Storybook and CineForge surface extra recurring lanes
  - Dossier stays on the smaller shared story/eval/alignment spine

## Classification

- **Intentional adaptation**: CineForge keeping a generated `docs/build-map.md`
  dashboard is a deliberate local choice, not unexplained drift. Dossier,
  Storybook, and doc-web archiving the path is also legitimate once
  state/graph owns mutable planning truth. Procedural versus conceptual
  runbook style, plus repo-specific optional lanes and coverage surfaces,
  should stay local.
- **Portable improvement**: operator-facing setup docs should always make the
  current role of `docs/build-map.md` explicit whenever the path still exists:
  archived redirect, generated dashboard, or intentionally unused. The setup
  checklist should also be honest about whether it is a current status snapshot
  or a live in-progress worklist.
- **Methodology conflict**: none in this slice once the shared rule is framed
  correctly: state/graph is the mutable authority, while `docs/build-map.md`
  may remain as a generated or archived navigation surface per repo.
- **Unclear drift**: Storybook's omission of the archived build-map role from
  the top-level setup/navigation docs looks more like documentation lag than an
  intentional local choice. Dossier's partially unchecked setup checklist also
  reads as stale packaging rather than an intentionally active refresh run.

## Recommendation

- **dossier**: Sync partially. Keep the archived redirect model and the
  procedural setup runbook, but refresh `docs/setup-checklist.md` so its check
  state matches the shipped package, or label it explicitly as an active
  in-progress worklist rather than a current-status snapshot.
- **storybook**: Sync partially. Keep the archived redirect model and the
  conceptual setup runbook, but add explicit archived-build-map guidance to the
  operator-facing setup/navigation surface so `docs/build-map.md` is not a
  silent leftover path.
- **doc-web**: Sync partially. Keep the coverage-matrix-first package and the
  archived redirect build-map, but mirror the archived-role guidance in the
  setup runbook/checklist so operators do not have to infer the path's status
  by opening `docs/build-map.md` directly.
- **cine-forge**: Keep local. The generated-dashboard role for
  `docs/build-map.md` is explicit and consistent across AGENTS, checklist, and
  runbook, so no convergence work is justified just for symmetry.

## Human Decision Needed

- None for the classification pass itself.
- If execution is desired, the clean scope is a narrow doc-clarification sweep
  in Storybook and doc-web plus a checklist-state refresh in Dossier. No
  portfolio-wide build-map standardization decision is required first.

## Result

- No target-project story or patch was created in this pass. The honest
  supervisor artifact is the alignment record because the current pressure is
  documentation clarity around an already-set methodology boundary, not a new
  cross-project migration.
- 2026-04-11 execution follow-up: prepared dedicated target-repo worktrees on
  branch `codex/build-map-setup-clarity`:
  - Dossier: `/Users/cam/.codex/worktrees/build-map-setup-clarity/dossier`
  - Storybook: `/Users/cam/.codex/worktrees/build-map-setup-clarity/storybook`
  - doc-web: `/Users/cam/.codex/worktrees/build-map-setup-clarity/doc-web`
- Applied the narrow doc-clarification landing only:
  - Dossier: refreshed `docs/setup-checklist.md` so the state/graph migration
    boxes reflect the already-shipped package
  - Storybook: added explicit archived-`docs/build-map.md` guidance to
    `AGENTS.md` and `docs/runbooks/setup-methodology.md`
  - doc-web: added explicit archived-`docs/build-map.md` guidance to
    `AGENTS.md` and `docs/runbooks/setup-methodology.md`
- Verified the target worktrees with repo-local checks:
  - Dossier: `make methodology-check PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python`
  - Storybook: `pnpm methodology:check`
  - doc-web: `make methodology-check`
- 2026-04-16 verification follow-up: checked the dedicated worktree tip commits
  against the corresponding target `main` branches and confirmed the landing is
  already complete:
  - Dossier: `c3e7c0f` is an ancestor of `main`
  - Storybook: `23d7637` is an ancestor of `main`
  - doc-web: `9b2c55a` is an ancestor of `main`
- 2026-04-16 cleanup follow-up: removed the dedicated local
  `codex/build-map-setup-clarity` worktrees after verification. The local
  worktree cleanup for this line is complete.

## Follow-Up

- No new Conductor story was created.
- The classification follow-up is executed and verified as landed.
- 2026-04-16 branch cleanup follow-up: deleted the merged local
  `codex/build-map-setup-clarity` branches after confirming no remaining
  worktree still had them checked out.
- Supervisor memory for this line is current; no further local worktree or
  merged-branch cleanup is pending.
