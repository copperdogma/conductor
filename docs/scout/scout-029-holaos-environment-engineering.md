# Scout 029 - Evaluate holaOS Environment Engineering for Workflow Learning

**Source**: `https://x.com/LunarResearcher/status/2050510337737154984`, `https://x.com/i/article/2050464055144468480`, `https://github.com/holaboss-ai/holaOS`, `https://www.holaos.ai/docs`
**Status**: Adapt
**Reviewed**: 2026-05-05
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge, boardgame-ingester, roborally, echo-forge

## Summary

The LunarResearcher article frames holaOS as "environment engineering": the
durable environment around an agent should own memory, continuity, capability
visibility, app wiring, outputs, and learning, while the harness remains a
swappable execution layer. That framing is close to Cam's existing
harness-agnostic workflow, but holaOS is not just a blog post. The public repo
contains a real local runtime, Electron desktop shell, SQLite state store,
workspace filesystem contract, memory service, output/artifact model,
capability projection layer, cron/subagent execution path, app lifecycle model,
and a conservative evolve loop that drafts memory and skill candidates.

The right decision is not to switch Conductor or the tracked projects over to
holaOS. The current workflow already has the most important part of the thesis:
distributed project ownership, repo-local instructions, durable stories,
validation surfaces, memory, and explicit human review. Porting that into
holaOS would trade a lightweight distributed harness for a much larger runtime,
Electron shell, Pi harness assumptions, app marketplace model, hosted model
proxy assumptions, and early-stage operational risk.

The useful move is selective borrowing. holaOS gives strong names and code
examples for ideas that should improve Conductor's existing supervisor method:
environment-contract vocabulary, per-run capability manifests, coordinator vs
worker capability projection, durable output/artifact records, generated
capability registry state, and the learning loop's review boundary.

The most interesting "learning" piece is real but narrower than the article's
marketing language. holaOS can draft reusable skill candidates from completed
runs on a cadence, store them separately, raise a task proposal, and only
promote a live skill after an accepted review session. That is exactly the
boundary Conductor should preserve: learn by drafting inspectable candidates,
not by silently rewriting live skills or standing project policy.

## Retrieval Notes

- The Conductor Twitter connector found the tweet and article metadata, but
  direct thread/reply retrieval hit a URL-metadata error. I resolved the
  `t.co` link and used the article target plus the public repository/docs.
- The article said the repo had about 3.7k stars. Live GitHub search on
  2026-05-05 showed about 4.7k stars and a latest release dated 2026-05-03, so
  the article's star count is already stale.
- The repo was cloned read-only for this scout at commit
  `0c2dddefe2eb1936ecb7d88b9ded32a3dff59132`.
- A bounded `/loop-verify` evidence pass used five read-only shards:
  workspace/memory/continuity, runtime/harness/capabilities,
  desktop/app/browser/bridge, self-evolution/skills, and
  packaging/security/operational risk. All shards returned `RESULT: no-issue`
  with no file edits.

## How holaOS Works

### Environment Contract

holaOS separates a durable environment from the harness that executes a run.
The public docs define the harness as the execution subsystem and the
environment as the durable operating context around it. The docs explicitly
ask the harness-swap question: if the harness changed tomorrow, what should
still remain true?

The environment contract is described as four layers:

- durable authored state: workspace structure, app manifests, skills, commands,
  standing instructions
- durable adaptive state: memory, outputs, traces, feedback, reviewed
  improvements
- runtime continuity state: turn results, snapshots, checkpoints, warm context
- projected execution state: visible/callable surface, model routing,
  attachments, MCP visibility, permissions, run metadata

This is highly aligned with Conductor's own framing. Conductor already treats
repo-local `AGENTS.md`, skills, stories, scout logs, alignment logs, and
methodology state as the durable environment around whatever harness is being
used in the moment.

### Workspace And State Model

The holaOS workspace model is concrete. A workspace has authored surfaces such
as `workspace.yaml`, `AGENTS.md`, `ONBOARD.md`, `skills/`, and `apps/`.
Runtime-owned state lives separately in `.holaboss/`, `state/runtime.db`, and
an OS-global `memory/` root.

The SQLite store is substantial. It includes workspaces, sessions, runtime
state, queued inputs, post-run jobs, turn results, request snapshots, memory
entries, memory update proposals, evolve skill candidates, outputs, output
folders, cronjobs, notifications, and subagent runs. That state store is the
runtime's execution truth; markdown memory and authored workspace policy are
kept separate.

The strongest borrowable design here is the separation, not the schema itself:

- authored policy belongs in files humans can review
- execution truth belongs in a durable runtime record
- runtime continuity should not be treated as durable knowledge
- durable memory should be indexed, typed, and provenance-aware

### Run Lifecycle

