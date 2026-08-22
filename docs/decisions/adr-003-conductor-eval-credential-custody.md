# ADR-003 — Conductor Custodies Evaluation Credentials

## Status

Accepted

## Context

Conductor now selects and coordinates model-evaluation campaigns across the
portfolio, but the original orchestration contract required every owning repo
to already possess the candidate provider credential. Recent evaluations then
stopped before capability measurement even when Cam had a suitable test key in
another repo. Agents repeatedly rediscovered, borrowed, and remapped the same
keys, which made credential provenance inconsistent and turned routine eval
access into manual cross-repo work.

The benchmark, fixtures, scoring, evidence, and adoption decision must remain
owned by the target repository. Credential custody is a different concern:
eval-only provider keys are portfolio-level access infrastructure used by
Conductor on Cam's behalf.

## Decision

Conductor will be the local custodian for **evaluation-only** provider
credentials.

- The canonical local vault is
  `~/.config/conductor/eval-credentials.env`, outside every git worktree.
- The vault directory is mode `0700` and the file is mode `0600`.
- Tracked files record provider names and procedures only, never values,
  fingerprints, authorization headers, or signed URLs.
- A selected Stage 2 evaluation authorizes Conductor to copy only the required
  provider key into the selected isolated owner worktree's ignored environment
  under that repo's expected variable name. It does not authorize copying the
  whole vault.
- The temporary owner copy is removed after the campaign unless Cam explicitly
  asks to provision that owner permanently. The central vault remains the
  source of truth and can be recopied for a later eval.
- OpenAI, Anthropic, Gemini, and other normal product/runtime credentials stay
  owner-managed. A provider enters the central vault only when Cam designates
  it as evaluation infrastructure or explicitly provisions it for that role.
- Owner-repo instructions continue to control fixtures, prompts, scorers,
  privacy eligibility, spend, evidence, and adoption. Central custody does not
  authorize private payloads, account-policy changes, broader routing, default
  changes, commits, pushes, or deployment.
- `scripts/eval_credentials.py` is the only normal import/copy/remove/status
  interface. It parses dotenv files without sourcing them, writes atomically,
  enforces mode `0600`, refuses symlinks, and reports names/status only.

Initial centralized eval providers are OpenRouter, xAI/Grok, and Moonshot/Kimi.
Direct DeepSeek and Z.ai remain unconfigured until Cam supplies keys. No
Mistral credential was centralized because current evidence did not establish
it as portfolio eval-only infrastructure.

## Options Considered

- **Conductor-owned local eval vault — accepted.** Matches the new orchestration
  role, removes repeated key hunts, and keeps benchmark ownership distributed.
- **Keep duplicating keys independently in every owner — rejected.** Creates
  drift, stale copies, ambiguous provenance, and unnecessary manual setup.
- **Use only one repo as an informal key donor — rejected.** Recreates a hidden
  canonical dependency and encourages agents to inspect unrelated product
  environments.
- **Move immediately to macOS Keychain or an external secrets manager —
  deferred.** Stronger at-rest controls may become worthwhile, but they add
  integration and operator overhead beyond the current single-user local
  workflow. The helper isolates that future storage change from the eval skill.

## Consequences

- Positive:
  - selected evaluations can obtain known eval access without manual repo hunts
  - one central rotation updates future campaigns
  - owner repos retain their harnesses, evidence, privacy rules, and decisions
  - secret values remain outside git and absent from agent output
- Tradeoffs:
  - Conductor becomes a meaningful local trust boundary
  - compromise of the local user account can expose several eval providers
  - temporary owner copies require cleanup and status auditing
  - account privacy/routing settings remain separate external decisions and can
    still block a centrally credentialed evaluation

## References

- Ideal: I2 distributed ownership, I3 recommendation-first supervision, I5
  minimal overhead
- Spec: spec:3.3 staged model-evaluation orchestration
- State/Graph: Story 031 owning-repo orchestration; Story 032 credential custody
- Related decisions: ADR-001 supervisor-not-canonical-core; this decision
  centralizes access custody, not the distributed harness

## Open Questions

- When should the local vault migrate to macOS Keychain or another encrypted
  store?
- Should a future direct DeepSeek or Z.ai key be added after account creation,
  or should OpenRouter remain the preferred eval route when its privacy and
  strict-contract gates qualify?
