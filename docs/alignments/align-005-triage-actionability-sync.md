# Alignment 005 — Triage Actionability Sync

**Date**: 2026-04-10
**Focus**: Port Dossier's compiled triage actionability improvements into the
other tracked product repos
**Source Project**: `dossier`
**Target Projects**: `storybook`, `doc-web`, `cine-forge`

## Surfaces Compared

- Dossier commits `f69736f` and `fe34ed4`
- Dossier `scripts/methodology_graph.py`
- Dossier `.agents/skills/triage/SKILL.md`
- Dossier `.agents/skills/triage-evals/SKILL.md`
- Storybook `scripts/methodology-graph.ts`
- Storybook `.agents/skills/triage/SKILL.md`
- Storybook `.agents/skills/triage-evals/SKILL.md`
- Storybook `docs/runbooks/triage.md`
- Storybook `docs/runbooks/triage-evals.md`
- doc-web `scripts/methodology_graph.py`
- doc-web `tests/test_methodology_graph.py`
- doc-web `.agents/skills/triage/SKILL.md`
- doc-web `.agents/skills/triage-evals/SKILL.md`
- CineForge `scripts/methodology-graph.js`
- CineForge `tests/unit/test_methodology_graph.py`
- CineForge `.agents/skills/triage/SKILL.md`
- CineForge `.agents/skills/triage-evals/SKILL.md`
- CineForge `docs/runbooks/triage.md`
- CineForge `docs/runbooks/triage-evals.md`

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the sync target is shared meaning, not text identity.
- Dossier is the current innovation lane for the methodology package. Its
  `f69736f` compiler change introduced a structured actionability summary into
  the generated methodology graph, and `fe34ed4` fixed the compromise fallback
  path so triage can still explain why a closed line should stay closed.
- Storybook and CineForge already had some human-facing triage guardrails about
  blocked lines and exhausted retry triggers, but they did not yet compile the
  same inspectable actionability surface into `docs/methodology/graph.json`.
- doc-web was further behind: it needed both the compiler-backed actionability
  metadata and the triage prompt updates that consume it.

## Key Differences

- Dossier now compiles story actionability from work-log and blocker truth,
  eval actionability from attempts and retry conditions, and compromise
  actionability from the best available story or eval lineage.
- Storybook and CineForge already expressed some of the same judgment in skill
  prose, but their methodology graph compilers did not export the same
  reusable fields (`lastRelevantAction`, retry-trigger posture, and a clear
  "why now" summary).
- doc-web lacked both the richer compiler output and the stronger triage/triage-evals
  guidance that prefers compiled actionability over ad hoc inference.
- The portable improvement is the structured actionability contract, not a
  literal copy of Dossier's implementation language. Each repo keeps its own
  compiler language, test style, and runbook wording.
- Third-pass audit note: Dossier's free-text retry-trigger inference is not a
  clean portable default for Storybook or CineForge. Their older eval
  descriptions include historical phrases like "after golden fix" that would
  incorrectly resurrect settled lines as live retry candidates. The structured
  `retry_when` / retry-state metadata is the portable contract; broad text-hint
  inference stays repo-specific.

## Classification

- **Portable improvement**: compile actionability metadata into the methodology
  graph and teach triage surfaces to prefer that metadata when deciding what is
  actionable now.
- **Intentional adaptation**: keep each repo's compiler language, local
  runbook structure, and repo-specific story/eval wording.
- **Methodology conflict**: none found in this slice.
- **Unclear drift**: none strong enough to justify holding the sync.

## Recommendation

- **dossier**: Keep local as the current source reference for this actionability
  model.
- **storybook**: Sync partially. Port the compiled actionability surface into
  the TypeScript compiler and update triage docs to require last-action and
  why-now reasoning from the generated graph.
- **doc-web**: Sync partially. Port the Python compiler additions, add the
  missing test coverage, and update triage wrappers/prompts to consume the new
  graph fields.
- **cine-forge**: Sync partially. Port the JavaScript compiler additions and
  update the triage runbooks without removing CineForge's own dashboard/design-aware
  context.

