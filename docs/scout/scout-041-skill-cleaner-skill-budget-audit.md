# Scout 041 - Evaluate Skill Cleaner for Skill-Surface Budget Audits

**Source**:
`https://github.com/steipete/agent-scripts/blob/main/skills/skill-cleaner/SKILL.md`
and
`https://raw.githubusercontent.com/steipete/agent-scripts/main/skills/skill-cleaner/scripts/skill-cleaner.ts`

**Status**: Adapt
**Projects Reviewed**: conductor, dossier, storybook, doc-web, cine-forge,
boardgame-ingester, roborally, echo-forge

## Summary

Peter Steinberger's `skill-cleaner` is a Codex/OpenClaw maintenance skill for
auditing skill prompt-budget pressure, duplicate skills, unused candidates,
loaded roots, disabled roots, and long descriptions. The companion analyzer
walks Codex skill roots, plugin cache roots, optional extra roots, and recent
Codex/OpenClaw logs, then reports budget pressure, duplicates by name/body, and
heuristic usage evidence.

This is useful for Cam's repos, but not as a direct import. The useful local
shape is a Conductor-owned, report-first skill-surface audit that reads
`projects.yaml`, understands the real loaded skill roots for the active
checkout, and produces candidate findings for human review. It should not
delete, disable, or rewrite skills automatically.

The immediate value is real because the local dry run exposed concrete signal:

- The current Conductor-like skill set plus Codex/plugin roots discovered 65
  enabled skills. Full rendered skill lines cost about 6,474 tokens against the
  modeled 5,440-token 2% budget, so Codex budgeting would truncate 4,057
  description characters even without omitting any skills.
- The portfolio inventory pass across the tracked repo skill roots discovered
  274 enabled skills. Treating that as one comparison set, full rendered lines
  cost about 18,672 tokens; minimum no-description lines still cost about
  7,868 tokens; the modeled budget would include 182 skills and omit 92.
- The analyzer found 13 plugin install/backup skill copies under the plugin
  cache and many repeated repo-local skill names/bodies.

Those numbers are enough to justify a lightweight audit lane. They are not
enough to justify deleting repo-local distributed skills, because repeated
repo-local copies are often intentional local ownership rather than accidental
drift.

## Project Relevance

- **conductor**: `Adapt`. Best owner. Conductor should wrap or borrow the
  analyzer as an alignment/scout helper for skill-surface inventory, prompt
  budget pressure, duplicate plugin-cache copies, and long-description
  candidates.
- **dossier**: `Defer`. Useful as an audit subject because it carries many
  repo-local skills, but no direct Dossier story should be created until a
  Conductor audit identifies a concrete local cleanup candidate.
- **storybook**: `Defer`. Same as Dossier. Repeated skills may be intentional
  distributed harness ownership.
- **doc-web**: `Defer`. Useful audit subject only; do not create local cleanup
  pressure from heuristic usage counts.
- **cine-forge**: `Defer`. Strong audit subject because it has many local
  skills, but active product/runtime work should not be interrupted by generic
  skill cleanup unless the audit finds high-confidence waste.
- **boardgame-ingester**: `Defer`. Lower direct leverage; include in the
  Conductor inventory pass.
- **roborally**: `Defer`. Include in the inventory pass, but avoid broad skill
  churn while the repo is still small.
- **echo-forge**: `Defer`. Include in the inventory pass; any repo-local edits
  should use isolated worktrees because the primary checkout is often active.

## Recommendation

Adapt this into a Conductor-owned "skill surface audit" rather than installing
`skill-cleaner` into every repo.

Recommended first story scope:

1. Create a report-only Conductor helper or skill that reads `projects.yaml`
   and passes the tracked `.agents/skills` roots explicitly.
2. Separate two modes:
   - active-session mode: audit the skills actually loaded for the current
     checkout and active plugins
   - portfolio-inventory mode: compare repo-local skill roots across tracked
     projects without pretending they are all loaded in one prompt
