import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from quota_burn_gate import decide


def payload(used=79, weekly_used=10):
    return {"rateLimitsByLimitId": {"codex": {
        "primary": {"usedPercent": used, "windowDurationMins": 300},
        "secondary": {"usedPercent": weekly_used, "windowDurationMins": 10080},
    }}}


class BurnGateTests(unittest.TestCase):
    def test_above_reserve_can_continue(self):
        self.assertEqual(decide(payload())["action"], "continue")

    def test_exactly_twenty_and_lower_drain(self):
        for used in (80, 81, 100):
            with self.subTest(used=used):
                self.assertEqual(decide(payload(used))["action"], "drain")

    def test_weekly_window_independently_drains(self):
        self.assertEqual(decide(payload(0, 80))["action"], "drain")

    def test_missing_and_malformed_quota_drain(self):
        for value in (None, {}, payload(float("nan")), payload(True)):
            with self.subTest(value=value):
                self.assertEqual(decide(value)["reason"], "quota_unavailable")

    def test_reset_cannot_clear_latched_drain(self):
        result = decide(payload(0, 0), draining=True)
        self.assertEqual(result["action"], "drain")
        self.assertEqual(result["reason"], "already_draining")

    def test_optional_null_window_is_not_invented(self):
        value = {"rateLimits": {"primary": None, "secondary": {
            "usedPercent": 2, "windowDurationMins": 10080}}}
        self.assertEqual(decide(value)["action"], "continue")

    def test_blocked_account_drains(self):
        self.assertEqual(decide({"ordinaryUsageAllowed": False})["action"], "drain")

    def test_authoritative_bucket_does_not_fall_back(self):
        value = payload()
        value["rateLimitsByLimitId"] = {}
        value["rateLimits"] = {"primary": {"usedPercent": 0, "windowDurationMins": 300}}
        self.assertEqual(decide(value)["reason"], "quota_unavailable")


if __name__ == "__main__":
    unittest.main()