## Result

- Prepared dedicated target-repo worktrees on branch
  `codex/triage-actionability-sync`:
  - Storybook: `/Users/cam/.codex/worktrees/triage-actionability-sync/storybook`
  - doc-web: `/Users/cam/.codex/worktrees/triage-actionability-sync/doc-web`
  - CineForge: `/Users/cam/.codex/worktrees/triage-actionability-sync/cine-forge`
- Applied the compiled actionability sync inside each target repo's local task
  worktree:
  - Storybook: updated `scripts/methodology-graph.ts`,
    `.agents/skills/triage/SKILL.md`, `.agents/skills/triage-evals/SKILL.md`,
    `docs/runbooks/triage.md`, and `docs/runbooks/triage-evals.md`
  - doc-web: updated `scripts/methodology_graph.py`,
    `tests/test_methodology_graph.py`, `.agents/skills/triage/SKILL.md`,
    `.agents/skills/triage-evals/SKILL.md`, and regenerated the triage Gemini
    wrappers
  - CineForge: updated `scripts/methodology-graph.js`,
    `tests/unit/test_methodology_graph.py`,
    `.agents/skills/triage/SKILL.md`, `.agents/skills/triage-evals/SKILL.md`,
    `docs/runbooks/triage.md`, and `docs/runbooks/triage-evals.md`
- Verified the target patches with repo-local checks:
  - Storybook: `pnpm methodology:test`, `pnpm methodology:compile`,
    `pnpm methodology:check`, `./scripts/sync-agent-skills.sh --check`
  - doc-web: `pytest tests/test_methodology_graph.py -q`,
    `make methodology-compile methodology-check`,
    `./scripts/sync-agent-skills.sh --check`
  - CineForge: `pytest tests/unit/test_methodology_graph.py -q`,
    `node scripts/methodology-graph.js build`,
    `node scripts/methodology-graph.js check`, and
    `./scripts/sync-agent-skills.sh --check`
- Second-pass audit follow-up: the first execution pass left two incomplete
  compiler carry-throughs that were fixed before closeout:
  - Storybook was still dropping eval `description` and top-level `retry_when`
    metadata from the generated graph, which also caused some exhausted retry
    lines to degrade to `no-trigger-recorded`
  - CineForge was still dropping eval `description` and top-level scalar
    `retry_when` metadata from the generated graph
  - After patching those parsers, the same repo-local compile/check/test passes
    were rerun and the generated graphs now carry the missing actionability
    fields
- Added closeout regression coverage before landing:
  - Storybook: `scripts/methodology-graph.test.mjs` plus a
    `package.json` `methodology:test` script
  - CineForge: an extra regression in
    `tests/unit/test_methodology_graph.py` covering eval `description` plus
    top-level `retry_when` carry-through
- Landed the validated task branches onto each target repo's `main` branch:
  - Storybook: `c163be7` (`Compile triage actionability into methodology graph`)
  - doc-web: `984ec49` (`Compile triage actionability into methodology graph`)
  - CineForge: `aba2ac5` (`Compile triage actionability into methodology graph`)
- CineForge's existing UI-scout freshness warning remained present during the
  final `node scripts/methodology-graph.js check` pass, but it is pre-existing
  planning state rather than a regression from this sync.
- 2026-04-16 verification follow-up: checked those landing commits against the
  current target `main` branches and confirmed they remain ancestors of `main`.
- 2026-04-16 cleanup follow-up: removed the dedicated local
  `codex/triage-actionability-sync` worktrees after verification. The local
  worktree cleanup for this line is complete.

## Follow-Up

- No new Conductor story was created. The honest supervisor artifact for this
  line is the alignment record plus the landed target-repo updates.
- Conductor itself was not a sync target for this pass. The change belongs to
  the tracked product repos' methodology packages, not to the supervisor loop.
- 2026-04-16 branch cleanup follow-up: deleted the merged local
  `codex/triage-actionability-sync` branches after confirming no remaining
  worktree still had them checked out.
- Supervisor memory for this line is current; no further local worktree or
  merged-branch cleanup is pending.
