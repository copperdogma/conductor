---
name: triage
description: Choose the highest-leverage next supervisor action to reduce cross-project busywork
user-invocable: true
---

# /triage [stories|inbox] [sub-arg]

> Alignment check: Before choosing an approach, verify it aligns with
> `docs/ideal.md`, `docs/methodology-ideal-spec-compromise.md`,
> `docs/spec.md`, `docs/methodology/state.yaml`, and
> `docs/methodology/graph.json`. If the recommendation touches a settled
> workflow choice, read the relevant record in `docs/decisions/`. If none
> apply, say so explicitly.

`/triage` is the proactive supervisor meta-skill. Its job is to choose the one
next action that most reduces recurring cross-project busywork or converts raw
supervisor pressure into durable ready work.

The required order is:

1. Ideal — what repeated comparison, routing, or research burden is costing the
   most operator time right now?
2. Spec / state — which supervisor lane owns it: registry-routing, alignment,
   scouting, story-prep, or memory?
3. Existing work — which inbox items, stories, alignment records, or scout
   records already advance that exact pressure?
4. Action shape — what is the smallest honest artifact that moves it forward:
   inbox processing, alignment pass, scout mission, story continuation, new
   story, or no-op?

Unlike the product repos, inbox pressure is a first-class signal here because
`inbox.md` is the actual supervisor intake surface. But inbox volume still does
not outrank higher-leverage work automatically; prioritize the pressure that
removes the most repeated work, compresses the most human judgment, or creates
the clearest reusable memory.

## Routing

- `/triage` — full-sweep read-only recommendation
- `/triage stories` — delegate to `/triage-stories`
- `/triage inbox` — process the inbox into the right supervisor artifacts
- `/triage inbox scan` — read-only inbox routing report

When a scope is provided, hand off completely to the leaf skill. Do not keep a
second implementation here, except for `inbox`, which is owned directly by this
skill.

## Leaf Skills

- `/triage-stories` — backlog prioritization and story-line continuity

`/align-projects` and `/scout` remain specialized supervisor lanes, not triage
leaf skills. Unscoped `/triage` may recommend either of them as the next move
when that is the most honest first artifact.

## Inbox mode

Use `/triage inbox` or `/triage inbox scan` when the honest next move is to
route raw capture in `inbox.md`.

### Steps

1. Read `inbox.md`.
2. For each live item, search:
   - `docs/stories/`
   - `docs/scout/`
   - `docs/alignments/`
   - `docs/decisions/`
3. Classify the item:
   - stale
   - live
   - partially handled
4. Choose the right landing zone:
   - existing story
   - new story
   - scout mission
   - alignment pass
   - ADR
   - reject / defer

### `scan` mode

Return a compact report only. Do not edit files.

### Processing mode

After user confirmation:

- create or update the right artifact
- remove or rewrite the processed inbox item
- keep `inbox.md` short, current, and truly raw
- avoid creating a story when a scout or alignment pass is the more honest
  first move

## Full-sweep mode

When invoked with no scope, run a supervisor-first orchestration pass.

1. **Read the shared frame**
   - `docs/ideal.md`
   - `docs/methodology-ideal-spec-compromise.md`
   - `docs/spec.md`
   - `docs/methodology/state.yaml`
   - `docs/methodology/graph.json`
   - `projects.yaml`
   - `inbox.md`
   - `docs/scout.md`
   - `docs/align-projects.md`
   - recent `git log --oneline -20`
   - Goal: identify the highest-leverage supervisor pressure before treating
     existing artifacts as a backlog.

2. **Name the primary supervisor pressure**
   - State the pressure in plain language
   - Map it to the owning spec section(s)
   - Map it to the owning state category and phase
   - State why it wins right now. Common reasons:
     - multiple projects likely benefit
     - same comparison or research will otherwise be repeated
     - stale inbox capture is blocking honest routing
     - an existing supervisor work line is close to producing durable leverage
     - a human decision can be narrowed substantially by one comparison pass
   - Also name 1-2 runner-up pressures

3. **Read the decision and memory constraints for that pressure**
   - Open the relevant decision record(s), if any
   - Read the relevant alignment or scout entry when the pressure continues an
     existing line
   - If no decision record applies, say so explicitly

4. **Query the existing work under that pressure**
   - Stories: `/triage-stories`
   - Inbox: `/triage inbox scan`
   - Alignment memory: inspect the relevant entry or confirm that comparison
     history is missing
   - Scout memory: inspect the relevant entry or confirm that source memory is
     missing
   - Interpret each source through one question:
     - what already exists that advances this exact pressure?
   - Do not let a convenient story shell or a novel inbox item outrank the
     chosen pressure just because it is easier to start

5. **Choose one next action**
   Prefer this order:
   - continue the active story, alignment, or scout line that directly reduces
     the chosen pressure
   - process or rewrite the inbox when raw capture debt is the real bottleneck
     and the honest first move is routing, not execution
   - run `/align-projects` when the pressure is unexplained cross-project drift
     or a shared methodology change that needs comparison
   - run `/scout` when the pressure is an unevaluated external source with
     likely multi-project or repeated value
   - create or promote a story when the work now needs a durable execution home
   - recommend `no-op` only when no candidate is honestly actionable yet
   - when leverage is otherwise comparable, prefer the action that creates the
     clearest reusable memory with the least extra structure

6. **Return one compact report**
   - End with a direct yes-ready handoff sentence
   - A bare `yes` should be enough to authorize the one recommended action on
     the next turn

## Output

```markdown
## Triage

### Primary Pressure
- {cross-project busywork / routing / research pressure}
- Spec: {spec refs}
- State: {category + substrate + phase}

### Recommended Action
- ...

### Kickoff
- ...

### Why
- ...
- ...

### Runner-Ups
- ...
- ...

### Lane Notes
- Stories: ...
- Inbox: ...
- Alignment: ...
- Scout: ...

### Health Flags
- ...

### Decision
- Reply `yes` to proceed with: ...
```

## Guardrails

- Scoped invocations delegate. Do not duplicate leaf logic here.
- `inbox` is the one scoped mode owned directly by this skill.
- Unscoped `/triage` is read-only.
- Recommend one next action, not a grab bag.
- Prefer the smallest honest artifact that reduces repeated work.
- Do not optimize Conductor's internal tidiness over leverage for the tracked
  projects.
- Do not create a story when an alignment pass, scout mission, or inbox-routing
  step is the more honest first artifact.
- Do not recommend target-project execution as "the next step" unless
  Conductor's supervisor-side preparation is already in place or genuinely
  unnecessary.
- Treat stale inbox pressure as real, but do not churn through low-value items
  just to empty the inbox.
- Prefer continuing a coherent active line when leverage is comparable, but do
  not let continuity override a clearly higher-leverage supervisor move.
