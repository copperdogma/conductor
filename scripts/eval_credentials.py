#!/usr/bin/env python3
"""Safely manage Conductor's local evaluation-credential environment."""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import tempfile
from pathlib import Path


DEFAULT_VAULT = Path.home() / ".config" / "conductor" / "eval-credentials.env"
PROVIDER_VARIABLES = {
    "deepseek": "EVAL_DEEPSEEK_API_KEY",
    "mistral": "EVAL_MISTRAL_API_KEY",
    "moonshot": "EVAL_MOONSHOT_API_KEY",
    "openrouter": "EVAL_OPENROUTER_API_KEY",
    "xai": "EVAL_XAI_API_KEY",
    "zai": "EVAL_ZAI_API_KEY",
}
ASSIGNMENT_RE = re.compile(
    r"^(?P<prefix>\s*(?:export\s+)?)"
    r"(?P<key>[A-Za-z_][A-Za-z0-9_]*)"
    r"(?P<separator>\s*=\s*)"
    r"(?P<value>.*)$"
)


class CredentialError(RuntimeError):
    """Raised for fail-closed credential operations."""


def vault_path(raw: str | None) -> Path:
    if raw:
        return Path(raw).expanduser().resolve(strict=False)
    configured = os.environ.get("CONDUCTOR_EVAL_ENV_FILE")
    if configured:
        return Path(configured).expanduser().resolve(strict=False)
    return DEFAULT_VAULT


def ensure_regular_or_missing(path: Path, *, purpose: str) -> None:
    if path.is_symlink():
        raise CredentialError(f"Refusing symlink {purpose}: {path}")
    if path.exists() and not path.is_file():
        raise CredentialError(f"Expected regular-file {purpose}: {path}")


def parse_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
        if raw.strip().startswith('"'):
            value = value.replace("\\\"", '"').replace("\\\\", "\\")
    if not value:
        raise CredentialError("Credential value is empty")
    if any(character in value for character in ("\x00", "\n", "\r")):
        raise CredentialError("Credential value contains an unsupported control character")
    return value


def read_assignments(path: Path) -> dict[str, str]:
    ensure_regular_or_missing(path, purpose="environment file")
    if not path.exists():
        return {}
    result: dict[str, str] = {}
    for raw_line in path.read_text().splitlines():
        match = ASSIGNMENT_RE.match(raw_line)
        if not match:
            continue
        key = match.group("key")
        if key in result:
            raise CredentialError(f"Duplicate variable in {path}: {key}")
        result[key] = parse_value(match.group("value"))
    return result


def quoted(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', "\\\"")
    return f'"{escaped}"'


def updated_text(existing: str, key: str, value: str | None) -> str:
    lines = existing.splitlines()
    found = False
    output: list[str] = []
    for line in lines:
        match = ASSIGNMENT_RE.match(line)
        if not match or match.group("key") != key:
            output.append(line)
            continue
        if found:
            raise CredentialError(f"Duplicate target variable: {key}")
        found = True
        if value is not None:
            output.append(f"{key}={quoted(value)}")
    if value is not None and not found:
        if output and output[-1] != "":
            output.append("")
        output.append(f"{key}={quoted(value)}")
    return "\n".join(output).rstrip() + ("\n" if output else "")


def atomic_write(path: Path, text: str, *, private_parent: bool = False) -> None:
    ensure_regular_or_missing(path, purpose="target environment file")
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if private_parent:
        os.chmod(path.parent, 0o700)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o600)
        os.replace(temporary, path)
        os.chmod(path, 0o600)
    finally:
        if temporary.exists():
            temporary.unlink()


def provider_variable(provider: str) -> str:
    try:
        return PROVIDER_VARIABLES[provider]
    except KeyError as error:
        supported = ", ".join(sorted(PROVIDER_VARIABLES))
        raise CredentialError(f"Unsupported provider {provider!r}; choose {supported}") from error


def validate_variable_name(name: str) -> None:
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        raise CredentialError(f"Invalid environment variable name: {name!r}")


def import_credential(args: argparse.Namespace) -> None:
    validate_variable_name(args.source_var)
    source = Path(args.source_env).expanduser().resolve(strict=True)
    assignments = read_assignments(source)
    if args.source_var not in assignments:
        raise CredentialError(f"Source variable is not configured: {args.source_var}")
    destination = vault_path(args.vault)
    central_key = provider_variable(args.provider)
    central_assignments = read_assignments(destination)
    if central_key in central_assignments and not args.replace:
        raise CredentialError(
            f"Central credential already exists; pass --replace to rotate: {args.provider}"
        )
    existing = destination.read_text() if destination.exists() else ""
    atomic_write(
        destination,
        updated_text(existing, central_key, assignments[args.source_var]),
        private_parent=True,
    )
    print(f"{args.provider}: imported into {destination} as {central_key}")


