#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF' >&2
Usage: hotspot-grep.sh <repo-root> [target]

Run a deterministic hotspot search using rg. The optional target is a path
inside the repo root and defaults to ".".
EOF
}

if [[ $# -lt 1 || $# -gt 2 ]]; then
  usage
  exit 1
fi

if ! command -v rg >/dev/null 2>&1; then
  echo "ERROR: rg is required for hotspot-grep.sh" >&2
  exit 1
fi

ROOT="$1"
TARGET="${2:-.}"

if [[ ! -d "$ROOT" ]]; then
  echo "ERROR: repo root does not exist: $ROOT" >&2
  exit 1
fi

ABS_ROOT="$(cd "$ROOT" && pwd)"
ABS_TARGET="$ABS_ROOT/$TARGET"

if [[ ! -e "$ABS_TARGET" ]]; then
  echo "ERROR: target does not exist inside repo root: $TARGET" >&2
  exit 1
fi

cd "$ABS_ROOT"

print_section() {
  local title="$1"
  local pattern="$2"
  local matches

  matches="$(rg -n --hidden \
    -g '!node_modules/**' \
    -g '!.git/**' \
    -g '!dist/**' \
    -g '!build/**' \
    -g '!coverage/**' \
    "$pattern" "$TARGET" 2>/dev/null || true)"

  echo
  echo "## $title"
  if [[ -z "$matches" ]]; then
    echo "No matches."
    return
  fi

  printf '%s\n' "$matches" | sed -n '1,20p'
  local total
  total="$(printf '%s\n' "$matches" | wc -l | tr -d ' ')"
  if [[ "$total" -gt 20 ]]; then
    echo "... ($((total - 20)) more matches omitted)"
  fi
}

echo "# Security Hotspot Grep"
echo "repo_root: $ABS_ROOT"
echo "target: $TARGET"

print_section "Possible secrets" 'API_KEY|ACCESS_KEY|SECRET(_KEY|_ACCESS_KEY)?|CLIENT_SECRET|PASSWORD|AUTH_TOKEN|ACCESS_TOKEN|REFRESH_TOKEN|PRIVATE_KEY|BEGIN (RSA|OPENSSH|PRIVATE)'
print_section "Auth and permission boundaries" 'jwt|session|cookie|csrf|authorize|permission|capability|admin|allow_origins|CORS|auth[A-Z_]|auth[.-]'
print_section "Command and process execution" 'eval\(|exec\(|subprocess|shell=True|os\.system|spawn\(|child_process|subprocess\.run\('
print_section "File and path handling" 'open\(|Path\(|unlink\(|rmtree|rm -rf|upload|download|tempfile|mktemp'
print_section "Network and callback surfaces" 'fetch\(|axios\(|requests\.|httpx\.|urllib|webhook|oauth|redirect_uri|redirectUrl'
print_section "Template and HTML sinks" 'innerHTML|dangerouslySetInnerHTML|render_template_string|Markup\('
print_section "Agent and tool boundaries" 'system prompt|tool call|function call|allowed_tools|approval|sandbox'
