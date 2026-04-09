---
name: align-projects
description: Compare infrastructure surfaces across tracked projects and recommend what should sync
user-invocable: true
---

# /align-projects [optional focus]

Use this to compare shared-ish infrastructure surfaces across the tracked projects.

## Typical surfaces

- `AGENTS.md`
- `docs/ideal.md`
- `docs/spec.md`
- `docs/methodology-ideal-spec-compromise.md`
- `docs/methodology/state.yaml`
- `docs/methodology/graph.json`
- `docs/build-map.md`
- `docs/setup-checklist.md`
- `docs/runbooks/setup-methodology.md`
- `docs/scout.md`
- `docs/scout/`
- `docs/decisions/`
- `.agents/skills/`
- story templates
- skill sync tooling
- setup or methodology docs

## Steps

1. Read `projects.yaml` to identify the projects and comparison surfaces.
2. Choose the relevant surface area for this pass.
3. Compare the source and target projects.
4. Classify each important difference:
   - intentional adaptation
   - portable improvement
   - methodology conflict
   - unclear drift
5. Recommend per project:
   - sync now
   - sync partially
   - keep local
   - ask for a decision
6. Write an alignment entry under `docs/alignments/`.
7. Update `docs/align-projects.md`.
8. If warranted, create follow-up stories.

## Output shape

- surfaces compared
- key differences
- classification of those differences
- recommended next action by project
- what still needs human judgment

## Guardrails

- Do not force exact textual identity.
- Do not treat local product-specific adaptation as accidental drift by default.
- When methodology intent truly conflicts, surface it clearly and ask whether it should converge.
