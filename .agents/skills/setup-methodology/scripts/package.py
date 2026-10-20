#!/usr/bin/env python3
"""Audit or copy the explicitly selected product package, preserving existing files."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

BUNDLE = Path(__file__).resolve().parents[1]
SOURCE = BUNDLE.parents[2]
RECEIPT = Path('docs/methodology/package.json')


def relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError(f'Unsafe package path: {value}')
    return path


def manifest() -> dict:
    value = json.loads((BUNDLE / 'package.json').read_text())
    if value.get('version') != 1:
        raise ValueError('Unsupported package manifest version')
    return value


def selected_modules(data: dict, requested: list[str]) -> list[str]:
    names = set(requested or data['profiles']['product'])
    pending = list(names)
    while pending:
        name = pending.pop()
        if name not in data['modules']:
            raise ValueError(f'Unknown module: {name}')
        for dependency in data['modules'][name].get('requires', []):
            if dependency not in names:
                names.add(dependency)
                pending.append(dependency)
    return sorted(names)


def inventory(data: dict, names: list[str]) -> dict[Path, Path]:
    files = {}
    # Explicit overlays select a product variant while retaining shared helpers.
    overlays = {}
    for name in names:
        module = data['modules'][name]
        for skill in module.get('skills', []):
            root = SOURCE / '.agents/skills' / relative(skill)
            if not (root / 'SKILL.md').is_file():
                raise ValueError(f'Missing skill source: {root}')
            for path in sorted(root.rglob('*')):
                if path.is_symlink():
                    raise ValueError(f'Package source may not be a symlink: {path}')
                if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
                    files[path.relative_to(SOURCE)] = path
        for source, target in module.get('files', {}).items():
            dest = relative(target)
            if dest in files:
                raise ValueError(f'Duplicate destination: {dest}')
            files[dest] = SOURCE / relative(source)
        for source, target in module.get('overlays', {}).items():
            dest = relative(target)
            if dest in overlays:
                raise ValueError(f'Duplicate variant: {dest}')
            overlays[dest] = SOURCE / relative(source)
    files.update(overlays)
    for dest, source in files.items():
        if not source.is_file() or source.is_symlink():
            raise ValueError(f'Missing/unsafe source for {dest}: {source}')
    return files


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_destination(root: Path, dest: Path) -> Path:
    path = root / dest
    for part in [path, *path.parents]:
        if part == root:
            break
        if part.is_symlink():
            raise ValueError(f'Refusing destination symlink: {part}')
        if part != path and part.exists() and not part.is_dir():
            raise ValueError(f'Destination parent is not a directory: {part}')
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['audit', 'plan', 'install'])
    parser.add_argument('--target', type=Path)
    parser.add_argument('--modules', nargs='+', default=[])
    args = parser.parse_args(argv)
    try:
        data = manifest()
        if args.command == 'audit' and not args.modules:
            receipt = SOURCE / RECEIPT
            modules = json.loads(receipt.read_text())['modules'] if receipt.exists() else list(data['modules'])
        else:
            modules = args.modules
        names = selected_modules(data, modules)
        files = inventory(data, names)
        if args.command == 'audit':
            print(json.dumps({'status': 'ok', 'modules': names, 'source_files': len(files)}, indent=2))
            return 0
        if args.target is None:
            raise ValueError('--target is required')
        # Do not resolve away a symlinked target before detecting it.
        target = args.target.absolute()
        if not target.is_dir() or target.is_symlink():
            raise ValueError('Target must be an existing directory, not a symlink')
        target = target.resolve()
        if target == SOURCE or SOURCE in target.parents or target in SOURCE.parents:
            raise ValueError('Package target must be separate from the source checkout')
        for truth in ['docs/ideal.md', 'docs/spec.md']:
            p = safe_destination(target, Path(truth))
            if not p.is_file() or not p.read_text().strip():
                raise ValueError(f'Reviewed project-specific intake required before package installation: {truth}')
        conflicts, creates, identical = [], [], []
        for dest, source in files.items():
            path = safe_destination(target, dest)
            if not path.exists():
                creates.append(str(dest))
            elif path.is_file() and path.read_bytes() == source.read_bytes():
                identical.append(str(dest))
            else:
                conflicts.append(str(dest))
        receipt_path = safe_destination(target, RECEIPT)
        receipt = {'version': 1, 'variant': 'product', 'modules': names,
                   'files': {str(dest): digest(source) for dest, source in sorted(files.items())}}
        receipt_bytes = (json.dumps(receipt, indent=2, sort_keys=True) + '\n').encode()
        if receipt_path.exists() and (not receipt_path.is_file() or receipt_path.read_bytes() != receipt_bytes):
            conflicts.append(str(RECEIPT))
        report = {'variant': 'product', 'modules': names, 'create': creates, 'identical': identical,
                  'conflicts': conflicts, 'authored_truth': 'Ideal/Spec/state are never generated or overwritten'}
        if args.command == 'plan':
            print(json.dumps(report, indent=2))
            return 1 if conflicts else 0
        if conflicts:
            raise ValueError('No files copied. Existing files need a reviewed adaptation: ' + ', '.join(conflicts))
        # All conflicts and path hazards are checked before any target writes.
        for dest, source in sorted(files.items()):
            path = safe_destination(target, dest)
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open('xb') as stream:
                    stream.write(source.read_bytes())
                shutil.copymode(source, path)
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        if not receipt_path.exists():
            with receipt_path.open('xb') as stream:
                stream.write(receipt_bytes)
        report['status'] = 'copied; setup checklist and project evidence remain to be completed'
        print(json.dumps(report, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'package: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
