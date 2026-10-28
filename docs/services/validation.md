# Service catalog validation — 2026-10-28

Scope: local service catalog, selected credential copies and private helper.
No provider operations, target project changes or live authentication tests.

## Checks completed

- `python3 -m unittest discover -s tests -p 'test_service_credentials.py' -v`:
  seven tests pass. Synthetic fixtures cover selected-key boundaries,
  literal parsing/no shell execution, duplicate/missing/placeholder/multiline
  rejection, vault permissions, symlink rejection, no overwrite, Git ignore and
  tracked-file export guards, Fly key selection, metadata/error output redaction.
- `python3 scripts/repo_checks.py lint`: passes.
- `python3 scripts/methodology_graph.py check`: current. Planning inputs unchanged.
- All eight profiles / 18 values compare equal to selected source assignments;
  comparison prints only aggregate results. Rechecked after parser correction.
- Vault directory `0700`, file `0600`; Git ignores `.private/` and tracks no
  vault files. Known copied values were checked against the task's public
  documentation/code artifacts without printing values; no matches found.
- Scoped whitespace and local Markdown link checks pass. Existing unrelated
  checkout changes are preserved. Implementation used no worktree; close-out
  uses the isolated landing checkout below.

An independent bounded review found that shell-style parsing could silently
truncate unquoted hashes/backslashes. Replaced it with a small literal parser,
added regressions and verified all current copies again. Standard dotenv files
are not shell programs: the helper preserves embedded hashes/backslashes, treats
whitespace followed by a hash as a comment, supports quoted single-line literals,
and performs no expansion. Unsupported multiline values are rejected.

## Limits

These checks establish selected local copying and handling, not current provider
access. DreamHost directory rights, Fly session expiry, Cloudflare account/token
access and Google client registrations remain unverified. The vault is local
plaintext with restrictive permissions, not encrypted or backed up off-host.
The initial inventory is a metadata snapshot; refreshed profiles need their own
scope/validity checks. See [catalog](../services.md) for discovery coverage.

## Close-out candidate

Cam authorized check-in and push. Candidate is based on remote main `16a25b8`
with only this chat's catalog, helper, tests, discovery pointers, ignore rule,
changelog and inbox receipt. Prior unrelated primary-checkout changes are not
part of the candidate. Credentials remain in the primary checkout's `.private/`;
no vault is copied into the integration checkout.

Worktree: `/Users/cam/.codex/worktrees/service-catalog-20261028/conductor`.
Owner: this shared-service catalog chat. Branch: `codex/service-catalog-20261028`.
Retained as the validated landing checkout; cleanup was not requested.

Close-out checks run on this isolated candidate: the seven focused synthetic
credential tests, lint, methodology graph check, scoped whitespace/local-link
checks and secret-value exclusion over the full candidate diff. Provider
validity and permissions remain outside this landing's validation.
