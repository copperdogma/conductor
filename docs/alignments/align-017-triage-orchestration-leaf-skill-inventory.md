# Alignment 017 — Triage Orchestration Leaf-Skill Inventory

**Date:** 2026-04-25
**Focus:** Inventory the triage leaf skills across tracked repos, preserve the
useful local guidance, and define the upgrade plan for the Storybook pilot plus
the later adapted rollout.

## Surfaces Compared

- Conductor `docs/ideal.md`, `docs/spec.md`, `docs/methodology/state.yaml`,
  `docs/methodology/graph.json`, `projects.yaml`, and Story 005.
- Tracked repo `.agents/skills/triage*/SKILL.md` files.
- Tracked repo `.agents/skills/ui-scout/SKILL.md` where present.
- Tracked repo `.agents/skills/codebase-improvement-scout/SKILL.md` where
  present.
- Tracked repo methodology state surfaces for architecture and UI-scout lanes.
- Primary target repo git state, read-only, to decide whether rollout edits
  must be isolated.

## Decision Context

- Conductor [ADR-001](../decisions/adr-001-conductor-as-supervisor-not-canonical-core.md)
  applies: the rollout should sync meaning and behavior, not exact text.
- Conductor [ADR-002](../decisions/adr-002-methodology-lanes-as-investigative-loops.md)
  applies: health lanes should stay focused investigative loops, not recurring
  bureaucracy.
- [Story 005](../stories/story-005-triage-orchestration-pilot-and-rollout.md)
  is the active rollout story.
- The target-repo edit-isolation rule applies: read primary checkouts as
  needed, but perform target repo edits in dedicated worktrees under
  `/Users/cam/.codex/worktrees/<task>/<project-key>` on `codex/` branches from
  `origin/main` unless Cam explicitly asks to work in place.

## Current Checkout Reality

The inventory pass was read-only in target repos. Several primary checkouts are
active or behind, so the implementation phase must not edit them directly:

| Project | Current primary checkout signal | Rollout implication |
| --- | --- | --- |
| Dossier | `main` behind `origin/main` by 1 commit | Create isolated worktree from `origin/main` before edits. |
| Storybook | Active `codex/story-112...` branch with dirty `docs/inbox.md` | Pilot must use an isolated worktree, not the active checkout. |
| doc-web | `main` behind `origin/main` by 3 commits with many local changes | Use isolated worktree; avoid interpreting dirty local changes as rollout baseline. |
| CineForge | Active `codex/story-190...` branch | Use isolated worktree. |
| Board Game Ingester | Clean `main` | Still prefer isolated worktree for supervisor rollout consistency. |
| Robo Rally | Clean `main` | Still prefer isolated worktree for supervisor rollout consistency. |
| Echo Forge | Clean `main` | Still prefer isolated worktree for supervisor rollout consistency. |

## Current Leaf-Skill Inventory

| Project | Current triage-adjacent skills and lanes |
| --- | --- |
| Conductor | `triage`, `triage-stories`, `loop-verify`, `scout`, plus `align-projects` as the supervisor-only alignment lane. |
| Dossier | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `codebase-improvement-scout`, `discover-models`, `golden-verify`, `loop-verify`, `scout`, `align`. No explicit `triage-architecture` or `ui-scout` lane found. |
| Storybook | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `triage-architecture`, `ui-scout`, `codebase-improvement-scout`, `triage-dossier-upstream`, `discover-models`, `golden-verify`, `loop-verify`, `scout`, `align`. This is the richest pilot surface. |
| doc-web | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `triage-architecture`, `codebase-improvement-scout`, `discover-models`, `loop-verify`, `scout`, `align`. No `ui-scout` or `golden-verify` skill found. |
| CineForge | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `triage-architecture`, `codebase-improvement-scout`, `discover-models`, `golden-verify`, `loop-verify`, `scout`, `align`. UI-scout docs/state exist, but no `ui-scout` skill was found. |
| Board Game Ingester | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `triage-architecture`, `codebase-improvement-scout`, `discover-models`, `loop-verify`, `scout`, `align`. No `ui-scout` or `golden-verify` skill found. |
| Robo Rally | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `triage-architecture`, `codebase-improvement-scout`, `golden-verify`, `loop-verify`, `scout`, `align`. `ui_scout` is absent/deferred in state. |
| Echo Forge | `triage`, `triage-stories`, `triage-inbox`, `triage-evals`, `triage-architecture`, `ui-scout`, `codebase-improvement-scout`, `discover-models`, `golden-verify`, `loop-verify`, `scout`, `align`. |