def copy_credential(args: argparse.Namespace) -> None:
    validate_variable_name(args.target_var)
    source = vault_path(args.vault)
    assignments = read_assignments(source)
    central_key = provider_variable(args.provider)
    if central_key not in assignments:
        raise CredentialError(f"Central evaluation credential is not configured: {args.provider}")
    target = Path(args.target_env).expanduser().resolve(strict=False)
    existing = target.read_text() if target.exists() else ""
    target_assignments = read_assignments(target)
    if args.target_var in target_assignments:
        raise CredentialError(
            "Target variable already exists; use the owner credential or "
            f"choose a new ignored env: {args.target_var}"
        )
    atomic_write(target, updated_text(existing, args.target_var, assignments[central_key]))
    print(f"{args.provider}: copied to {target} as {args.target_var}")


def remove_credential(args: argparse.Namespace) -> None:
    validate_variable_name(args.target_var)
    target = Path(args.target_env).expanduser().resolve(strict=False)
    ensure_regular_or_missing(target, purpose="target environment file")
    if not target.exists():
        print(f"{args.target_var}: target file absent; nothing to remove")
        return
    atomic_write(target, updated_text(target.read_text(), args.target_var, None))
    print(f"{args.target_var}: removed from {target}")


def status(args: argparse.Namespace) -> None:
    source = vault_path(args.vault)
    assignments = read_assignments(source)
    configured = {
        provider: variable in assignments
        for provider, variable in sorted(PROVIDER_VARIABLES.items())
    }
    payload = {
        "vault": str(source),
        "exists": source.exists(),
        "mode": oct(stat.S_IMODE(source.stat().st_mode)) if source.exists() else None,
        "configured": configured,
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return
    print(f"vault: {source}")
    print(f"mode: {payload['mode'] or 'missing'}")
    for provider, present in configured.items():
        print(f"{provider}: {'configured' if present else 'missing'}")


def check(args: argparse.Namespace) -> None:
    source = vault_path(args.vault)
    assignments = read_assignments(source)
    unknown = sorted(set(assignments) - set(PROVIDER_VARIABLES.values()))
    if unknown:
        raise CredentialError("Unknown central variables: " + ", ".join(unknown))
    if source.exists() and stat.S_IMODE(source.stat().st_mode) != 0o600:
        raise CredentialError(f"Credential vault mode must be 0600: {source}")
    print(f"credential vault check: OK ({len(assignments)} configured providers)")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    subparsers = root.add_subparsers(dest="command", required=True)

    import_parser = subparsers.add_parser("import", help="Import one key without printing it")
    import_parser.add_argument("--provider", required=True, choices=sorted(PROVIDER_VARIABLES))
    import_parser.add_argument("--source-env", required=True)
    import_parser.add_argument("--source-var", required=True)
    import_parser.add_argument("--vault")
    import_parser.add_argument(
        "--replace", action="store_true", help="Explicitly rotate an existing provider key"
    )
    import_parser.set_defaults(func=import_credential)

    copy_parser = subparsers.add_parser("copy", help="Copy one central key into an owner env")
    copy_parser.add_argument("--provider", required=True, choices=sorted(PROVIDER_VARIABLES))
    copy_parser.add_argument("--target-env", required=True)
    copy_parser.add_argument("--target-var", required=True)
    copy_parser.add_argument("--vault")
    copy_parser.set_defaults(func=copy_credential)

    remove_parser = subparsers.add_parser("remove", help="Remove one injected owner variable")
    remove_parser.add_argument("--target-env", required=True)
    remove_parser.add_argument("--target-var", required=True)
    remove_parser.set_defaults(func=remove_credential)

    status_parser = subparsers.add_parser("status", help="Show provider presence only")
    status_parser.add_argument("--vault")
    status_parser.add_argument("--json", action="store_true")
    status_parser.set_defaults(func=status)

    check_parser = subparsers.add_parser("check", help="Validate names and file permissions")
    check_parser.add_argument("--vault")
    check_parser.set_defaults(func=check)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
    except (CredentialError, OSError) as error:
        print(f"credential operation failed: {error}", file=os.sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
