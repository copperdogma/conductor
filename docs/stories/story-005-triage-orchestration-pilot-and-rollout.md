---
title: "Triage Orchestration Pilot and Rollout"
status: "Done"
priority: "High"
ideal_refs:
  - "I1"
  - "I2"
  - "I3"
  - "I4"
  - "I5"
spec_refs:
  - "spec:1.1"
  - "spec:2.2"
  - "spec:4.2"
  - "spec:5.1"
decision_refs:
  - "ADR-001"
  - "ADR-002"
depends_on: []
category_refs:
  - "alignment"
  - "story-prep"
  - "memory"
tracked_projects:
  - "storybook"
  - "dossier"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 005 — Triage Orchestration Pilot and Rollout

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-001, ADR-002
**Depends On**: None

## Goal

Upgrade the shared triage pattern so unscoped `/triage` becomes a sharper,
more reliable decision system:

- it ranks work against each repo's own `docs/ideal.md` and `docs/spec.md`
- it avoids tiny story fragments by recommending the largest coherent
  validated move that is worth story overhead
- it uses neutral, contracted subagent fan-out for judgment-heavy evidence
  gathering
- it runs cheap mechanistic facts directly in the main thread while subagents
  work
- it surfaces the top three cross-domain recommendations before naming the
  final yes-ready recommendation, so Cam can intentionally choose a runner-up
  when local priorities differ
- it accounts for health/freshness lanes that can honestly outrank new feature
  work when architecture, UI truth, eval truth, provider/dependency health, or
  codebase churn would make continued feature work risky
- it proves the new pattern in Storybook first, then rolls the refined pattern
  across the rest of the tracked projects

## Acceptance Criteria

- [x] A durable Conductor alignment entry records the triage-orchestration
  design, the Storybook pilot scope, and the criteria for wider rollout.
- [x] Storybook receives the first implementation in an isolated task worktree:
  updated `/triage` instructions, a scripted triage fact collector, and a
  health/freshness leaf skill or equivalent focused leaf surface.
- [x] Before rewriting or replacing any existing Storybook leaf skill, the
  current leaf-skill advice is inventoried and preserved, intentionally moved,
  or explicitly rejected with a reason.
- [x] The Storybook pilot is live-checked by running the new triage flow against
  Storybook's current repo state and comparing the recommendation against
  `docs/ideal.md`, `docs/spec.md`, state/graph, UI-scout, architecture, eval,
  inbox, story, and codebase-health evidence.
- [x] The pilot goes through `/loop-verify` with repeated full rounds until one
  full round returns no material issues, or the loop is blocked or clearly
  non-convergent. Material fixes reset the full verification pass; minor/local
  typo, whitespace, or non-contract wording fixes may be accepted with a
  targeted check instead of restarting the full loop.
- [x] This story contains and maintains a verify-loop-ready instruction artifact
  that future agents can follow when rolling the new triage pattern to other
  repos.
- [x] After the Storybook pilot is accepted, Dossier, doc-web, CineForge, Board
  Game Ingester, Robo Rally, and Echo Forge receive locally adapted versions in
  isolated worktrees, with repo-native validation.
- [x] Each target repo gets its own leaf-skill preservation map before edits,
  so battle-tested local advice is preserved, moved, intentionally replaced, or
  explicitly rejected with evidence.
- [x] The rollout preserves local differences: absent/deferred lanes stay
  explicit instead of being forced into every repo.
- [x] Final validation proves skill wrappers, methodology compile/check, script
  tests or smoke checks, and `git diff --check` pass in every touched repo.

## Out of Scope

- Making Conductor the canonical copy of every triage skill.
- Forcing every repo to have every health lane when the lane is absent,
  deferred, or not applicable by design.
- Running heavy provider-backed evals, UI scouts, or architecture audits during
  ordinary triage unless the new triage result recommends that as the next
  action.
- Casually replacing existing leaf skills such as `/triage-stories`,
  `/triage-evals`, `/triage-architecture`, `/ui-scout`, or
  `/codebase-improvement-scout` without first preserving their battle-tested
  instructions. Full rewrites are allowed only when the old advice has been
  inventoried and deliberately carried forward, moved, or rejected.
