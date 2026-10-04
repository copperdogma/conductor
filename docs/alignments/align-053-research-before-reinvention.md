# Alignment 053 — Research Before Reinvention

**Date**: 2026-10-04
**Status**: Implemented, validated, committed, and verified on remote main in all
eleven approved owner projects. Cam approved commit and landing on 2026-10-04.
Active primary checkouts were preserved; Conductor completion record is prepared
from current remote main after verified owner landings.
**Focus**: Use established techniques before investing in bespoke solutions to
nontrivial obstacles.
**Source**: Cam's Ultima IV feedback, current global and Ultima instructions,
and Conductor's project setup and execution skills.

## Assessment

Adopt the principle. A short investigation of the general problem class can
avoid repeated speculative fixes. Improve the trigger, stopping condition, and
local verification; do not add a mandatory research phase to every task.

At the initial audit, the rule already existed in `/Users/cam/.codex/AGENTS.md` (lines 3–22) and
`/Users/cam/Documents/Projects/ultima-iv-web/AGENTS.md` (lines 31–43). The latter
explicitly permits general techniques while preserving the boundary against
borrowing completed game implementations. Conductor's repository AGENTS lacked
a portable equivalent, although the session received the global instruction.
The local implementation below closes that gap.

## Surfaces Compared

- Global and Ultima IV `AGENTS.md`, Conductor `AGENTS.md`.
- Conductor `/init-project`, its kickoff runbook, `/setup-methodology`, its
  local runbook and checklist.
- Conductor `/build-story`, `/validate`, `/scout`, `/ideation`, `/create-story`,
  `/create-adr`, `/learning-review`, `/loop-verify`, `/evaluate-model`, and
  `/finish-and-push`; Ultima IV's `/improve-eval` as a targeted comparison.
- Follow-up: Storybook's current repository `/loop-review` and Conductor's
  `/loop-verify` cadence, convergence, and stopping provisions. Conductor had
  no local `/loop-review` copy at audit time; implementation adds one below.
- Conductor Ideal/spec, methodology state/graph, registry, inbox, and existing
  alignment/scout records, including Alignment 028's current-docs guidance.

This is a focused comparison, not a completed portfolio inventory or rollout.

## Refinements

1. Start with enough local evidence to name the obstacle: logs, reproduction,
   existing tests, prior research, or a known runbook. An obvious correction
   does not need an external literature search.
2. Research before the first speculative workaround for an unfamiliar material
   obstacle. Repeated failure is an additional trigger, not a prerequisite.
3. Generalize the mechanism while retaining relevant constraints. Search for
   nondeterministic tests, controlled replay, asynchronous state transitions,
   or changing navigation state; avoid a query overloaded with project names.
4. Inspect a few relevant primary sources and stop once a source-backed option
   and a discriminating local experiment are clear. This is a ceiling on
   exploration, not a source quota. If evidence is insufficient, state the gap
   and choose a bounded experiment or report the actual blocker.
5. Compare assumptions, complexity, reuse permissions, and maintenance cost.
   Adopt, adapt, reject, or improve an existing approach with a concrete reason.
6. Verify applicability locally. Research supports a hypothesis; a source link
   alone does not establish that the approach fixes this project.
7. Save reusable findings in the existing story log or research notes: problem
   class, useful sources, decision, local result, remaining uncertainty. Reuse
   still-applicable findings. No new ledger, story, ADR, or scout is required
   for every obstacle.

## Approved Changes

