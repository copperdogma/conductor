---
type: research-prompt
adr: "ADR-003"
short_name: "conductor-eval-credential-custody"
title: "Conductor Custodies Evaluation Credentials"
created: "2026-08-21"
---

# ADR Research Prompt

## Context

Conductor now recommends and executes approved model-evaluation campaigns in
isolated owning-repo worktrees. Repeated campaigns have shown that keeping
eval-only credentials scattered across product repos causes access blocks,
manual key hunting, stale copies, and ambiguous provenance. The target repos
must still own prompts, fixtures, scoring, evidence, privacy, and adoption.

The current environment is a single-user macOS development machine. Secret
values must never enter git or agent output. The desired operator experience is
one approval for selected evals, followed by safe provider-key availability in
each temporary owner worktree.

## What I Need

1. Should eval-only credentials be centralized in Conductor while product
   credentials remain owner-managed?
2. What is the smallest safe local storage and transfer contract for this
   single-user workflow?
3. Which permissions must remain separate from credential possession,
   especially private fixtures, account privacy settings, spend, and rollout?

## Output Format

For each major option, provide:

1. Recommended choice with reasoning
2. Main tradeoffs and failure modes
3. What would need to be true for a different choice to win
4. Evidence or examples