- Editing tracked project primary checkouts unless Cam explicitly requests
  in-place work.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, alignment, and decision
  context.
- [x] Create the Conductor alignment entry for the triage-orchestration design.
- [x] Inventory current triage leaf skills across tracked repos and record the
  preservation/upgrading plan by skill type.
- [x] Build the Storybook pilot in an isolated worktree:
  - [x] create a task branch from `origin/main`
  - [x] inventory Storybook's current triage leaf skills and classify which
    advice must be preserved, moved, rewritten, or dropped
  - [x] update Storybook `/triage` to use contracted neutral fan-out
  - [x] add a main-thread triage fact collector script
  - [x] add or update a health/freshness leaf surface
  - [x] regenerate wrappers and methodology outputs
- [x] Live-check the Storybook pilot by running the upgraded triage flow and
  recording whether the recommendation is actually better.
- [x] Run `/loop-verify` on the Storybook pilot until it converges under the
  materiality gate.
- [x] Revise the verify-loop-ready instructions in this story from pilot
  findings.
- [x] Roll out the refined pattern to the remaining tracked repos in isolated
  worktrees, adapting to local surfaces.
  - [x] inventory each repo's current triage and leaf-skill advice before
    editing that repo
  - [x] record the preservation map in that repo's work log or the Conductor
    alignment entry
- [x] Run `/loop-verify` across the multi-repo rollout until it converges.
- [x] Update related scout or alignment memory if applicable.
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] If agent tooling changed: `make skills-check`
  - [x] If scripts or repo checks changed: `make test`
- [x] Run each target repo's repo-native checks.
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

- `docs/stories/story-005-triage-orchestration-pilot-and-rollout.md` — story
  plan, work log, and verify-loop-ready rollout instructions.
- `docs/alignments/align-017-triage-orchestration-pilot.md` — durable
  alignment record for the design and rollout criteria.
- `docs/align-projects.md` — alignment index entry.
- Storybook isolated worktree files, expected:
  - `.agents/skills/triage/SKILL.md`
  - `.agents/skills/triage-health/SKILL.md` or locally better equivalent
  - `.gemini/commands/*.toml`
  - `scripts/triage-facts.*` or locally better equivalent
  - methodology/runbook/test surfaces needed to keep the pattern honest
- Later target repo isolated worktree files for Dossier, doc-web, CineForge,
  Board Game Ingester, Robo Rally, and Echo Forge, adapted to each repo's
  existing skill/script layout.

## Notes

User intent:

- Use scoped, contracted fan-out for subagent subtasks.
- The main thread keeps the north star: triage advice must be aligned with the
  repo's own `docs/ideal.md` and `docs/spec.md`.
- Subagents should neutrally report the top candidates in their domains rather
  than being over-focused on a gap chosen too early.
- The main thread should surface the top three cross-domain recommendations,
  then clearly state its final recommended action at the end. The final line
  should still be yes-ready, but the runner-ups should be visible so Cam can
  steer to recommendation 2 or 3 when human context changes the call.
- Triage should not optimize for tiny tasks. It should recommend story-scale or
  artifact-scale moves that are worth the overhead and meaningfully move the
  app/repo toward the Ideal.
- Health lanes may outrank larger feature gaps when stale architecture, janky
  UI, broken eval truth, provider fragility, methodology drift, or codebase
  churn would make continued feature work likely to compound debt.
- Cheap objective checks should become scripts where practical. The main thread
  should run those while subagents do judgment-heavy analysis.
- Pilot in Storybook first, live-check the result, revise these instructions,
  then roll out to the rest.

Current triage target inventory from the 2026-04-25 planning discussion:

| Target | Current portfolio shape |
| --- | --- |
| Ideal/spec north star | Present everywhere; must anchor final ranking. |
| Methodology state/graph | Present everywhere; richness varies. |
| Stories | Present everywhere via `/triage-stories`. |
| Inbox | Present in product repos via `/triage-inbox`; Conductor owns inbox directly. |
| Evals / eval ladder | Present in product repos via `/triage-evals`; not Conductor. |
| Architecture audits | Present in Storybook, CineForge, doc-web, Board Game Ingester, Robo Rally, and Echo Forge; not currently a Dossier or Conductor triage lane. |
| UI scout / product truth | Strong in Storybook, present in CineForge docs/state, present in Echo Forge, absent/deferred in several repos. |
| Codebase-improvement freshness | Skill exists in product repos; Dossier has the clearest triage wiring. |
| Input coverage / coverage matrix | Strong in Storybook, Echo Forge, doc-web, and Board Game Ingester; not universal. |
| Model/provider/golden triggers | Mostly handled through eval-ladder, `discover-models`, and `golden-*` surfaces; needs clearer triage fact capture. |
| External scout/adoption | Present via `/scout`; Conductor has the strongest supervisor role. |
| Cross-repo alignment | Conductor-only via `/align-projects`. |
| Methodology/tooling integrity | Present indirectly through compile/check/wrapper scripts and some architecture domains; should be explicit in triage facts. |

ADR-001 applies: the rollout should sync intent and meaning, not force exact
text. ADR-002 applies: triage health/freshness checks are investigative lanes
and should only become recurring defaults when they solve real repeated
problems.

Target repo edits must follow the `align-projects` isolation rule: read primary
checkouts as needed, but perform edits in dedicated worktrees under
`/Users/cam/.codex/worktrees/<task>/<project-key>` on `codex/` branches from
`origin/main` unless Cam explicitly asks to work in place.

## Plan

1. Record the design in Conductor alignment memory before implementation.
2. Investigate Storybook's current triage and leaf-skill advice before any
   rewrite so battle-tested guidance is not lost.
3. Implement the Storybook pilot first.
4. Live-check the Storybook pilot from a real current Storybook triage run.
5. Run `/loop-verify` over the Storybook pilot and revise this story's rollout
   instructions from any issues found.
6. Roll the refined pattern out to the other tracked repos using isolated
   worktrees and local adaptation, starting each repo with its own leaf-skill
   preservation map.
7. Run `/loop-verify` across the multi-repo rollout.
8. Run repo-native checks and close out only after the story, alignment, and
   target repos agree.

## Verify-Loop Ready Instructions Artifact

Use these instructions when building and verifying the triage upgrade.

### Desired triage behavior

Unscoped `/triage` should produce one recommendation by combining:

- objective facts gathered by scripts
- neutral domain reports from subagents
- the main thread's final Ideal/spec synthesis

The recommendation should be the largest coherent move that is bounded enough
to validate and worth story or artifact overhead. It should not be the smallest
possible task.

### Main-thread duties

Before launching subagents:

1. Read `docs/ideal.md`, `docs/spec.md`, `docs/methodology/state.yaml`, and
   `docs/methodology/graph.json`.
2. Build a broad candidate frame without choosing the winner yet.
3. Launch neutral subagents for judgment-heavy lanes without preselecting the
   winning gap.
4. Run the repo's parseable triage fact collector directly while the lane
   packets run.
5. Note which lanes are present, absent-by-design, blocked/deferred, or not
   applicable yet.

While subagents run, the main thread may run cheap read-only checks:

- `git status --short --branch`
- recent `git log --oneline -20`
- methodology graph/state summaries
- wrapper drift checks when cheap
- latest codebase-improvement state/report lookup
- architecture-audit freshness extraction
- UI-scout freshness extraction
- eval registry and latest-attempt summaries

After subagents return:

1. Rank candidates against the repo's Ideal/spec.
2. Let health/freshness work outrank feature work when building more feature
   weight would compound architectural, UI, eval, provider, or tooling risk.
3. Reject story fragments and consolidate adjacent candidates that share a
   user-facing outcome, validation boundary, subsystem, or Ideal promise.
4. Surface the top three cross-domain recommendations with why each is or is
   not the final pick.
5. Return one final yes-ready recommendation with a validation/stop condition.
   The final handoff should use the exact form `Reply yes to proceed with:
   ...` so Cam can approve the next action unambiguously.

### Leaf-skill preservation pass

Before changing any existing triage leaf skill, inventory its current guidance
and classify each meaningful instruction:

- preserve in the same leaf skill
- move into `/triage`
- move into the fact collector
- move into a new health/freshness leaf skill
- replace with a stronger version
- drop because it is stale, duplicated, or contradicted by newer evidence

This pass must cover at least:

- `/triage-stories`
- `/triage-inbox`
- `/triage-evals`
- `/triage-architecture`
- `/ui-scout` where present
- `/codebase-improvement-scout`
- any repo-specific triage leaf such as Storybook's `/triage-dossier-upstream`

The pilot should not claim a leaf skill is upgraded until its preservation map
is recorded in the Storybook work log or the Conductor alignment entry.

### Scripted fact collector

Add a repo-local script such as `scripts/triage-facts` that is cheap,
read-only, and deterministic. Prefer JSON output with a concise text mode. The
machine-readable proof command should call the underlying script directly, for
example `node --experimental-strip-types scripts/triage-facts.ts --json`, so
package-manager banners cannot pollute JSON stdout. Package scripts may remain
as convenience aliases, but rollout validation should not depend on bannered
`pnpm ... --json` output unless the repo proves it is machine-clean.

The script should report, where applicable:

- current branch and dirty status
- latest generated graph recommendations/actionability
- story counts and active/recommended stories
- inbox item count and untriaged markers
- eval registry health, retry triggers, latest attempts, and golden/scorer
  freshness
- architecture audit domains, cadence, last audit, stories since audit, open
  findings, and stale domains
- UI-scout status, canonical scenarios, last run, due/recheck/issues state
  using actual graph/story records after the last UI-scout story marker, not
  naive numeric ID subtraction that assumes contiguous story IDs
- codebase-improvement state/report freshness and recent churn by path/domain
- methodology/tooling health: wrapper drift, compile/check freshness, generated
  artifact drift if cheap to detect
- provider/model/dependency health if the repo has an existing surface for it
- lanes that are absent, deferred, or not applicable yet

The script should not run heavy evals, browser scouts, provider calls, or long
test suites. It should only summarize facts that help triage decide what to do.

### Subagent lane contract

Each triage subagent owns one lane and returns up to three candidates.

Required fields per candidate:

- candidate name
- Ideal promise and spec refs it advances
- evidence and source files
- why now
- suggested action shape: continue story, create story, eval, scout,
  architecture audit, UI scout, codebase-improvement, ADR, alignment, or no-op
- whether it is story-worthy or too small
- validation or stop condition
- blockers, stale evidence, and reasons not to do it

The main thread should merge lane candidates into a top-three cross-domain
shortlist, not just a single winner. Each shortlist item should include:

- recommendation
- Ideal/spec value
- why now
- validation/stop condition
- why it ranked above or below the others

Suggested lanes:

- product/Ideal gap
- stories and inbox
- evals/goldens/model evidence
- architecture freshness
- UI/product-truth freshness
- codebase/churn freshness
- methodology/tooling/dependency health
- Conductor-only: scout/alignment memory

Subagents are read-only during unscoped triage. Health/freshness lanes should
also stay read-only in direct scan mode: they may recommend follow-up commands
or skills, but should not run deeper audits, UI scouts, dependency upgrades, or
provider/model checks as part of ordinary triage.

### Pilot verification loop

For the Storybook pilot, run `/loop-verify` after the first implementation.

Scope:

- Storybook triage skill
- new fact collector script and tests/smoke checks
- new or updated health/freshness skill
- generated command wrappers
- methodology/runbook surfaces touched by the pilot

Shard suggestions:

- triage prompt semantics and output shape
- leaf-skill preservation map and lossiness check
- fact collector correctness and cheapness
- health/freshness lane coverage
- Storybook-local adaptation and current `docs/ideal.md` alignment
- generated wrappers, methodology graph/state, and validation commands

If any shard returns `RESULT: fixed` or the main thread makes a fix from a
finding, classify it before deciding whether to reset:

- Material fixes reset the full original scope with fresh workers. Material
  means semantic prompt changes, executable/script changes, contract/output
  shape changes, generated-surface changes that may affect another shard, or
  anything with non-obvious secondary effects.
