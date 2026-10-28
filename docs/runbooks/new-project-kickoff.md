# Runbook: New Project Kickoff

This runbook standardizes what happens after Cam creates a raw idea seed such
as `docs/initial-concept.md`.

The goal is not to make the AI decide everything alone. The goal is to give the
AI a map of the available methodology pieces, make it form a recommendation,
then interview Cam until the project shape is clear enough to set up.

## Standard Prompt

Use this when starting a new project:

```text
Read and follow the Conductor kickoff skill:
<conductor-root>/.agents/skills/init-project/SKILL.md

The repo is <path>. Start from docs/initial-concept.md.

Do not scaffold yet. The skill will tell you how to find its companion runbook.
Read the seed, classify the project, explain which setup surfaces you recommend
and why, discuss alternatives with me, and wait for approval before creating
files.
```

## Reference discovery

During kickoff, browse `docs/reference.md` in the Conductor source checkout and
read matching entries before proposing the first implementation. Discuss useful
tools and working examples with the user, including reuse/adaptation value,
limitations, and current alternatives. Treat entries as leads; verify current
primary sources before recommending adoption. Carry the result into setup notes
without repeating an applicable review. If access is unavailable or nothing
fits, state that and continue. The library need not be copied into the target.

## Phases

When hosting, DNS or Google sign-in is needed, read the Conductor source
[shared service catalog](../services.md) before mining another project's
environment. Choose a compatible recipe and selected credential profile;
confirm resource scope and use a dedicated new-app credential where appropriate.
Carry the service choice and public resource identities into the target's setup
notes. Keep private credential values out of copied methodology, prompts and Git.

### 1. Seed

The user or agent creates one preserved raw intake file. Prefer:

- `docs/initial-concept.md` for chat captures, long idea dumps, or compiled
  early decisions.
- `docs/inbox.md` later for loose follow-up ideas.

The seed can be messy. The kickoff pass should extract meaning, not preserve
chronology.

### 2. Interview

The agent reads the seed and returns a kickoff brief:

- what the project appears to be;
- what kind of project it is;
- which methodology pieces should be adopted, adapted, deferred, or rejected;
- which proof should come first;
- what material questions remain.

This phase is conversational. Cam can correct the classification, add missing
constraints, reject overhead, or ask for a different first proof.

When the seed exposes a nontrivial obstacle with an uncertain next step, use
local evidence to name its general problem class before proposing a workaround.
Check applicable prior research first; otherwise consult a few relevant primary
sources and choose a small local check of applicability. Skip research ceremony
for obvious fixes. When setup creates `AGENTS.md`, include a concise version of
this rule, reuse boundaries from intake, and direct reusable sources, decisions,
results, and uncertainty to existing project notes.

### 3. Approval

Setup starts only after Cam approves a named plan. A bare `yes` means "do the
specific setup action just described." It does not imply commit, push, target
repo rollout, or future automation beyond the named action.

### 4. Setup

After approval, the agent creates the agreed first surfaces. For most projects
that means:

- preserve `docs/initial-concept.md`;
- create `docs/ideal.md`;
- create `docs/spec.md`;
- create `docs/inbox.md`;
- create `AGENTS.md`;
- create the first story under `docs/stories/`.

Only after the Ideal/spec are real and reviewed should the agent run or adapt
the broader `/setup-methodology` package.

## Writing the Ideal

The Ideal answers: **what should be true for the user if technical capability
were no obstacle?** It is a short north star for the AI building the project.
Keep the language concrete and grounded in the user's intent. Remove today's
technical limitations from the desired outcome, without inventing new wishes.

Use the Ideal authoring contract embedded in `/init-project`: zero
implementation, one readable page by default (usually 200–500 words, shorter
when sufficient), and no duplicate catalog of the raw intake. Product and
execution ideals describe outcomes; neither is a place for implementation or
agent process. Preserve detailed raw intake separately.

| Ideal: desired outcome | Elsewhere: means, constraints, or proof |
| --- | --- |
| Relevant past knowledge is available when needed. | Spec/ADR: vector database, embedding model, retrieval pipeline. |
| My private material remains under my control. | Spec/ADR: local storage, encryption scheme, provider policy. |
| I can use the project wherever I need it, including without a connection. | Spec/story: service worker, cache schema, synchronization algorithm. |
| Improving the project requires little supervision and preserves working behavior. | AGENTS/runbook/eval: worktree commands, approval gates, test suite. |

