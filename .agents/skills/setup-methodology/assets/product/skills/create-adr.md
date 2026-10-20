---
name: create-adr
description: Record a consequential product or technical decision with alternatives, rationale, and consequences
user-invocable: true
---

# /create-adr <number> <short-name> "<title>"

Use an ADR for a hard-to-reverse or widely consequential choice that cannot be
captured clearly as an ordinary story decision. Read `AGENTS.md`, relevant
Ideal/Spec constraints, and existing decisions first.

## Create

1. Confirm the question is open and decision-worthy. Identify whether the
   unresolved issue is a human preference, a technical recommendation, or an
   evidence gap. Do not use an ADR to defer a small reversible implementation.
2. Check existing ADR numbers, names, and overlap. Use the installed
   `.agents/skills/create-adr/scripts/start-adr.sh` helper when available; if
   absent, follow local conventions and do not overwrite existing records.
3. Write context, the decision question, meaningful alternatives including a
   no-change option where relevant, tradeoffs, constraints, references, and
   open questions. Separate facts from assumptions and recommendations.
   Describe why each option is viable and what would make it unsuitable; avoid
   straw alternatives or a decision disguised as an open question.
4. Keep the decision status honest. A proposed ADR is not an accepted decision.
   Leave the choice to the owner when it depends on product direction, taste,
   risk tolerance, or other human judgment.
5. Use research scaffolding only when outside facts could change the decision.
   Verify drift-prone claims from current primary sources; research does not
   authorize provider calls, installs, or implementation.
6. Note affected local surfaces and the kind of follow-up the decision may
   require. Do not claim the decision has propagated until those surfaces are
   updated and checked.
7. Keep the record concise enough that a future reader can find the decision,
   rationale, consequences, and status without reconstructing the discussion.

Show the created path and summarize the unresolved choice. Recommend one local
next route: discussion, evidence gathering, decision, story, or alignment.
Product alignment uses `/align`; do not route through supervisor-only
cross-project skills. Never commit or push unless asked.
