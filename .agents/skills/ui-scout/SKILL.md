---
name: ui-scout
description: Assess an implemented user interface through real runtime screenshots and observed interaction
user-invocable: true
---

# /ui-scout [area]

Use for a qualitative review of an interface that actually runs. Gather visual
evidence before judging it; do not invent screens or treat mockups as runtime
proof.

## Steps

1. Read `AGENTS.md`, the relevant Ideal/Spec and prior UI findings, if present.
2. Locate the repo's documented launch path and start only the required local
   app or use an already running instance. Do not guess a command or deploy.
3. Capture a screenshot of the real rendered UI before interaction. Record the
   route/screen, viewport, runtime state, and any setup needed to reach it.
4. Inspect the screenshot for hierarchy, readability, affordances, consistency,
   accessibility cues, and fit with the target user's task. Then exercise a
   small number of relevant real interactions and capture resulting evidence.
5. Separate observed defects from hypotheses. Do not claim a control works from
   appearance alone or infer unseen states from a static screenshot.
6. Review the flow from the user's task, not from source structure. Note the
   action attempted, visible feedback, and whether recovery is clear.
7. Keep the review bounded to the requested area and the few interactions that
   distinguish its main usability questions.
8. Avoid broad claims about accessibility from visual inspection alone; mark
   keyboard, assistive-technology, and other untested behavior as unverified.

## Full-triage packet mode

When `/triage` requests a packet, use current screenshots/reports or a bounded
real-runtime observation for up to three neutral UI candidates. Include
evidence, product value, why now, next action, stop condition, blockers, and
reasons not now. Do not choose a lane winner, write a kickoff, or make the
overall project recommendation. Direct invocation may recommend one next move.

## Limits and report

If no real runtime can be launched or reached, report the blocker and defer the
visual assessment. Do not substitute fabricated UI, generated screenshots, or
source-only guesses.

Return a concise report with: runtime and screens observed; screenshot paths;
strongest findings with evidence and user impact; accessibility concerns;
unobserved states; and one recommended next step. Do not edit the interface in
this skill unless separately asked to implement a finding.