Review every sentence for the outcome/mechanism boundary, then compress repeated
ideas and check coverage of distinct user needs. Do not use another project's
Ideal as a content template: it may contain the same implementation leakage.
During retrofit, infer proposed outcomes from code/docs but keep current
implementation facts out of the Ideal; confirm uncertain intent with the user.

## Project Shapes

Use these as starting classifications, not rigid boxes.

| Shape | Typical Setup | First Proof |
| --- | --- | --- |
| Creative/writing | Ideal, blueprint/spec, inbox, notes, lightweight stories, ADRs only for hard choices | A chapter/page/architecture pass that proves the creative spine works |
| Prototype/hardware | Ideal, spec, assumptions, risk log, stories, minimal runtime docs | Physical feasibility or calibration spike |
| Web app/product | Ideal, spec, stories, local runtime/ports, UI/browser proof lane when UI exists | Thin usable vertical slice in browser |
| AI pipeline/eval-heavy | Ideal, spec, eval/golden plan, fixtures, stories, provider freshness rules | One root eval or deterministic fixture proving the core behavior gap |
| Tooling/library | Ideal, spec/API contract, tests, README, stories | Small CLI/API path with tests |
| Supervisor/workflow | Ideal, spec, inbox, stories, scout/alignment logs, decisions | One routing/alignment/scout artifact that reduces repeated work |
| Personal utility/no-code | Ideal, tiny spec, inbox, sparse stories | The smallest artifact that changes the user's real workflow |

Hybrids are normal. Pick a primary type, then borrow only the useful pieces from
secondary types.

## Reusable package source

Conductor maintains the reviewed reusable skills and methodology baseline.
Select relevant pieces here, keeping the target's product requirements and
justified adaptations local. Project-local skills may be newer or better for
that project; generic, non-overfit improvements can be reviewed for promotion
back into Conductor. New-project setup should benefit from that accumulated
learning without inheriting unrelated domain machinery.

## Surface Menu

Classify each surface as adopt, adapt, defer, or reject.

| Surface | Use When |
| --- | --- |
| `docs/ideal.md` | Always, once the seed has enough meaning to synthesize a north star |
| `docs/spec.md` | Always, but adapt the name/purpose to the domain: blueprint, product spec, API contract, etc. |
| `docs/inbox.md` | Usually; use as the single raw capture surface after kickoff |
| `AGENTS.md` | Usually; keeps AI operating rules local to the repo |
| `docs/stories/` | Usually; create the first proof story as soon as setup is approved |
| `docs/methodology/state.yaml` and `graph.json` | Use when the repo benefits from state/graph-backed triage; defer for very small or creative repos unless useful |
| `docs/setup-checklist.md` | Use when running the broader methodology package |
| eval/golden surfaces | Use when product quality depends on repeated AI/pipeline behavior |
| local runtime/ports | Use when the repo has a real browser/API/local service |
| UI scout or visual inspection | Use when user-facing UI quality is a product risk |
| source-intake/scout logs | Use when external material or references will be repeatedly investigated |
| ADRs | Use for hard-to-reverse workflow, architecture, canon, or product decisions |
| Codex environment setup | Use when fresh worktrees need dependency hydration before validation |
| Deterministic scheduled-work kit | Use when recurring collection, exception monitoring or report preparation should happen before AI; select/adapt the optional `scheduled-work` module, leaving live scheduling and adapters disabled until configured |

## First Story Rule

Story 001 should reduce the largest real uncertainty, not simply create more
scaffolding.

Examples:

- Hardware/projection project: prove the physical calibration or projection
  geometry is viable.
- Writing/module project: prove the spine, revelation structure, or first table
  page works.
- Web app: ship a thin vertical slice in a real browser.
- AI pipeline: create one honest fixture/eval that shows the current gap.
- Tooling/library: implement one end-to-end command or API path with tests.

## Guardrails

- Do not import Storybook, doc-web, Dossier, or any other repo wholesale.
- Do not create fake evals, UI scouts, architecture audits, or runtime launchers
  just because the package supports them.
- Do not turn the seed into a chronological mega-spec. Preserve the seed, then
  distill Ideal/spec from it.
- Do not skip the interview unless the user explicitly asks for direct setup.
  Even then, stop for approval when the correct package shape is uncertain.
