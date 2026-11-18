#!/usr/bin/env python3
"""One bounded APFS storage pass over the five retained Scout 117 worktrees."""
import argparse
from collections import Counter
import ctypes as C
from datetime import datetime, timezone
import errno
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import struct
import subprocess
import tempfile
import time
import uuid

CONDUCTOR = Path(__file__).resolve().parent.parent
EVIDENCE = CONDUCTOR / "docs/scout/evidence"
BASE = Path("/Users/cam/.codex/worktrees/gpt62-sol-20261117")
ROOTS = {
    "dossier": ("dossier", ("docs/evals/artifacts",)),
    "doc-web": ("doc-web", ("docs/evals/evidence",)),
    "storybook": ("Storybook/storybook", ("docs/evals/artifacts",)),
    "cine-forge": ("cine-forge", ("docs/evals/evidence", "docs/evals/snapshots",
                                "docs/evals/landing-fable-20261110", "benchmarks/results")),
    "boardgame-ingester": ("boardgame-ingester", ("benchmarks/results",)),
}
CURRENT = re.compile(r"scout[-_]?117|gpt[-_.]?6[-_.]?2[-_.]?sol", re.I)
SAFE_TEXT_ENCODING = b"com.apple.TextEncoding"
XATTR_READ = 0x61  # XATTR_NOFOLLOW | XATTR_SHOWCOMPRESSION | XATTR_NOFOLLOW_ANY
XATTR_WRITE = 0x41  # XATTR_NOFOLLOW | XATTR_NOFOLLOW_ANY
NOFOLLOW = 0x801   # FSOPT_NOFOLLOW | FSOPT_NOFOLLOW_ANY

class AttrList(C.Structure):
    _fields_ = [("count", C.c_uint16), ("reserved", C.c_uint16), ("common", C.c_uint32),
                ("vol", C.c_uint32), ("dir", C.c_uint32), ("file", C.c_uint32), ("fork", C.c_uint32)]

class TimeSpec(C.Structure):
    _fields_ = [("seconds", C.c_int64), ("nanos", C.c_int64)]

def bind(name, args, result):
    fn = getattr(C.CDLL(None, use_errno=True), name)
    fn.argtypes, fn.restype = args, result
    return fn

clone = bind("clonefile", [C.c_char_p, C.c_char_p, C.c_int], C.c_int)
listx = bind("listxattr", [C.c_char_p, C.c_void_p, C.c_size_t, C.c_int], C.c_ssize_t)
getx = bind("getxattr", [C.c_char_p, C.c_char_p, C.c_void_p, C.c_size_t, C.c_uint32, C.c_int], C.c_ssize_t)
setx = bind("setxattr", [C.c_char_p, C.c_char_p, C.c_void_p, C.c_size_t, C.c_uint32, C.c_int], C.c_int)
remx = bind("removexattr", [C.c_char_p, C.c_char_p, C.c_int], C.c_int)
getacl = bind("acl_get_link_np", [C.c_char_p, C.c_int], C.c_void_p)
astext = bind("acl_to_text", [C.c_void_p, C.POINTER(C.c_ssize_t)], C.c_void_p)
aclfree = bind("acl_free", [C.c_void_p], C.c_int)
getattrs = bind("getattrlist", [C.c_char_p, C.POINTER(AttrList), C.c_void_p, C.c_size_t, C.c_ulong], C.c_int)
setattrs = bind("setattrlist", [C.c_char_p, C.POINTER(AttrList), C.c_void_p, C.c_size_t, C.c_ulong], C.c_int)

def check(result):
    if result < 0:
        code = C.get_errno()
        raise OSError(code, os.strerror(code))
    return result

def clone_file(src, dst):
    # CLONE_NOFOLLOW | CLONE_ACL | CLONE_NOFOLLOW_ANY. No copy fallback.
    check(clone(os.fsencode(src), os.fsencode(dst), 0xD))

def birth(path, value=None):
    attrs = AttrList(5, 0, 0x200)  # ATTR_CMN_CRTIME
    p = os.fsencode(path)
    if value is not None:
        buf = TimeSpec(*value)
        check(setattrs(p, C.byref(attrs), C.byref(buf), C.sizeof(buf), NOFOLLOW))
        return
    buf = C.create_string_buffer(20)
    check(getattrs(p, C.byref(attrs), buf, C.sizeof(buf), NOFOLLOW))
    size, seconds, nanos = struct.unpack("=Iqq", buf.raw)
    if size != C.sizeof(buf):
        raise ValueError("unexpected-creation-time-layout")
    return seconds, nanos

