# Scout 003 — Evaluate Cursor Security Agents for Autonomous Codebase Safety

**Source**: `https://cursor.com/blog/security-agents`
**Status**: Defer
**Projects Reviewed**: dossier, storybook, doc-web, cine-forge

## Summary

The source is real and more substantial than a generic thought piece. On
2026-03-16, Cursor published a concrete case study describing four internal
security automations built on Cursor Automations and cloud agents:
`Agentic Security Review` for pull requests, `Vuln Hunter` for existing-code
search, `Anybump` for dependency patching, and `Invariant Sentinel` for daily
drift checks against security and compliance properties.

That makes this a credible workflow reference, not just launch gloss. The
strongest portable ideas are methodological: keep security review separate from
general code review, stage rollout from private triage to PR comments to
blocking gates, normalize and deduplicate findings before they become noise,
and require agents to revalidate or execute code before escalating drift or
dependency claims.

But direct adoption is not the honest next step for the tracked repos. Cursor's
implementation assumes hosted background agents, GitHub/webhook triggers, Slack
routing, serverless MCP-backed memory, Terraform-managed deployment, and in one
case a canary safety gate after merge. The tracked repos are still primarily
local, solo-operated workflows that rely on explicit `/validate` and
close-out checks rather than a standing security-automation platform.

## Project Relevance

- **dossier**: `Defer`. Highest conceptual relevance because Dossier is the
  main methodology and workflow-innovation lane, but the current gap is not a
  missing hosted security-agent substrate. If revisited later, the honest first
  move would be a narrow security-review prompt or validate mode, not Cursor's
  full automation stack.
- **storybook**: `Defer`. Some future relevance around dependency audits or
  stricter repo guardrails, but there is no present evidence that background
  security agents outrank the repo's current product and methodology work.
- **doc-web**: `Defer`. The repo already leans on a `detect -> validate ->
  targeted escalate -> validate` discipline. Cursor's case study mostly
  reinforces that shape rather than exposing a missing substrate that doc-web
  should adopt now.
- **cine-forge**: `Defer`. Similar conceptual value for invariant-style checks
  and safer dependency work, but no current pressure justifies Slack/GitHub
  security automation or a new cross-cutting agent layer.

## Recommendation

- Keep this at `Defer`.
- Do **not** create a Conductor story or a target-repo story from this scout
  alone.
- Do **not** route it to a target repo inbox yet. There is no single project
  with enough live security or dependency-review pressure to own the follow-up.
- A later supervisor story now exists for a narrower carry-through:
  `docs/stories/story-002-security-audit-lane.md` incubates a local-first
  `/security-audit` skill without adopting Cursor's hosted substrate.
- Treat Cursor's post as a design-reference bundle for future guardrail work,
  not as a platform-adoption recommendation.
- If revisited later, extract only the smallest portable patterns:
  1. a prompt-tuned security review lane separate from general code review
  2. staged rollout from private signal to visible comments to blocking gates
  3. dependency-fix automation only when reachability, tests, and rollback
     checks are all cheap enough
  4. explicit invariant definitions plus evidence-backed revalidation before
     drift reports become action items
- The most likely future owner is Dossier or a Conductor alignment pass, but
  only after real repeated security-review pressure appears across more than
  one tracked repo.

## Confidence

- Medium-high. The judgment is grounded in Cursor's primary source plus the
  current repo workflow docs, but I did not inspect the released automation
  templates or run any Cursor automation directly.

## Evidence

- `https://cursor.com/blog/security-agents`
- Article highlights:
  - four concrete security automations: PR review, legacy vuln hunting,
    dependency patching, and invariant drift checks
  - background-agent substrate: webhooks, GitHub PR actions, cloud-agent tools
    and observability, Slack reporting, persistent memory, and Terraform
    deployment flow
  - staged rollout pattern: private triage first, then PR comments, then
    blocking gate once the signal quality is trusted
- Original capture note: `Smart ass audit` / `3AM test`
- Local workflow context:
  - `/Users/cam/Documents/Projects/dossier/AGENTS.md`
  - `/Users/cam/Documents/Projects/Storybook/storybook/AGENTS.md`
  - `/Users/cam/Documents/Projects/doc-web/AGENTS.md`
  - `/Users/cam/Documents/Projects/cine-forge/AGENTS.md`

## Open Questions

- Which tracked repo, if any, first accumulates enough dependency churn or
  repeated safety misses that a dedicated security-review lane beats lighter
  prompt-only auditing?
- If a smaller carry-through is desired before then, should it live as a
  `/validate` variant, a close-out checklist, or a repo-local dependency-audit
  automation?
