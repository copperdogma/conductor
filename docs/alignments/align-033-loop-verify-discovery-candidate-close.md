# Alignment 033 — Loop Verify Discovery and Candidate-Close Phases

**Date:** 2026-05-16

## Focus

Refine `/loop-verify` after doc-web exposed a second runaway-loop class: strict
verification treated every material fix as a near-final candidate and repeatedly
paid expensive closeout costs before the defect landscape had stabilized.

Surfaces compared:

- doc-web Story 229 post-mortem supplied by Cam
- Conductor `/loop-verify` after Alignment 029 runaway controls
- Conductor `/validate` and Alignment 030 closeout boundary
- prior Storybook, Echo Forge, and doc-web verification-loop memories

## Source Failure

The doc-web post-mortem identified that the failure was not simply "too much
verification." The problem was sequencing:

- finding breadth and expensive closure work were interleaved too early
- same-class portability/privacy issues were discovered one instance at a time
- full suites, proof generation, generated docs, and closeout surfaces ran
  while new material defect classes were still likely
- main-agent context was spent rereading large diffs and logs instead of
  maintaining a compact finding ledger

Alignment 029 already fixed recursion, uncapped docs/ADR loops, worker scope
widening, stale-agent noise, and weak expansion gates. Alignment 030 already
kept `/validate` as the closure authority. The missing behavior is strict-mode
phase discipline.

## Contract

Strict `/loop-verify` work should be phase-based:

- **Discovery:** find-only worker breadth scans across disjoint threat surfaces.
  Output is a finding ledger grouped by defect class.
- **Systemic-fix:** when a defect class repeats, stop instance-by-instance
  resets and patch the class centrally or with one clearly owned slice.
- **Focused-confirmation:** run direct probes and focused regressions for the
  whole defect class.
- **Candidate-close:** only after discovery and focused confirmation stop
  finding new material classes, run affected suites, generated proofs/docs,
  changelog/story updates, full suite, advisory review, or other expensive
  final confidence signals.

Validation tiers should be explicit:

- Tier 0: direct probes, helper scripts, schema checks, static searches, tiny
  reproductions
- Tier 1: focused regression tests for the affected class
- Tier 2: affected suite or package-level checks
- Tier 3: generated docs, proof artifacts, snapshots, changelog/story updates
- Tier 4: full suite, advisory review, broad evals, deploy smoke

While the ledger is dirty, stay in Tier 0-1 unless a higher tier is required to
reproduce the defect. Run Tier 3-4 only in candidate-close.

## Classification

Portable improvement with local adaptation.

The behavior should sync to every tracked repo that carries `/loop-verify`
because the failure mode is task-shape based rather than doc-web-specific.
Repos may keep local check commands, generated-wrapper requirements, and
project-specific examples.

## Recommendation

Adopt the refined strict-mode phase contract across tracked repos that already
carry `/loop-verify`.

Rollout should be narrow:

- update `.agents/skills/loop-verify/SKILL.md`
- regenerate wrappers or methodology surfaces only where repo-local tooling
  requires it
- validate with repo-native skill/methodology checks and `git diff --check`
- do not touch `/validate`, target-product code, provider config, or historical
  story evidence unless local tooling requires generated index refreshes

## Stop Conditions

- Do not run another broad `/loop-verify` to validate this change; that would
  use the failure-prone workflow while editing the workflow.
- Do not delete strict-until-clean. It remains useful for objective,
  contract-critical work once candidate-close is reached.
- Do not claim target repos have the behavior until isolated target worktrees
  apply and validate it.
- Do not treat generated docs/changelog/story work as dirty-loop validation
  evidence. It belongs at candidate-close.

## Practical Impact

This should make the next doc-web-style portability or privacy hardening loop
notice same-class defects earlier, patch them once, and avoid burning hours on
full closeout ceremony before the runtime contract has stabilized.

## Rollout Evidence

Implementation work happened in isolated worktrees on branch
`codex/loop-verify-discovery-close-20260516`:

- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/dossier`
- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/storybook`
- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/doc-web`
- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/cine-forge`
- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/boardgame-ingester`
- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/roborally`
- `/Users/cam/.codex/worktrees/loop-verify-discovery-close-20260516/echo-forge`

All target worktrees were created from current `origin/main`:

| Project | Base |
| --- | --- |
| Dossier | `998db9c` |
| Storybook | `e2348f6` |
| doc-web | `0000863` |
| CineForge | `16cb6be` |
| Board Game Ingester | `75491af` |
| Robo Rally | `673c979` |
| Echo Forge | `1cf191c` |

Applied changes:

- Dossier, doc-web, Board Game Ingester, Robo Rally, and Echo Forge changed only
  `.agents/skills/loop-verify/SKILL.md`.
- Storybook changed `.agents/skills/loop-verify/SKILL.md` plus regenerated
  `docs/methodology/graph.json` and `docs/stories.md`; the generated diff only
  advanced UI-scout freshness from 11 to 12 days.
- CineForge changed `.agents/skills/loop-verify/SKILL.md` plus regenerated
  `docs/build-map.md`, `docs/methodology/graph.json`, and `docs/stories.md`;
  the generated diff only advanced the last-generated date and UI-scout
  freshness from 34 to 35 days.

Validation evidence:

| Project | Checks |
| --- | --- |
| Dossier | `./scripts/sync-agent-skills.sh --check`, `PYTHONDONTWRITEBYTECODE=1 PYTHON=/Users/cam/Documents/Projects/dossier/.venv/bin/python make methodology-check`, and `git diff --check` passed. Existing legacy/non-local metadata warnings remain unrelated. |
| Storybook | `pnpm methodology:compile`, `./scripts/sync-agent-skills.sh --check`, `pnpm methodology:check`, and `git diff --check` passed. |
| doc-web | `PYTHONDONTWRITEBYTECODE=1 make skills-check methodology-check` and `git diff --check` passed. |
| CineForge | `npm run methodology:compile`, `./scripts/sync-agent-skills.sh --check`, `npm run methodology:check`, and `git diff --check` passed. Existing architecture-audit and UI-scout freshness warnings remain unrelated. |
| Board Game Ingester | `PYTHONDONTWRITEBYTECODE=1 make skills-check methodology-check lint` and `git diff --check` passed. |
| Robo Rally | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. |
| Echo Forge | `npm run skills:check`, `npm run methodology:check`, and `git diff --check` passed. Existing `No Ideal requirements parsed` warning remains unrelated. |

Primary target checkouts were inspected before rollout and kept untouched.
Storybook, CineForge, and Echo Forge had unrelated dirty files; Board Game
Ingester's primary checkout was on a feature branch. The rollout used isolated
worktrees for all target repos.
