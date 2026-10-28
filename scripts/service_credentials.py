#!/usr/bin/env python3
"""Local service credential profiles. Output metadata only; never print values."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / ".private/service-credentials.json"
KEYS = {
    "dreamhost": {"DREAMHOST_SFTP_HOST", "DREAMHOST_SFTP_USERNAME",
                  "DREAMHOST_SFTP_PASSWORD", "DREAMHOST_API_KEY"},
    "fly": {"FLY_API_TOKEN"},
    "cloudflare": {"CLOUDFLARE_API_TOKEN", "CLOUDFLARE_ACCOUNT_ID",
                   "CLOUDFLARE_ZONE_ID", "CF_API_TOKEN"},
    "google": {"GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET",
               "GOOGLE_OAUTH_CLIENT_ID", "GOOGLE_OAUTH_CLIENT_SECRET",
               "AUTH_GOOGLE_ID", "AUTH_GOOGLE_SECRET"},
}


class CredentialError(ValueError):
    pass


def regular(path: Path) -> None:
    # Refuse parent symlinks as well as a symlink at the final component.
    if any(p.is_symlink() for p in [path, *path.parents]):
        raise CredentialError("Symlink paths are not supported")
    if path.exists() and not path.is_file():
        raise CredentialError("Expected a regular file")


def parse_literal(raw: str) -> str:
    """A deliberately small dotenv grammar; no expansion or shell parsing."""
    raw = raw.strip()
    if not raw:
        return ""
    if raw[0] not in {"'", '"'}:
        # An embedded hash/backslash is data; only whitespace introduces a comment.
        return re.split(r"\s+#", raw, maxsplit=1)[0].rstrip()
    quote = raw[0]
    chars = []
    index = 1
    while index < len(raw):
        char = raw[index]
        if char == quote:
            tail = raw[index + 1:]
            if tail.strip() and not re.fullmatch(r"\s+#.*", tail):
                raise CredentialError("Unsupported characters after quoted value")
            return "".join(chars)
        if char == "\\" and index + 1 < len(raw):
            following = raw[index + 1]
            if following in {quote, "\\"}:
                chars.append(following)
                index += 2
                continue
            # Keep unknown escapes literal rather than silently changing secrets.
        chars.append(char)
        index += 1
    raise CredentialError("Unclosed quoted value")


def read_selected(path: Path, keys: set[str], fly_config: bool = False) -> dict[str, str]:
    regular(path)
    result = {}
    for line in path.read_text().splitlines():
        pattern = r"^\s*access_token\s*:\s*(.*)$" if fly_config else r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$"
        match = re.match(pattern, line)
        if not match:
            continue
        key, raw = ("FLY_API_TOKEN", match[1]) if fly_config else (match[1], match[2])
        if key not in keys:
            continue
        if key in result:
            raise CredentialError("Duplicate selected variable")
        value = parse_literal(raw)
        if not value:
            continue
        if any(c in value for c in "\x00\n\r"):
            raise CredentialError("Selected values must be single-line literals")
        if not value or re.search(r"^(?:your[_-]|replace[_-]|changeme$|placeholder$|<)", value, re.I):
            continue
        result[key] = value
    if keys - result.keys():
        raise CredentialError("Missing, empty or placeholder selected variables")
    return result


def load(path: Path = VAULT) -> dict:
    regular(path)
    if not path.exists():
        return {"version": 1, "profiles": {}}
    if stat.S_IMODE(path.stat().st_mode) != 0o600 or stat.S_IMODE(path.parent.stat().st_mode) != 0o700:
        raise CredentialError("Vault requires file mode 0600 and directory mode 0700")
    data = json.loads(path.read_text())
    if data.get("version") != 1 or not isinstance(data.get("profiles"), dict):
        raise CredentialError("Unsupported vault format")
    return data


def save(data: dict, path: Path = VAULT) -> None:
    regular(path)
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(path.parent, 0o700)
    descriptor, name = tempfile.mkstemp(dir=path.parent, prefix=".credentials-")
    try:
        with os.fdopen(descriptor, "w") as handle:
            json.dump(data, handle, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def import_profile(data: dict, name: str, service: str, source: Path,
                   keys: set[str], scope: str, fly_config: bool = False) -> None:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,79}", name):
        raise CredentialError("Invalid profile name")
    if name in data["profiles"]:
        raise CredentialError("Profile exists; choose a new versioned name for refresh")
    if not keys or not keys <= KEYS[service] or (fly_config and service != "fly"):
        raise CredentialError("Unsupported variable selection")
    values = read_selected(source, keys, fly_config)
    data["profiles"][name] = {
        "service": service, "source": str(source.absolute()), "scope": scope,
        "copied_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "validation": "copied-only; provider validity and permissions unverified",
        "values": values,
    }


def export_profile(profile: dict, keys: set[str], target: Path) -> None:
    regular(target)
    if not keys or not keys <= profile["values"].keys():
        raise CredentialError("Select existing profile variables explicitly")
    if not target.parent.is_dir():
        raise CredentialError("Target directory must already exist")
    # Require an ignored, untracked destination in a real Git repository.
    def git(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", "-C", str(target.parent), *args], capture_output=True)
    if git("rev-parse", "--show-toplevel").returncode:
        raise CredentialError("Target must be inside a Git working tree")
    if git("ls-files", "--error-unmatch", "--", target.name).returncode == 0:
        raise CredentialError("Refusing a tracked destination")
    if git("check-ignore", "-q", "--", target.name).returncode:
        raise CredentialError("Target must be Git-ignored before export")
    # JSON is intentionally used rather than executable shell/dotenv syntax.
    # Libraries can load it literally without expansion or shell evaluation.
    payload = json.dumps({key: profile["values"][key] for key in sorted(keys)}, indent=2) + "\n"
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as handle:
        handle.write(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="Metadata only")
    imp = sub.add_parser("import-env", help="Copy only explicit service variables")
    imp.add_argument("profile")
    imp.add_argument("--service", choices=KEYS, required=True)
    imp.add_argument("--source", type=Path, required=True)
    imp.add_argument("--key", action="append", required=True)
    imp.add_argument("--scope", required=True, help="Known resource scope, or explicitly unknown")
    imp.add_argument("--fly-config", action="store_true", help="Read local flyctl access_token")
    exp = sub.add_parser("export-json", help="Copy selected keys to a NEW ignored 0600 JSON file")
    exp.add_argument("profile")
    exp.add_argument("--key", action="append", required=True)
    exp.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()
    try:
        data = load()
        if args.command == "list":
            print(json.dumps({name: {**{k: v for k, v in p.items() if k != "values"},
                                     "keys": sorted(p["values"])}
                              for name, p in data["profiles"].items()}, indent=2))
        elif args.command == "import-env":
            import_profile(data, args.profile, args.service, args.source.expanduser().absolute(),
                           set(args.key), args.scope, args.fly_config)
            save(data)
            print("Copied selected variables; provider validity unverified")
        else:
            if args.profile not in data["profiles"]:
                raise CredentialError("Unknown profile")
            export_profile(data["profiles"][args.profile], set(args.key), args.target.expanduser().absolute())
            print("Created ignored credential JSON with mode 0600")
    except (CredentialError, OSError, ValueError):
        # Never echo raw parse errors, input lines, values, or command payloads.
        print("Credential operation refused; check selection, format, permissions and destination", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