| Surface | Recommendation |
| --- | --- |
| Repository `AGENTS.md` | Add a concise portable rule. Keep detailed domain examples and reuse boundaries local. Global instructions already cover this machine; repository instructions make the norm travel with the project. |
| `/init-project` and kickoff runbook | Include the rule when creating the first AGENTS file, including lean projects that defer full methodology setup. Extract reuse boundaries from intake; ask only when a material boundary is unclear. |
| `/setup-methodology` | Add the rule to AGENTS installation/refresh and core-loop wiring. Extend the current upstream-docs rule to cover established problem-solving techniques. Align the runbook/checklist, preserving intentional lean variants. |
| `/build-story` | Add a short trigger both during planning and when implementation hits a nontrivial obstacle. Record the selected practice and smallest local check in the existing work log; this must remain active after the plan is approved. |
| `/validate` | Before repeated unexplained failures lead to retries, sleeps, relaxed assertions, or special cases, apply the same research rule. Preserve the acceptance contract and proportional evidence reuse. |
| `/scout`, `/ideation`, `/create-adr` | Keep their existing jobs. Source scouting, divergent option generation, and durable decisions are useful when warranted; routine obstacle research need not invoke them. |
| `/loop-verify` | Add a coordinator strategy check before continuing a round and a periodic bounded comparison with established techniques for longer authorized runs. Research informs the existing systemic-audit route; it does not override hard stops or extend budgets. |
| `/loop-review` | Add a source-backed challenge of the current approach at each existing strategic review checkpoint, reusing still-applicable prior research. Compare against a meaningfully different established technique, including when local metrics improve but the user outcome does not. |
| `/evaluate-model`, `/improve-eval`, `/finish-and-push` | Preserve existing diagnosis, experiment budgets, uncertainty, and validation rules. Start with inherited AGENTS guidance rather than duplicating a full research procedure. |

## Follow-up: Research Within Long-Running Loops

Cam identified `/loop-verify` and `/loop-review` as important places to challenge
local optima and myopic approaches on a regular cadence. This revises the initial
recommendation to leave `/loop-verify` covered only by inherited guidance.

Existing stop controls limit non-convergent work, but do not necessarily supply
an established alternative. `/loop-review` already asks about actual utility,
bottlenecks, alternatives, opportunity cost, and previous recommendation
follow-through; its alternatives can still come entirely from the agent's own
current framing. Research is a useful addition to that existing step.

Recommended division:

- `/loop-verify`: the coordinator checks progress, repeated assumptions, and
  accumulating special cases at each round boundary before choosing another
  round. Workers retain one bounded shard assignment. On longer authorized
  runs, periodically compare the current technique against established
  approaches; a new uncertain obstacle can trigger that comparison earlier.
  A clean scoped result still ends verification. Any mismatch between the
  verified contract and the broader user outcome is a separate review finding,
  not a reason to keep resetting the verifier.
- `/loop-review`: at each existing strategic checkpoint, challenge the chosen
  problem framing and technique using a short comparison with established
  alternatives. This should be proactive: gradual improvement of a proxy or
  subproblem does not establish that the current approach remains worthwhile.
  Reuse a recent source-backed comparison only when its assumptions, relevant
  constraints, and observed failure modes still apply; state that reason.
  Otherwise do a bounded general-problem-class source pass.

Use the cadence already requested by Cam. Where a long active loop has no
specified cadence, a proposed initial default is a strategy checkpoint after
roughly 30 minutes of active work or three substantive rounds, whichever comes
first. This is a tunable starting policy, not a measured optimum. It applies
within an authorized active run; it neither creates a recurring automation nor
extends a short loop. Verified dependency waiting is not repeated execution.
Preserve cadence state across interruptions instead of restarting the clock.

Existing hard stops take precedence. In particular, `/loop-verify` already
stops for two consecutive same-class material passes, two resets without risk
narrowing, scope expansion, and other non-convergence signals. Do not wait for
the periodic checkpoint when one occurs. Any research for a proposed systemic
follow-up must fit the remaining authorized audit scope and budget; it cannot
justify another otherwise-disallowed round or automatic implementation.

A checkpoint should answer:

1. What outcome or uncertainty improved since the previous checkpoint?
2. Would we choose this approach again given what we now know?
3. What established, meaningfully different approach addresses this problem
   class, and which assumptions make it applicable or inapplicable here?
4. What small comparison would justify continuing or changing approach?

Record the source comparison (or applicable reused evidence), disposition,
next experiment when warranted, and reassessment trigger in the existing log.
Continuing is a valid decision; novelty and new web searches are not quotas.
Research and experiments count against existing budgets. Keep quality gates,
owner boundaries, nonrecursive workers, and existing review/handoff authority.

After patching, check scenarios with repeated same-class failures, genuine
progress, improving proxy metrics without user benefit, applicable recent
research, an interrupted cadence, and an exhausted budget. These cases should
distinguish useful reconsideration from ritual browsing and stop-rule bypass.

## Proposed Compact Rule

