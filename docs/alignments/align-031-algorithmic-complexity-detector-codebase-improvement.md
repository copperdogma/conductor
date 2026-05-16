# Alignment 031 - Algorithmic Complexity Detector Guidance for Codebase Improvement

**Date**: 2026-05-16
**Classification**: Portable improvement
**Source**: [Scout 033](../scout/scout-033-codex-complexity-optimizer-codebase-improvement.md)
**Story**: [Story 014](../stories/story-014-algorithmic-complexity-detector-codebase-improvement.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Decision

Adapt the useful parts of `codex-complexity-optimizer` into the existing
`/codebase-improvement-scout` lane as instruction-level detector guidance.

Do not install the npm package globally, require `npx
codex-complexity-optimizer`, or create a standalone "complexity optimizer" lane.
The package is a useful reference, but the tracked repos already have the more
important local discipline: report-first scans, repo-native proof, ranking by
leverage, one best next step, and guarded story or auto-fix follow-up.

## Portable Guidance

When a repo has enough code for `/codebase-improvement-scout`, treat
algorithmic complexity as one optional deterministic detector category. It can
surface leads such as:

- nested scans or callback loops
- membership/search inside loops
- sort-in-loop behavior
- render-derived collection work in UI components
- N+1-shaped IO, query, or API loops
- repeated expensive derivations that can be moved, memoized, indexed, grouped,
  batched, or measured

These are leads, not findings by themselves. Before a candidate becomes a story
or patch, the scan must inspect the local code, confirm the data shape and hot
path, and explain why the current behavior is plausibly costly.

## Report Shape

For accepted complexity candidates, the codebase-improvement report should
capture:

- current pattern
- estimated current complexity
- recommended change
- estimated complexity after the change
- why behavior should remain equivalent
- risk level
- tests, benchmarks, profiler/browser evidence, or manual measurements needed

For UI-heavy repos, browser or profiler evidence matters more than a generic
scanner result before claiming performance improvement. For pipeline-heavy
repos, artifact truth and benchmark/driver output remain the proof surface.

## Boundaries

- Keep default behavior report-only.
- Keep scanner output non-authoritative.
- Do not auto-refactor performance findings without behavior tests,
  meaningful input-size evidence, and an ownership boundary.
- Do not let performance tuning outrank product, artifact, provider, or
  UI-taste work without repo-local triage evidence.
- If a helper script is ever added, vendor or recreate a reviewed local helper
  instead of requiring remote npm execution in normal workflows.

## Rollout Decision

Roll the guidance into target repos that already carry
`.agents/skills/codebase-improvement-scout/SKILL.md`, preserving local variants
and proof surfaces. This is a small methodology wording update, not a product
story in any target repo.

## Evidence

- Scout 033 inspected the X post, GitHub repo, npm metadata, and npm tarball on
  2026-05-16 without installing or running the package.
- The package defaults analysis requests to no file modification and correctly
  frames scanner output as leads.
- Conductor's existing alignment memory already defines codebase improvement as
  report-first, deterministic, ranked by churn/size/complexity/risk, and
  separate from architecture triage.
- Current target repos already have `codebase-improvement-scout` skill
  variants, so adaptation can stay lightweight and local.
