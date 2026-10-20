# Alignment 058 — Complete and exercise the reusable setup package

Date: 2026-10-18. Scope: Conductor source library and disposable test projects.
The five target Ideal rewrites remain paused. No project enrollment or rollout.

## Owner intent and scope

Cam approved completing and testing Conductor's reusable setup package before
returning to other projects. Cam then highlighted that Conductor's own skills
are tailored to supervisor work and cannot all be assumed universal.

The package therefore selects explicit role variants rather than copying the
supervisor wholesale. The [source package manifest](../../.agents/skills/setup-methodology/package.json)
is the inventory; the [installation guide](../../.agents/skills/setup-methodology/references/package-installation.md)
explains role selection, preservation, adaptation and proof limits. ADR-004
continues to govern reusable baseline ownership and learning from local work.

## Source comparison and extraction

Read-only comparison covered Dossier, Storybook, Doc Web, CineForge and Echo
Forge. Local product copies contain useful common semantics and meaningful
local assumptions: format/EntityGraph schemas, pinned upstream dependencies,
model discovery scripts, framework commands, fixture paths, browser scenarios,
and source-intake/production rules. These are not copied into a generic core.

[Source provenance](evidence/align-058-package-sources.json) records 44 inspected
skill/resource/tool source files with hashes and their use. The new generic
skills and product variants are adaptations of common contracts, not byte-copy
or universal-equivalence claims.

- Storybook checklist/modes and create-eval/golden workflows informed bundled
  setup/evidence assets; force-fit dual ideals and domain fixture rules removed.
- Doc Web's improve-eval guidance informed evidence freshness and bounded
  experiments; product deployment/crop/model specifics removed.
- Product triage/align/health patterns informed neutral packet semantics and
  local product prioritization, separate from Conductor portfolio judgment.
- The small Echo Forge compiler/facts pattern informed product tooling;
  hardcoded identity/Ideal-ID grammar and silent malformed-input fallbacks
  were not retained. JSON syntax in state YAML is a locally used subset,
  explicitly documented; established richer compilers remain project-local.

## What is supplied

- Product profile: shared helpers plus explicit product triage/story/scout/ADR
  variants, project AGENTS/checklist/runbook/methodology starter resources,
  dependency-free product graph/index compiler and sparse JSON fact collector.
- Evidence module: create/improve eval and create/verify/reset golden guidance,
  registry/attempt/format starter assets with **unmeasured root proof deferred**
  and a reason/trigger. No fake golden, schema, validator or passing eval.
- Conditional modules: architecture, codebase improvement, UI, strategic review,
  security. Installing a skill does not activate its lane without a real need.
- Runtime/dependency adaptation reference: requires actual target allocation,
  commands and applicability proof; does not supply a fake generic server.
- Existing Conductor supervisor workflows remain local. New source guidance
  does not make product runtime, fixtures or decisions centrally owned.

## Copy helper behavior and tests

`package.py audit` checks inventory source availability. `plan` is read-only;
`install` copies selected product resources after intake exists. The helper
never writes Ideal/Spec/state, overwrites a different existing file, installs
through target symlinks, runs providers, or claims that copying completes setup.
Its receipt records modules and source hashes; it is provenance, not acceptance.

Seven focused package tests cover a nonmutating plan, intact authored truths,
correct role variants, repeat install, conflict/missing-intake refusal before
writes, target symlinks, module selection, installed-source audit/story helpers,
and preservation of real or external compatibility surfaces.

Eleven product-tooling tests cover sparse no-story compilation, installed-path
root discovery, current graph/index check, malformed input, duplicate/unknown
refs, category alignment, phases, deferral triggers, and canonical/link/alias
presence versus drift. These are scaffold guarantees, not product correctness.

## Independent review

A fresh read-only reviewer found two material defects:

1. The product story template required absent `make lint`/`make test` targets.
   Fixed by making product lint/test gates conditional on real project commands,
   keeping mandatory package consistency checks.
2. The inherited skill-sync helper followed a symlinked `.claude`/`.cursor`
   parent outside the target. Fixed with parent preflight before any mutation;
   existing real directories and external links are preserved. Focused tests
   exercise both hazards.

The reviewer confirmed both fixes and found no new defect in their changed
scope. This is bounded independent review, not exhaustive security acceptance.

## Forward exercise and execution failure

