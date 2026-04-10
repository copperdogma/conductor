# Scout 014 — Evaluate Agent-Skills Additions for Test Consolidation and Hard Cuts

**Source**: multiple inbox items
**Status**: Spike
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Queued from the inbox as two concrete `agent-skills` leads from the same repo.
The likely value is whether `consolidate-test-suites` and `hard-cut` expose
portable validation and control patterns that reduce repeated cross-project
work without importing another skill library wholesale.

## Project Relevance

- **dossier**: Relevant if either skill suggests lighter shared methodology for
  validation scope or bounded execution.
- **storybook**: Relevant because the repo has a large test surface and
  tool-heavy workflows that could benefit from tighter test targeting or faster
  stop conditions.
- **doc-web**: Relevant because the repo carries a broad Python and CLI test
  surface where consolidation or early cutoffs could reduce routine overhead.
- **cine-forge**: Relevant for integration-heavy workflows where bounded stops
  and narrower validation passes can save time and cost.

## Recommendation

- Run a focused `/scout` pass on these two skills only. Adopt at most the parts
  that reduce repeated validation or cleanup work; reject the rest instead of
  importing a parallel skill tree.

## Evidence

- `https://github.com/regenrek/agent-skills/blob/main/skills/consolidate-test-suites/SKILL.md`
- `https://github.com/regenrek/agent-skills/blob/main/skills/hard-cut/SKILL.md`
- Inbox notes: `shared harness test consolidation` and `hard-cut skill`

## Open Questions

- Is `consolidate-test-suites` solving a real recurring pain in the tracked
  repos, or just generic neatness?
- Does `hard-cut` belong as shared execution guidance, a repo-local helper, or
  nowhere at all?