The runtime is a local Fastify orchestration server. It exposes runtime config,
workspaces, apps, sessions, queued inputs, output streams, background tasks,
cronjobs, terminal sessions, browser capability routes, and runtime-tool
capability routes.

The execution path is process-based:

1. API routes enqueue session input records.
2. A queue worker claims runnable inputs with bounded concurrency.
3. `NativeRunnerExecutor` shells out to the TypeScript runner with a base64
   request payload.
4. The runner prepares workspace state, model routing, capabilities, MCP
   payloads, prompt layers, and a reduced execution package.
5. The runner launches a harness-host process and relays JSONL events.
6. Completed turns persist `turn_results`, request snapshots, outputs, and
   post-run jobs.

This is a serious orchestration runtime, not a lightweight prompt harness. It
is also more machinery than Conductor needs today.

### Harness Boundary

The harness abstraction exists, but the current open-source implementation is
effectively one harness. The runtime/harness registries point at `pi`, and a
lot of code assumes that path. The plugin shape is useful, but the current repo
does not prove broad harness portability across Codex, Claude Code, and other
real harnesses.

Conductor should borrow the boundary language, not the harness implementation.
The current distributed workflow is already more harness-agnostic in practice
because each project owns its own instruction and validation surfaces rather
than depending on one central execution host.

### Capability Projection

Capability projection is one of the strongest implemented ideas. holaOS builds
a per-run capability manifest with explicit kinds, policies, trust levels,
authority boundaries, concurrency behavior, visibility, MCP aliases, and a
fingerprint. It also filters capabilities by session shape: main/coordinator
sessions do not get the same direct browser and MCP access as delegated
subagent sessions.

This maps directly to Conductor. Conductor often needs to keep the main thread
as the north-star arbiter and delegate bounded shards to subagents. A durable
capability manifest for a story or loop-verify run could reduce accidental
tool-surface drift and make handoffs more reviewable.

### Memory And Evolve

holaOS has a typed durable-memory model: preference, identity, fact, procedure,
blocker, and reference. It distinguishes:

- `state/runtime.db` for execution truth and catalog metadata
- `memory/workspace/<workspace-id>/runtime/` for volatile runtime projections
- `memory/workspace/<workspace-id>/runtime/session-memory/` for
  resume-oriented snapshots
- `memory/workspace/<workspace-id>/knowledge/` for durable workspace memory
- `memory/preference/` and `memory/identity/` for user-scoped memory

Durable memory writeback is conservative. Completed turns enqueue an `evolve`
job. The evolve worker performs deterministic and optional model-assisted
durable extraction, writes markdown leaves and catalog rows, and refreshes
indexes only for changed scopes. User preference/profile updates stay behind a
proposal/acceptance path instead of being silently written by the queued
evolve pass.

The skill learning path is the most relevant part for Cam:

- skill review runs on a completed-turn cadence and requires a background
  model
- the model is asked to propose only reusable workspace-local skill candidates
- drafts are written under memory, not live `skills/`
- candidate metadata is stored in `state/runtime.db`
- candidates become task proposals
- only an accepted review session can promote the draft into live
  `skills/<slug>/SKILL.md`

That is the right governance shape. The term "auto-promote" is misleading if it
means "live behavior changes automatically." The code supports auto-drafting
and proposing; live promotion still has a human/review boundary.

### Continuity Gap

The continuity story is partly implemented and partly overstated. Runtime APIs
can expose sessions, runtime state, history, turn results, request snapshots,
and resume context from session-memory files when those files exist. However,
the implementation-focused `docs/runtime-post-run-evolve-stage.md` and tests
show that the foreground post-run/evolve path does not consistently write
runtime continuity or `runtime/session-memory` files. This conflicts with the
public docs' stronger claim that immediate writeback refreshes session memory.

For Conductor, this is a caution: do not borrow claims about automatic
continuity unless the write path and restoration path are both tested. The
idea is good; the specific implementation evidence is not yet fully coherent.

### Apps, Bridge, Outputs

holaOS models apps as durable capability units. A workspace declares apps in
`workspace.yaml`; each app has an `apps/<id>/app.runtime.yaml` manifest with
lifecycle, ports, health checks, environment contracts, integrations, and MCP
tools. Runtime install/startup can reconcile the workspace MCP registry so
durable tools appear as `app.tool` ids rather than ad hoc UI state.

The bridge SDK is also worth noticing. It wraps brokered integration calls,
workspace outputs, turn-scoped artifacts, turn-context recovery, resource
presentation, and workspace DB access. Its output helpers return `null` when
publishing is unavailable in local development instead of pretending success.

For Conductor, the output/artifact pattern is more useful than the whole app
model. Scout and alignment work already produces durable markdown artifacts;
future tooling could make those artifacts first-class records with source,
status, owning story, provenance, and review state.