def xattrs(path):
    p = os.fsencode(path)
    n = check(listx(p, None, 0, XATTR_READ))
    if not n:
        return {}
    buf = C.create_string_buffer(n)
    if check(listx(p, buf, n, XATTR_READ)) != n:
        raise ValueError("xattr-list-changed")
    result = {}
    for key in buf.raw.rstrip(b"\0").split(b"\0"):
        size = check(getx(p, key, None, 0, 0, XATTR_READ))
        value = C.create_string_buffer(size)
        if check(getx(p, key, value, size, 0, XATTR_READ)) != size:
            raise ValueError("xattr-value-changed")
        result[key] = value.raw
    return result

def acl(path):
    obj = getacl(os.fsencode(path), 0x100)  # ACL_TYPE_EXTENDED
    if not obj:
        if C.get_errno() == errno.ENOENT:
            return None
        check(-1)
    try:
        size = C.c_ssize_t()
        text = astext(obj, C.byref(size))
        if not text:
            check(-1)
        try:
            return C.string_at(text, size.value)
        finally:
            aclfree(text)
    finally:
        aclfree(obj)

def profile(path, st):
    return ((st.st_mode, st.st_uid, st.st_gid, st.st_flags), acl(path), xattrs(path))

def content_identity(s):
    return (s.st_dev, s.st_ino, s.st_mode, s.st_uid, s.st_gid, s.st_size, s.st_nlink,
            s.st_flags, s.st_blocks, s.st_mtime_ns, s.st_ctime_ns, s.st_birthtime)

def digest(path, expected):
    sha = hashlib.sha256()
    git_blob = hashlib.sha1(f"blob {expected.st_size}\0".encode())
    with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK), "rb") as f:
        if content_identity(os.fstat(f.fileno())) != content_identity(expected):
            raise ValueError("changed-before-content-read")
        while data := f.read(1024 * 1024):
            sha.update(data)
            git_blob.update(data)
        if content_identity(os.fstat(f.fileno())) != content_identity(expected):
            raise ValueError("changed-during-content-read")
    return sha.hexdigest(), git_blob.hexdigest()

def restore_text_encoding(path, existing, desired):
    p = os.fsencode(path)
    if SAFE_TEXT_ENCODING in desired:
        value = desired[SAFE_TEXT_ENCODING]
        check(setx(p, SAFE_TEXT_ENCODING, value, len(value), 0, XATTR_WRITE))
    elif SAFE_TEXT_ENCODING in existing:
        check(remx(p, SAFE_TEXT_ENCODING, XATTR_WRITE))

def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, check=True,
                            env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"}, timeout=20)
    return result.stdout

def git_status(root):
    return git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--no-renames")

def unchanged_index(root, prefixes):
    head = {}
    for line in git(root, "ls-tree", "-rz", "HEAD", "--", *prefixes).split(b"\0"):
        if line:
            fields, name = line.split(b"\t", 1)
            mode, kind, oid = fields.split()
            if kind == b"blob" and mode in (b"100644", b"100755"):
                head[name] = mode, oid
    result = {}
    for line in git(root, "ls-files", "-vz", "--stage", "--", *prefixes).split(b"\0"):
        if line:
            fields, name = line.split(b"\t", 1)
            flag, mode, oid, stage = fields.split()
            if flag == b"H" and stage == b"0" and head.get(name) == (mode, oid):
                result[name] = mode, oid
    for args in (("diff",), ("diff", "--cached")):
        for name in git(root, *args, "--no-renames", "--name-only", "-z", "--", *prefixes).split(b"\0"):
            result.pop(name, None)
    return result

def open_files():
    r = subprocess.run(["/usr/sbin/lsof", "-nP", "-Fn"], capture_output=True, timeout=15)
    if r.returncode or r.stderr:
        raise RuntimeError("could-not-check-visible-open-files")
    return {os.fsdecode(line[1:]) for line in r.stdout.splitlines() if line.startswith(b"n")}

def now():
    return datetime.now(timezone.utc).isoformat()

