#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF' >&2
Usage: run-local-audit.sh <repo-root> [options]

Options:
  --mode <repo|dependency>  Audit mode (default: repo)
  --target <path>           Relative path inside repo root for surface-focused scans
  --allow-uvx               Allow uvx bootstrap for missing Python tools
  --include-gitleaks        Run an explicit secret scan
  --allow-docker            Allow Docker-backed Gitleaks execution if local
                            gitleaks is unavailable

The script is read-only. It prints explicit skip reasons instead of silently
assuming scanners are available.
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 1
fi

ROOT="$1"
shift

MODE="repo"
TARGET="."
ALLOW_UVX=0
INCLUDE_GITLEAKS=0
ALLOW_DOCKER=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --allow-uvx)
      ALLOW_UVX=1
      shift
      ;;
    --include-gitleaks)
      INCLUDE_GITLEAKS=1
      shift
      ;;
    --allow-docker)
      ALLOW_DOCKER=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ "$MODE" != "repo" && "$MODE" != "dependency" ]]; then
  echo "ERROR: --mode must be repo or dependency" >&2
  exit 1
fi

if [[ ! -d "$ROOT" ]]; then
  echo "ERROR: repo root does not exist: $ROOT" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ABS_ROOT="$(cd "$ROOT" && pwd)"
ABS_TARGET="$ABS_ROOT/$TARGET"

if [[ ! -e "$ABS_TARGET" ]]; then
  echo "ERROR: target does not exist inside repo root: $TARGET" >&2
  exit 1
fi

have() {
  command -v "$1" >/dev/null 2>&1
}

print_header() {
  echo
  echo "## $1"
}

run_step() {
  local label="$1"
  shift

  print_header "$label"
  echo "command: $*"
  if "$@"; then
    echo "status: ok"
  else
    local rc=$?
    echo "status: command exited $rc"
  fi
}

echo "# Local Security Audit Helper"
echo "repo_root: $ABS_ROOT"
echo "target: $TARGET"
echo "mode: $MODE"
echo "allow_uvx: $ALLOW_UVX"
echo "include_gitleaks: $INCLUDE_GITLEAKS"
echo "allow_docker: $ALLOW_DOCKER"

HAS_PACKAGE_JSON=0
HAS_PNPM_LOCK=0
HAS_PYPROJECT=0

[[ -f "$ABS_ROOT/package.json" ]] && HAS_PACKAGE_JSON=1
[[ -f "$ABS_ROOT/pnpm-lock.yaml" ]] && HAS_PNPM_LOCK=1
[[ -f "$ABS_ROOT/pyproject.toml" ]] && HAS_PYPROJECT=1

print_header "Detected stack"
echo "package.json: $HAS_PACKAGE_JSON"
echo "pnpm-lock.yaml: $HAS_PNPM_LOCK"
echo "pyproject.toml: $HAS_PYPROJECT"

print_header "Tool availability"
for tool in rg semgrep pnpm npm pip-audit uv gitleaks docker; do
  if have "$tool"; then
    echo "$tool: $(command -v "$tool")"
  else
    echo "$tool: MISSING"
  fi
done

run_step "Hotspot grep" "$SCRIPT_DIR/hotspot-grep.sh" "$ABS_ROOT" "$TARGET"

if [[ "$MODE" == "repo" ]]; then
  if have semgrep; then
    run_step "Semgrep" semgrep scan --quiet --disable-version-check --config auto "$ABS_TARGET"
  else
    print_header "Semgrep"
    echo "status: skipped"
    echo "reason: semgrep is not installed"
  fi
fi

if (( HAS_PACKAGE_JSON == 1 )); then
  if (( HAS_PNPM_LOCK == 1 )) && have pnpm; then
    run_step "pnpm audit" pnpm audit --dir "$ABS_ROOT" --prod --audit-level moderate --ignore-registry-errors
  elif have npm; then
    run_step "npm audit" npm audit --prefix "$ABS_ROOT" --omit=dev --audit-level=moderate
  else
    print_header "JavaScript dependency audit"
    echo "status: skipped"
    echo "reason: package.json exists but pnpm/npm is unavailable"
  fi
fi

if (( HAS_PYPROJECT == 1 )); then
  if have pip-audit; then
    run_step "pip-audit" pip-audit --progress-spinner off "$ABS_ROOT"
  elif (( ALLOW_UVX == 1 )) && have uv; then
    run_step "pip-audit via uvx" uvx --from pip-audit pip-audit --progress-spinner off "$ABS_ROOT"
  else
    print_header "Python dependency audit"
    echo "status: skipped"
    echo "reason: pip-audit is not installed"
    if have uv; then
      echo "hint: rerun with --allow-uvx to permit uvx bootstrap"
    fi
  fi
fi

summarize_gitleaks() {
  local report_path="$1"
  python3 - "$report_path" <<'PY'
import json, pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text().strip()
if not text:
    print("status: ok")
    print("findings: 0")
    sys.exit(0)
findings = json.loads(text)
print("status: ok")
print(f"findings: {len(findings)}")
for finding in findings[:15]:
    file = finding.get("File", "")
    line = finding.get("StartLine", "?")
    rule = finding.get("RuleID", "")
    print(f"- {file}:{line} — {rule}")
if len(findings) > 15:
    print(f"... ({len(findings) - 15} more findings omitted)")
PY
}

if (( INCLUDE_GITLEAKS == 1 )); then
  print_header "Gitleaks secret scan"
  if have gitleaks; then
    echo "command: gitleaks dir $ABS_ROOT --redact --exit-code 0 --no-banner --report-format json --report-path -"
    tmp_report="$(mktemp)"
    if gitleaks dir "$ABS_ROOT" --redact --exit-code 0 --no-banner --report-format json --report-path - >"$tmp_report"; then
      summarize_gitleaks "$tmp_report"
    else
      rc=$?
      echo "status: command exited $rc"
    fi
    rm -f "$tmp_report"
  elif (( ALLOW_DOCKER == 1 )) && have docker; then
    echo "command: docker run --rm -v $ABS_ROOT:/repo ghcr.io/gitleaks/gitleaks:latest dir /repo --redact --exit-code 0 --no-banner --report-format json --report-path -"
    tmp_report="$(mktemp)"
    if docker run --rm -v "$ABS_ROOT:/repo" ghcr.io/gitleaks/gitleaks:latest dir /repo --redact --exit-code 0 --no-banner --report-format json --report-path - >"$tmp_report"; then
      summarize_gitleaks "$tmp_report"
    else
      rc=$?
      echo "status: command exited $rc"
    fi
    rm -f "$tmp_report"
  else
    echo "status: skipped"
    echo "reason: gitleaks is not installed"
    if have docker; then
      echo "hint: rerun with --allow-docker to permit Docker-backed gitleaks"
    fi
  fi
fi

print_header "Notes"
echo "- This helper is read-only and prints raw tool output to stdout."
echo "- Secret scanners are optional and are not part of the default bundle."
echo "- Any finding here still needs manual code review before it becomes a bug report."
