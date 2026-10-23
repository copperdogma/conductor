"""Offline contract tests for the finite model-watch shadow scheduler.

The tests use a temporary runtime root and injected readers/collectors. They do
not invoke launchd, Codex, quota transport, or the model-watch collector.
"""

from __future__ import annotations

from datetime import date, datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "model_watch_shadow.py"
TZ = ZoneInfo("America/Edmonton")
RUNTIME_FILES = (
    "scripts/model_watch_shadow.py",
    "scripts/model_watch_collect.py",
    "scripts/codex_quota.py",
    "docs/model-watch/collector-sources.json",
)


def load_shadow():
    spec = importlib.util.spec_from_file_location("model_watch_shadow", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load shadow module at {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def manifest_for(runtime_root: Path) -> dict:
    hashes = {}
    for relative in RUNTIME_FILES:
        path = runtime_root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"offline fixture for {relative}\n", encoding="utf-8")
        hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "version": 1,
        "label": "com.copperdogma.conductor.model-watch-shadow",
        "timezone": "America/Edmonton",
        "start_date": "2026-10-24",
        "end_date": "2026-10-30",
        "hour": 7,
        "minute": 45,
        "deadline_hour": 8,
        "deadline_minute": 0,
        "quota_min_remaining_percent": 20,
        "python_path": sys.executable,
        "codex_path": "/fixture/bin/codex",
        "runtime_sha256": hashes,
    }


class ShadowFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve() / "state"
        self.runtime_root = self.root / "runtime"
        self.runtime_root.mkdir(parents=True)
        self.manifest = manifest_for(self.runtime_root)
        self.shadow = load_shadow()
        self.prepare_root(self.root, self.manifest)

    def prepare_root(self, root: Path, manifest: dict):
        root.mkdir(parents=True, exist_ok=True)
        runtime = root / "runtime"
        runtime.mkdir(parents=True, exist_ok=True)
        for relative in RUNTIME_FILES:
            path = runtime / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"offline fixture for {relative}\n", encoding="utf-8")
        root.joinpath("campaign.json").write_text(json.dumps(manifest), encoding="utf-8")
        return self.shadow.make_launchagent(root, manifest)

    def tick(self, when: datetime, *, quota=None, collector=None, **kwargs):
        calls = {"quota": 0, "collector": 0, "disable": 0}

        def read_quota():
            calls["quota"] += 1
            return quota if quota is not None else {
                "status": "eligible",
                "assessed_windows": [
                    {"name": "weekly", "duration_mins": 10080, "remaining_percent": 45},
                ],
            }

        def collect():
            calls["collector"] += 1
            return collector if collector is not None else {
                "status": "complete", "packet_ref": "runs/fixture/packet.json",
            }

        def disable():
            calls["disable"] += 1
            return True

        receipt = self.shadow.tick(
            self.root,
            now=when,
            quota_reader=read_quota,
            collector=collect,
            disabler=disable,
            zone_reader=lambda: "America/Edmonton",
            **kwargs,
        )
        return receipt, calls


class LaunchAgentPlanTests(ShadowFixture):
    def test_campaign_is_finite_and_has_seven_ticks_and_expiry(self):
        job = self.shadow.make_launchagent(self.root, self.manifest)
        entries = job["StartCalendarInterval"]
        expected = [date(2026, 10, day) for day in range(24, 31)]
        actual_tick_dates = [
            date(2026, item["Month"], item["Day"])
            for item in entries
            if item.get("Hour") == 7 and item.get("Minute") == 45
        ]
        expiry = [item for item in entries if item.get("Hour") == 0 and item.get("Minute") == 5]
        self.assertEqual(actual_tick_dates, expected)
        self.assertEqual(len(expiry), 1)
        self.assertEqual(date(2026, expiry[0]["Month"], expiry[0]["Day"]), date(2026, 10, 31))
        self.assertTrue(all("Year" not in item for item in entries))
        self.assertIs(job["RunAtLoad"], True)
        self.assertIs(job["KeepAlive"], False)

    def test_validates_campaign_bounds_and_utc_conversion(self):
        job = self.shadow.make_launchagent(self.root, self.manifest)
        # The selected 07:45 Alberta wall-clock start is 13:45 UTC while MDT
        # is active. A tick supplied in UTC must reserve the Alberta date.
        start = datetime(2026, 10, 24, 13, 45, tzinfo=timezone.utc)
        self.assertEqual(len([x for x in job["StartCalendarInterval"] if x.get("Minute") == 45]), 7)
        receipt, calls = self.tick(start)
        self.assertEqual(receipt["status"], "collected_complete")
        days = json.loads((self.root / "days.json").read_text(encoding="utf-8"))
        self.assertEqual(days["days"][0]["date"], "2026-10-24")
        for field, value in (("end_date", "2026-10-31"), ("hour", 24), ("minute", 60),
                             ("deadline_minute", 60)):
            invalid = dict(self.manifest)
            invalid[field] = value
            with self.subTest(field=field), self.assertRaises((ValueError, RuntimeError)):
                self.shadow.make_launchagent(self.root, invalid)


