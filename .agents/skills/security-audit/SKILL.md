---
name: security-audit
description: Review a repo, diff, dependency surface, or subsystem for concrete security risks and the smallest honest fixes. Use when the user wants a security audit, trust-boundary review, dependency-risk pass, or agent/tool-safety review for an AI-driven codebase.
user-invocable: true
---

# /security-audit [diff|surface|repo|dependency] [optional focus]

Use this for bounded security review of a codebase, diff, subsystem, or
dependency surface.

## Modes

- `diff` — audit changed files only. Prefer this when there is a live diff.
- `surface` — audit one subsystem or trust boundary.
- `repo` — run a lightweight broad pass across the repo.
- `dependency` — focus on manifests, lockfiles, install/update scripts, and
  dependency exposure.

## Read First

- `AGENTS.md`
- relevant specs, ADRs, or runbooks for the audited surface
- `references/checklist.md`
- `references/tooling.md` when choosing local scanners or dependency-audit
  commands

## Bundled Helpers

- `scripts/hotspot-grep.sh <repo-root> [target]`
  - deterministic fallback for finding high-signal hotspots with `rg`
  - use this when scanners are missing, noisy, or you need a fast first map
- `scripts/run-local-audit.sh <repo-root> [options]`
  - orchestrates a small local scan bundle without modifying the target repo
  - detects repo shape and installed tools
  - prints explicit skip reasons when a tool is unavailable
  - supports repo, dependency, and target-path surface scans
  - `--allow-uvx` opt-in is required before it will bootstrap Python tools
    such as `pip-audit` via `uvx`
  - `--include-gitleaks` enables an explicit secret-scan pass
  - `--allow-docker` allows Docker-backed Gitleaks execution when the binary is
    not installed locally

## Steps

1. Establish the scope and threat shape.
   - What is in scope: diff, subsystem, repo, or dependency lane?
   - What matters here: auth, secrets, untrusted input, file/process access,
     model tools, public endpoints, admin surfaces, or automation?
2. Read the local guardrails first.
   - Start with `AGENTS.md`.
   - Read relevant specs, runbooks, or ADRs when the audit touches an existing
     workflow choice.
3. Map the trust boundaries.
   - Inputs and untrusted content
   - AuthN/AuthZ and role gates
   - Secrets, tokens, and credentials
   - File, network, subprocess, or shell access
   - Persistence, logging, and data export
   - Agent/tool permissions and automation triggers
4. Read code and manifests.
   - Prefer targeted reading over repo-wide wandering.
   - Use `rg` to find hotspots before opening files.
   - For broad passes or when you need search starters, read
     `references/checklist.md` or run `scripts/hotspot-grep.sh`.
   - For repo or dependency scans, prefer `scripts/run-local-audit.sh` over
     ad hoc command strings so availability and skip behavior stay honest.
5. Look for concrete risks, not generic category matches.
   - Secrets checked into code or written to logs/artifacts
   - Missing or weak authorization checks on real paths
   - Untrusted content reaching commands, queries, templates, or file paths
   - Unsafe file/network/process access or over-broad tool permissions
   - Dependency or install/update behavior that can silently expand risk
   - Insecure defaults, missing human gates, or unsafe automation assumptions
   - Agent-specific issues such as prompt injection exposure or tool misuse
6. Validate before escalating.
   - Cite exact files and lines.
   - Distinguish a proven issue from a suspicion or hardening opportunity.
   - If a quick local command can validate the claim safely, use it.
7. Choose the smallest honest follow-up.
   - fix now
   - create a story
   - add a guardrail, test, or validate-mode check
   - document an accepted risk
   - no finding
8. Route broader lessons correctly.
   - If the finding reveals a reusable cross-project methodology need, route it
     to Conductor alignment or ADR prep rather than inventing vague repo-local
     process.

## Tool Selection Rules

- Start with built-in and already-installed tools before adding new
  dependencies.
- Keep secret scanning separate from general code scanning; do not pretend grep
  or Semgrep replaces a dedicated secret scanner.
- Use explicit opt-in before bootstrapping missing tools from the network.
- Use explicit opt-in before Docker-backed secret scans that may need to pull an
  image.
- Treat dependency audits as one signal, not as a complete security judgment.
- Prefer deterministic local commands over hosted dashboards or CI-only flows
  for the first pass of this lane.

## Mode Guidance

- `diff`
  - read the git diff first
  - inspect changed trust boundaries manually
  - use `scripts/hotspot-grep.sh` on changed files or narrow Semgrep targets
  - do not run a full repo scan if the question is specifically about the diff
- `surface`
  - narrow to the subsystem path or trust boundary first
  - use `scripts/run-local-audit.sh <repo-root> --target <path>` when local
    scanners are helpful
- `repo`
  - use the helper script for an initial scan bundle, then manually inspect the
    surfaced hotspots and findings
- `dependency`
  - prefer package-manager or ecosystem-native tooling
  - inspect install/update scripts and lockfile behavior, not just advisory
    counts
- secret sweep
  - use `scripts/run-local-audit.sh <repo-root> --include-gitleaks` only when
    the question is specifically about leaked credentials or working-tree
    secret hygiene
  - if `gitleaks` is not installed, add `--allow-docker` to opt into the
    Docker-backed path
  - review findings carefully; generated artifacts and docs can create noisy
    generic-key matches

## Output Shape

- Findings first, ordered by severity
- Exact file references and evidence for each finding
- Assumptions and areas not reviewed
- Smallest recommended next action
- Explicit statement when no meaningful findings were found

## Guardrails

- Do not dump generic OWASP advice.
- Do not inflate severity to sound cautious.
- Do not claim exploitability without code-backed evidence.
- Do not silently broaden the audit beyond the agreed scope.
- Distinguish workflow-security issues from product-runtime issues.
- For AI-driven repos, only apply agent-specific checks when the repo actually
  exposes model, tool, or automation surfaces.
- Do not silently install scanners. If a tool requires `uvx`, `pipx`, `brew`,
  `npm`, or other downloads, say so and use explicit opt-in.
- A helper-script finding is only a lead. Read the code before calling it a bug.

## References

- `references/checklist.md` — hotspot map, search starters, audit lenses, and
  severity guidance for broad or ambiguous passes
- `references/tooling.md` — local-tool support matrix, adoption decisions, and
  scanner tradeoffs for the tracked repo mix
