---
name: validate
description: Review a product story and current changes against acceptance criteria and applicable evidence
user-invocable: true
---

# /validate [story-id]

Validate the current candidate. Findings-first review is part of validation;
green checks do not hide a concrete defect. The main thread owns the final
assessment even when bounded reviewers or check runners help.

## Review

1. Read `AGENTS.md`, the story, relevant Ideal/Spec/state/graph, decisions, and
   current changes. Confirm which files and candidate revision are in scope.
2. Review for correctness, regressions, missing proof, security/trust issues,
   and operational hazards. For drift-prone external interfaces, confirm that
   current primary-source facts were checked or explain why they are irrelevant.
3. Report material findings first with evidence paths/locations. Treat
   additional reviewer output as advisory and verify each finding against the
   actual candidate.
4. Map each acceptance criterion and workflow gate to current evidence. Separate
   implemented behavior, structural checks, integration proof, and unverified
   assumptions.

## Select evidence proportionally

- Read local validation instructions and run mandatory gates plus the narrowest
  meaningful checks for changed behavior.
- Reuse prior results only when the tested inputs, environment, configuration,
  and candidate behavior remain applicable. Rerun affected checks after a
  relevant change; broaden only when shared effects justify it.
- Do not require a particular CLI or full suite when the repository does not
  provide it. Do not run paid, destructive, or external checks without scope
  and authorization.
- If a material failure is unexplained or repeated, research its problem class
  before retrying or weakening the acceptance contract.

## Report

Return findings first, then Met / Partial / Unmet per acceptance criteria,
evidence selected and reused, residual risk, and one closure recommendation:
close, keep open, rescope, or mark blocked. Do not mark the story done here.