class AdmissionAndTimingTests(ShadowFixture):
    def test_blocked_and_unavailable_quota_never_collect(self):
        instant = datetime(2026, 10, 24, 7, 46, tzinfo=TZ)
        for quota in (
            {"status": "blocked", "assessed_windows": [{"duration_mins": 300, "remaining_percent": 19.99}]},
            {"status": "unavailable", "assessed_windows": []},
            {"status": "eligible", "assessed_windows": []},
            {"status": "eligible", "assessed_windows": [{"duration_mins": 300, "remaining_percent": 19.99}]},
        ):
            with self.subTest(quota=quota):
                root = self.root / str(len(list(self.root.iterdir())))
                self.prepare_root(root, self.manifest)
                calls = {"collector": 0}
                receipt = self.shadow.tick(
                    root, now=instant, quota_reader=lambda q=quota: q,
                    collector=lambda: calls.__setitem__("collector", calls["collector"] + 1),
                    disabler=lambda: True, zone_reader=lambda: "America/Edmonton",
                )
                self.assertIn(receipt["status"], {"quota_blocked", "quota_unavailable"})
                self.assertEqual(calls["collector"], 0)
                retry = self.shadow.tick(
                    root, now=instant.replace(minute=50),
                    quota_reader=lambda: self.fail("a quota-skipped date must not retry"),
                    collector=lambda: self.fail("a quota-skipped date must not collect later"),
                    disabler=lambda: True, zone_reader=lambda: "America/Edmonton",
                )
                self.assertEqual(retry["status"], "duplicate_day")

    def test_exactly_twenty_percent_weekly_only_is_eligible(self):
        quota = {"status": "eligible", "assessed_windows": [
            {"name": "secondary", "duration_mins": 10080, "remaining_percent": 20},
        ]}
        receipt, calls = self.tick(datetime(2026, 10, 24, 7, 46, tzinfo=TZ), quota=quota)
        self.assertEqual(receipt["status"], "collected_complete")
        self.assertEqual(calls["collector"], 1)

    def test_outside_before_missed_and_duplicate_day_do_not_collect_twice(self):
        scenarios = (
            (datetime(2026, 10, 23, 7, 50, tzinfo=TZ), "outside_window"),
            (datetime(2026, 10, 24, 7, 44, 59, tzinfo=TZ), "before_slot"),
            (datetime(2026, 10, 24, 8, 0, 1, tzinfo=TZ), "missed_window"),
            (datetime(2026, 10, 31, 7, 50, tzinfo=TZ), "expired"),
        )
        for instant, expected in scenarios:
            with self.subTest(instant=instant):
                receipt, calls = self.tick(instant)
                self.assertEqual(receipt["status"], expected)
                self.assertEqual(calls["collector"], 0)

        instant = datetime(2026, 10, 24, 7, 46, tzinfo=TZ)
        first, calls = self.tick(instant)
        second, second_calls = self.tick(instant.replace(minute=50))
        self.assertEqual(first["status"], "collected_complete")
        self.assertEqual(second["status"], "duplicate_day")
        self.assertEqual(calls["collector"], 1)
        self.assertEqual(second_calls["collector"], 0)

    def test_slot_and_deadline_boundaries_are_inclusive(self):
        for instant in (
            datetime(2026, 10, 24, 7, 45, tzinfo=TZ),
            datetime(2026, 10, 24, 8, 0, tzinfo=TZ),
        ):
            with self.subTest(instant=instant):
                root = self.root / instant.strftime("%H%M")
                self.prepare_root(root, self.manifest)
                receipt = self.shadow.tick(
                    root, now=instant,
                    quota_reader=lambda: {"status": "eligible", "assessed_windows": [
                        {"duration_mins": 300, "remaining_percent": 20},
                    ]},
                    collector=lambda: {"status": "complete", "packet_ref": "runs/boundary/packet.json"},
                    disabler=lambda: True, zone_reader=lambda: "America/Edmonton",
                )
                self.assertEqual(receipt["status"], "collected_complete")

    def test_timezone_mismatch_and_runtime_hash_drift_fail_closed(self):
        instant = datetime(2026, 10, 24, 7, 46, tzinfo=TZ)
        receipt = self.shadow.tick(
            self.root, now=instant, quota_reader=lambda: self.fail("quota must not be read"),
            collector=lambda: self.fail("collector must not run"), disabler=lambda: True,
            zone_reader=lambda: "UTC",
        )
        self.assertEqual(receipt["status"], "error")

        path = self.runtime_root / "scripts/model_watch_collect.py"
        path.write_text("changed after manifest\n", encoding="utf-8")
        receipt = self.shadow.tick(
            self.root, now=instant, quota_reader=lambda: self.fail("quota must not be read"),
            collector=lambda: self.fail("collector must not run"), disabler=lambda: True,
            zone_reader=lambda: "America/Edmonton",
        )
        self.assertEqual(receipt["status"], "error")


