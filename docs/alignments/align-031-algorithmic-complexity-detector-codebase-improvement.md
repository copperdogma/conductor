# Alignment 031 - Optional Detector Guidance for Codebase Improvement

**Date**: 2026-05-16
**Classification**: Portable improvement
**Source**: [Scout 033](../scout/scout-033-codex-complexity-optimizer-codebase-improvement.md)
and [Scout 034](../scout/scout-034-clawpatch-automated-code-review.md)
**Story**: [Story 014](../stories/story-014-algorithmic-complexity-detector-codebase-improvement.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Decision

Adapt useful external detector ideas into the existing
`/codebase-improvement-scout` lane as instruction-level guidance.

Do not install the npm package globally, require `npx
codex-complexity-optimizer`, or create a standalone "complexity optimizer" lane.
The package is a useful reference, but the tracked repos already have the more
important local discipline: report-first scans, repo-native proof, ranking by
leverage, one best next step, and guarded story or auto-fix follow-up.

Scout 034 adds a heavier sibling detector shape: occasional report-only
semantic review with Clawpatch or a similar repo-wide AI reviewer. That belongs
in the same codebase-improvement lane when used, not in `/validate`, CI, or
every-story closeout.

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

Treat periodic AI semantic review as a separate optional detector category. It
is appropriate when codebase-improvement freshness is stale, a repo has seen
substantial churn, tests are thin around an important area, a release or cleanup
pass needs another bug-discovery signal, or Cam explicitly asks for a broader
latent-bug sweep.

Semantic review tools must stay report-only in this lane:

- run in an isolated worktree
- pin the package version or source commit
- keep generated state outside the repo when possible
- use limited review batches first
- never run tool-managed fix paths during scout-mode use
- verify every accepted finding against local code and repo-native tests before
  creating stories or patches

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
- Do not run semantic review tools as normal validation, CI, or every-story
  closeout.
- Do not let performance tuning outrank product, artifact, provider, or
  UI-taste work without repo-local triage evidence.
- If a helper script is ever added, vendor or recreate a reviewed local helper
  instead of requiring remote npm execution in normal workflows.

## Rollout Decision

Roll the guidance into target repos that already carry
`.agents/skills/codebase-improvement-scout/SKILL.md`, preserving local variants
and proof surfaces. This is a small methodology wording update, not a product
story in any target repo.

The completed Story 014 target-repo rollout covered Scout 033's deterministic
complexity detector guidance. Scout 034 extends that same target-repo guidance
with optional semantic review now. The first natural use in each repo is the
pilot: if the tool is noisy, awkward, or exposes a better local pattern, fix the
local skill/runbook first and then use Conductor alignment to distribute the
improved wording where it applies.

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
- Scout 034 concluded that Clawpatch is credible enough for a bounded
  report-only detector role, but not for always-on adoption.