### Browser And Operator Surface

The Electron desktop shell is a real local runtime host. It creates persistent
browser partitions per workspace, keeps separate user and agent browser spaces,
and exposes authenticated localhost browser automation routes with workspace,
session, input, and browser-space headers. E2E tests cover localStorage
isolation across workspace switches and relaunches.

The operator-surface context is a strong idea: the shell reports browser/app
editor surfaces into runtime context, and the prompt can use that context for
references like "this page" or "here." Conductor does not need a desktop shell,
but it could borrow the principle when reasoning about active local validation
surfaces.

### Cron And Background Work

Cron/background execution is first-class. Agent-created cronjobs persist
schedules and delivery settings; due jobs either create notifications or queue
subagent session runs. Those runs are tracked as child sessions/subagent runs
with tool profiles, model selection, status, and ownership.

This confirms the same task-shape boundary already recorded in Conductor's
Symphony scout: unattended execution is most credible for objective,
golden-backed, low-opinion work. High-taste UI and manual-verifier workflows
should stay interactive.

## Maturity And Risk

The repo is impressive but early-stage:

- The open-source runtime is tightly coupled to the Pi harness path.
- Desktop/runtime packages are around `0.1.0`; SDK packages are early.
- Platform support is uneven: macOS is the supported desktop path while
  Windows/Linux are still in progress or optional in release CI.
- Installer/docs are inconsistent: README points at `holaboss-ai/holaOS` and
  Node 24.14.1, while `INSTALL.md` and `scripts/install.sh` still reference
  `holaboss-ai/holaboss-ai` and older Node assumptions.
- The install script downloads Node without a full archive checksum
  verification step.
- Standalone runtime bootstrap can bind to `0.0.0.0`, which is risky if copied
  into local development without an auth/network boundary.
- The migration registry is sparse; much of the state-store upgrade behavior
  is still in ensure/migration helper code rather than a mature versioned
  migration system.
- The docs have some path and continuity inconsistencies, especially around
  OS-global memory vs workspace-local memory and automatic session-memory
  writeback.
- Security disclosure exists but is minimal.

These are not reasons to ignore the repo. They are reasons not to make it the
base layer for Cam's current workflow.

## Project Relevance

- **conductor**: `Adapt`. Strong fit as methodology reference. Borrow
  environment-contract vocabulary, capability manifests, candidate promotion
  lifecycle, output/artifact records, and coordinator-vs-worker capability
  projection. Do not adopt the runtime wholesale.
- **dossier**: `Defer`. Dossier could later use the evolve/candidate-review
  pattern for extraction-loop learning, but current pressure should stay in
  repo-local eval stories and existing memory/scout surfaces.
- **storybook**: `Defer`. Storybook already has product-specific methodology
  and memory concerns. The useful future idea is candidate skill/memory review,
  not an app/runtime switch.
- **doc-web**: `Defer`. The durable output/artifact model may be relevant to
  document conversion artifacts, but doc-web should not depend on a holaOS
  runtime.
- **cine-forge**: `Defer`. Cron/subagent patterns may fit future
  golden-backed eval or render-lane hillclimbs. High-taste scene/UI work should
  remain interactive.
- **boardgame-ingester**: `Defer`. The artifact/output and eval-trace
  vocabulary could help later, but the repo's current ingestion substrate does
  not need a new runtime.
- **roborally**: `Reject for now`. The private proof-of-concept game should
  keep authoritative game truth headless and avoid adding an external agent OS
  layer.
- **echo-forge**: `Defer`. Echo Forge may eventually benefit from durable app
  capability and output records, but current product shaping does not warrant a
  runtime switch.

## Decision

Keep this scout as `Adapt`.

Do not switch to holaOS. Do not port Cam's existing distributed workflow into
holaOS. Do not install or depend on the runtime as part of Conductor.

Borrow these ideas into the existing workflow instead:

1. **Environment contract vocabulary** - explicitly name authored policy,
   runtime truth, durable memory, continuity, capabilities, outputs, and
   review boundaries in Conductor guidance.
2. **Learning with review** - candidate memories/skills should move through
   `draft -> proposed -> accepted -> promoted`; dismissed candidates stay
   terminal unless fresh evidence reopens them. Accepted candidates can be
   dismissed only before promotion when Cam explicitly reverses acceptance, and
   promoted candidates are terminal/idempotent. Candidates should never move
   straight into live behavior.
3. **Per-run capability manifests** - record the actual tool/capability surface
   available to main vs worker/subagent runs, with enough fingerprinting to
   debug drift.
4. **Coordinator-vs-worker projection** - main Conductor threads should retain
   north-star judgment; workers get bounded tool surfaces appropriate to their
   shard.
