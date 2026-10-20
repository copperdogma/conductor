---
name: codebase-improvement-scout
description: Inspect a repository for evidence-backed maintainability or reliability improvements and produce a report-first scan
user-invocable: true
---

# /codebase-improvement-scout [scope]

Run only when requested. This is a local, report-first scan for meaningful
improvements, not permission to fix code or create a story automatically.

## Scan

1. Read `AGENTS.md` and the relevant Ideal, Spec, decisions, and existing scan
   reports/state when present. Respect repo-owned commands and boundaries.
2. Inspect the requested scope using deterministic, available tools. Report
   which detectors ran and which were unavailable; do not add dependencies.
3. Look for evidence-backed issues such as duplicated ownership, obsolete or
   unreachable paths, fragile boundaries, missing safeguards, data-loss risks,
   and algorithmic complexity. For complexity, identify an input-size variable,
   growth pattern, and observed or reasoned impact; avoid speculative rewrites.
4. If useful and available, request one isolated, read-only semantic review
   against a pinned code snapshot/model configuration. Keep it report-only;
   independently verify every candidate against repository evidence before
   including it. Treat unverified reviewer output as a lead, not a finding.
5. Rank findings by user impact, confidence, and repair leverage. Suppress
   repeated findings only with a recorded reason. Prefer one useful next step.

## Report and boundaries

When invoked to scan, create one dated report under
`docs/reports/codebase-improvement/`, following local conventions if present.
If the directory is absent, create it for that report only. Do not create
long-lived state files unless the repository already owns such a surface.

The scan is read-only: no autofixes, file rewrites, dependency installation,
network helpers, provider calls, commits, or pushes. Story creation is a
separate user-requested action after the report is reviewable.

Record scope, revision, detectors and limitations, evidence paths, finding
classification, recommendation, and any optional-review provenance. If no
material findings are supported, say so. Never present raw reviewer claims or
complexity guesses as confirmed defects.
