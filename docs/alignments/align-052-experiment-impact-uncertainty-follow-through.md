# Alignment 052 — Experiment impact, uncertainty, and review follow-through

Date: 2026-10-03 (America/Edmonton)
Classification: Portable improvements with owner-specific adaptation
State: Eight owner patches landed on verified remote main; supervisor close-out included here

## Decision and scope

Cam requested review of Board Game Ingester's three-skill feedback and authorized
updates where agreed, followed by adaptation to the managed portfolio. The prior
membership decision in this conversation added Ultima IV Web, Financial Hub, and
Financial Monthly Analysis to the existing seven. All ten are covered below;
other projects from the app/local inventory remain outside the managed list for
now. No repeated membership question was needed for the same inventory.

Agree with the focused update. Prioritize end-to-end impact over local percentages,
separate numerical threshold passes from convincing adoption evidence, and verify
that previous reviews changed the work. The pasted 5.045% result and two-of-three
pairs below 5% motivate uncertainty discipline; this task did not rerun or
independently audit that historical experiment. The numeric example is user-supplied
evidence, not a new measurement.

## Portable changes

- `triage-evals`: estimate stage share of total time, cost, or human effort and
  plausible overall savings. For additive work, use share × fractional reduction;
  consider the critical path for parallel work. Keep quality defects and critical
  dependencies as independent reasons for action. Qualify inherited rules that
  favored any bounded experiment regardless of impact or opportunity cost.
- `improve-eval`: record hypothesis, baseline/metric/aggregation, quality gates,
  meaningful threshold, budget, stopping conditions, and adoption/rejection rules
  before results. Start with the cheapest evidence that can settle the decision.
  Assess paired variation, sample limits, and precision; a borderline numerical
  pass may receive one predeclared confirmation within authorization or remain
  uncertain. Preserve outcomes and prohibit favorable-result fishing. Label
  development/independent-validation inputs, disclose tuning exposure, and use
  fresh material for the next independent confirmation. Link local proportional
  validation policy and reuse applicable evidence; SHA differences alone do not
  force reruns. Reconcile automatic repeat-run and always-measure wording with
  bounded confirmation and offline rejection.
- `loop-review`: check previous recommendation follow-through, user utility or
  decision evidence, opportunity cost, and finish/change/defer/stop choices.
  Preserve requested deadlines and cadence across interruptions, distinguish
  useful failed experiments and verified dependency waits from bookkeeping,
  and separate story completion from the goal's stopping condition.

Use existing attempt records and story logs. No new experimental ledger, registry
schema, runtime thresholds, historical scores, fixtures, or schedules are introduced.

## Owner patches

Every target branch is `codex/experiment-discipline-20261003`. Bases are the inspected
`origin/main` commits below. Primary checkouts remain untouched. Several primary
checkouts lag their remote-tracking branch; preserve newer base skill versions,
including existing `loop-review` skills missing from older primaries. Board Game
Ingester and Ultima's selected primary skill files matched the base; adaptations
were made in the isolated copies.

| Project | Skills / disposition | Worktree | Base SHA |
| --- | --- | --- | --- |
| Dossier | triage-evals, improve-eval, loop-review | [dossier](/Users/cam/.codex/worktrees/experiment-discipline-20261003/dossier) | `400c4c8e5ef9eb5730e7ff47de32a4604b647737` |
| Storybook | triage-evals, improve-eval, loop-review | [storybook](/Users/cam/.codex/worktrees/experiment-discipline-20261003/storybook) | `b27f84dc02ccf6efcfc4a1f7f89cdae786944dd3` |
| Doc Web | triage-evals, improve-eval, loop-review | [doc-web](/Users/cam/.codex/worktrees/experiment-discipline-20261003/doc-web) | `982847aa8dc79094e640a0dac2a9406fdac4564d` |
| CineForge | triage-evals, improve-eval, loop-review | [cine-forge](/Users/cam/.codex/worktrees/experiment-discipline-20261003/cine-forge) | `2c0a7ee25972790f53920cd19d59013c8ba695dd` |
| Board Game Ingester | triage-evals, improve-eval, loop-review | [boardgame-ingester](/Users/cam/.codex/worktrees/experiment-discipline-20261003/boardgame-ingester) | `136b6cea6206b2351ee8aa92e7fec877aa1314b1` |
| Robo Rally | triage-evals, improve-eval, loop-review | [roborally](/Users/cam/.codex/worktrees/experiment-discipline-20261003/roborally) | `4123c2bbe22dc680748fc7823303a140d8ecf1ed` |
| Echo Forge | triage-evals, improve-eval, loop-review | [echo-forge](/Users/cam/.codex/worktrees/experiment-discipline-20261003/echo-forge) | `726864e531c2327d73462fcfd2be81c444fea504` |
| Ultima IV Web | triage-evals, improve-eval | [ultima-iv-web](/Users/cam/.codex/worktrees/experiment-discipline-20261003/ultima-iv-web) | `a35905f917000a3979efc7ed324cf6fd2794b5d2` |
| Financial Hub | No matching skills; unchanged | — | — |
| Financial Monthly Analysis | No matching skills; unchanged | — | — |

The finance repositories have none of these three skills in either inspected
primary or base. They remain managed, but this rollout leaves them unchanged;
no new skills or finance data mutations are justified. Their clean task-created
inspection worktrees/branches were removed. Ultima has no `loop-review`.

