---
name: triage-adr
description: Review an existing product ADR and identify what remains decided, open, unsupported, or ready to align
user-invocable: true
---

# /triage-adr [ADR path or identifier]

Use when an existing decision record's maturity or next action is unclear. This
is advisory and read-only; it does not decide, rewrite, or create the ADR.

## Read and classify

1. Read the named ADR and its linked evidence. Then read relevant Ideal/Spec,
   state/graph, stories, and local decisions. Do not summarize from memory.
2. Classify each remaining issue as settled, human preference/product
   direction, technical recommendation, evidence gap, integration gap, blocked,
   or stale/superseded.
3. Recommend a technical path when the choice is mainly technical and evidence
   suffices. Ask only for genuine owner judgment; name the consequence of the
   choice. Use research when facts are missing and `/ideation` when option
   quality—not evidence—is the blocker.
4. Check whether the decision has been reflected in local specs, stories,
   methodology views, or agent guidance. Recommend `/align` for local
   consistency work when needed.

## Output

```markdown
## ADR Triage — {record}
- Maturity and evidence: ...
- Settled decisions: ...
- Human decisions: ...
- Technical recommendation: ...
- Evidence or integration gaps: ...
- Recommended next route: ...
```

Choose one primary next route: continue discussion, make a recommendation, do
research, improve options, update the ADR, create/adjust a story, align local
surfaces, accept/reject, or mark superseded. Do not route product work through
Conductor's `/align-projects` or other supervisor-only lanes.
