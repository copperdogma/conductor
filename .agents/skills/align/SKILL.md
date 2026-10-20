---
name: align
description: Check whether changed local project documents and generated views still express one coherent methodology
user-invocable: true
---

# /align [what-changed]

Review local consistency after a meaningful change to product direction,
constraints, planning state, evidence, workflow, or agent guidance. This skill
is repository-local; it does not compare or edit other repositories.

## Steps

1. Read `AGENTS.md` and the relevant local decision records.
2. Inspect the changed surface and its declared neighbors. Common surfaces are
   the Ideal, Spec, methodology state/graph, generated story index, story files,
   evaluations, runbooks, and agent instructions. Not every repository has all
   of these; report unavailable surfaces instead of inventing them.
3. Check that meaning agrees across sources: product intent, active constraints,
   current status, ownership, evidence, and generated views.
4. Check source ownership: generated files should point back to their writable
   source; local exceptions should have an explicit reason where needed.
5. Recommend only the smallest corrections needed to restore consistency.
   Do not make edits unless the user separately asks for them.

## Report

```markdown
## Local Alignment
- Change reviewed: ...
- Surfaces that agree: ...
- Conflicts or stale references: ...
- Missing/deferred surfaces: ...
- Recommended corrections: ...
```

Separate confirmed contradictions from possible drift. Do not treat every
project-specific difference as an error, promote an implementation detail into
product intent, or claim generated output is current without checking it.