def probe():
    with tempfile.TemporaryDirectory(prefix=".scout117-clone-probe-", dir=BASE / "dossier") as folder:
        src, dst = Path(folder) / "source", Path(folder) / "clone"
        src.write_bytes(b"A" * 4096)
        clone_file(src, dst)
        s, t = src.stat(), dst.stat()
        value = b"UTF-8;134217984"
        restore_text_encoding(dst, {}, {SAFE_TEXT_ENCODING: value})
        encoding_ok = (xattrs(dst).get(SAFE_TEXT_ENCODING) == value
                       and SAFE_TEXT_ENCODING not in xattrs(src))
        restore_text_encoding(dst, xattrs(dst), {})
        encoding_remove_ok = SAFE_TEXT_ENCODING not in xattrs(dst)
        saved = birth(dst)
        probe_time = (saved[0] - 100, 123456789)
        birth(dst, probe_time)
        birth_ok = birth(dst) == probe_time and birth(src) != probe_time
        with dst.open("r+b") as f:
            f.write(b"B")
        src_independent = src.read_bytes() == b"A" * 4096
        with src.open("r+b") as f:
            f.write(b"C")
        dst_independent = dst.read_bytes() == b"B" + b"A" * 4095
        return {"same_volume_distinct_inodes_single_links": s.st_dev == t.st_dev and
                s.st_ino != t.st_ino and s.st_nlink == t.st_nlink == 1,
                "source_and_clone_writes_independent": src_independent and dst_independent,
                "clone_creation_time_set_exact_without_source_change": birth_ok,
                "clone_text_encoding_set_remove_without_source_change": encoding_ok and encoding_remove_ok}

def meta_reason(source, target):
    a, b = source[2], target[2]
    changed = {key for key in a.keys() | b.keys() if a.get(key) != b.get(key)}
    reasons = []
    if source[0] != target[0]:
        reasons.append("mode-owner-group-flags")
    if source[1] != target[1]:
        reasons.append("acl")
    if b"com.apple.provenance" in changed:
        reasons.append("macos-provenance-xattr")
    if b"com.apple.quarantine" in changed:
        reasons.append("macos-quarantine-xattr")
    if SAFE_TEXT_ENCODING in changed:
        reasons.append("text-encoding-xattr")
    if changed - {b"com.apple.provenance", b"com.apple.quarantine", SAFE_TEXT_ENCODING}:
        reasons.append("other-xattrs")
    return "+".join(reasons) or "same"

def inspect(src, dst, volume):
    if src.resolve(strict=True) != src or dst.resolve(strict=True) != dst:
        raise ValueError("noncanonical-or-symlinked-path")
    s, t = src.lstat(), dst.lstat()
    if (not stat.S_ISREG(s.st_mode) or not stat.S_ISREG(t.st_mode)
        or s.st_dev != volume or t.st_dev != volume or s.st_nlink != 1 or t.st_nlink != 1
        or s.st_ino == t.st_ino or s.st_size != t.st_size or t.st_size < 4096):
        raise ValueError("regular-same-volume-stable-file-check")
    return s, t