> When a nontrivial obstacle makes the next step uncertain, inspect enough
> local evidence to name the general problem class, then check established
> approaches before inventing a workaround. Reuse applicable prior research;
> otherwise consult a few primary sources, retaining the constraints that
> affect applicability. Stop once you can choose an approach and a small local
> test. Prefer the simplest permitted technique that fits; explain material
> departures. If attempts keep failing, revisit the diagnosis and assumptions
> before adding retries or special cases. Record reusable sources, the
> decision, local evidence, and uncertainty in existing project notes. Obvious
> fixes need no research ceremony. Preserve project reuse boundaries and
> acceptance criteria.

## Sources and Applicability

- [OpenAI AGENTS guidance](https://developers.openai.com/codex/guides/agents-md)
  documents global and repository instruction scopes.
  [Skill guidance](https://developers.openai.com/codex/skills) documents that
  full skill bodies load when selected. These support putting the default
  behavior in AGENTS with narrow reinforcement in relevant skills.
- [pytest flaky tests](https://pytest.org/en/latest/explanation/flaky.html)
  treats uncontrolled state and isolation as common causes. This supports
  diagnosing the source of nondeterminism before adding test retries.
- [Hypothesis settings](https://hypothesis.readthedocs.io/en/latest/settings.html)
  and [flakiness guidance](https://hypothesis.readthedocs.io/en/latest/tutorial/flaky.html)
  distinguish reproducible generation from other sources of nondeterminism.
  Seeded regression and broader randomized coverage answer different questions;
  controlling a seed alone does not control timing or external state.
- [Selenium waits](https://www.selenium.dev/documentation/webdriver/waits/)
  documents condition-based waiting. This is a useful analogue for an
  asynchronous dialogue/state transition, subject to local observability.
- [Nav2 behavior-tree walkthrough](https://docs.nav2.org/rolling/getting_started/nav2_behavior_trees/detailed_behavior_tree_walkthrough/detailed_behavior_tree_walkthrough/)
  documents replanning and recovery. This is a source of general techniques for
  changing obstacles, not a demonstrated Ultima fix or a proposal to install
  robotics middleware.

No Ultima implementation experiment or instruction-effectiveness evaluation was
run in the initial advisory pass. After a patch, a small scenario check should cover an
obvious fix, an unfamiliar flaky test, a repeatedly failing workaround, and a
project with restricted implementation reuse. Inspect whether research changed
the next useful action without weakening verification or adding routine overhead.

## Local Implementation and Validation

Cam approved all recommended changes here and explicitly excluded rollout to
other projects. The work is bounded by this alignment; no separate story or
managed-project inventory is needed for this Conductor-only implementation.

- Added the portable problem-class research rule and strategy cadence to
  Conductor `AGENTS.md`.
- Updated `/init-project`, `/setup-methodology`, both setup runbooks, and the
  lean checklist so the rule survives kickoff, deferred full setup, and refresh.
  Setup also carries the build/validation triggers and optional loop guidance.
- Updated `/build-story` for planning and mid-implementation obstacles, and
  `/validate` for unfamiliar or repeatedly unexplained failures, retaining
  proportional checks and acceptance criteria.
- Updated `/loop-verify` with coordinator round checks, periodic source
  comparisons, interruption continuity, explicit budget/stop precedence, and
  a distinction between a clean verifier and an incomplete broader goal.
- Added the existing `/loop-review` workflow to Conductor and extended it with
  source-backed strategic checkpoints. Baseline: Storybook's repository skill,
  last file commit `3da1ed40` (2026-10-03); inspected source SHA-256
  `d48efe319e44f13eb7aaef3c1c1efdae81271be637990d4e0e190a96fceabbf3`.
  Its owner file was read only. The local copy retains read-only audit,
  approval, thread-handoff, and goal-state boundaries, and shortens discovery
  text. README now exposes this workflow.

Current validation:

- `make skills-check`: passed, 21 canonical skills and valid compatibility links.
  Existing directory links discover the added skill without regeneration.
- `make methodology-check`: passed, existing graph current; no regeneration.
- `make lint`: passed.
- Generic `skill-creator/scripts/quick_validate.py` rejects the repository's
  established `user-invocable` frontmatter field. It passed for all six touched
  skills on temporary projections omitting only that field; each original was
  checked for matching name and `user-invocable: true`. Source files retain the
  local convention. This is a qualified schema check, not an unmodified generic
  validator pass.
- Scoped diff hygiene passed, including the new untracked skill and alignment.
- Independent simulated forward testing read the instructions and six skills
  without the authoring report or expected answers. Eleven hypothetical
  scenarios covered obvious fixes, an exhausted verifier budget, repeated
  same-class defects, proxy improvement without user benefit, applicable
  research reuse, active-time/round continuity, overdue timed reviews, a clean
  verifier with an incomplete goal, restricted implementation reuse, lean
  kickoff, and unavailable research. The reviewer identified three wording
  ambiguities: strict reset scope in setup, optional first-story creation,
  and missed-checkpoint handling. These were corrected, and the reviewer
  rechecked the affected cases plus resumption after a hard deadline with zero
  budget. No material ambiguity remained in those cases.

Key scenario decisions:

| Scenario | Observed instruction decision |
| --- | --- |
| Obvious typo | Fix and use the targeted check; no research ritual. |
| All 12 verifier minutes consumed | Report continuation needed; no research or extra round beyond budget. |
| Two same-class material passes | Stop for systemic audit immediately, before the periodic checkpoint. |
| Benchmark improves, corrections unchanged | Refresh the outdated comparison and propose an outcome-based experiment; audit does not execute it. |
| Prior research still applies | Reuse with a reason and continue when outcome evidence supports it. |
| 20 active minutes/two rounds, interruption, then 11 minutes/one round | Deeper comparison is due at 31 active minutes/three rounds; brief checks do not reset counters. |
| 15:00 review missed; resume 15:10 before 18:00 deadline | One current-state review, next review still 16:00, original deadline retained. |
| Clean verifier, broader goal incomplete | End verification; perform the broader strategy review separately. |
| General techniques permitted; completed remake forbidden | Use permitted replay research and local proof, preserving the implementation boundary. |
| Lean kickoff | Install the rule in initial AGENTS; story creation depends on the approved package. |
| No applicable sources in bounded pass | Report uncertainty; use only authorized diagnostics or stop. |
| Resume after hard deadline with no budget | Report the missed check; no catch-up work or implicit extension. |

Validation is proportional to instructions/docs changes. Product suites, paid
evals, actual long-running thread interventions, schedules, and target-project
changes were outside the initial Conductor-only implementation. Scenario walkthroughs assess instruction
decisions, not measured production savings or proof that agents always comply.

## Classification and Next Action

Portable improvement: a research trigger and setup coverage.
Intentional adaptation: Ultima's domain examples and implementation-reuse limits.
No standalone research skill, automation, dependency, or research framework was
added. The new local skill is an adaptation of the existing `/loop-review`.

The changes are ready for local Conductor use. The next useful effectiveness
evidence is an actual authorized long-running Conductor task; this pass does
not start one or claim measured token/time savings.
Cam's subsequent rollout request supersedes the earlier deferral. The rollout
performs the managed-project check and uses dedicated worktrees. Commits and
pushes require separate authorization.

## Rollout Preparation — 2026-10-04

Read-only inventory checked the current Codex project list and local Git markers
through three levels under `/Users/cam/Documents/Projects`, excluding known
dependency/generated/vendor trees, plus the two external app Git roots for
Hardware Specs and Matt's campaign images. Git common-directory identity
deduplicates worktrees. Remaining vendor, archived, backup, and inactive entries
are discovery evidence, not targets or automatic registry additions.

Current managed membership: Dossier, Storybook, Doc Web, CineForge, Board Game
Ingester, Robo Rally, Echo Forge, Ultima IV Web, Financial Hub, and Financial
Monthly Analysis. At discovery all ten had local `origin/main` refs; these were subsequently
refreshed for execution. Primary checkouts were dirty except Robo Rally.

| Additional candidate with methodology skills | Path | Observed last commit | Skills in primary |
| --- | --- | --- | --- |
| VLC Thumbs | `/Users/cam/Documents/Projects/ultima-iv-web/vlc-thumbs` | 2026-10-03 `fdf25f2` | 33 |
| Ravenloft Cthulhu | `/Users/cam/Documents/Projects/ravenloft-cthulhu` | 2026-05-26 `4421cdf` | 28 |
| RPG Map Projector | `/Users/cam/Documents/Projects/rpg-map-projector` | 2026-06-03 `7d628da` | 16 |
| Canmore Town Council | `/Users/cam/Documents/Projects/canmore-town-council` | 2026-07-18 `a17e92a` | 17 |
| Alain Lessard Book | `/Users/cam/Documents/Projects/alain-lessard-book` | 2026-07-19 `592d711` | 25 |
| Onward to the Unknown Website | `/Users/cam/Documents/Projects/onward-to-the-unknown-website` | 2026-07-19 `83d8338` | 25 |
| Codex Forge | `/Users/cam/Documents/Projects/codex-forge` | 2026-03-19 `45b1e10` | 22 |

Other instruction-bearing app roots include Hardware Specs, Box of Death,
Death the Fortune-Telling Skeleton, Fighting Fantasy Engine, and Matt's campaign
images. They lack matching methodology skills in their primary copies and are
not recommended for a full skill-package rollout from that fact alone. Activity
dates do not prove managed membership. The skill-bearing candidate list above
was presented for additions/removals; recommended initial choice is retain the
ten and add the recently initialized, separate VLC Thumbs repository.

Read-only owner comparison found:

- The eight product/game repos have setup, build, validation, and loop-verify
  skills on their current local `origin/main` refs. All but Ultima IV also have
  loop-review there. Init-project is absent in Dossier and Doc Web.
- Shared setup/verification guidance is broadly portable, but local build,
  validation, and kickoff skills differ substantially. Apply narrow semantic
  updates instead of replacing product-specific content with Conductor's
  supervisor versions. Preserve Ultima's completed-implementation exclusion.
- The two finance repos have none of the six targeted skills on those refs.
  A portable root research rule is relevant; preserve their lean workflows,
  source ownership, private-data and production gates, without installing a
  full methodology package simply to match the other projects.
- Owner-native documentation/skill and methodology checks are applicable;
  product suites or billable API evaluations are not implied by this change.

Cam resolved membership with “Ten plus VLC”: retain all ten, add VLC Thumbs,
and do not add the other six skill-bearing candidates from this inventory.
Their exclusion is recorded for this pass; it is not a judgment about future
relevance. The registry now contains eleven projects and generated methodology
references were refreshed.

## Approved owner execution

Fetched each target's origin and created a dedicated worktree from current
origin/main. Every target uses branch `codex/research-before-reinvention-20261004`
under `/Users/cam/.codex/worktrees/research-before-reinvention-20261004/`.
Existing primary checkouts were not edited or switched. No owner chats were messaged. During preparation no commits or pushes were
performed; Cam then explicitly authorized the close-out recorded below. No
schedules, paid evaluations, or deployments were performed.

Nine product/game/media projects receive root instructions and focused changes
to existing setup, build, validation, verification, review, and available kickoff
surfaces. Ultima receives the missing loop-review skill. Local product workflow
and reuse boundaries remain intact. The shared setup research guidance is
adapted to each owner's existing strict full-scope verifier resets rather than
changing its convergence model as part of this rollout.

The finance projects receive a root research rule and manual strategic
checkpoints. Their lean workflow is preserved; no missing harness is installed.
Search queries exclude private household context, and research never opens
financial intake, mutation, publication, or external-action gates.

VLC retains its historical skill-import provenance while recording current
adopted hashes. Its native scaffold check receives a narrow Git-worktree
compatibility fix so the same check works in primary and isolated checkouts.
These checks do not prove native timeline features, persistence, media integrity,
or build behavior.


### Owner patch receipt

[Machine-readable validation receipt](evidence/align-053-research-rollout.json)
records complete bases, paths, file hashes, native check commands/results, and
intentional adaptations. The prepared owner notes live in each worktree at
`docs/research-before-reinvention.md`.

| Owner | Base | Prepared scope | Native validation |
| --- | --- | --- | --- |
| Board Game Ingester | `9ba7543e9154` | Root + existing workflow surfaces; owner contracts retained | Methodology + skills |
| CineForge | `714802a53275` | Root + existing workflow surfaces; owner contracts retained | Methodology + skills |
| Doc Web | `6fec86222129` | Root + existing workflow surfaces; owner contracts retained | Methodology + skills |
| Dossier | `ed7b0d6b4cfe` | Root + existing workflow surfaces; owner contracts retained | Methodology + skills (existing owner Python) |
| Echo Forge | `4a5cddb37cc2` | Root + existing workflow surfaces; owner contracts retained | Methodology + skills |
| Financial Hub | `21e9b0211095` | Root research/manual checkpoints; privacy preserved | Preservation inspection + diff hygiene |
| Financial Monthly Analysis | `555cd158cc6d` | Root research/manual checkpoints; privacy preserved | Preservation inspection + diff hygiene |
| Robo Rally | `4bbef77e0b50` | Root + existing workflow surfaces; owner contracts retained | Methodology + skills |
| Storybook | `14767978eeb5` | Root + existing workflow surfaces; owner contracts retained | Methodology + skill checks |
| Ultima IV Web | `4bbc2e632364` | Root + existing workflow surfaces; owner contracts retained; loop-review added | Methodology + skills + two workflow tooling tests |
| VLC Thumbs | `4b16323224b3` | Root + existing workflow surfaces; owner contracts retained | make validate (methodology, skills, scaffold/hashes) |

Validation is limited to changed instructions, methodology metadata, skills,
and VLC's narrow scaffold compatibility fix. Existing methodology warnings in
Dossier, CineForge, and Echo Forge remain documented in the receipt. None is
proof of native feature behavior or measured time/token savings.

Independent applied-adaptation review checked setup/verifier consistency,
source boundaries, finance privacy, stop/cadence behavior, and preservation of
product-specific skill bodies. It found missing future-setup checklist hooks
in three owners; these were corrected and their final native skill/diff checks
passed before close-out.

All eleven primary AGENTS.md hashes match their pre-rollout snapshots. Primary
status is unchanged for ten; Ultima's active owner work added unrelated campaign
research files during this pass, which were preserved. The isolated patches were subsequently committed and landed under Cam's
explicit approval, with remote-main receipts below. Primary checkouts retain
their existing branches and dirty work; their agents adopt these instructions
when their owning workflow integrates current main.

## Verified landing — 2026-10-04

Cam replied “Yes” to commit and land the eleven validated owner patches.
Preflight confirmed every owner remote still matched its prepared base.
Original instruction/tooling hashes remained unchanged. Only public authorization
notes and the six required existing owner changelogs were added for close-out.
Reused validation remains applicable; final staged diff checks passed.
Ultima's required workflow compile/check and two tooling tests also passed.

Each execution branch and remote main received the scoped commit. Remote
`refs/heads/main` was then checked against the exact committed SHA:

| Owner | Verified remote main commit |
| --- | --- |
| Board Game Ingester | `b6e6edf8a4fe6592b2596f03482df921cf01e19f` |
| CineForge | `2e148974583e731bedd32e4896b282a94134aeff` |
| Doc Web | `dd4438435a2c06749b03185149603c7284d0d227` |
| Dossier | `15ac295ea705a9fdd00590b2e5855b34ee05a256` |
| Echo Forge | `95b176e11b7760e7ca2472552a418cd5d413ce27` |
| Financial Hub | `f6f44b5ea467c336a5e469b4fb9174fd1b029a29` |
| Financial Monthly Analysis | `dfa19f563a82b6a0d80cb645cf6469cb1e794e63` |
| Robo Rally | `475ce183a7aece3c7b3badc68875a45cc140d5d9` |
| Storybook | `fedc582ee5e8a4dfde1244a372ecdd1aa3dd7dbf` |
| Ultima IV Web | `70a0d14e2fb5ca7bfc36e3730e0adc76b616db7b` |
| VLC Thumbs | `476d7ea8fa963f934cdd23751ec3858bbcca522c` |

Conductor integration starts from current `origin/main` (`897724a`), preserving
previously landed decision-model guidance, loop-review follow-through, and the
ten-project registry. Only this task's changes were transferred using the
pre-task snapshot; VLC is the sole registry addition. Generated references,
skills, lint, diff hygiene, and independent integration review passed.

Primary work was neither reset, stashed, switched, nor synchronized. Task
worktrees and branches are retained. Other owner branches can adopt current
main through their normal integration workflow; no owner chats were interrupted.
No product effectiveness or token-saving claim follows from this landing.