## Upgrade Target

The upgraded `/triage` should become an orchestration skill:

1. Read the repo's `docs/ideal.md` and `docs/spec.md` as the north star.
2. Run cheap deterministic fact collection in the main thread.
3. Send judgment-heavy lanes through scoped contracts when subagents are
   available or explicitly requested; otherwise run the same lane contracts
   sequentially in the main thread and state the fallback.
4. Require each lane to return up to three candidates without preselecting the
   final winner.
5. Merge lane results into the top three cross-domain recommendations.
6. End with one final recommendation phrased as a yes-ready next action.
7. Prefer the largest coherent, bounded move that meaningfully advances the
   Ideal over tiny story fragments.
8. Allow health work to outrank features when stale architecture, UI truth,
   eval truth, provider/dependency health, methodology/tooling drift, or
   codebase churn would make feature work compound risk.

## Preservation and Upgrade Plan by Skill Type

### `/triage`

Preserve:

- Ideal/spec-first ranking.
- Current-state and graph awareness.
- Completion sanity before accepting a no-op or maintenance-only answer.
- Eval-ladder awareness where the repo has AI/eval lanes.
- Anti-fragmentation rules from earlier alignments.
- Repo-local lanes and absent/deferred lane handling.
- Runner-up and health-flag reporting.

Upgrade:

- Make `/triage` explicitly own orchestration, not all deep analysis.
- Add the top-three cross-domain recommendation section before the final pick.
- Require a final yes-ready recommendation with validation or stop condition.
- Add a story-worthiness check: reject candidates too small for story overhead
  unless they are direct fixes inside an already-approved story.
- Require the main thread to run the fact collector while judgment lanes run.
- Make stale health lanes first-class ranking inputs, not afterthoughts.

Do not:

- Replace local triage shapes with a single canonical Conductor prompt.
- Let subagents choose the final cross-domain priority.
- Let a single early "largest gap" guess over-focus every lane.

### `/triage-stories`

Preserve:

- Always read actual story files, not just titles or compiled summaries.
- Read Ideal/spec/state/graph before ranking story shells.
- Name top live gaps before ranking story candidates.
- Treat Draft/Pending status as packaging, not value.
- Treat Blocked status as evidence that needs a blocker and unblock condition.
- Prefer continuity on active or recently unresolved lines when leverage is
  comparable.
- Avoid fragmenting same-line work; prefer continue, expand, reopen, or
  consolidate when the real boundary has not changed.
- Verify critical substrate in code when an architecture-dependent story
  depends on it.
- For AI-capability work, check root, parent, and child eval evidence before
  packaging implementation backlog.
- Present ranked candidates plus one default yes-ready action.

Upgrade:

- Return a lane packet to `/triage`: up to three story candidates, each with
  Ideal/spec value, why-now evidence, story-worthiness, and validation/stop
  condition.
- Add an explicit "too small / merge into existing story" field.
- Make active-story continuity a ranking input, not an automatic winner.

### `/triage-inbox`

Preserve:

- Scan mode is read-only.
- Processing mode creates artifacts or removes inbox items only after the user
  has approved that handling.
- Read the methodology frame before classifying notes.
- Sweep for stale or already-handled items.
- Map inbox items to methodology gaps.
- Prefer folding notes into existing stories over creating backlog fragments.
- Ask what happens if the item is ignored.
- Do not let inbox novelty outrank a larger Ideal/spec/state/graph gap without
  saying why.
- For links and external resources, summarize and recommend the next artifact
  shape before auto-scouting.

Upgrade:

- Return top inbox/routing candidates as a lane packet to `/triage`.
- Add explicit candidate shapes: no-op, append to existing story, new story,
  scout, alignment, ADR, or defer.
- Feed inbox counts, stale markers, and unhandled note signals into the fact
  collector when cheap.

### `/triage-evals`

Preserve:

- Read eval registry, methodology state, graph, and compiled actionability
  before recommending eval work.
- Keep default triage cheap and read-only; do not run heavy promptfoo/provider
  checks just to triage.
- Check model freshness cheaply through `discover-models` where present.
- Respect phase semantics: climb quality/proof, hold efficiency/simpler,
  converge deletion only when the gate is green.
- Classify stale scores, retry triggers, exhausted triggers, missing
  root/parent/child evals, unclassified parent failures, and
  golden/scorer/model/architecture limits.
- Do not recommend the same failed approach without a new model, approach,
  golden, or architecture reason.
- Do not convert a big red gap into action without a why-now trigger.
- Do not force eval work when the real bottleneck is product substrate.
- Preserve repo-local expected-fail semantics.

Upgrade:

- Return up to three eval candidates to `/triage`, each with the ladder node,
  trigger, why now, and stop condition.
- Let the fact collector summarize eval freshness, retry triggers, latest
  attempts, and absent/deferred eval lanes without running heavy evals.
- Keep Storybook and Robo Rally's root/parent/child eval-ladder guidance as
  the strongest source for repos that have similar AI capability surfaces.

### `/triage-architecture`

Preserve:

- Current mature architecture-audit behavior in Storybook, doc-web, CineForge,
  Board Game Ingester, Robo Rally, and Echo Forge.
- Read `architecture_audits` state, cadence, domains, last audit time, stories
  since audit, and open findings.
- Pick the most due domain from open findings, cadence, recent story churn
  without audit, and longest-untouched active areas.
- Inspect recent work and current code reality before recommending an audit.
- Bias toward simplification: delete, merge, or re-home before adding
  abstraction.
- Audit at most one or two domains in a pass.
- Treat no-op audit as a valid result.
- Keep scan mode read-only.

Upgrade:

- Make architecture freshness one health lane feeding `/triage`, not a forced
  default action.
- Add fact-collector extraction for stale domains, open findings, and
  stories-since-audit.
- Let architecture outrank feature work when evidence shows feature work would
  build on stale or disputed foundations.
- Decide during rollout whether Dossier needs a light architecture lane or
  whether codebase-improvement plus eval/story surfaces cover the current need.
  Conductor itself should not gain product-architecture triage unless a real
  supervisor architecture pain appears.

### `/ui-scout`

Preserve:

- Storybook's stronger UI-scout guidance as the source behavior: use the real
  surfaced UI, walk normal paths, capture evidence, inspect console/runtime
  symptoms, record what works as well as what breaks, group recommendations,
  and avoid one story per small nit.
- Echo Forge's lighter UI-scout skill where present.
- CineForge's existing UI-scout docs/state lane even though no skill exists.
- Robo Rally's explicit absent/deferred state.

Upgrade:

- Treat UI/product-truth freshness as a triage health lane only where the repo
  has a real UI surface or explicit UI-scout state.
- Add fact-collector extraction for last scout, scenario coverage, due/recheck
  state, and open UI findings.
- For CineForge, create or update a `ui-scout` skill only if the rollout finds
  repeated UI-scout work that should not remain docs-only.
- Do not force UI scout into document/headless/data repos where it is absent by
  design.

### `/codebase-improvement-scout`

Preserve:

- Default report-only behavior.
- Deterministic discovery: git/status/hygiene baseline, project-native quality
  checks, optional detectors, and targeted code reads.
- Scan artifact and state updates.
- Triage/classify improvements before creating implementation backlog.
- Hotspot scoring from recent churn, size, complexity, and known risk.
- At most one highest-value story unless the user asks for broader packaging.
- Optional auto-fix only on side branches, for narrow safe classes, with hard
  limits and verification.

Upgrade:

- Wire codebase-improvement freshness into `/triage` everywhere the skill
  exists, not only in Dossier.
- Add fact-collector summaries for latest report age, open hotspots, recent
  churn by path/domain, and whether a scan is stale.
- Let codebase health outrank features when churn or static findings indicate
  feature work would increase risk.
- Keep it distinct from architecture: codebase-improvement is tactical code
  quality and hotspots; architecture is domain boundary and design health.

### Repo-Specific Leaf Skills

Preserve:

- Storybook `triage-dossier-upstream`: check the current Dossier boundary,
  compare refs, inspect upstream changes, run narrow proof when needed, judge
  Storybook value, and recommend one move. Restore pinned runtime after proof
  and do not claim Storybook benefit without evidence.
- `discover-models`: cheap model/provider freshness input where present.
- `golden-verify`: artifact/golden proof lane where present.
- `align` and `scout`: repo-local adoption or external-source lanes; Conductor
  owns the cross-repo versions.
- `loop-verify`: verification loop after implementation, not ordinary triage
  discovery.

Upgrade:

- Treat repo-specific skills as optional lane packets when their domain is in
  play.
- Keep them local. Do not generalize Storybook's Dossier-upstream lane into
  repos without the same upstream dependency.
- Let fact collectors report whether these trigger surfaces are present,
  absent, deferred, or stale.

## Fact Collector Plan

Each product repo should get a cheap read-only script, with the exact language
matching local tooling. Prefer JSON output plus a concise text summary.

Minimum useful fields:

- branch, dirty status, and whether the checkout is primary or task worktree
- latest graph recommendation/actionability
- story counts, active stories, and recommended stories
- inbox count, stale markers, and unhandled notes
- eval registry health, retry triggers, latest attempts, and stale scores
- architecture domains, cadence, last audit, stories since audit, open findings
- UI-scout status, last scout, scenario coverage, due/recheck/open issue state
- codebase-improvement report age, hotspots, and recent churn summary
- wrapper/methodology/generated-artifact drift when cheap to detect
- provider/model/dependency health when an existing surface already records it
- explicit absent/deferred/not-applicable lanes

The fact collector must not run heavy evals, browser scouts, provider calls, or
long test suites. It summarizes existing evidence so the main thread can spend
judgment on ranking.

## Pilot Plan

Use Storybook first because it has the richest live surface:

1. Create an isolated worktree from Storybook `origin/main`, for example
   `/Users/cam/.codex/worktrees/triage-orchestration/storybook`, on a
   `codex/triage-orchestration-pilot` branch.
2. Create a Storybook preservation map before editing any skill. The map must
   classify each meaningful instruction as preserved, moved to `/triage`, moved
   to the fact collector, moved to health/freshness, replaced, or dropped with
   reason.
3. Update Storybook `/triage` into the orchestration skill:
   - Ideal/spec first
   - contracted neutral lane fan-out
   - fact collector in main thread
   - top three cross-domain recommendations
   - final yes-ready recommendation
   - story-worthiness and anti-fragmentation checks
4. Add the fact collector script and smoke/test coverage.
5. Add or adapt a health/freshness leaf surface only if existing leaf skills do
   not cleanly cover architecture, UI, eval, codebase, methodology/tooling, and
   provider/dependency freshness.
6. Regenerate wrappers and methodology surfaces.
7. Live-check by running the upgraded Storybook triage against current repo
   state and judging whether the recommendation is better aligned with
   Storybook `docs/ideal.md` and `docs/spec.md`.
8. Run `/loop-verify` on the pilot until one complete round returns clean.
9. Revise Story 005's verify-loop-ready instructions from pilot findings before
   touching other repos.

## Rollout Plan by Repo Family

| Repo family | Upgrade approach |
| --- | --- |
| Storybook | Pilot source. Full orchestration, fact collector, preservation map, and health lane integration. |
| Echo Forge | Adapt the Storybook shape, preserving Echo Forge's selective-import boundary and lighter UI-scout surface. |
| CineForge | Add orchestration and fact collection; decide whether the existing UI-scout docs/state deserve a skill or should remain a state-only lane. Preserve provider/pipeline/sidequest language. |
| Robo Rally | Add orchestration and fact collection while preserving absent/deferred `ui_scout` state and private proof-of-concept framing. Preserve golden/eval artifact lanes. |
| doc-web | Add orchestration and fact collection, but keep it document-pipeline native. Do not force UI-scout or golden-verify where absent. |
| Board Game Ingester | Add orchestration and fact collection around rulebook/component/golden-fixture truth. Do not force UI-scout. |
| Dossier | Add orchestration and fact collection around eval/model/codebase freshness. Decide whether a light architecture lane is useful or whether existing codebase-improvement and eval surfaces are sufficient. |
| Conductor | Keep supervisor triage focused on inbox, stories, alignments, scouts, project registry, and methodology memory. Do not import product eval/UI lanes except as cross-project alignment facts. |