class ReservationAndLifecycleTests(ShadowFixture):
    def test_corrupt_or_missing_campaign_disables_without_dependencies(self):
        for raw in (b"not-json", b"{}", None):
            with self.subTest(raw=raw):
                campaign = self.root / "campaign.json"
                if raw is None:
                    campaign.unlink(missing_ok=True)
                else:
                    campaign.write_bytes(raw)
                receipt, calls = self.tick(datetime(2026, 10, 31, 0, 5, tzinfo=TZ))
                self.assertEqual(receipt["status"], "error")
                self.assertTrue(receipt["disabled"])
                self.assertEqual(calls["disable"], 1)
                self.assertEqual(calls["quota"], 0)
                self.assertEqual(calls["collector"], 0)

    def test_reserves_once_per_date_before_quota_and_survives_interruption(self):
        instant = datetime(2026, 10, 24, 7, 46, tzinfo=TZ)
        order = []

        def interrupted_quota():
            order.append("quota")
            raise RuntimeError("simulated interruption after reservation")

        receipt = self.shadow.tick(
            self.root, now=instant, quota_reader=interrupted_quota,
            collector=lambda: order.append("collector"), disabler=lambda: True,
            zone_reader=lambda: "America/Edmonton",
        )
        self.assertIn(receipt["status"], {"quota_unavailable", "error"})
        self.assertEqual(order, ["quota"])
        second = self.shadow.tick(
            self.root, now=instant.replace(minute=50),
            quota_reader=lambda: self.fail("a reserved date must not retry quota"),
            collector=lambda: self.fail("a reserved date must not retry collection"),
            disabler=lambda: True, zone_reader=lambda: "America/Edmonton",
        )
        self.assertEqual(second["status"], "duplicate_day")
        days = json.loads((self.root / "days.json").read_text(encoding="utf-8"))
        self.assertEqual(len(days["days"]), 1)
        self.assertEqual(days["days"][0]["date"], "2026-10-24")

    def test_expiry_and_last_campaign_day_disable_the_job(self):
        expiry = datetime(2026, 10, 31, 0, 5, tzinfo=TZ)
        receipt, calls = self.tick(expiry)
        self.assertEqual(receipt["status"], "expired")
        self.assertEqual(calls["disable"], 1)
        self.assertEqual(calls["quota"], 0)

        root = self.root / "final-day"
        self.prepare_root(root, self.manifest)
        receipt = self.shadow.tick(
            root, now=datetime(2026, 10, 30, 7, 46, tzinfo=TZ),
            quota_reader=lambda: {"status": "eligible", "assessed_windows": [
                {"duration_mins": 300, "remaining_percent": 50},
            ]},
            collector=lambda: {"status": "complete", "packet_ref": "runs/final/packet.json"},
            disabler=lambda: True, zone_reader=lambda: "America/Edmonton",
        )
        self.assertEqual(receipt["status"], "collected_complete")
        self.assertTrue(receipt.get("disabled") or receipt.get("campaign_complete"))

    def test_overlap_is_reported_without_running_dependencies(self):
        lock_path = self.root / "campaign.lock"
        lock_path.touch()
        import fcntl
        with lock_path.open("r+") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            receipt = self.shadow.tick(
                self.root, now=datetime(2026, 10, 24, 7, 46, tzinfo=TZ),
                quota_reader=lambda: self.fail("quota must not run under overlap"),
                collector=lambda: self.fail("collector must not run under overlap"),
                disabler=lambda: True, zone_reader=lambda: "America/Edmonton",
            )
        self.assertEqual(receipt["status"], "overlap")


if __name__ == "__main__":
    unittest.main()
