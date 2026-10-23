"""Offline contract tests for the deterministic model-watch collector.

These tests deliberately exercise the public pure functions and replay CLI. They
never make network requests and never rewrite the checked-in source snapshots.
"""

from __future__ import annotations

import hashlib
import fcntl
import importlib.util
import json
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import urllib.error
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "model_watch_collect.py"
DATA = ROOT / "docs" / "model-watch" / "daily"


def load_collector():
    spec = importlib.util.spec_from_file_location("model_watch_collect", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load collector module at {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_snapshot(day: str) -> dict:
    path = DATA / f"{day}-catalogs.json"
    return json.loads(path.read_text(encoding="utf-8"))


def body_for(day: str, feed: str) -> dict:
    """Return the unwrapped saved catalog for tests that need a small fixture."""
    document = read_snapshot(day)
    return load_collector().extract_snapshot(document, feed)


def row(identity: str, modality: str = "text", **fields) -> dict:
    return {"id": identity, "architecture": {"output_modalities": [modality]}, **fields}


def catalog(rows: list[dict], total: int, next_url=None) -> dict:
    return {"data": rows, "total_count": total, "links": {"next": next_url}}


class FakeResponse:
    status = 200

    def __init__(self, url, payload, headers=None, read_error=None):
        self.url = url
        self.payload = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
        self.headers = headers or {}
        self.read_error = read_error
        self.reads = 0

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def geturl(self):
        return self.url

    def read(self, _size=-1):
        self.reads += 1
        if self.read_error:
            raise self.read_error
        if self.reads > 1:
            return b""
        return self.payload


class FakeOpener:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def open(self, request, timeout=None):
        self.requests.append((request, timeout))
        item = self.responses.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item


class SnapshotExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.collector = load_collector()

    def test_supported_envelopes_and_legacy_sample_coverage(self):
        # The saved October 20–23 files cover both sources and both modern
        # wrappers, including the sources[feed].body format.
        for day in ("2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23"):
            for feed in ("general", "decisions"):
                result = self.collector.extract_snapshot(read_snapshot(day), feed)
                self.assertEqual(result["coverage"], "complete", (day, feed))
                self.assertTrue(result["rows"], (day, feed))
                self.assertIsInstance(result.get("observed_at"), (str, type(None)))

        for day in ("2026-10-13", "2026-10-17"):
            result = self.collector.extract_snapshot(read_snapshot(day), "general")
            self.assertEqual(result["coverage"], "sample", day)
            self.assertTrue(result["rows"], day)
        for day in ("2026-10-13", "2026-10-17"):
            result = self.collector.extract_snapshot(read_snapshot(day), "decisions")
            self.assertEqual(result["coverage"], "complete", day)
            self.assertTrue(result["rows"], day)

    def test_simple_data_and_body_wrappers(self):
        rows = [row("vendor/model", name="Model")]
        for document in (
            {"general": catalog(rows, 1)},
            {"sources": {"general": {"body": catalog(rows, 1)}}},
            {"generation": {"models": rows, "count": 1}},
        ):
            result = self.collector.extract_snapshot(document, "general")
            self.assertEqual(result["coverage"], "complete")
            self.assertEqual(result["rows"], rows)

    def test_duplicate_or_malformed_ids_are_rejected(self):
        malformed = [
            {"general": catalog([{"name": "missing id"}], 1)},
            {"general": catalog([row("same/model"), row("same/model")], 2)},
            {"general": catalog([row("   ")], 1)},
            *({"general": catalog([row(identity)], 1)} for identity in ("/", "/model", "vendor/", "vendor/ model")),
        ]
        for document in malformed:
            with self.subTest(document=document), self.assertRaises((ValueError, RuntimeError)):
                self.collector.extract_snapshot(document, "general")


class ExactDiffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.collector = load_collector()

    def rows(self, day: str, feed: str):
        return self.collector.extract_snapshot(read_snapshot(day), feed)["rows"]

    def test_october_21_to_22_exact_id_changes(self):
        expected = {
            "general": (
                {"minimax/minimax-m3.1-flash", "recursive/flint-v1.0:free"},
                {"google/gemini-2.5-flash-lite:batch", "minimax/minimax-m3.1-flash:free"},
            ),
            "decisions": (
                {"baseten/elephant-1:free", "baseten/mammoth-1:free", "nace-ai/drex-max"},
                set(),
            ),
        }
        for feed, (added, removed) in expected.items():
            before = self.rows("2026-10-21", feed)
            after = self.rows("2026-10-22", feed)
            delta = self.collector.diff_rows(before, after)
            self.assertEqual(delta["comparison"], "compared")
            self.assertEqual(set(delta["added"]), added, feed)
            self.assertEqual(set(delta["removed"]), removed, feed)

    def test_october_20_to_21_and_22_to_23_are_empty_id_deltas(self):
        for older, newer in (("2026-10-20", "2026-10-21"), ("2026-10-22", "2026-10-23")):
            for feed in ("general", "decisions"):
                delta = self.collector.diff_rows(self.rows(older, feed), self.rows(newer, feed))
                self.assertEqual(delta["comparison"], "compared", (older, newer, feed))
                self.assertEqual(delta["added"], [], (older, newer, feed))
                self.assertEqual(delta["removed"], [], (older, newer, feed))

    def test_first_baseline_does_not_report_everything_as_added(self):
        delta = self.collector.diff_rows(None, self.rows("2026-10-20", "general"))
        self.assertEqual(delta["comparison"], "baseline")
        self.assertEqual(delta["added"], [])
        self.assertEqual(delta["removed"], [])

    def test_same_id_metadata_and_unknown_field_changes_are_visible(self):
        before = [{"id": "vendor/model", "name": "Before", "unknown": {"x": 1}}]
        after = [{"id": "vendor/model", "name": "After", "unknown": {"x": 2}}]
        delta = self.collector.diff_rows(before, after)
        self.assertEqual(delta["added"], [])
        self.assertEqual(delta["removed"], [])
        self.assertEqual(len(delta["changed"]), 1)
        self.assertEqual(delta["changed"][0]["id"], "vendor/model")
        fields = delta["changed"][0]["fields"]
        self.assertTrue(any("name" in path for path in fields), fields)
        self.assertTrue(any("unknown" in path for path in fields), fields)
        self.assertTrue(all(path.startswith("/") for path in fields), fields)

    def test_row_and_object_key_order_do_not_change_the_diff(self):
        before = [{"id": "b", "nested": {"x": 1, "y": 2}}, {"id": "a", "v": [1, 2]}]
        reordered = [{"v": [1, 2], "id": "a"}, {"nested": {"y": 2, "x": 1}, "id": "b"}]
        self.assertEqual(self.collector.diff_rows(before, reordered)["changed"], [])


class MockTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.collector = load_collector()
        cls.config = cls.collector.load_config(cls.collector.DEFAULT_CONFIG)

    def test_pagination_accepts_a_final_page_shorter_than_total(self):
        first_url = self.config["sources"]["general"]
        second_url = first_url + "?offset=2"
        first = FakeResponse(first_url, catalog([row("a/model"), row("b/model")], 3, "?offset=2"))
        last = FakeResponse(second_url, catalog([row("c/model")], 3))
        opener = FakeOpener([first, last])
        result = self.collector.fetch_feed("general", self.config, None,
                                           self.collector.Budget(10), opener=opener)
        self.assertEqual([item["id"] for item in result["snapshot"]["rows"]],
                         ["a/model", "b/model", "c/model"])
        self.assertEqual(len(result["pages"]), 2)
        self.assertEqual(len(opener.requests), 2)
        self.assertEqual(result["snapshot"]["total_count"], 3)

    def test_valid_304_uses_integrity_checked_complete_cache(self):
        cached_snapshot = {"coverage": "complete", "rows": [row("cached/model")],
                           "total_count": 1, "body_sha256": "verified"}
        cache = {"conditional_ok": True, "snapshot": cached_snapshot, "etag": '"etag"'}
        error = urllib.error.HTTPError(self.config["sources"]["general"], 304,
                                       "not modified", {}, None)
        opener = FakeOpener([error])
        result = self.collector.fetch_feed("general", self.config, cache,
                                           self.collector.Budget(10), opener=opener)
        self.assertEqual(result["http_status"], 304)
        self.assertEqual(result["snapshot"]["rows"], cached_snapshot["rows"])
        self.assertEqual(opener.requests[0][0].get_header("If-none-match"), '"etag"')

    def test_invalid_304_cache_and_forbidden_response_are_not_unchanged(self):
        url = self.config["sources"]["general"]
        invalid_cache = {"conditional_ok": False,
                         "snapshot": {"coverage": "sample", "rows": [row("x/model")]},
                         "etag": '"etag"'}
        cases = [
            (urllib.error.HTTPError(url, 304, "not modified", {}, None), invalid_cache),
            # A cache marked usable without a request validator cannot turn a
            # bare 304 response into an unchanged result.
            (urllib.error.HTTPError(url, 304, "not modified", {}, None),
             {"conditional_ok": True, "snapshot": {"coverage": "complete", "rows": [row("x/model")]}}),
            (urllib.error.HTTPError(url, 403, "forbidden", {}, None),
             {"conditional_ok": True, "snapshot": {"coverage": "complete", "rows": [row("x/model")]},
              "etag": '"etag"'}),
        ]
        for error, cache in cases:
            with self.subTest(status=error.code), self.assertRaises(self.collector.CollectionError):
                self.collector.fetch_feed("general", self.config, cache,
                                          self.collector.Budget(10), opener=FakeOpener([error]))

    def test_response_read_failure_does_not_return_a_snapshot(self):
        url = self.config["sources"]["general"]
        response = FakeResponse(url, b"ignored", read_error=OSError("injected read failure"))
        with self.assertRaises(self.collector.CollectionError) as caught:
            self.collector.fetch_feed("general", self.config, None,
                                      self.collector.Budget(10), opener=FakeOpener([response]))
        self.assertEqual(caught.exception.evidence["pages"], [])
        attempt = caught.exception.evidence["attempts"][0]
        self.assertEqual(attempt["http_status"], 200)
        self.assertIn("bytes", attempt)

    def test_malformed_http_200_is_committed_as_failed_source_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()

            def invalid_json_fetch(feed, config, cache, budget):
                url = config["sources"][feed]
                response = FakeResponse(url, b"{not valid json")
                return self.collector.fetch_feed(feed, config, cache, budget,
                                                 opener=FakeOpener([response]))

            receipt = self.collector.run(self.config, state_root, "collect",
                                         fetcher=invalid_json_fetch)
            self.assertEqual(receipt["status"], "unavailable")
            run_dir = state_root / "runs" / receipt["run_id"]
            record = json.loads((run_dir / "snapshot.json").read_text())
            delta = json.loads((run_dir / "delta.json").read_text())
            for feed in ("general", "decisions"):
                self.assertEqual(delta["feeds"][feed]["comparison"], "unavailable")
                self.assertEqual((run_dir / f"{feed}-page-000.json").read_bytes(), b"{not valid json")
                attempt = record["http"][feed]["attempts"][0]
                self.assertEqual(attempt["http_status"], 200)
                self.assertIn("error", delta["feeds"][feed])

    def test_transport_failure_keeps_last_good_baseline_and_never_claims_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()
            rows = {
                "general": [row("vendor/model")],
                "decisions": [row("vendor/decision", "decisions")],
            }

            def good_fetch(feed, _config, _cache, _budget):
                snapshot = {"coverage": "complete", "rows": rows[feed], "total_count": 1,
                            "observed_at": "2026-10-23T12:00:00Z", "body_sha256": "body"}
                return {"snapshot": snapshot, "pages": [b"fixture"], "http_status": 200}

            baseline = self.collector.run(self.config, state_root, "collect", fetcher=good_fetch)
            original_state = json.loads((state_root / "state.json").read_text())
            original_refs = original_state["feeds"]

            def failed_fetch(_feed, _config, _cache, _budget):
                raise self.collector.CollectionError("http_403")

            failed = self.collector.run(self.config, state_root, "collect", fetcher=failed_fetch)
            self.assertEqual(baseline["status"], "complete")
            self.assertEqual(failed["status"], "unavailable")
            state = json.loads((state_root / "state.json").read_text())
            self.assertEqual(state["feeds"], original_refs)
            delta = json.loads((state_root / "runs" / failed["run_id"] / "delta.json").read_text())
            for feed in ("general", "decisions"):
                self.assertEqual(delta["feeds"][feed]["comparison"], "unavailable")

    def test_row_order_only_change_does_not_advance_semantic_changed_at(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()
            by_feed = {
                "general": [row("vendor/a"), row("vendor/b")],
                "decisions": [row("vendor/c", "decisions"), row("vendor/d", "decisions")],
            }
            calls = {"general": 0, "decisions": 0}

            def reordered_fetch(feed, config, cache, budget):
                source_rows = list(by_feed[feed])
                if calls[feed] % 2:
                    source_rows.reverse()
                calls[feed] += 1
                response = FakeResponse(config["sources"][feed],
                                         catalog(source_rows, len(source_rows)))
                return self.collector.fetch_feed(feed, config, cache, budget,
                                                 opener=FakeOpener([response]))

            first = self.collector.run(self.config, state_root, "collect", fetcher=reordered_fetch)
            first_record = json.loads((state_root / "runs" / first["run_id"] / "snapshot.json").read_text())
            second = self.collector.run(self.config, state_root, "collect", fetcher=reordered_fetch)
            second_record = json.loads((state_root / "runs" / second["run_id"] / "snapshot.json").read_text())
            for feed in ("general", "decisions"):
                self.assertEqual(first_record["feeds"][feed]["semantic_sha256"],
                                 second_record["feeds"][feed]["semantic_sha256"])
                self.assertEqual(first_record["feeds"][feed]["semantic_changed_at"],
                                 second_record["feeds"][feed]["semantic_changed_at"])


class ReplayCliTests(unittest.TestCase):
    def run_cli(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, expected, result.stderr + result.stdout)
        try:
            receipts = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
        except json.JSONDecodeError as exc:
            self.fail(f"CLI stdout must contain compact JSON receipts: {exc}: {result.stdout!r}")
        self.assertTrue(receipts, "CLI should emit a receipt")
        for receipt in receipts:
            self.assertIn(receipt.get("status"), {"complete", "partial", "unavailable", "overlap", "error"})
        return receipts

    def test_historical_replay_persists_runs_and_survives_process_restart(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            paths = [DATA / f"2026-10-{day}-catalogs.json" for day in ("20", "21", "22", "23")]
            source_hashes = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
            receipts = self.run_cli("replay", "--state-root", state_root, "--snapshots", *paths)
            receipt = receipts[-1]
            self.assertEqual(receipt["status"], "complete")
            self.assertEqual(len(receipts), len(paths))
            self.assertTrue(receipt.get("run_id"))
            state_path = state_root / "state.json"
            first_state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertIn("config_sha256", first_state)
            self.assertIn("feeds", first_state)
            run_dirs = sorted((state_root / "runs").iterdir())
            self.assertGreaterEqual(len(run_dirs), 4)
            for run_dir in run_dirs:
                snapshot_path = run_dir / "snapshot.json"
                delta_path = run_dir / "delta.json"
                packet_path = run_dir / "packet.json"
                self.assertTrue(snapshot_path.is_file())
                self.assertTrue(delta_path.is_file())
                self.assertTrue(packet_path.is_file())
                self.assertLessEqual(packet_path.stat().st_size, 8192)
            for feed in ("general", "decisions"):
                self.assertIn(feed, first_state["feeds"])
                self.assertIn("run_id", first_state["feeds"][feed])
                self.assertIn("snapshot_sha256", first_state["feeds"][feed])

            # A second invocation reads the committed manifest and must not
            # erase or rewrite any immutable earlier run artifact.
            before = {
                path: hashlib.sha256(path.read_bytes()).hexdigest()
                for path in state_root.glob("runs/**/*")
                if path.is_file()
            }
            self.run_cli("replay", "--state-root", state_root, "--snapshots", paths[-1])
            after = {
                path: hashlib.sha256(path.read_bytes()).hexdigest()
                for path in state_root.glob("runs/**/*")
                if path.is_file()
            }
            for path, digest in before.items():
                self.assertEqual(after.get(path), digest, f"immutable run artifact changed: {path}")
            self.assertTrue(state_path.is_file())
            for path, digest in source_hashes.items():
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest,
                                 f"source snapshot was modified: {path}")

    def test_packet_remains_bounded_when_source_rows_are_large(self):
        rows = [
            row(f"synthetic/model-{n:04d}-" + "x" * 460, description="x" * 500)
            for n in range(180)
        ]
        with tempfile.TemporaryDirectory() as temp:
            snapshot_path = Path(temp) / "large.json"
            decisions = [row("test/decision", "decisions")]
            snapshot_path.write_text(json.dumps({"general": catalog(rows, len(rows)),
                                                "decisions": catalog(decisions, len(decisions))}),
                                     encoding="utf-8")
            state_root = Path(temp) / "state"
            receipt = self.run_cli("replay", "--state-root", state_root, "--snapshots", snapshot_path)[0]
            run_dir = state_root / "runs" / receipt["run_id"]
            packet = json.loads((run_dir / "packet.json").read_text(encoding="utf-8"))
            self.assertLessEqual((run_dir / "packet.json").stat().st_size, 8192)
            self.assertTrue(packet["feeds"]["general"].get("omitted_rows"), packet)
            self.assertLess(len(packet["feeds"]["general"]["selected"]), 40)
            self.assertIn("omitted_delta_details", packet)
            self.assertTrue(packet.get("review_backlog_ref"), packet)

    def test_legacy_sample_replay_never_creates_full_set_removals(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            receipt = self.run_cli("replay", "--state-root", state_root,
                                   "--snapshots", DATA / "2026-10-13-catalogs.json", expected=2)[0]
            self.assertEqual(receipt["status"], "partial")
            delta = json.loads((state_root / "runs" / receipt["run_id"] / "delta.json").read_text())
            self.assertEqual(delta["feeds"]["general"]["comparison"], "sample_only")
            self.assertNotIn("removed", delta["feeds"]["general"])

    def test_interruption_leaves_last_attempt_in_progress(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            snapshot = DATA / "2026-10-20-catalogs.json"
            code = (
                "import importlib.util,sys,time; "
                f"spec=importlib.util.spec_from_file_location('collector',{str(SCRIPT)!r}); "
                "m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); "
                "m.run=lambda *a,**k: time.sleep(20); "
                "m.main(['replay','--state-root',sys.argv[1],'--snapshots',sys.argv[2]])"
            )
            process = subprocess.Popen([sys.executable, "-c", code, str(state_root), str(snapshot)],
                                       cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            last_attempt = state_root / "last-attempt.json"
            deadline = time.monotonic() + 3
            observed = False
            while time.monotonic() < deadline:
                if last_attempt.exists():
                    try:
                        observed = json.loads(last_attempt.read_text()).get("status") == "in_progress"
                    except (OSError, json.JSONDecodeError):
                        observed = False
                    if observed:
                        break
                if process.poll() is not None:
                    break
                time.sleep(0.02)
            if not observed:
                process.kill()
                process.communicate(timeout=2)
                self.fail("collector did not persist in_progress before entering the run")
            process.send_signal(signal.SIGTERM)
            try:
                process.communicate(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.communicate(timeout=1)
                self.fail("interrupted collector did not exit promptly")
            self.assertEqual(process.returncode, -signal.SIGTERM)
            self.assertEqual(json.loads(last_attempt.read_text())["status"], "in_progress")

    def test_corrupt_state_fails_without_silently_resetting(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()
            state_file = state_root / "state.json"
            state_file.write_text("{broken", encoding="utf-8")
            receipt = self.run_cli("replay", "--state-root", state_root,
                                   "--snapshots", DATA / "2026-10-20-catalogs.json", expected=2)
            receipt = receipt[0]
            self.assertIn(receipt["status"], {"error", "unavailable"})
            self.assertEqual(state_file.read_text(encoding="utf-8"), "{broken")

    def test_existing_job_lock_reports_overlap(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()
            lock = state_root / "job.lock"
            with lock.open("a") as held_lock:
                fcntl.flock(held_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                receipt = self.run_cli("replay", "--state-root", state_root,
                                       "--snapshots", DATA / "2026-10-20-catalogs.json", expected=0)[0]
            self.assertEqual(receipt["status"], "overlap")

    def test_prepared_run_output_failure_does_not_create_a_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()
            # Block run preparation while leaving the requested input readable.
            (state_root / "runs").write_text("blocked", encoding="utf-8")
            receipt = self.run_cli("replay", "--state-root", state_root,
                                   "--snapshots", DATA / "2026-10-20-catalogs.json", expected=2)
            receipt = receipt[0]
            self.assertEqual(receipt["status"], "error")
            self.assertFalse((state_root / "state.json").exists())

    def test_commit_failure_preserves_old_manifest_and_retains_orphan_evidence(self):
        collector = load_collector()
        config = collector.load_config(collector.DEFAULT_CONFIG)
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            state_root.mkdir()
            collector.run(config, state_root, "replay", DATA / "2026-10-21-catalogs.json")
            before = (state_root / "state.json").read_bytes()
            original = collector.atomic_bytes

            def fail_manifest(path, raw):
                if path == state_root / "state.json":
                    raise OSError("injected commit failure")
                return original(path, raw)

            with mock.patch.object(collector, "atomic_bytes", side_effect=fail_manifest):
                with self.assertRaises(OSError):
                    collector.run(config, state_root, "replay", DATA / "2026-10-22-catalogs.json")
            self.assertEqual((state_root / "state.json").read_bytes(), before)
            self.assertEqual(len(list((state_root / "runs").iterdir())), 2)
            state = collector.load_state(state_root, config, "replay")
            for feed in ("general", "decisions"):
                self.assertIsNotNone(collector.previous_feed(state_root, state, feed))

    def test_replay_mode_and_config_identity_cannot_be_mixed_silently(self):
        with tempfile.TemporaryDirectory() as temp:
            state_root = Path(temp) / "state"
            snap = DATA / "2026-10-20-catalogs.json"
            self.run_cli("replay", "--state-root", state_root, "--snapshots", snap)
            alternate = Path(temp) / "alternate.json"
            collector = load_collector()
            config = collector.load_config(collector.DEFAULT_CONFIG)
            alternate.write_text(json.dumps(config, indent=3), encoding="utf-8")
            self.run_cli("replay", "--state-root", state_root, "--snapshots", snap,
                         "--config", alternate)
            config["limits"]["newest_slice"] -= 1
            alternate.write_text(json.dumps(config, separators=(",", ":")), encoding="utf-8")
            receipt = self.run_cli("replay", "--state-root", state_root, "--snapshots", snap,
                                   "--config", alternate, expected=2)
            receipt = receipt[0]
            self.assertEqual(receipt["status"], "error")


if __name__ == "__main__":
    unittest.main()