## Rollout Execution Summary

After the Storybook pilot converged, the remaining repos were upgraded in
isolated worktrees under
`/Users/cam/.codex/worktrees/triage-orchestration-rollout/` on branch
`codex/triage-orchestration-rollout`. Primary checkouts were not edited.

| Repo | Base | Preservation and adaptation result | Loop verification |
| --- | --- | --- | --- |
| Dossier | `eabc640` | Preserved eval/model/codebase freshness and kept architecture as a health/facts signal rather than forcing a product architecture leaf. Added direct facts and triage-health. | 2 rounds; clean Round 2. |
| doc-web | `aca1922` | Preserved document-pipeline, benchmark, architecture, and codebase-improvement guidance without forcing UI-scout or golden-verify assumptions. | 10 rounds; clean Round 10. |
| CineForge | `5dda308` | Preserved provider/runtime, storyboard/eval, architecture, and UI-scout state boundaries; added direct facts and health packet guidance. | 4 rounds; clean Round 4. |
| Board Game Ingester | `ca368fd` | Preserved raw scan, rulebook/component/golden-asset, coverage matrix, no-downsampling, traceability, and eval-before-build guidance. | 10 rounds; clean Round 10. |
| Robo Rally | `c46edf4` | Preserved private proof-of-concept, headless-first, rulebook-driven, golden/eval artifact guidance, and deferred UI-scout state. | 2 rounds; clean Round 2. |
| Echo Forge | `d6547dc` | Preserved browser-first/frontend-only runtime, fun/easy/engaging product goal, ADR-001/ADR-002 boundaries, UI-scout scenario truth, Scout 003 competitive baseline, and eval registry/attempt semantics. | 34 rounds; clean Round 34. |

Repo-native validation passed in each worktree. Known caveats are local and
pre-existing: Dossier's broader `make lint` still reports unrelated failures
outside the rollout, and CineForge's methodology check still reports the
existing architecture-audit-due warning.

The Echo Forge loop exposed a useful process upgrade for future greenfield or
recently imported repos: after any material fact-semantic fix, do a local
propagation sweep across main triage, leaves, health/preservation runbooks,
facts, tests, and wrappers before the next full loop. This prevents workers
from spending many rounds rediscovering the same semantic in adjacent surfaces.

## Setup Methodology Follow-Up

The same greenfield problem applies one step earlier than triage: a repo with
little or no code cannot produce runtime, UI-scout, architecture, eval-attempt,
or codebase-improvement evidence yet. The portable product-repo
`/setup-methodology` skill was therefore upgraded once in the Storybook rollout
worktree and copied exactly into the other product worktrees.

The shared product setup skill now requires real `docs/ideal.md` and
`docs/spec.md` from `/init-project` or equivalent intake before package setup,
installs the upgraded triage/triage-health/loop-verify surfaces, marks
code-dependent lanes absent or deferred instead of broken, adds sparse-safe
facts when tooling exists, and runs cheap validation instead of long subagent
loops over evidence that cannot exist yet.

Conductor's own `/setup-methodology` remains supervisor-specific, but now
records the operational rule for product repos: upgrade one shared source,
perform a local no-code propagation sweep, copy the exact skill file to the
other product repos, regenerate wrappers, and validate.

## Human Decisions to Keep Visible

- Whether Dossier should gain a real `triage-architecture` skill or only a
  lighter health-freshness summary.
- Whether CineForge should gain a `ui-scout` skill to match its docs/state lane.
- Whether every repo needs a named `triage-health` skill, or whether
  orchestration plus fact collector plus existing leaf skills is cleaner.
- How much model/provider freshness belongs in the default fact collector
  versus remaining inside `triage-evals` or `discover-models`.

## Recommendation

Proceed with the Storybook pilot first. Do not rewrite any leaf skill until the
Storybook preservation map is written. After the pilot is live-checked and
loop-verified, update Story 005's rollout instructions and only then adapt the
pattern to the remaining repos in isolated worktrees.