- Minor fixes do not automatically reset the loop if their effect is confined
  to that shard and a targeted check passes. Minor means typo, whitespace,
  formatting, or wording cleanup that does not change the triage contract.

Stop when a complete round returns no material issues. Do not use a hard round
cap: if a round finds solid material issues, run another fresh full round even
if that means many rounds. Stop instead when a round contains only minor/local
fixes that pass targeted checks, when an unresolved blocker remains, or when
the loop is clearly non-convergent because workers are oscillating or widening
scope.

If a worker stalls but the other shards return clean and make no changes, close
and replace only the stalled shard. Do not call the round clean until that
replacement shard also returns `RESULT: no-issue`; do not reset the full loop
unless the replacement makes a material fix.

### Pilot findings to carry forward

The Storybook pilot surfaced specific issues that future repo rollouts should
guard against:

- Do not let the shared frame or actionability gate name a "primary gap" before
  lane packets have had a chance to return neutral candidates.
- Keep lane-packet mode distinct from standalone/direct-scan mode. Standalone
  yes/no kickoff language must not override a full-sweep `/triage` lane packet.
- The exact final handoff matters: use `Reply yes to proceed with: ...`.
- Health/freshness scans are read-only candidate packets. They recommend
  architecture, UI, codebase, methodology, dependency, or provider follow-ups;
  they do not execute deeper lane work during triage.
- JSON fact proof should use the direct script command, not bannered package
  manager output.
- UI-scout freshness must count actual completed graph/story records after the
  last scout marker, not subtract numeric story IDs.
- Preservation maps should include generated wrappers, the fact collector,
  methodology graph integration scripts, and final regression gates.

### Multi-repo rollout findings to carry forward

The adapted rollout across Dossier, doc-web, CineForge, Board Game Ingester,
Robo Rally, and Echo Forge added a second set of non-obvious checks:

- Run a local propagation sweep before each fresh loop round when the previous
  round changed a shared fact semantic. Check the main triage skill, leaf
  skills, health/preservation runbooks, fact script, tests, and wrappers for
  the same semantic before asking workers to rediscover it.
- Preserve direct fact commands and package-script behavior separately. Direct
  commands are the parse-safe proof surface; package scripts are convenience
  aliases and may emit banners unless explicitly run in silent mode.
- Optional or not-yet-run lanes are facts, not failures. Absent
  codebase-improvement reports, missing UI scout runs, or deferred lanes should
  become freshness/attention evidence only when they affect the current
  Ideal/spec ranking.
- Facts need repo-native status language. `absent`, `attention`, `ok`,
  `deferred`, `partial`, and `drift` are not interchangeable, and confusing
  them creates false triage pressure.
- UI-scout facts must distinguish empty report paths from broken report
  pointers. A scenario can need attention because it has never produced a
  current report while `missing reports 0` remains true.
- Wrapper facts need both sides of the contract. Missing wrapper infrastructure
  should be `absent`, not drift; wrapper status `ok` with drift `0` should not
  become a health recommendation.
- Eval facts must keep registry identity, fixture attempts, and written attempt
  reports separate. A registry `path` is not the same thing as an
  `attempt_path`, and `missing registry reports 0` only proves that registered
  attempt report pointers resolve.
- Architecture facts should preserve concrete domain ids. If facts say
  `platform` and `audio-generation`, triage should not hide that behind generic
  architecture wording.
- Greenfield or recently imported repos are more prone to long loops because
  they have sparse runtime history and many copied methodology surfaces. Do a
  pre-integration semantic sweep there before each reset, and expect product
  ideals, ADRs, browser-proof rules, and eval/UI-scout semantics to need
  explicit local language.

### Multi-repo rollout verification loop

After Storybook is accepted and the instructions are revised, roll out in
isolated worktrees. Run `/loop-verify` across the rollout with one shard per
repo plus one cross-repo consistency shard.

Every repo worker must check:

- local triage wording preserves the repo's own Ideal/spec north star
- the repo's existing triage and leaf-skill advice has a preservation map
  before rewrite
- absent/deferred lanes remain explicit and are not forced
- scripts are cheap, read-only, and deterministic
- machine-readable fact proof uses a direct script command with clean JSON
  stdout
