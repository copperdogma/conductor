import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import codex_quota


def core_payload(primary_used=30, secondary_used=40, **extra):
    payload = {
        "rateLimitsByLimitId": {
            "codex": {
                "primary": {"usedPercent": primary_used, "windowDurationMins": 300},
                "secondary": {"usedPercent": secondary_used, "windowDurationMins": 10080},
            }
        }
    }
    payload.update(extra)
    return payload


class EvaluateTests(unittest.TestCase):
    def test_both_core_windows_are_assessed_and_exactly_twenty_is_eligible(self):
        result = codex_quota.evaluate(core_payload(80, 12.5))
        self.assertEqual(result["status"], "eligible")
        self.assertEqual(result["assessed_windows"], [
            {"name": "primary", "duration_mins": 300, "remaining_percent": 20.0},
            {"name": "secondary", "duration_mins": 10080, "remaining_percent": 87.5},
        ])
        self.assertNotIn("codex", json.dumps(result))

    def test_any_window_below_twenty_blocks(self):
        result = codex_quota.evaluate(core_payload(81, 0))
        self.assertEqual(result["status"], "blocked")
        self.assertEqual([w["remaining_percent"] for w in result["assessed_windows"]], [19.0, 100.0])

    def test_secondary_below_twenty_blocks_independently(self):
        result = codex_quota.evaluate({"rateLimits": {
            "primary": {"usedPercent": 10, "windowDurationMins": 300},
            "secondary": {"usedPercent": 81, "windowDurationMins": 10080},
        }})
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["assessed_windows"][1]["remaining_percent"], 19.0)

    def test_weekly_only_core_window_is_eligible(self):
        result = codex_quota.evaluate({"rateLimits": {
            "secondary": {"usedPercent": 79, "windowDurationMins": 10080},
        }})
        self.assertEqual(result["status"], "eligible")
        self.assertEqual(result["assessed_windows"], [
            {"name": "secondary", "duration_mins": 10080, "remaining_percent": 21.0},
        ])

    def test_ordinary_usage_false_blocks_even_without_windows(self):
        result = codex_quota.evaluate({"rateLimits": {"ordinaryUsageAllowed": False}})
        self.assertEqual(result, {"status": "blocked", "assessed_windows": []})

    def test_either_explicit_false_usage_flag_blocks_conflicts(self):
        core = {"primary": {"usedPercent": 0, "windowDurationMins": 300}}
        cases = (
            {"ordinaryUsageAllowed": True, "rateLimits": {**core, "ordinaryUsageAllowed": False}},
            {"ordinaryUsageAllowed": None, "rateLimits": {**core, "ordinaryUsageAllowed": False}},
            {"ordinaryUsageAllowed": False, "rateLimits": {**core, "ordinaryUsageAllowed": True}},
        )
        for payload in cases:
            with self.subTest(payload=payload):
                self.assertEqual(codex_quota.evaluate(payload)["status"], "blocked")

    def test_valid_true_usage_flags_and_optional_null_are_allowed(self):
        core = {"primary": {"usedPercent": 0, "windowDurationMins": 300}}
        cases = (
            {"ordinaryUsageAllowed": True, "rateLimits": core},
            {"ordinaryUsageAllowed": None, "rateLimits": {**core, "ordinaryUsageAllowed": None}},
            {"rateLimits": {**core, "ordinaryUsageAllowed": True}},
        )
        for payload in cases:
            with self.subTest(payload=payload):
                self.assertEqual(codex_quota.evaluate(payload)["status"], "eligible")

    def test_malformed_selected_bucket_usage_flag_is_unavailable_even_with_top_true(self):
        payload = {
            "ordinaryUsageAllowed": True,
            "rateLimits": {
                "ordinaryUsageAllowed": "yes",
                "primary": {"usedPercent": 0, "windowDurationMins": 300},
            },
        }
        self.assertEqual(codex_quota.evaluate(payload)["status"], "unavailable")

    def test_missing_usage_flag_does_not_block_when_window_is_usable(self):
        payload = {"rateLimits": {"primary": {"usedPercent": 0, "windowDurationMins": 300}}}
        self.assertEqual(codex_quota.evaluate(payload)["status"], "eligible")

    def test_unavailable_when_no_core_window_can_be_assessed(self):
        for payload in (
            {},
            {"rateLimits": {"primary": {"usedPercent": 10, "windowDurationMins": 60}}},
            {"rateLimitsByLimitId": {"codex": {}}, "rateLimits": core_payload()["rateLimitsByLimitId"]["codex"]},
        ):
            with self.subTest(payload=payload):
                self.assertEqual(codex_quota.evaluate(payload)["status"], "unavailable")

    def test_by_id_mapping_is_authoritative_and_legacy_is_only_fallback(self):
        good = {"rateLimits": {"primary": {"usedPercent": 0, "windowDurationMins": 300}}}
        self.assertEqual(codex_quota.evaluate(good)["status"], "eligible")
        mixed = {
            "rateLimitsByLimitId": {"codex": None},
            "rateLimits": good["rateLimits"],
        }
        self.assertEqual(codex_quota.evaluate(mixed)["status"], "unavailable")
        preferred = {
            "rateLimitsByLimitId": {"codex": {"primary": {"usedPercent": 90, "windowDurationMins": 300}}},
            "rateLimits": good["rateLimits"],
        }
        self.assertEqual(codex_quota.evaluate(preferred)["status"], "blocked")

    def test_malformed_core_window_and_percent_are_unavailable(self):
        cases = [
            {"primary": "bad"},
            {"primary": {"usedPercent": True, "windowDurationMins": 300}},
            {"primary": {"usedPercent": float("nan"), "windowDurationMins": 300}},
            {"primary": {"usedPercent": float("inf"), "windowDurationMins": 300}},
            {"primary": {"usedPercent": -1, "windowDurationMins": 300}},
            {"primary": {"usedPercent": 101, "windowDurationMins": 300}},
        ]
        for limits in cases:
            with self.subTest(limits=limits):
                self.assertEqual(codex_quota.evaluate({"rateLimits": limits})["status"], "unavailable")

    def test_malformed_present_duration_is_unavailable(self):
        for duration in (None, "300", True, 300.0, float("nan")):
            with self.subTest(duration=duration):
                payload = {"rateLimits": {"primary": {"usedPercent": 0, "windowDurationMins": duration}}}
                self.assertEqual(codex_quota.evaluate(payload)["status"], "unavailable")

    def test_absent_slot_is_not_invented_and_known_non_core_slot_is_ignored(self):
        payload = {"rateLimits": {
            "primary": {"usedPercent": 0, "windowDurationMins": 300},
            "secondary": {"usedPercent": 99, "windowDurationMins": 60},
        }}
        result = codex_quota.evaluate(payload)
        self.assertEqual(result["status"], "eligible")
        self.assertEqual([window["name"] for window in result["assessed_windows"]], ["primary"])

    def test_invalid_ordinary_usage_flag_is_unavailable(self):
        payload = core_payload(ordinaryUsageAllowed="yes")
        self.assertEqual(codex_quota.evaluate(payload)["status"], "unavailable")

    def test_core_window_duration_may_appear_in_either_slot(self):
        payload = {"rateLimits": {
            "primary": {"usedPercent": 20, "windowDurationMins": 10080},
            "secondary": {"usedPercent": 10, "windowDurationMins": 300},
        }}
        result = codex_quota.evaluate(payload)
        self.assertEqual(result["status"], "eligible")
        self.assertEqual([w["duration_mins"] for w in result["assessed_windows"]], [10080, 300])


