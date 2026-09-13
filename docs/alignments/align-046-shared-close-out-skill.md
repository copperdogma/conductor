# Alignment 046 — Shared Close-Out Skill

**Date**: 2026-09-13
**Classification**: Portable improvement with repo-local validation requirements
**Scope**: Conductor and all seven projects in `projects.yaml`
**Status**: All seven target repos landed and verified; this supervisor commit closes the rollout

## Decision

Cam approved consolidating close-out into `finish-and-push`, deleting `check-in`
and its repo-specific equivalents without compatibility aliases, fixing the
identified workflow ambiguities, and distributing identical skill content across
the tracked repos. The invoking agent remains responsible for completion and
delegates bounded work according to capability and expected total cost.

The shared skill defines authorization, scope, completion, validation evidence,
landing recovery, and optional cleanup. Repo-specific commands and artifact
conventions remain documented by their owning repos. This alignment does not
make Conductor the canonical owner of the distributed harness.

The review was informed by OpenAI's
[Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra):
retain workflow-specific policies while reducing repeated recipes and unnecessary
stop rules. No model-specific identifiers or pricing are embedded in the skill.

## Changes and preservation boundaries

- One shared `finish-and-push/SKILL.md`; no `check-in` or `check-in-diff` alias.
- Read-only audit mode takes precedence over execution and cleanup instructions.
- Story closure occurs once, using each repo's own supported convention.
- Local commands and specific acceptance gates remain in local documentation;
  the shared proportional-validation policy governs close-out and its handoffs.
  Reuse depends on relevant content, environment, and check inputs, not the
  creation of a new commit or entry into another workflow stage.
- Multi-repo preflight and per-repo results support honest partial landing
  recovery, without automatic rollback of successful pushes.
- Cleanup is explicit and limited to eligible task-owned local resources,
  including inspection of ignored content and other tasks' usage.
- Learning detection after landing remains read-only, with separate drafting.
- Active references and generated command surfaces are migrated; historical
  records retain the names used at the time.
- Primary target checkouts, unrelated edits, runtime defaults, and product code
  are outside this rollout's edit scope.

## Execution record

Target worktrees use `/Users/cam/.codex/worktrees/closeout-skill-20260913/<key>`
and branch `codex/closeout-skill-20260913`, based on each repo's freshly fetched
remote main. The [rollout manifest](evidence/shared-close-out-rollout.json)
records full original and integrated base SHAs, worktree paths, branches,
reviewed file allowlists, and verified remote commit receipts. All seven target
main branches and execution branches were pushed without force.

The shared source is `.agents/skills/finish-and-push/SKILL.md` in Conductor.
Expected SHA-256:
`2805622da7e195cacef321898fd7379abee9110462d0149fdcefbe9b56e9de1b`.

| Repo | Base | Validation | State |
| --- | --- | --- | --- |
| Conductor | Current task checkout | Methodology, lint, skills, whitespace; independent scenario review | Supervisor record in this commit |
| Dossier | `ff5ce057` | `make skills-check`; whitespace/reference review | Landed `1c7ede93` |
| Storybook | `16990502` | Skill sync check; `pnpm methodology:check`; whitespace/reference review | Landed `42f25e4d` |
| Doc Web | `bb3c6ffa` | `make skills-check`; `make methodology-check`; whitespace/reference review | Landed `9f09aca6` |
| CineForge | `a8b13f8a` | `make skills-check`; `pnpm methodology:check`; whitespace/reference review | Landed `b5140648` |
| Board Game Ingester | `2aea3fe7` | `make skills-check`; `make check-size`; whitespace/reference review | Landed `89ea2e17` |
| Robo Rally | `42ed0dca` | Skills and methodology checks; `npm run validate`; `npm test` (61 pass); whitespace/reference review | Landed `deef51fe` |
| Echo Forge | `ede96d83` | Skills and methodology checks; `npm run deploy:preflight`; whitespace/reference review | Landed `f8bcfbbf` |

Coordinator verification confirmed all seven target skills match the shared
source byte-for-byte, both retired skill paths are absent, and file changes
remain within the reviewed rollout scope. All target primary checkouts were
preserved. Conductor's earlier skill/README edits remain in the current task
checkout with the alignment record; its unrelated model-watch edits remain outside this rollout. Only the `2026-09-13-03` addition to Conductor's
already-dirty `CHANGELOG.md` belongs to this work.

## Local differences retained