def change(owner, rel, src, dst, s, t, metadata, oid):
    sha = digest(src, s)
    if sha != digest(dst, t) or sha[1] != oid:
        raise ValueError("sha256-or-git-blob-mismatch")
    source_created, target_created = birth(src), birth(dst)
    temp = dst.with_name(f".scout117-cow-{uuid.uuid4().hex}")
    clone_file(src, temp)
    try:
        new = temp.lstat()
        actual = profile(temp, new)
        why = meta_reason(actual, metadata)
        if why == "text-encoding-xattr":
            restore_text_encoding(temp, actual[2], metadata[2])
        elif why != "same":
            raise ValueError("cloned-metadata-ineligible")
        if new.st_nlink != 1 or new.st_dev != t.st_dev or new.st_ino in (s.st_ino, t.st_ino):
            raise ValueError("temporary-clone-identity-invalid")
        if digest(temp, temp.lstat()) != sha:
            raise ValueError("temporary-clone-content-mismatch")
        os.utime(temp, ns=(t.st_atime_ns, t.st_mtime_ns), follow_symlinks=False)
        birth(temp, target_created)
        new = temp.lstat()
        if (profile(temp, new) != metadata or birth(temp) != target_created
            or (new.st_atime_ns, new.st_mtime_ns) != (t.st_atime_ns, t.st_mtime_ns)):
            raise ValueError("temporary-clone-target-metadata-mismatch")
        if (content_identity(src.lstat()) != content_identity(s)
            or content_identity(dst.lstat()) != content_identity(t)
            or profile(dst, dst.lstat()) != metadata or birth(dst) != target_created):
            raise ValueError("source-or-target-changed-before-replacement")
        os.replace(temp, dst)
    finally:
        temp.unlink(missing_ok=True)
    # After installation, any verification failure halts the entire pass.
    try:
        after, source_after = dst.lstat(), src.lstat()
        if (after.st_ino != new.st_ino or after.st_nlink != 1 or profile(dst, after) != metadata
            or birth(dst) != target_created or after.st_mtime_ns != t.st_mtime_ns
            or content_identity(source_after) != content_identity(s) or birth(src) != source_created
            or digest(src, source_after) != sha or digest(dst, after) != sha):
            raise ValueError("installed clone verification failed")
        if dst.lstat().st_atime_ns != t.st_atime_ns:
            os.utime(dst, ns=(t.st_atime_ns, t.st_mtime_ns), follow_symlinks=False)
            birth(dst, target_created)
        end = dst.lstat()
        if (end.st_atime_ns, end.st_mtime_ns) != (t.st_atime_ns, t.st_mtime_ns) or birth(dst) != target_created:
            raise ValueError("final timestamp verification failed")
    except (OSError, ValueError) as exc:
        raise RuntimeError(f"post-install verification failed for {owner}/{rel}") from exc
    return [owner, rel, t.st_size, t.st_blocks * 512, sha[0], oid, s.st_ino, t.st_ino, after.st_ino]

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="install the verified batch and write the follow-up receipt")
    apply = ap.parse_args().apply
    receipt = EVIDENCE / "scout117-local-clone-followup.json"
    if apply and receipt.exists():
        raise SystemExit("follow-up pass already recorded")
    baseline = json.loads((EVIDENCE / "scout117-local-clone-result.json").read_text())
    prev = {(r[0], r[1]) for r in baseline["files"]}
    roots, statuses, tree_info = {}, {}, {}
    for owner, (primary, prefixes) in ROOTS.items():
        source, target = CONDUCTOR.parent / primary, BASE / owner
        if any(path.resolve(strict=True) != path for path in (source, target)):
            raise SystemExit("unexpected checkout location")
        worktrees = git(target, "worktree", "list", "--porcelain").splitlines()
        if worktrees[0] != b"worktree " + os.fsencode(source):
            raise SystemExit("target is not a worktree of the known primary")
        for path in (source, target):
            if git(path, "rev-parse", "--show-object-format").strip() != b"sha1":
                raise SystemExit("unexpected git object hash format")
            statuses[path] = git_status(path)
        roots[owner] = source, target, prefixes
        tree_info[owner] = {"source_root": str(source), "target_root": str(target), "prefixes": prefixes,
                            "target_head": git(target, "rev-parse", "HEAD").decode().strip()}
    proof = probe() if apply else None
    if apply and not all(proof.values()):
        raise SystemExit("disposable probe failed")
    handles = open_files()
    last_check = time.monotonic()
    deadline = last_check + 175
    start = now()
    free_before = shutil.disk_usage(BASE).free
    queue, summary, mismatch_counts = [], {}, {}
    vol = BASE.stat().st_dev
    owner_counts = {owner: Counter() for owner in roots}
    for owner, (source, target, prefixes) in roots.items():
        source_idx, target_idx = unchanged_index(source, prefixes), unchanged_index(target, prefixes)
        for filename, item in target_idx.items():
            rel = os.fsdecode(filename)
            if (owner, rel) in prev or CURRENT.search(rel) or source_idx.get(filename) != item:
                continue
            src, dst = source / rel, target / rel
            try:
                size = dst.lstat().st_size
            except FileNotFoundError:
                continue
            if size >= 4096:
                queue.append((size, owner, rel, item[1].decode()))
    queue.sort(reverse=True)
    rows, fatal = [], None
    for i, (_, owner, rel, oid) in enumerate(queue):
        c = owner_counts[owner]
        if time.monotonic() > deadline:
            fatal = f"wall bound reached with {len(queue) - i} candidates remaining"
            break
        source, target, _ = roots[owner]
        src, dst = source / rel, target / rel
        try:
            if time.monotonic() - last_check > 12:
                handles, last_check = open_files(), time.monotonic()
            if str(src) in handles or str(dst) in handles:
                c["visible-open-file"] += 1
                continue
            s, t = inspect(src, dst, vol)
            metadata = profile(dst, t)
            why = meta_reason(profile(src, s), metadata)
            if why != "same":
                c["metadata:" + why] += 1
                c["metadata_logical_bytes:" + why] += t.st_size
            if why not in ("same", "text-encoding-xattr"):
                continue
            c["eligible_metadata_count"] += 1
            c["eligible_metadata_logical_bytes"] += t.st_size
            if apply:
                rows.append(change(owner, rel, src, dst, s, t, metadata, oid))
                c["cloned_count"] += 1
                c["cloned_logical_bytes"] += t.st_size
        except RuntimeError as exc:
            fatal = str(exc)
            break
        except (OSError, ValueError) as exc:
            c[f"skip:{exc.errno}" if isinstance(exc, OSError) else f"skip:{exc}"] += 1
    for owner, (source, target, _) in roots.items():
        tree_info[owner]["source_git_status_unchanged"] = git_status(source) == statuses[source]
        tree_info[owner]["target_git_status_unchanged"] = git_status(target) == statuses[target]
        summary[owner] = {key: val for key, val in owner_counts[owner].items() if not key.startswith("metadata")}
        mismatch_counts[owner] = {key: val for key, val in owner_counts[owner].items() if key.startswith("metadata")}
    free_after = shutil.disk_usage(BASE).free
    report = {
        "campaign": "Scout 117", "started_utc": start, "ended_utc": now(),
        "script": str(Path(__file__).resolve()), "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "mode": "apply" if apply else "inspection", "fatal": fatal,
        "sources": ["Darwin clonefile(2)", "Darwin listxattr(2), getxattr(2), setxattr(2)",
                    "Darwin getattrlist(2), setattrlist(2)", "Command Line Tools SDK sys/attr.h"],
        "method": "Each historical file is an ordinary single-link same-volume tracked file in both checkouts, matching HEAD, index, on-disk SHA-1 Git blobs and SHA-256. The primary source is read-only. Direct clonefile(2) into a unique sibling followed by verification of the temporary clone and atomic target replacement. Both hashes and target mode/owner/group/flags/ACL/xattrs and atime/mtime/creation time verified after install.",
        "metadata_policy": "Protected provenance, quarantine, other xattr mismatches, ACL and Unix metadata differences were skipped. Only the ordinary text-encoding attribute could be exactly reproduced on a temporary clone, as checked by a disposable probe. Inodes and ctime follow replacement semantics. Primary reads may update atime.",
        "scope": "Greater than or equal to 4096 logical bytes in named historical output prefixes. Prior pass paths, active campaign paths, modified/untracked files, links and visible open handles excluded. Owner runs had completed before the pass.",
        "probe": proof, "worktrees": tree_info, "eligible_index_candidates": len(queue), "owners": summary,
        "metadata_mismatches": mismatch_counts, "count": len(rows), "logical_bytes": sum(row[2] for row in rows),
        "remaining_safe_batch": ("No further verified batch in the inspected scope. Files that failed metadata or "
                                 "clone checks were left as-is." if apply and fatal is None else "Unknown."),
        "availability": {"before_bytes": free_before, "after_bytes": free_after,
                         "observed_delta_bytes": free_after - free_before,
                         "caveat": "Shared APFS volume before/after measurement includes concurrent activity and deferred filesystem reclamation."},
        "file_columns": ["owner", "relative_path", "bytes", "former_target_reported_allocated_bytes",
                         "sha256_both", "git_blob_sha1_both", "source_inode", "former_target_inode", "clone_inode"],
    }
    if apply:
        with tempfile.NamedTemporaryFile("w", dir=receipt.parent, prefix=".scout117-followup-", delete=False) as f:
            temp = Path(f.name)
            f.write(json.dumps(report, indent=2)[:-2] + ',\n  "files": [\n')
            f.write(",\n".join("    " + json.dumps(row, separators=(",", ":")) for row in rows))
            f.write("\n  ]\n}\n")
        os.chmod(temp, 0o644)
        os.replace(temp, receipt)
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