The first independent worker used relative target writes from Conductor's cwd,
briefly overwriting its source Ideal and Spec. It then restored Git HEAD,
erasing the previously uncommitted approved versions of those two files. The
worker admitted the exact commands. The coordinator interrupted it and restored
the earlier approved 350-word Ideal and Spec changes from this conversation,
including the existing managed-project preflight text. Other local source work
was retained. This attempt is a **failed exercise**, not clean setup evidence.

Kickoff now explicitly requires absolute destinations or a verified target
working directory for every mutation. Reading a source skill by path never
changes cwd. Wrong-checkout writes require stopping/reporting; Git HEAD must not
be used to overwrite potentially uncommitted work. The product template and
link fixes above were already identified independently, not excuses for the
worker's path mistake.

A fresh second exercise uses a separate temp target with a realistic camping
checklist seed, no product implementation/provider/runtime, a planning-only
approval, and source Ideal/Spec/AGENTS hash guards. Its outcome is recorded
below after direct artifact inspection; the first attempt remains visible.

## Final exercise result

The independent second worker authored a 161-word outcome-only Ideal, kept all
seed needs, and placed React/Postgres/GPT/vector database suggestions in the
Spec as unselected mechanisms. It completed the planning package and one Draft
first-proof story, recorded concrete deferral triggers, and passed scaffold
checks without source writes. It also identified a real source mismatch:
setup promised `/loop-verify` in the sparse core, while the manifest only
selected it through optional strategic review.

The manifest now includes `/loop-verify` in core as an available tool, never a
mandatory invocation. Optional strategic review adds `/loop-review`. The old
exercise retains its previous-source limitation. A **fresh final-source
install** reuses only the independently authored/reviewed intake, state, Draft
story and explicitly reviewed local adaptations; it does not reuse the old
source kit. Final compile/check, package audit, skill links (23 skills), and
direct JSON facts all pass. One Draft story and zero measured evals remain.
Core loop-verify is present, optional loop-review and supervisor registry absent.
Seed/Ideal/Spec remain unchanged, and the source Ideal/Spec/AGENTS hash guards
match. [Exercise record](evidence/align-058-package-exercise.json) retains exact
temp paths, commands/results, adaptations, limitations, and the failed attempt.

## Validation

- `make test`: 25 tests passed (7 existing credential tests, 11 new product
  methodology tests, 7 new package tests). Later manifest/template/test changes
  received the affected 7 package tests again; unchanged tooling results reused.
- Source `package.py audit`: all 87 resources available, selected modules
  dependency-complete. Markdown links in new package resources resolve.
- `make methodology-check`, `make skills-check`, `make lint` and
  `git diff --check` pass for the local package work. Final docs/evidence changes
  receive reference/JSON and methodology checks rather than product suites.
- Independent review: two findings fixed and specifically confirmed. Independent
  setup exercise: one manifest mismatch fixed and fresh-source install confirmed.
- No provider calls, product implementation, target primary-checkout changes,
  commits, pushes, registry enrollment, or scheduled work.

## Evidence boundaries and next route

A successful sparse exercise proves new-project planning/package setup for that
scenario. It cannot prove all project shapes, real UI/runtime integration,
paid-provider evals, hardware, consumer adoption, or that every useful local
skill has already been promoted. Those remain project-specific, scoped work.
No primary checkout outside Conductor is modified by this package completion.
Existing five-project Ideal proposals remain paused. Landing of the scoped
Conductor work is a separate explicit step; unrelated dirty work is not included.

## Scoped close-out — 2026-10-20

Cam explicitly approved committing and pushing this Conductor work only.
Integrated into managed worktree `conductor-setup-package-landing/conductor`
on branch `codex/conductor-reusable-setup` from current `origin/main` c695adb.
The shared primary checkout and its unrelated dirty/staged work are retained.
Overlapping AGENTS/setup/runbook edits preserve newer upstream staffing and
decision-model guidance instead of copying stale primary files wholesale.

The integrated candidate passes all 25 repo tests, source inventory audit,
methodology/skill/lint/whitespace checks, and a new disposable product setup.
Its current library has 88 resources after upstream integration, compared with
87 in the historical October 18 exercise. The fresh target installs 23 product
skills, preserves authored Ideal/Spec, compiles and checks state/graph, emits
valid facts, leaves measured evals empty/deferred, and omits the supervisor
registry. A bounded independent integration review found no material issues.
See [integration evidence](evidence/align-058-integration-check.json) for exact
source identities, commands, results and applicability limits.

The validated candidate is ready for the authorized branch/main push; final
remote identities are verified and reported in the close-out handoff. This
close-out does not resume target-project Ideal rewrites or authorize a rollout.
