---
name: build-story
description: Implement a product story through a reviewed plan, bounded changes, and applicable evidence
user-invocable: true
---

# /build-story [story-id]

Implement a product story within its accepted scope. The owning repository's
`AGENTS.md`, privacy rules, tools, and acceptance contract take precedence.

## Explore and plan

1. Read the story, relevant Ideal/Spec/state/graph, and linked decisions.
   Verify prerequisites and substrate in the repository, not only in planning
   records. Check workspace state and protect unrelated changes.
2. For a change to a drift-prone interface, verify current primary
   documentation. For an unfamiliar material obstacle, diagnose the general
   problem class, consult a few established sources, and choose a small local
   applicability check before adding retries or special cases. Reuse existing
   research and record useful provenance and uncertainty.
3. Write a concrete plan in the story: changes, outputs, inspection, checks,
   external facts needed, risks, and stop conditions. State whether it is ready,
   needs human judgment, or is blocked.
4. Pause for plan approval before implementation unless existing explicit
   authorization already covers the bounded plan. If scope, risk, access, or
   verification assumptions change, pause and update the plan.

## Implement and hand off

- Keep changes within the approved story. Prefer the smallest complete outcome
  and inspect actual outputs, not only command success.
- Delegate only when useful and authorized. After the plan gate, assign bounded,
  disjoint work; the main thread owns integration, scope, and final judgment.
- Revisit research when a new material uncertainty or repeated failure appears.
- Run the narrowest applicable checks from `AGENTS.md` and the story; include
  mandatory repository gates and evidence for changed behavior. Do not claim
  product acceptance from compile, lint, or fixture structure alone.
- Update the work log with concrete results and residual uncertainty. Leave
  validation and completion gates honest; recommend `/validate` when ready.

Do not commit, push, deploy, or change external accounts unless separately
authorized. End with what changed, what evidence applies, remaining risks, and
one yes-ready next step.