5. **Durable outputs/artifacts** - scout, alignment, eval, and proof packets
   should be first-class inspectable records, not only freeform markdown
   blobs.
6. **Capability units** - if a project capability grows beyond a script or
   MCP tool, treat it as an explicit installed capability with health,
   lifecycle, registry, and output contracts.
7. **Browser/workspace isolation** - if Conductor later manages browser
   validation state, isolate it per project/workspace and make the operator
   surface explicit.

## Recommended Follow-Up

Follow-up created as
[Story 008 — Add Reviewed Learning Candidate Workflow](../stories/story-008-reviewed-learning-candidates.md).

The story should build the reviewed-learning part first, not the whole
environment-contract list. It should compare current Conductor/skill surfaces
against the narrower borrowed idea and produce one of:

- a small Conductor alignment note if the ideas are already mostly covered
- targeted skill wording updates if the review-boundary language is weak
- a lightweight schema/proposal for future capability manifests or artifact
  records if the current surfaces are missing a real need

At scout time, this was not ready to fan out to target projects. Conductor
needed to first decide which borrowed ideas were genuinely portable and how they
fit the existing distributed methodology. Story 008 later did that
Conductor-local review, and Alignment 024 now records Cam's approved
tracked-repo rollout scope; that rollout still requires isolated target
worktrees, repo-local validation, and loop verification before it can be called
complete.

## Evidence

- X article: `https://x.com/i/article/2050464055144468480`
- Tweet: `https://x.com/LunarResearcher/status/2050510337737154984`
- Repo: `https://github.com/holaboss-ai/holaOS`
- Docs: `https://www.holaos.ai/docs`
- Repo commit reviewed: `0c2dddefe2eb1936ecb7d88b9ded32a3dff59132`
- `website/docs/content/docs/concepts/environment-engineering.mdx`: defines
  harness vs environment, hot/warm/cold context, durable authored/adaptive
  state, runtime continuity, projected execution state, and reviewed
  improvement boundaries.
- `website/docs/content/docs/concepts/workspace-model.mdx`: defines
  `workspace.yaml`, `AGENTS.md`, `skills/`, `apps/`, `.holaboss/`,
  `state/runtime.db`, OS-global `memory/`, and run compilation.
- `website/docs/content/docs/concepts/memory-and-continuity/*.mdx`: defines
  durable memory, runtime continuity, recall, evolve, and human review
  boundaries.
- `runtime/state-store/src/store.ts`: implements turn results, request
  snapshots, memory entries, task proposals, evolve skill candidates,
  cronjobs, outputs, notifications, sessions, and subagent runs.
- `runtime/api-server/src/evolve.ts`,
  `runtime/api-server/src/evolve-worker.ts`, and
  `runtime/api-server/src/evolve-skill-review.ts`: implement queued evolve
  jobs, durable-memory writeback, skill candidate review, task proposal
  creation, and reviewed skill promotion.
- `runtime/api-server/src/agent-capability-registry.ts`: implements per-run
  capability manifests and fingerprints.
- `runtime/api-server/src/runner-prep.ts`,
  `runtime/api-server/src/ts-runner.ts`, and
  `runtime/harness-host/src/*`: implement workspace runtime preparation,
  MCP sidecar/aliasing, harness-host execution, and event relay.
- `runtime/api-server/src/cron-worker.ts`: implements cron delivery as
  notifications or queued subagent runs.
- `desktop/electron/browser-pane/*` and
  `desktop/e2e/browser-workspace-isolation.test.mjs`: implement and verify
  per-workspace browser state isolation and authenticated browser capability
  routing.
- `website/docs/content/docs/build/apps/*.mdx`,
  `runtime/api-server/src/workspace-apps.ts`, and `sdk/bridge/src/*`:
  implement app manifests, MCP registry reconciliation, bridge integration
  helpers, workspace outputs, and turn-scoped artifacts.

## Confidence

High for the top-level decision: selectively borrow ideas, do not switch or
port the current workflow. The repo evidence is broad and the loop-verify
shards agreed across independent areas.

Medium for exact implementation maturity. I did not run the holaOS test suite
or launch the desktop/runtime. The evidence pass was source and docs based.
Several implementation/doc mismatches were visible enough that any future
adoption story should re-check the specific target area before copying code.

## Open Questions

- Should Conductor add a lightweight capability-manifest record to story or
  loop-verify runs, or is that too much overhead until a concrete failure
  appears?
- Should Conductor's memory/skill workflow gain an explicit
  draft/proposed/accepted/promoted vocabulary?
- Which Conductor artifact should own future "environment contract" guidance:
  an alignment note, a skill update, or a methodology doc update?
- Can the existing memory system already capture most of this without new
  repository artifacts?