Each target now has a small `docs/runbooks/close-out.md` containing local checks
and artifact conventions, except Echo Forge, which keeps that content at its
existing `docs/runbooks/finish-and-push.md` path. Conductor uses its README.
Duplicate landing recipes were removed instead of copying shared policy into
the local runbooks. Active story-close callers return to the enclosing workflow
without recursively invoking close-out.

Dossier, Doc Web, and CineForge had global delegation advice that differed from
the approved policy. Their `AGENTS.md` files now explicitly defer to the shared
Coordination section for this workflow while retaining general coding policy.
There are no remaining material close-out policy conflicts. Broader model-era
instruction cleanup remains a separate scope.

Historical references were retained. CineForge's active methodology surface
list was updated to the replacement runbook and its retired legacy Cursor
check-in command was removed. Robo Rally has no tracked changelog; none was
introduced. Echo Forge retains its exact-SHA deployment validation rules.

Validation limits and existing warnings:

- Application suites were not run for docs/skill-only changes unless the repo's
  applicable requirements called for them. Checks above are the actual evidence,
  not a claim that every product test was rerun.
- CineForge retained existing architecture-audit and UI-scout freshness warnings;
  its generated outputs were current.
- Board Game Ingester's size check reported existing oversized Python files.
- Echo Forge retained its existing Ideal-parser and Vite chunk-size warnings.
  Its required deployment preflight was local validation, not deployment. Locked
  dependencies and ignored build/private-spell outputs remain in its task
  worktree; they are outside the landing allowlist.

## Remaining work

No target landing work remains. Cam explicitly authorized "finish and push".
Worktrees and branches were retained because cleanup was not requested. Target
primary checkouts were not synchronized; their unrelated work remains intact.

## Approved correction: proportional validation and evidence reuse

Before landing, Cam asked to investigate the Qwen3.8 Flash check-in task
`01a03f1b-a3a0-7722-9dbe-a89227ab283f` and approved correcting the process.
The live task read and timestamped local execution records showed:

- The check-in turn ran from 17:07:36 to 17:40:10 UTC on September 13:
  1,953.598 seconds, versus 1,368.901 seconds for the preceding eval turn.
- Doc Web ran the 975-test product suite twice: 811.18 and 800.64 seconds,
  totaling 82.5% of check-in wall time. CineForge's suite ran concurrently.
- Between Doc Web's suites, changes were changelog/story bookkeeping and
  methodology generation, followed by commit/push; there was no integration
  conflict or remote advance requiring retesting the product code.
- Doc Web's focused adapter, budget-guard, and crop-substrate checks passed
  34 tests in 0.31 seconds. Its landed commit `c88a757` included benchmark
  adapter/probe/configuration code and tests, so "no adoption" did not mean
  the entire diff was documentation-only.

The correction uses actual dependency impact, not verdict labels or filename
extensions, to select checks. Evidence/docs receive integrity and record checks;
isolated tooling receives focused tests/lint and affected-interface checks;
runtime/shared/dependency/build changes justify broader coverage. Explicit task
acceptance requirements and mandatory CI/release gates remain required.

The policy is applied to `finish-and-push`, `validate`, `mark-story-done`, local
close-out runbooks, and scoped `AGENTS.md` guidance. Generic current-pass/full-suite
wording no longer forces redundant executions. A test that genuinely consumes
Git metadata includes that metadata in its reuse decision. Unchanged application
tests and deployment preflight evidence from the initial rollout need not be
repeated for this instruction-only correction.

Independent read-only scenario review verified the intended decisions for
evidence-only rejection records, isolated benchmark adapters, runtime parsing
changes, integration-time dependency/test-config changes, and a build test that
embeds the commit SHA. The review retained broader checks and mandatory gates
where inputs or affected consumers changed; it did not interpret "do not adopt"
as an exemption from testing.

The correction was checked with affected skill/document checks and per-repo
contradiction scans, rather than rerunning unchanged application suites. The
coordinator compared all eight shared copies and reviewed local handoff rules.
Echo Forge's earlier deployment preflight remains applicable because its
package, runtime, private-spell, and build inputs did not change; its separate
actual-deployment exact-SHA and smoke requirements remain intact.

Landing integrated the advanced remote bases in Doc Web and Storybook. Each
had one mechanical changelog conflict; all upstream entries were retained, with
rollout entries numbered `2026-09-13-03` and `2026-09-13-06` respectively. The
affected skill/document/methodology checks passed after integration. No changed
product inputs required repeating the prior application suites. All seven
primary inboxes were inspected and had no uncommitted capture to reconcile.