Conductor adapts the impact and experiment-decision principles in its existing
`evaluate-model` and `triage` skills, and the follow-through rules in the newer
`loop-review` found on remote main. Approved supervisor changes, including the
managed-project check and three registry additions from this same request, are
isolated in `/Users/cam/.codex/worktrees/experiment-discipline-20261003/conductor`
on `codex/experiment-discipline-20261003` from `eeaad59b2e35b300bcc870751255bd05db4b3886`.
Only this request's hunks were carried over; prior evaluation-skill changes were
already present on remote main. Other primary checkout changes are preserved.

## Validation

Documentation/skill changes only: inspect behavior, links, retained authorization
and owner-specific conventions, skill compatibility, generated methodology
records where required, and diff hygiene. Product suites and paid evals are not
needed for this change.

An independent read-only forward test of the updated Board Game Ingester skills
covered four scenarios: 5% stage share × 30% stage-time reduction (1.5% overall);
a 5.045% borderline aggregate with exposed validation cases and exhausted budget;
scorer-only reuse of bound outputs after a docs-only SHA change; and an interrupted
10:00–18:00 hourly review window with missing crop proof. Decisions correctly
qualified uncertainty, preserved the deadline, rejected repeated sampling, and
kept the broader goal incomplete. Two inherited wording conflicts were repaired:
mandatory before/after runs versus offline rejection, and read-only triage versus
proposed measurement execution.

Local skill checks and diff hygiene are recorded for each prepared owner patch.
`make skills-sync`/`make skills-check` (or the repo's equivalent shell skill
sync/check) passed for Dossier, Doc Web, CineForge, Storybook, Robo Rally, and
Echo Forge; Ultima's `make skills-check` passed. All eight owner diffs passed
`git diff --check`. Together they contain 23 existing-skill updates.
Board Game Ingester's `make skills-sync`, `make skills-check`,
`make methodology-compile`, and `make methodology-check` pass; generated graph
and story index remain unchanged. Conductor's skill compatibility, registry/graph
consistency, lint, and diff checks pass. No product-quality or live-rollout claim
follows from these documentation checks.

Methodology checks passed across all eight owners. Dossier required its existing
Miniconda Python (`make methodology-check PYTHON=/Users/cam/miniconda3/bin/python`)
because the default Python lacked PyYAML; its pre-existing migration/link warnings
remain. Doc Web used `make methodology-check`; Storybook used
`node --experimental-strip-types scripts/methodology-graph.ts check`; Robo Rally
and Echo Forge used `node scripts/methodology-graph.mjs check`; Ultima used
`make methodology-check`. Echo retains its existing no-Ideal-requirements warning.
CineForge's initial `node scripts/methodology-graph.js check` found a calendar-age
warning one day stale. Running its native `build` then `check` passed and refreshed
only that warning (173 → 174 days) in graph, story index, and build-map; those
three generated files are included alongside its three skill files. Existing
architecture/UI freshness warnings were not treated as rollout fixes.

## Close-out

Cam explicitly approved scoped commit and landing with `yes`. Close-out follows
`/finish-and-push`: add locally required changelog entries, retain applicable
validation evidence, integrate latest remote main, push execution branches, and
fast-forward each remote main without altering active primary checkouts. No
runtime adoption, deployment, paid calls, or messages to other active chats are
part of this rollout. Retain task worktrees/branches; cleanup was not requested.


## Verified owner landings

The coordinator independently checked `git ls-remote` after all owner landings.
Each commit below is present on remote `main` and the execution branch; every
owner task worktree is clean. No implicit primary-checkout synchronization follows
from landing: existing active/dirty checkouts retain their branches and files.

| Repository | Commit | Remote main / execution branch |
| --- | --- | --- |
| Dossier | `f2cc4088356f40a56aad791ad704a9afe6c556f6` | Verified / verified |
| Storybook | `3da1ed40cebd90828e5b2d9b9007be036ee8d7a5` | Verified / verified |
| Doc Web | `6fec862221296ae8036b26a298b61af71645fa94` | Verified / verified |
| CineForge | `2552378ba595841296671eec9b8f422e9f4b2fe8` | Verified / verified |
| Board Game Ingester | `e33ade61b34c5022947db38e84d8821bddeec4ad` | Verified / verified |
| Robo Rally | `4bbef77e0b50cff9b745c639392a354608be147f` | Verified / verified |
| Echo Forge | `4a5cddb37cc21cd7cff08722315d499344a7de30` | Verified / verified |
| Ultima IV Web | `b1488047b8e3eaeee221160aed56130742e08326` | Verified / verified |

Board Game Ingester integrated upstream `9544690` before landing and includes
changelog entry `2026-10-03-07`. Storybook integrated upstream `73f1a090`, retained
its Story 185 entry, and added `2026-10-03-02`. Both integrations leave the skill
changes intact; affected skill/methodology/record checks passed. Dossier, Doc Web,
CineForge, and Echo Forge also include their locally required changelog entries.
Robo Rally and Ultima have no tracked changelog requirement for this scope.

Ultima's scoped methodology, skill, and diff checks pass. An additional
`make validate` attempt passed those and two methodology-tool tests, then stopped
at the asset check because ignored `input/legacy/source` assets are absent from
its task worktree. This is an unavailable full asset-validation lane, not a
skill-check failure; no game behavior was changed or claimed verified, and no
source assets were copied or symlinked. Existing Dossier, CineForge, and Echo
methodology warnings remain as recorded above.

Conductor's close-out contains only approved supervisor/registry/skill changes,
this landing record and related scoped inbox/index entries. Its four skill
surfaces include the newly discovered existing `loop-review` on latest main.
The isolated supervisor passed `make methodology-compile`,
`make methodology-check`, `make skills-check` (21 skills), `make lint`, and diff
hygiene. Final supervisor remote verification occurs after its close-out push.