- UI-scout/story-interval facts, where present, use actual graph/story records
  rather than assuming contiguous IDs
- health/freshness lanes remain read-only in scan mode and only recommend
  deeper follow-up commands
- lane-packet mode cannot be overridden by standalone yes/no handoff language
- final triage output includes the exact `Reply yes to proceed with: ...`
  handoff
- facts and prompt/runbook wording agree on status semantics such as absent,
  attention, ok/drift, and broken/missing pointers
- wrappers are regenerated and checked
- repo-native methodology checks pass
- no primary checkout was modified

Cross-repo worker must check:

- shared intent is consistent
- local adaptations are justified
- no repo lost an existing triage lane
- no repo copied Storybook-only lanes or proof assumptions where they do not
  apply
- the output shape is succinct enough for actual use

### Required checks

Run at least:

- Conductor: `make methodology-compile`, `make methodology-check`,
  `make lint`, `make test` if scripts changed, `make skills-check` if agent
  tooling changed, and `git diff --check`
- Target repos: repo-native methodology compile/check, skill wrapper check,
  direct fact-collector JSON parse, fact-collector smoke/test, and
  `git diff --check`

## Work Log

20260425-0904 — story-created: created Story 005 from the triage
orchestration planning discussion. The agreed direction is Storybook pilot
first, live-check and loop-verify, then revise the rollout instructions before
upgrading the rest of the tracked repos. Next step: compile methodology
surfaces and begin the Conductor alignment entry.

20260425-0922 — inventory-plan: compared current triage-adjacent leaf skills
across Conductor, Dossier, Storybook, doc-web, CineForge, Board Game Ingester,
Robo Rally, and Echo Forge. Added Alignment 017 with the preservation map by
skill type, repo-family rollout plan, target checkout isolation notes, and the
Storybook-first pilot recommendation. Target repos stayed read-only.

20260425-0929 — validation: ran Conductor `make methodology-compile`,
`make methodology-check`, `make skills-check`, `make lint`, `make test`, and
`git diff --check` for the story/alignment artifact pass.

20260425-1017 — storybook-pilot-implemented: created isolated Storybook
worktree `/Users/cam/.codex/worktrees/triage-orchestration/storybook` on
branch `codex/triage-orchestration-pilot` from `origin/main`. Implemented the
pilot preservation map, upgraded `/triage` to run
`node --experimental-strip-types scripts/triage-facts.ts --json` directly while
neutral lane packets run, merge those packets into a top-three shortlist, and
then make one final recommendation. Added `/triage-health`, added
`scripts/triage-facts.ts` and its smoke test, updated leaf skills with
lane-packet contracts, regenerated Gemini wrappers, and refreshed methodology
surfaces. Target primary checkout stayed untouched.
Validation in the Storybook worktree: `pnpm install --frozen-lockfile --offline`,
`pnpm triage:facts`, `pnpm triage:facts -- --json`,
`pnpm triage:facts:check`, `pnpm methodology:compile`,
`pnpm methodology:check`, `pnpm methodology:test`,
`bash scripts/sync-agent-skills.sh`, `bash scripts/sync-agent-skills.sh
--check`, `pnpm typecheck`, `pnpm lint`, `pnpm test`, and `git diff --check`.
Fact smoke surfaced the expected current health signals: 3 untriaged inbox
items, `infrastructure_and_deploy` never audited, UI-scout due by story
interval, no codebase-improvement report, and zero wrapper drift after sync.

20260425-1115 — storybook-live-check-and-loop-verify: live-checked the
upgraded Storybook triage pattern against current `docs/ideal.md`,
`docs/spec.md`, state/graph, UI-scout, architecture, eval, inbox, story, and
codebase-health evidence. The top three recommendations were: S1 UI-scout
freshness for first-capture/onboarding truth, C3 identity eval safety rerun,
and the question-answer persistence inbox item. The final recommendation was
S1 UI-scout because it had the clearest current freshness trigger and protects
the first-capture Ideal promise without creating a tiny story fragment.

