---
type: synthesis-report
adr: "ADR-003"
short_name: "conductor-eval-credential-custody"
title: "Conductor Custodies Evaluation Credentials"
synthesis_model: "Codex GPT-5.6"
source_reports:
  - "2026-08-21 local provider-key inventory and recent eval evidence"
synthesized: "2026-08-21"
---

# Final Synthesis

## Recommendation

Use one Conductor-owned, git-external, mode-`0600` dotenv vault for eval-only
provider keys. Copy one required key at a time into an approved isolated owner
worktree, then remove the temporary copy after the campaign. Keep product keys,
benchmarks, fixtures, scoring, and adoption distributed.

## Why

Recent Grok, Kimi, DeepSeek, and OpenRouter attempts already treated certain
credentials as portfolio eval infrastructure, but did so through ad hoc sibling
borrowing. Central custody makes that reality explicit while avoiding a shared
benchmark core. The local inventory found known-valid OpenRouter, xAI, and
Moonshot keys suitable for initial migration.

## Risks and Tradeoffs

- The local Conductor vault becomes a higher-value trust boundary.
- Plaintext local storage depends on OS user/file protections; future multi-user
  or remote use should trigger an encrypted secrets-store review.
- Credential possession does not solve provider route, strict-contract,
  privacy, quota, or account-policy incompatibility.

## Follow-Up

- Implement Story 032's helper, skill, spec, and validation changes.
- Add direct DeepSeek or Z.ai only when Cam explicitly supplies those eval keys.
- Consider Keychain migration if the workflow leaves a single-user local host.
