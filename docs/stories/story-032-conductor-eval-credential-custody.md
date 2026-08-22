---
title: "Conductor Evaluation Credential Custody"
status: "Done"
priority: "High"
ideal_refs:
  - "I2"
  - "I3"
  - "I5"
spec_refs:
  - "spec:3.3"
decision_refs:
  - "ADR-003"
depends_on:
  - "Story 031"
category_refs:
  - "registry-routing"
  - "story-prep"
tracked_projects:
  - "conductor"
  - "dossier"
  - "storybook"
  - "doc-web"
  - "cine-forge"
  - "boardgame-ingester"
  - "roborally"
  - "echo-forge"
---

# Story 032 — Conductor Evaluation Credential Custody

**Priority**: High
**Status**: Done
**Decision Refs**: ADR-003
**Depends On**: Story 031

## Goal

Make Conductor the safe local custodian for eval-only provider credentials so
approved owner-repo evaluations can receive the one key they need without
repeated cross-repo key searches, while preserving distributed benchmark,
privacy, evidence, spend, and adoption ownership.

## Acceptance Criteria

- [x] A names-only historical audit identifies which providers are genuinely
      eval infrastructure and never prints secret values.
- [x] One git-external, mode-`0600` Conductor vault contains known-valid
      OpenRouter, xAI, and Moonshot eval keys.
- [x] A tested helper imports, reports, copies, and removes one provider key at
      a time without sourcing dotenv files or exposing values.
- [x] `/evaluate-model` treats selected Stage 2 approval as authority for
      temporary central eval-key injection, not private data, account-setting
      changes, product keys, higher spend, or rollout.
- [x] Ideal/spec/AGENTS/ADR and owner protocol preserve target-repo control of
      fixtures, harnesses, evidence, and adoption.
- [x] Methodology, skill, lint, tests, and whitespace checks pass.

## Out of Scope

- Centralizing normal OpenAI, Anthropic, Gemini, ElevenLabs, Deepgram, or other
  product/runtime credentials.
- Adding provider accounts or credentials that do not currently exist.
- Changing OpenRouter privacy settings, provider billing, runtime defaults,
  deployment, commits, pushes, merges, or target-repo primary checkouts.
- Moving benchmarks, provider payloads, raw results, or adoption authority into
  Conductor.

## Tasks

- [x] Read the relevant Ideal, Spec, state, graph, Story 027/031, and ADR context
- [x] Audit recent eval providers and local credential names/status safely
- [x] Record ADR-003 and its lightweight research/synthesis
- [x] Implement the credential helper and focused tests
- [x] Update the eval skill, owner protocol, and workflow surfaces
- [x] Run required checks:
  - [x] `make methodology-compile`
  - [x] `make methodology-check`
  - [x] `make lint`
  - [x] `make skills-check`
  - [x] `make test`
- [x] Verify Conductor tenets I2, I3, and I5

## Workflow Gates

- [x] Build complete
- [x] Validation complete or explicitly skipped by user
- [x] Story marked done via `/mark-story-done`

## Files to Modify

- `scripts/eval_credentials.py` and `tests/test_eval_credentials.py` — safe
  local vault import/copy/remove/status behavior.
- `.agents/skills/evaluate-model/SKILL.md` and credential/owner references —
  central custody plus temporary owner injection contract.
- `docs/decisions/adr-003-conductor-eval-credential-custody.md` — durable trust
  boundary.
- `docs/ideal.md`, `docs/spec.md`, `AGENTS.md`, and `CHANGELOG.md` — aligned
  operator and methodology behavior.
- generated methodology surfaces — current story state.

## Notes

- Initial inventory on 2026-08-21 found valid catalog authentication for the
  Dossier OpenRouter, xAI, and Moonshot keys. xAI had three distinct valid local
  keys; Dossier's prior successful direct Grok eval makes its key the preferred
  central source. Moonshot had three valid local keys and one stale doc-web 401
  copy; Dossier's prior Kimi catalog evidence makes its key the preferred
  source. All OpenRouter copies were the same account.
- The central vault is `~/.config/conductor/eval-credentials.env`, not a tracked
  Conductor worktree file.

## Plan

1. Centralize only known eval-specific provider keys with explicit canonical
   names and safe status output.
2. Add an atomic helper that never sources dotenv files or prints values.
3. Teach Stage 2 to inject one provider key into an isolated owner environment,
   preserve all owner privacy/spend gates, and clean up afterward.
4. Align the durable decision, Ideal/spec, AGENTS, changelog, and story.
5. Run script, skill, methodology, lint, test, and secret-leak checks.

## Work Log

20260821-2100 — decision-and-inventory: Cam designated Conductor as the keeper
of eval-only credentials going forward. Safe names-only/equality checks and
zero-cost catalog probes identified known-valid OpenRouter, xAI, and Moonshot
sources without printing values. Imported one historically appropriate key per
provider into the git-external mode-`0600` Conductor vault. No product key,
provider account setting, target primary checkout, commit, or push changed.

20260821-2120 — implementation-and-validation: added atomic import/status/copy/
remove/check tooling with symlink refusal, explicit rotation, owner-key
overwrite refusal, mode enforcement, and six focused tests. Updated the skill,
credential and owner protocols, ADR, Ideal/spec, AGENTS, Alignment 042,
historical story notes, changelog, and generated methodology surfaces. Current
vault checks report three configured providers; zero-cost OpenRouter, xAI, and
Moonshot auth/catalog probes each returned HTTP 200. Exact-value scanning found
no central secret in tracked or untracked worktree changes; vault mode is
`0600`, parent mode is `0700`, and the vault is outside git. `make
methodology-compile`, `make methodology-check`, `make lint`, `make
skills-check`, `make test`, Python compilation, and `git diff --check` pass.
The generic skill-creator validator could not start because its environment
lacks PyYAML; the repo-native skill check passed. No target primary checkout,
account setting, commit, or push changed.

20260821-2125 — story-closed: confirmed every acceptance criterion, task, and
Build/Validation gate is satisfied with current-pass evidence. Marked Story 032
Done and regenerated methodology surfaces. Future provider additions remain
explicit credential-authority events; no follow-up implementation is required
for the initial OpenRouter/xAI/Moonshot custody set.
