# Evaluation Credential Custody

Read this reference during Stage 2 when a selected owning repo needs a provider
credential. Conductor safeguards eval-only access; the owner still controls the
benchmark, fixtures, privacy, spend, evidence, and adoption decision.

## Central Vault

The default vault is `~/.config/conductor/eval-credentials.env`. It is outside
git. The directory must be mode `0700`; the file must be mode `0600`.
`CONDUCTOR_EVAL_ENV_FILE` may point the helper at a different local vault.
Never source, print, attach, copy, or inspect the whole file.

Use Conductor's helper from the active Conductor source root:

```bash
python scripts/eval_credentials.py status --json
python scripts/eval_credentials.py check
```

These commands report provider names and presence only. Initial central
providers are OpenRouter, xAI/Grok, and Moonshot/Kimi. Missing direct DeepSeek,
Z.ai, or another provider remains missing until Cam explicitly provisions an
eval credential; never substitute or mine product repos for a new source.

## Owner Injection

1. Resolve the owner worktree and its normal credential variable name.
2. Prefer an existing owner variable. Check presence only; never compare or
   replace its value.
3. If missing, identify an owner env file that is ignored in that isolated
   worktree. Verify with `git check-ignore`. If no safe ignored target exists,
   use a protected temporary env outside the repo and pass its path through the
   owner's normal wrapper; do not create a trackable secret file.
4. Copy exactly one provider key:

   ```bash
   python scripts/eval_credentials.py copy \
     --provider openrouter \
     --target-env /absolute/owner/worktree/.env \
     --target-var OWNER_OPENROUTER_API_KEY
   ```

   The helper refuses symlinks and existing target variables, writes
   atomically, enforces mode `0600`, and never prints the value.
5. Tell the owner worker only which provider and variable are configured, the
   env path, and that the key is temporary. Do not include a value, fingerprint,
   authorization header, signed URL, or whole environment in task text.
6. Use the owner's wrapper to map that variable into the provider process. Do
   not source the central vault or expose unrelated central keys.

Stage 2 selection authorizes this narrow temporary injection for the selected
provider. It does not authorize private data, a different provider, account
privacy/billing changes, spend above the disclosed cap, default changes,
deployment, commit, push, or permanent owner provisioning.

## Cleanup

After the owner finishes or stops, remove only the injected variable:

```bash
python scripts/eval_credentials.py remove \
  --target-env /absolute/owner/worktree/.env \
  --target-var OWNER_OPENROUTER_API_KEY
```

Verify by variable name only that it is absent. Never remove an owner-managed
credential: the helper's refusal to overwrite an existing variable is the
boundary that makes cleanup safe. Record the provider, target variable, and
cleanup result in the campaign log without recording a secret value.

## Adding or Rotating an Eval Key

Adding a new provider or replacing a central value requires Cam's explicit
credential authorization. Import without printing:

```bash
python scripts/eval_credentials.py import \
  --provider xai \
  --source-env /absolute/protected/source.env \
  --source-var SOURCE_XAI_API_KEY
```

Then run `check` and a zero-cost provider-auth/catalog probe when available.
For an intentional rotation, repeat the import with `--replace`; the helper
otherwise refuses to overwrite a central provider key.
Delete or preserve the old source according to its owning repo's instruction;
centralization alone does not authorize removing product credentials.
