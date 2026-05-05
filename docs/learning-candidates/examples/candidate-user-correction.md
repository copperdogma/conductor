# Example - Candidate Warranted From User Correction

## Episode

During a Conductor closeout, Cam corrected the agent for treating a target
project's primary checkout as safe to edit even though Conductor guardrails
require isolated target-project worktrees for supervisor upgrades.

## Learning Review Output

```text
RESULT: candidate-warranted
Target surface: .agents/skills/build-story/SKILL.md
Trigger class: user-correction
Evidence: Conductor closeout thread for the target-project edit; Cam corrected
the agent for treating a primary target-project checkout as safe for
supervisor-driven edits; build-story target-project isolation guardrail was
missed before edits started.
Proposed change: Add an explicit pre-edit target-project checkout gate to
/build-story so target repo status is inspected and an isolated worktree is
chosen before any supervisor-driven target edit.
Promotion gate: Cam accepts that this should become a build-story rule rather
than remaining a one-off correction.
Confidence: high
Next step: run /learning-candidate to draft the candidate; do not promote during
the same closeout.
```

## Draft Shape

A candidate file would be created under `docs/learning-candidates/` with
`status: "Proposed"` if the correction is explicit enough to ask for an
accept/dismiss decision immediately. It would not edit `/build-story` until
promotion is explicitly approved. Its review cadence would be "review now"
because the trigger is a direct user correction with a concrete target surface.

Candidate storage would include the target surface, source run, correction
summary, evidence summary, proposed change, review cadence, and promotion gate
before asking for a decision. Promotion remains a separate approved action: this
example can create or update a `Proposed` candidate, but it cannot edit
`/build-story` until Cam first accepts the evidence and then separately approves
promotion from `Accepted` to `Promoted`. After promotion, the candidate is
terminal and re-running promotion must report no live changes.