20260425-1115 — loop-verify-materiality-update: ran three full `/loop-verify`
rounds on the Storybook pilot. Round 1 and Round 2 made material fixes to the
main triage prompt, leaf lane-packet contracts, health lane boundaries, fact
collector determinism, and preservation/runbook instructions. Round 3 found
more material fixes, including removing remaining early-winner language,
preventing standalone leaf handoffs from overriding lane-packet mode, and
making the fact collector preserve git status columns and fixed-date churn.
The user clarified that `/loop-verify` should not have a hard round cap:
material semantic/executable/contract/generated fixes reset the loop no matter
the round number, while minor typo/formatting/non-contract wording fixes only
need targeted checks. Conductor `/loop-verify` and this story were updated to
use that rule, and the Storybook pilot should continue with a fresh Round 4
because Round 3 found solid material issues.

20260426-0021 — storybook-loop-verify-converged: continued Storybook
`/loop-verify` under the corrected no-hard-cap rule. Rounds 4-7 each found at
least one material issue and therefore reset the full pass: remaining
early-winner/actionability wording, missing exact `Reply yes to proceed with:
...` handoff examples, health scan read-only boundaries, lane-packet/direct-scan
separation, UI-scout `stories_since_run` counting, and stale bannered `pnpm`
JSON proof commands. Round 8 returned no material or minor issues across the
main triage/runbook, leaf/health skills, fact collector/script integration, and
health/preservation runbook shards. Final Storybook validation passed:
`pnpm triage:facts`, direct
`node --experimental-strip-types scripts/triage-facts.ts --json` parse,
`pnpm triage:facts:check`, `pnpm methodology:compile`,
`pnpm methodology:check`, `pnpm methodology:test`,
`bash scripts/sync-agent-skills.sh --check`, `pnpm typecheck`, `pnpm lint`,
`pnpm test`, and `git diff --check`.

20260426-0023 — rollout-instructions-upgraded-from-loop-findings: revised the
verify-loop-ready instructions after reviewing the Storybook loop findings.
The story now explicitly carries forward the non-obvious lessons: launch
neutral lane packets before choosing a winner, keep lane-packet and standalone
scan modes separate, require the exact `Reply yes to proceed with: ...`
handoff, keep health scans read-only, validate JSON facts through the direct
script command, compute UI-scout story intervals from actual graph/story
records, include methodology graph integration in preservation maps, and
replace stalled verification shards without calling the round clean.

20260428-0748 — remaining-rollout-converged: upgraded the remaining tracked
repos one by one in isolated worktrees on branch
`codex/triage-orchestration-rollout`, leaving primary checkouts untouched.
Targets and loop results:

| Repo | Worktree | Base | Loop result |
| --- | --- | --- | --- |
| Dossier | `/Users/cam/.codex/worktrees/triage-orchestration-rollout/dossier` | `eabc640` | 2 rounds; Round 2 clean. |
| doc-web | `/Users/cam/.codex/worktrees/triage-orchestration-rollout/doc-web` | `aca1922` | 10 rounds; Round 10 clean. |
| CineForge | `/Users/cam/.codex/worktrees/triage-orchestration-rollout/cine-forge` | `5dda308` | 4 rounds; Round 4 clean. |
| Board Game Ingester | `/Users/cam/.codex/worktrees/triage-orchestration-rollout/boardgame-ingester` | `ca368fd` | 10 rounds; Round 10 clean. |
| Robo Rally | `/Users/cam/.codex/worktrees/triage-orchestration-rollout/roborally` | `c46edf4` | 2 rounds; Round 2 clean. |
| Echo Forge | `/Users/cam/.codex/worktrees/triage-orchestration-rollout/echo-forge` | `d6547dc` | 34 rounds; Round 34 clean. |

All six received locally adapted orchestration triage, lane-packet leaf
contracts, loop-verify materiality guidance, preservation/runbook coverage,
direct fact collectors, fact tests/smokes, and wrapper updates where local
tooling supports them. Local differences stayed explicit: Dossier kept no
forced architecture lane, UI scout remained absent/deferred where not
applicable, Board Game Ingester kept rulebook/golden-asset truth rather than
UI assumptions, Robo Rally preserved private proof-of-concept/headless-first
framing, CineForge preserved provider/runtime and UI-scout state boundaries,
and Echo Forge preserved its browser-first, fun/easy/engaging product goal,
ADRs, eval fixture/report semantics, and UI-scout scenario truth.

