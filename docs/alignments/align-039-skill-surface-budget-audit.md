# Alignment 039 - Skill Surface Budget Audit

**Date**: 2026-05-25
**Classification**: Portable audit helper with local adaptation
**Source**: [Scout 041](../scout/scout-041-skill-cleaner-skill-budget-audit.md)
**Story**: [Story 022](../stories/story-022-skill-surface-budget-audit.md)
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Focus

Turn Scout 041's `skill-cleaner` idea into a Conductor-owned, report-only
skill-surface audit.

The useful distinction is between:

- **active/current roots**: current Conductor worktree skills, Codex user
  skills, and plugin cache contents that may affect the current session
- **portfolio inventory roots**: Conductor plus tracked repo `.agents/skills`
  directories compared as distributed harness surfaces, not as one loaded
  prompt

This alignment records the first run and the routing decision. No target repo
files were edited.

## Implementation

Story 022 added:

- `scripts/skill_surface_audit.py` — report-only Python helper with `active`,
  `portfolio`, and `all` modes, Markdown/JSON output, skill-budget estimates,
  root summaries, duplicate name/body groups, plugin-cache candidates, long
  description candidates, and heuristic log usage evidence.
- `.agents/skills/skill-surface-audit/SKILL.md` — operator-facing wrapper that
  keeps the workflow report-first and forbids deleting, disabling, or rewriting
  skills from the audit alone.

The helper reads `projects.yaml` for tracked repo roots instead of assuming a
`~/Projects` layout. It also labels plugin cache findings as cache evidence,
not proof that every file is model-visible. Usage evidence reads the newest
available logs first, stops at the configured byte cap, and excludes rendered
prompt inventory paths from path-read evidence.

## First Run Summary

Command:

```bash
python3 scripts/skill_surface_audit.py --mode all
```

| Mode | Skills | Full skill tokens | Minimum tokens | Budget tokens | Included | Omitted | Main finding |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| active | 61 | 6,015 | 2,150 | 5,440 | 61 | 0 | Active-like roots exceed full-description budget, mainly due to plugin/cache/user descriptions; 13 plugin install/backup cache copies are cleanup candidates after cache-role verification. |
| portfolio | 246 | 14,516 | 6,614 | 5,440 | 202 | 44 | Portfolio roots are too large to think of as one prompt; repeated repo-local skill names/bodies are expected distributed ownership, not deletion proof. |

Other first-run counts:

| Mode | Log files read | Duplicate names | Duplicate bodies | Long descriptions | Low usage evidence |
| --- | ---: | ---: | ---: | ---: | ---: |
| active | 36 | 13 | 12 | 17 | 0 |
| portfolio | 36 | 39 | 23 | 12 | 5 |

## Decisions

| Finding class | Decision | Reason |
| --- | --- | --- |
| Plugin install/backup cache copies | `delete candidate` only after verification | The active audit found 13 cache copies under `plugin-install-*` and `plugin-backup-*`, but the Codex app may keep cache/install state for reasons outside model-visible prompt rendering. Verify before deleting. |
| Repo-local duplicate skill names | `keep` by default | Repeated names such as `build-story`, `validate`, `triage`, and `loop-verify` are the expected distributed harness shape. Treat as alignment inventory only. |
| Duplicate repo-local bodies | `review only` | Identical body hashes can mean healthy shared methodology, not accidental copy debt. A cleanup candidate needs a concrete local failure mode. |
| Long descriptions | `shorten candidate` only with trigger preservation | The helper reports long descriptions, but any edit must preserve product, tool, action, and object trigger nouns. |
| Low usage evidence | `no action` without workflow evidence | Log scans miss implicit skill activation, path-local workflows, and new skills. Low usage is a prompt for review, not proof of dead code. |
| Target repo notes/stories | reject now | The first run did not find high-confidence repo-local cleanup work. Creating target pressure would add overhead without a concrete failure mode. |

## Recommendation

Keep the audit as an on-demand Conductor tool. Use it when skill-budget
pressure, duplicated plugin cache entries, or wrong-skill activation becomes
suspect.

Do not make it a default recurring ceremony yet. Promotion into regular
methodology should wait until there is repeated evidence that the audit catches
real context-budget or wrong-skill failures that manual review misses.

The only plausible near-term cleanup lane is user/plugin-cache hygiene, and it
should be handled separately from this story after verifying which cache roots
the Codex app actually loads or needs for rollback/install bookkeeping.

## Practical Impact

Cam gets a cheap way to inspect skill-surface pressure without turning
distributed repo-local skills into fake drift. The audit makes context-budget
risk visible while preserving the rule that cleanup requires evidence and an
explicit follow-up.