class TransportTests(unittest.TestCase):
    def _fake_codex(self, directory, body):
        exe = Path(directory) / "codex-fake"
        exe.write_text("#!/usr/bin/env python3\n" + body, encoding="utf-8")
        exe.chmod(0o700)
        return str(exe)

    def test_transport_injection_receives_executable_and_clamped_timeout(self):
        seen = []
        payload = {"rateLimits": {"primary": {"usedPercent": 0, "windowDurationMins": 300}}}
        result = codex_quota.read_quota("fake-codex", timeout=99,
                                        transport=lambda exe, timeout: (seen.append((exe, timeout)) or payload))
        self.assertEqual(result["status"], "eligible")
        self.assertEqual(seen, [("fake-codex", 12.0)])

    def test_jsonl_subprocess_protocol_and_distilled_success(self):
        script = r'''
import json, sys
initialize = json.loads(sys.stdin.readline())
assert initialize["method"] == "initialize"
assert initialize["params"]["clientInfo"] == {"name":"conductor-quota-gate","title":"Conductor quota gate","version":"1.0"}
print(json.dumps({"jsonrpc":"2.0","id":1,"result":{}}), flush=True)
initialized = json.loads(sys.stdin.readline())
request = json.loads(sys.stdin.readline())
assert initialized["method"] == "initialized"
assert initialized["jsonrpc"] == "2.0" and "id" not in initialized
assert request["method"] == "account/rateLimits/read" and request["params"] == {}
assert not sys.stdin.closed
print(json.dumps({"jsonrpc":"2.0","id":2,"result":{"rateLimits":{"primary":{"usedPercent":80,"windowDurationMins":300}}}}), flush=True)
assert sys.stdin.read() == ""
'''
        with tempfile.TemporaryDirectory() as directory:
            codex = self._fake_codex(directory, script)
            result = codex_quota.read_quota(codex, timeout=2)
        self.assertEqual(result["status"], "eligible")
        self.assertEqual(result["assessed_windows"][0]["remaining_percent"], 20.0)
        self.assertNotIn("token", json.dumps(result).lower())

    def test_json_rpc_error_is_unavailable_without_returning_server_text(self):
        script = r'''
import json, sys
initialize = json.loads(sys.stdin.readline())
assert initialize["method"] == "initialize"
print(json.dumps({"jsonrpc":"2.0","id":1,"result":{}}), flush=True)
json.loads(sys.stdin.readline())
json.loads(sys.stdin.readline())
print(json.dumps({"jsonrpc":"2.0","id":2,"error":{"code":-1,"message":"private details"}}), flush=True)
'''
        with tempfile.TemporaryDirectory() as directory:
            result = codex_quota.read_quota(self._fake_codex(directory, script), timeout=2)
        self.assertEqual(result, {"status": "unavailable", "assessed_windows": [], "reason": "quota_rpc_error"})
        self.assertNotIn("private", json.dumps(result))

    def test_timeout_terminates_and_reaps_fake_server(self):
        with tempfile.TemporaryDirectory() as directory:
            pid_file = Path(directory) / "pid"
            script = f'''
import json, os, sys, time
open({str(pid_file)!r}, "w").write(str(os.getpid()))
initialize = json.loads(sys.stdin.readline())
print(json.dumps({{"jsonrpc":"2.0","id":1,"result":{{}}}}), flush=True)
json.loads(sys.stdin.readline())
json.loads(sys.stdin.readline())
time.sleep(20)
'''
            codex = self._fake_codex(directory, script)
            start = time.monotonic()
            result = codex_quota.read_quota(codex, timeout=1.0)
            elapsed = time.monotonic() - start
            self.assertEqual(result["status"], "unavailable")
            self.assertEqual(result["reason"], "timeout")
            self.assertLess(elapsed, 2)
            pid = int(pid_file.read_text(encoding="utf-8"))
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)

    def test_bad_executable_is_compact_unavailable(self):
        result = codex_quota.read_quota("/no/such/codex", timeout=0.2)
        self.assertEqual(result["status"], "unavailable")
        self.assertNotIn("/no/such/codex", json.dumps(result))


if __name__ == "__main__":
    unittest.main()
