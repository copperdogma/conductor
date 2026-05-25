---
name: skill-surface-audit
description: Audit Conductor and tracked repo SKILL.md surfaces for prompt-budget pressure, duplicate cache copies, repeated repo-local skills, long descriptions, and low-evidence usage without applying cleanup.
user-invocable: true
---

# /skill-surface-audit

Use this when skill count, duplicate skills, plugin-cache copies, long skill
descriptions, or wrong-skill activation may be adding context overhead.

## Workflow

1. Run the report-only helper:

```bash
python3 scripts/skill_surface_audit.py --mode all
```

Useful variants:

```bash
python3 scripts/skill_surface_audit.py --mode active
python3 scripts/skill_surface_audit.py --mode portfolio --no-logs
python3 scripts/skill_surface_audit.py --mode all --output /tmp/skill-surface-audit.md
python3 scripts/skill_surface_audit.py --mode all --format json
```

2. Read findings in this order:
   - budget pressure
   - root summary and root confidence
   - plugin-cache cleanup candidates
   - repeated repo-local names and body hashes
   - long description candidates
   - low usage evidence candidates

3. Before recommending cleanup, classify each finding:
   - `keep`
   - `shorten`
   - `disable`
   - `delete candidate`
   - `no action`

## Guardrails

- Report first; do not delete, disable, or rewrite skills from the audit alone.
- Treat plugin cache paths as cache evidence, not proof that Codex loaded them.
- Preserve trigger nouns when shortening descriptions.
- Treat repo-local duplicate skills as distributed ownership by default.
- Create target repo inbox notes or stories only for high-confidence local
  cleanup candidates with a concrete failure mode.
