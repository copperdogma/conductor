# Product workflow variant

Use this variant when the repository is a product/tool/creative project rather
than the Conductor supervisor. Its package receipt identifies `product`; existing
AGENTS and authored project purpose take precedence over filename heuristics.
Read Ideal, Spec, state, graph, and relevant ADRs before choosing work. Commands
below are the portable bootstrap defaults; retain established repo equivalents.

## triage

Read-only: compare desired outcomes against current evidence before treating
inbox volume or backlog size as priority. Read `docs/inbox.md`, generated
`docs/stories.md` and its authored story sources, eval registry/attempts when
installed, and run `python3 scripts/triage_facts.py --json` when available.
Invalid facts are errors, not evidence that a lane is empty. Optional lanes
marked absent/deferred do not create fake maintenance pressure.

Request up to three neutral candidates from available story, inbox, eval, and
health lanes; include architecture/UI only when active in state with a real
surface. Delegate bounded read-only packets only when permitted and useful;
otherwise gather sequentially. Each packet gives evidence, Ideal/spec value,
why now, next action, stop condition, blockers, and reasons not now. Main-thread
judgment owns the top-three comparison and one final yes-ready recommendation.
Scoped `triage inbox|stories|evals|health` hands off to the relevant installed
leaf. Full triage does not run provider calls, audits, fixes, or artifact creation.
Avoid repeating unchanged evals or low-value housekeeping. Quality and actual
user benefit outrank proxy speed, cost, and activity metrics.

## triage-stories

Read the graph/index, then relevant authored stories and their evidence. Identify
the highest-leverage actionable problem and whether it should continue an
existing story, create one, use a smaller action, or wait. Compare Ideal/spec fit,
readiness, dependencies, continuity, impact, and proof. IDs do not imply priority.
In full-triage packet mode return neutral candidates and stop conditions only;
in direct mode give a ranked recommendation and one next step. Stay read-only.

## scout

Investigate an external source for this project's needs. Prefer a relevant
source connector; verify drift-prone external facts against current primary
documentation. Separate external advice from local applicability and proof.
Read existing research first, then record reusable sources, the decision,
uncertainty and smallest local experiment in `docs/research/` or the project's
existing research surface. Classify adopt/adapt/defer/reject/spike. Do not install
or copy outside code, change dependencies, start provider work, or modify runtime
defaults merely because research recommends it. Check local reuse restrictions.

## Story loop and evidence

Use `/create-story` for a coherent outcome that needs its own acceptance and
proof; use small direct work when a story adds no value. `/build-story` owns
scope and the human plan gate, then may delegate bounded disjoint work.
`/validate` checks findings, current acceptance, and applicable evidence before
closure; `/mark-story-done` never hides unmet work. Use `/finish-and-push` only
when landing is requested. Product suites are project-owned additions to the
cheap package checks, not replaced by them.

State categories align to authored `spec:N` headings. The bootstrap compiler
accepts JSON syntax in `state.yaml` (valid YAML), as used by the source product
repos. It is intentionally a small projection, not a replacement for an
established richer compiler. Preserve an existing compiler and its schema on
retrofit; record adaptations instead of overwriting them.

## Sparse setup

Author state from the reviewed Ideal/Spec; never derive a generic Ideal from a
template. Start with real categories and zero invented completed stories. A
root eval/golden may be deferred with a reason and a concrete next trigger when
there is no runnable product path. Install evidence guidance where relevant but
do not manufacture a green score or call an empty fixture folder a golden.
Architecture/UI/codebase lanes stay absent/deferred until there is a real
surface. If a runtime or dependencies exist, use the runtime/dependency reference
and adapt project launch/bootstrap commands rather than treating them as proven.