3. Treat plugin install/backup duplicates as the first cleanup candidate, but
   verify whether Codex actually loads those paths before deleting anything.
4. Treat repo-local duplicate names as alignment inventory, not deletion
   candidates. Preserve local copies when they encode repo policy or operations.
5. Use long-description reports as human review prompts only. The upstream
   auto-suggestions are too coarse for Cam's trigger-heavy skill descriptions.
6. Add a no-delete output policy: the audit can recommend `keep`, `shorten`,
   `disable`, `delete`, or `no action`, but edits require an explicit follow-up
   story or user approval.

Do not route inbox notes to every tracked repo yet. The useful adoption point
is Conductor's cross-project skill governance, not target-project product work.

## Rejected Adaptations

- Do not adopt the script unchanged. It assumes `~/Projects` for repo roots,
  while the tracked registry uses `/Users/cam/Documents/Projects` and Codex
  worktrees can live under `/Users/cam/.codex/worktrees`.
- Do not use the plugin-cache scan as proof that every duplicate is
  model-visible. The local session skill list did not obviously expose the
  `plugin-install-*` and `plugin-backup-*` copies, so a local wrapper must
  distinguish cache contents from loaded roots.
- Do not delete skills from "unused" evidence alone. Skill usage can be
  implicit through descriptions, trigger rules, repo context, or workflow
  paths that logs do not capture.
- Do not auto-rewrite descriptions from the analyzer suggestions. The dry run
  produced generic suggestions such as reducing specific visual or ideation
  skills to vague verbs, which would lose important trigger nouns.
- Do not collapse distributed repo-local skills into one canonical copy. That
  conflicts with Conductor's distributed ownership model.

## Evidence

- The upstream `SKILL.md` says the tool is for trimming skill prompt budget,
  finding duplicates, auditing enabled/disabled roots, and deciding which
  skills/plugins to remove.
- The upstream workflow reads the report in this order: skill budget,
  description candidates, duplicates, unused candidates, and root summary.
- The analyzer models Codex's rendered skill-line shape and the 2% context
  budget rule, then reports full-line cost, minimum no-description cost,
  included/omitted skills, and truncated description characters.
- The analyzer scans `~/.codex/skills`, `~/.codex/plugins/cache`, optional
  roots, and recent Codex/OpenClaw logs. It uses heuristic usage evidence from
  `$skill` mentions, `SKILL.md` path reads, and "use/read/load skill" text.
- Local current-checkout dry run on 2026-05-25 with the Conductor worktree
  skill root found 65 enabled skills, 6,474 unbudgeted full tokens, 5,440
  budgeted tokens used, 4,057 truncated description characters, 13
  plugin-install/plugin-backup copies, and two repo-local unused heuristic
  candidates.
- Local portfolio inventory dry run on 2026-05-25 with the tracked repo skill
  roots found 274 enabled skills, 18,672 unbudgeted full tokens, 7,868 minimum
  no-description tokens, 5,426 budgeted tokens used, 92 modeled omissions, 52
  duplicate base-name groups, 35 duplicate body-hash groups, and 13
  plugin-install/plugin-backup copies.

## Confidence

High that this is useful as a Conductor audit/reference. Medium that the
upstream script's exact budget numbers match what Codex actually renders in
this app, because the local prompt's visible skill list appears narrower than
the plugin-cache filesystem scan.

## Open Questions

- What is the authoritative local source for skills actually loaded into a
  Codex session: the rendered prompt inventory, config roots, plugin metadata,
  or a combination?
- Are the `plugin-install-*` and `plugin-backup-*` skill dirs safe stale cache
  artifacts, or does the Codex app still need them for plugin rollback/install
  bookkeeping?
- Should a skill-surface audit become part of `/align-projects`, or remain a
  separate on-demand Conductor maintenance story?
- What threshold should trigger description cleanup: exhausted effective 2%
  budget, modeled omitted skills, repeated trigger collisions, or observed
  wrong-skill activations?
