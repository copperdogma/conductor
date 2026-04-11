# Security Audit Tooling

This reference records the current local-first tool choices for the
`/security-audit` lane.

Use it when deciding what to run, what to wrap, and what to skip.

## Selection Principles

- Prefer already-installed tools or ecosystem-native commands first.
- Do not silently download scanners during a normal audit run.
- Keep one cross-language code scanner plus a few ecosystem-native dependency
  checks instead of a sprawling tool belt.
- Prefer tools that produce actionable local output over hosted dashboards.
- Secret scanning is a separate lane from code scanning and should stay that
  way.

## Decisions

### Adopt

#### `rg` hotspot search

- Why:
  - always available in this workflow
  - fast, deterministic, and easy to retarget to a diff or subsystem
  - useful even when heavier scanners are absent
- Role:
  - first-pass hotspot discovery
  - fallback when scanners are missing
  - companion tool, not a replacement for deeper review

#### Semgrep

- Why:
  - cross-language scanner that works across Python and JavaScript
  - local CLI is already available here
  - good fit for bounded code and trust-boundary review
- Role:
  - primary code scan in the default local bundle
  - useful for repo and surface audits, less useful as a first move for pure
    dependency reviews
- Caveat:
  - `--config auto` fetches rules from the Semgrep registry and the CLI notes
    that this logs the project URL and may report metrics when registry-backed
    configs are used
- Default stance:
  - allowed in this lane, but keep the tradeoff explicit

#### `pnpm audit` / `npm audit`

- Why:
  - already bundled with the JavaScript package manager
  - zero extra tool installation
  - suitable for lightweight dependency pressure checks
- Role:
  - default dependency-audit signal for Node/pnpm repos
- Caveat:
  - advisory counts are not the same thing as reachable exploit paths
  - use as one signal alongside code and workflow review

### Adapt

#### `pip-audit`

- Why:
  - focused Python dependency advisories
  - can audit a local Python project path or locked dependency surface
- Role:
  - optional Python dependency-audit tool
  - good fit when the repo has a clear Python project root and dependency
    resolution is cheap enough
- Adaptation:
  - do not assume it is preinstalled
  - allow explicit `uvx` bootstrap when the operator wants that tradeoff
  - document skip behavior when the tool is absent

#### Gitleaks

- Why:
  - straightforward dedicated secret scanner
  - lighter local-first fit than a full hosted secret-management workflow
- Role:
  - optional specialist tool for secret sweeps
- Adaptation:
  - not part of the default helper bundle; use it only for explicit secret
    sweeps
  - local binary is preferred when installed
  - Docker-backed execution is acceptable as an explicit opt-in fallback
  - root-level scans can catch real `.env` / `.secrets` exposures, but repos
    with large generated artifact trees can create noisy generic-key matches
- Experiment result:
  - `storybook`: high signal for local secret hygiene because it surfaced real
    `.env` and `.secrets` files in the working tree, plus some doc/story noise
  - `dossier`: low signal in default root scan because most matches came from
    eval artifacts and fixtures rather than live credentials
- Current stance:
  - keep as an optional specialist path, not a default scan in every audit run

### Defer

#### Bandit

- Why deferred:
  - useful as a Python source-code analyzer, but overlaps with the default
    Semgrep-first lane
  - easy to add later for Python-heavy repos if Semgrep misses recurring
    patterns
- Current stance:
  - documented as an optional specialist, not part of the default wrapper

#### OSV-Scanner

- Why deferred:
  - credible polyglot vulnerability scanner and OSV database frontend
  - current tracked stack does not yet justify another default dependency
    scanner on top of ecosystem-native checks plus optional `pip-audit`
- Current stance:
  - revisit only if cross-ecosystem lockfile scanning becomes recurring

#### TruffleHog

- Why deferred:
  - strong secret-scanning product with credential verification
  - heavier than the current local-first lane needs
- Current stance:
  - useful specialist option when secret validation matters, but not part of
    the default helper bundle

## Default Local Bundle

### Python-heavy repo

1. `scripts/hotspot-grep.sh`
2. Semgrep if installed
3. `pip-audit` only when available or when explicit `--allow-uvx` is approved
4. Manual review of auth, file/process, agent/tool, and logging surfaces

### Node / pnpm repo

1. `scripts/hotspot-grep.sh`
2. Semgrep if installed
3. `pnpm audit` or `npm audit`
4. Manual review of scripts, webhooks, secrets, and automation surfaces

### Secret-focused review

1. use the hotspot grep to find obvious hard-coded exposures
2. if installed, run a dedicated secret scanner such as Gitleaks
3. if Gitleaks is not installed and the operator explicitly opts in, use the
   Docker-backed Gitleaks path
4. treat TruffleHog as an explicit stronger option when credential validation
   matters enough to justify the extra weight

## Tool Availability Policy

- Installed tool: use it.
- Missing tool with lightweight bootstrap path: only use it after explicit
  opt-in such as `--allow-uvx`.
- Missing heavy tool: skip it, say so clearly, and continue with the smaller
  honest bundle.

## Official Sources

- Semgrep CLI: `https://semgrep.dev/docs/getting-started/cli`
- npm audit: `https://docs.npmjs.com/cli/v10/commands/npm-audit`
- pnpm audit: `https://pnpm.io/cli/audit`
- pip-audit: `https://github.com/pypa/pip-audit`
- Bandit: `https://bandit.readthedocs.io/en/latest/`
- Gitleaks: `https://github.com/gitleaks/gitleaks`
- OSV-Scanner: `https://google.github.io/osv-scanner/`
- TruffleHog: `https://trufflesecurity.com/trufflehog`
