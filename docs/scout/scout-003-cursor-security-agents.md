# Scout 003 — Evaluate Cursor Security Agents for Autonomous Codebase Safety

**Source**: `https://cursor.com/blog/security-agents`
**Status**: Spike
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

Queued from the inbox as a possible safety or review-pattern source. The likely
value is security-oriented agent workflow design rather than a product feature
drop-in. The inbox now also carries Kevin Kern's lightweight audit prompts as a
useful low-overhead comparison point for the same guardrail problem.

## Project Relevance

- **dossier**: Relevant if the article exposes reusable safety or code-review
  guardrails for agentic development.
- **storybook**: Relevant for shared development workflow hardening rather than
  product functionality.
- **doc-web**: Relevant for shared engineering safety patterns if they stay
  lightweight.
- **cine-forge**: Relevant on the same basis as the other product repos.

## Recommendation

- Run a `/scout` pass focused on portable guardrails, approval patterns, and
  evaluation hooks that could improve the shared build loop without adding
  heavyweight process, then compare those ideas against lighter prompt-only
  review patterns before codifying anything.

## Evidence

- `https://cursor.com/blog/security-agents`
- `https://x.com/kevinkern/status/2042545273855938695?s=12&t=uFZE-MuhgWdh1YErEZzLtQ`
- Inbox note: `Smart ass audit` / `3AM test`

## Open Questions

- Is the value here practical workflow design or mostly marketing framing?
- Which ideas would be genuinely portable across the tracked repos?
- Do the best next steps belong in `/validate`, close-out prompts, or a lighter
  ad hoc review pattern?