20260428-0750 — target-repo-validation: ran repo-native validation in every
target worktree. Dossier passed skill wrapper checks, direct triage facts,
JSON parse, `triage-facts-check`, methodology compile/check, diff whitespace,
and scoped Ruff for new files; the broader `make lint` still reports unrelated
pre-existing failures outside this rollout. doc-web passed skill wrapper
checks, direct facts text/JSON, pytest, Ruff, graph check,
`make triage-facts-check`, `make methodology-check`, `make lint`, and
`git diff --check`. CineForge passed skill wrapper checks, facts JSON,
targeted pytest, scoped Ruff, `npm run methodology:check`, and
`git diff --check`; it still reports the repo's existing architecture-audit
due warning. Board Game Ingester passed skill wrapper checks, facts text/JSON,
`make triage-facts-check`, `make methodology-check`, `make test`, `make lint`,
and `git diff --check`. Robo Rally passed `npm run skills:check`, direct
facts text/JSON, `npm run triage-facts:check`,
`npm run methodology:check`, `npm test`, `npm run validate`, and
`git diff --check`. Echo Forge passed `npm run skills:check`, direct facts
text/JSON, `npm run triage-facts:check`, `npm run methodology:check`,
targeted `npm test`, `npm run typecheck`, `npm run lint`, and
`git diff --check`; the temporary untracked `node_modules` symlink used only
for validation was removed.

20260428-0754 — echo-forge-loop-lesson: Echo Forge required many more rounds
because it is greenfield and methodology-heavy: sparse runtime history,
selectively imported Storybook-shaped surfaces, no long-lived codebase-health
history, and several subtle fact semantics had to propagate across triage,
leaves, health runbooks, tests, and generated wrappers. The material issues
were real, not just nit churn: preserving direct Node facts, parse-safe JSON,
top-three/final yes-ready output, leaf packet boundaries, product feel,
ADR/browser-proof constraints, Scout 003 baseline, architecture domain ids,
eval registry-vs-attempt semantics, UI-scout empty-report semantics, and
wrapper `ok`/`absent`/`drift` semantics. The rollout instructions now include
a pre-integration propagation sweep for this kind of repo so later loops do
not spend many rounds rediscovering the same semantic in adjacent surfaces.

20260428-0759 — conductor-tracking-validation: updated the story and
Alignment 017 with the final rollout evidence, then ran Conductor validation:
`make methodology-compile`, `make methodology-check`, `make skills-check`,
`make lint`, `make test`, and `git diff --check`.

20260428-0812 — setup-methodology-greenfield-guardrail: upgraded the portable
product-repo `/setup-methodology` skill once in the Storybook rollout
worktree, then copied the exact file into Dossier, doc-web, CineForge, Board
Game Ingester, Robo Rally, and Echo Forge. The shared skill now installs the
upgraded triage, triage-health, sparse facts, and loop-verify package during
setup; routes blank repos back to `/init-project` for real Ideal/spec intake;
marks code-dependent lanes absent/deferred instead of broken; and runs cheap
checks rather than long subagent loops when no code exists yet. Hashes matched
across all seven product worktrees after the copy. Wrapper sync/check and
methodology checks passed in all seven; CineForge required a graph recompile
after wrapper sync and still reports its existing architecture/UI freshness
warnings. Conductor's own supervisor setup skill/runbook now records the rule:
keep product setup identical by upgrading one source and copying it, while
leaving Conductor's supervisor setup surface distinct.

20260428-0852 — story-closed-and-targets-landed: landed the linked target
worktrees on their `main` branches after fresh validation:
Storybook `6f708af`, Dossier `72103b3`, doc-web `983db09`, CineForge
`95905cc`, Board Game Ingester `0b20906`, Robo Rally `d9294aa`, and
Echo Forge `b8a0fc2`. Story 005 is complete: the Storybook pilot, adapted
rollout, setup-methodology greenfield guardrail, verification loops, repo-native
checks, and Conductor tracking artifacts are all done.
