"""Behavioral tests for the deterministic scheduled-work gate.

Collectors and dispatchers are temporary local scripts. These tests do not
contact a network, model provider, or operating-system scheduler.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[1]
JOB_SCRIPT = ROOT / ".agents/skills/setup-methodology/assets/scheduled-work/scheduled_job.py"


def _write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value), encoding="utf-8")


def _observation(*, status: str = "ok", signal: dict | None = None, period: str | None = None,
                 summary: str = "routine check", observed_at: str | None = None) -> dict:
    if observed_at is None:
        observed_at = datetime.now(timezone.utc).isoformat()
    result = {
        "status": status,
        "observed_at": observed_at,
        "signal": signal if signal is not None else {"count": 0},
        "summary": summary,
    }
    if period is not None:
        result["period"] = period
    return result


def _write_collector(directory: Path, *, delay: float = 0) -> tuple[Path, Path, Path]:
    script = directory / "collector.py"
    observation = directory / "observation.json"
    calls = directory / "collector-calls.txt"
    script.write_text(
        "import pathlib, sys, time\n"
        "pathlib.Path(sys.argv[2]).open('a').write('called\\n')\n"
        f"time.sleep({delay!r})\n"
        "print(pathlib.Path(sys.argv[1]).read_text())\n",
        encoding="utf-8",
    )
    return script, observation, calls


def _write_dispatcher(directory: Path, *, exit_code: int = 0, delay: float = 0) -> tuple[Path, Path]:
    script = directory / "dispatcher.py"
    calls = directory / "dispatches.jsonl"
    script.write_text(
        "import pathlib, sys, time\n"
        "payload = sys.stdin.read()\n"
        "with pathlib.Path(sys.argv[1]).open('a') as stream: stream.write(payload + '\\n')\n"
        f"time.sleep({delay!r})\n"
        f"raise SystemExit({exit_code})\n",
        encoding="utf-8",
    )
    return script, calls


def _make_job(
    directory: Path,
    *,
    mode: str = "monitor",
    dispatcher: bool = True,
    notify_recovery: bool = False,
    timeout_seconds: float = 2,
    max_age_seconds: float = 3600,
    collector_delay: float = 0,
    dispatcher_exit: int = 0,
    dispatcher_delay: float = 0,
) -> tuple[Path, Path, Path, Path, Path]:
    directory.mkdir(parents=True, exist_ok=True)
    collector, observation, collector_calls = _write_collector(directory, delay=collector_delay)
    dispatcher_script, dispatch_calls = _write_dispatcher(
        directory, exit_code=dispatcher_exit, delay=dispatcher_delay
    )
    config = {
        "version": 1,
        "job": "test-local-job",
        "mode": mode,
        "collector": [sys.executable, str(collector), str(observation), str(collector_calls)],
        "timeout_seconds": timeout_seconds,
        "max_age_seconds": max_age_seconds,
        "notify_recovery": notify_recovery,
    }
    if dispatcher:
        config["dispatcher"] = [sys.executable, str(dispatcher_script), str(dispatch_calls)]
    config_path = directory / "job.json"
    _write_json(config_path, config)
    state_dir = directory / "private state"
    return config_path, state_dir, observation, collector_calls, dispatch_calls


def _invoke(config: Path, state_dir: Path, action: str = "run", event_id: str | None = None):
    argv = [sys.executable, str(JOB_SCRIPT), action, "--config", str(config), "--state-dir", str(state_dir)]
    if event_id is not None:
        argv.extend(["--event-id", event_id])
    return subprocess.run(argv, capture_output=True, text=True, check=False, timeout=10)


def _receipt(result: subprocess.CompletedProcess[str]) -> dict:
    lines = result.stdout.strip().splitlines()
    if not lines:
        raise AssertionError(f"expected JSON receipt; stderr was {result.stderr!r}")
    return json.loads(lines[-1])


def _dispatches(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


class ScheduledWorkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_quiet_repeat_and_timestamp_or_prose_changes_do_not_dispatch(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root)
        _write_json(observation, _observation())

        first = _invoke(config, state)
        self.assertEqual(first.returncode, 0)
        self.assertEqual(_receipt(first)["decision"], "quiet")
        _write_json(observation, _observation(summary="A fresh narrative with no changed signal."))
        second = _invoke(config, state)

        self.assertEqual(second.returncode, 0)
        self.assertEqual(_receipt(second)["decision"], "unchanged")
        self.assertEqual(_dispatches(dispatches), [])

    def test_changed_attention_is_accepted_once(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root)
        _write_json(observation, _observation())
        self.assertEqual(_invoke(config, state).returncode, 0)
        _write_json(observation, _observation(status="attention", signal={"count": 2}))

        changed = _invoke(config, state)
        repeated = _invoke(config, state)

        self.assertEqual(_receipt(changed)["decision"], "accepted")
        self.assertEqual(_receipt(repeated)["decision"], "unchanged")
        self.assertEqual(len(_dispatches(dispatches)), 1)

    def test_attention_recovery_and_later_recurrence_each_dispatch_once(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root, notify_recovery=True)
        for status, signal in (
            ("attention", {"incident": "x"}),
            ("ok", {"incident": "x"}),
            ("attention", {"incident": "x"}),
        ):
            with self.subTest(status=status):
                _write_json(observation, _observation(status=status, signal=signal))
                result = _invoke(config, state)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(_receipt(result)["decision"], "accepted")
        self.assertEqual(len(_dispatches(dispatches)), 3)

    def test_report_period_is_part_of_identity_even_for_identical_data(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root, mode="report")
        _write_json(observation, _observation(period="2026-09"))
        september = _invoke(config, state)
        same_period = _invoke(config, state)
        _write_json(observation, _observation(period="2026-10"))
        october = _invoke(config, state)

        self.assertEqual(_receipt(september)["decision"], "accepted")
        self.assertEqual(_receipt(same_period)["decision"], "unchanged")
        self.assertEqual(_receipt(october)["decision"], "accepted")
        self.assertEqual(len(_dispatches(dispatches)), 2)

    def test_malformed_and_stale_collector_output_never_dispatch(self) -> None:
        for case, obs in (
            ("malformed", None),
            ("stale", _observation(observed_at="2020-01-01T00:00:00+00:00")),
            ("invalid-timestamp", _observation(observed_at=123)),
        ):
            with self.subTest(case=case):
                directory = self.root / case
                config, state, observation, _, dispatches = _make_job(
                    directory, max_age_seconds=60
                )
                if obs is None:
                    observation.write_text("not-json", encoding="utf-8")
                else:
                    _write_json(observation, obs)
                result = _invoke(config, state)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(_receipt(result)["decision"], "error")
                self.assertEqual(_dispatches(dispatches), [])

    def test_observation_can_expire_during_collection(self) -> None:
        config, state, observation, _, dispatches = _make_job(
            self.root, collector_delay=0.8, max_age_seconds=0.5
        )
        _write_json(observation, _observation(status="attention"))
        result = _invoke(config, state)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(_receipt(result)["decision"], "error")
        self.assertEqual(_dispatches(dispatches), [])

    def test_nonzero_collector_never_dispatches(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root)
        _write_json(observation, _observation())
        config_obj = json.loads(config.read_text())
        failing = self.root / "failing-collector.py"
        failing.write_text("raise SystemExit(3)\n", encoding="utf-8")
        config_obj["collector"] = [sys.executable, str(failing)]
        _write_json(config, config_obj)

        result = _invoke(config, state)

        self.assertEqual(result.returncode, 2)
        self.assertEqual(_receipt(result)["decision"], "error")
        self.assertEqual(_dispatches(dispatches), [])

    def test_failed_and_timed_out_dispatch_stays_uncertain_without_automatic_retry(self) -> None:
        for failure in ("nonzero", "timeout"):
            with self.subTest(failure=failure):
                directory = self.root / failure
                config, state, observation, _, dispatches = _make_job(
                    directory,
                    timeout_seconds=1.5 if failure == "timeout" else 2,
                    dispatcher_exit=1 if failure == "nonzero" else 0,
                    dispatcher_delay=3 if failure == "timeout" else 0,
                )
                _write_json(observation, _observation(status="attention", signal={"incident": "x"}))

                first = _invoke(config, state)
                second = _invoke(config, state)

                self.assertEqual(first.returncode, 2)
                self.assertEqual(_receipt(first)["decision"], "delivery_uncertain")
                self.assertTrue(_receipt(first)["dispatch_attempted"])
                self.assertEqual(second.returncode, 2)
                self.assertEqual(_receipt(second)["decision"], "delivery_uncertain")
                self.assertFalse(_receipt(second)["dispatch_attempted"])
                self.assertEqual(len(_dispatches(dispatches)), 1)

    def test_ack_and_retry_require_current_event_id_and_retry_preserves_event(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root, dispatcher_exit=1)
        _write_json(observation, _observation(status="attention", signal={"incident": "x"}))
        uncertain = _invoke(config, state)
        event_id = _receipt(uncertain)["event_id"]

        bad_ack = _invoke(config, state, "ack", "wrong-event")
        bad_retry = _invoke(config, state, "retry", "wrong-event")
        self.assertEqual(_receipt(bad_ack)["decision"], "error")
        self.assertEqual(_receipt(bad_retry)["decision"], "error")

        dispatcher = self.root / "successful-dispatcher.py"
        dispatcher.write_text(
            "import pathlib, sys\n"
            "with pathlib.Path(sys.argv[1]).open('a') as stream: stream.write(sys.stdin.read() + '\\n')\n",
            encoding="utf-8",
        )
        config_obj = json.loads(config.read_text())
        config_obj["dispatcher"] = [sys.executable, str(dispatcher), str(dispatches)]
        _write_json(config, config_obj)
        authorized_retry = _invoke(config, state, "retry", event_id)
        accepted = _invoke(config, state)

        self.assertEqual(_receipt(authorized_retry)["decision"], "retry")
        self.assertEqual(_receipt(accepted)["decision"], "accepted")
        self.assertEqual(_receipt(accepted)["event_id"], event_id)
        self.assertEqual([event["event_id"] for event in _dispatches(dispatches)], [event_id, event_id])

    def test_ack_with_current_event_id_accepts_pending_without_dispatch(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root, dispatcher_exit=1)
        _write_json(observation, _observation(status="attention", signal={"incident": "x"}))
        uncertain = _invoke(config, state)
        event_id = _receipt(uncertain)["event_id"]

        acknowledged = _invoke(config, state, "ack", event_id)
        repeated = _invoke(config, state)

        self.assertEqual(_receipt(acknowledged)["decision"], "ack")
        self.assertEqual(_receipt(repeated)["decision"], "unchanged")
        self.assertEqual(len(_dispatches(dispatches)), 1)

    def test_discard_requires_current_event_id_and_clears_pending(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root, dispatcher_exit=1)
        _write_json(observation, _observation(status="attention", signal={"incident": "x"}))
        uncertain = _invoke(config, state)
        event_id = _receipt(uncertain)["event_id"]

        rejected = _invoke(config, state, "discard", "wrong-event")
        accepted = _invoke(config, state, "discard", event_id)

        self.assertEqual(_receipt(rejected)["decision"], "error")
        self.assertEqual(_receipt(accepted)["decision"], "discard")
        saved_state = json.loads((state / "state.json").read_text())
        self.assertNotIn("pending", saved_state)
        self.assertEqual(len(_dispatches(dispatches)), 1)

    def test_prepared_request_with_stale_observation_refuses_dispatch(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root, dispatcher=False)
        _write_json(observation, _observation(status="attention", signal={"incident": "x"}))
        prepared = _invoke(config, state)
        event_id = _receipt(prepared)["event_id"]

        saved_state = json.loads((state / "state.json").read_text())
        saved_state["pending"]["observation"]["observed_at"] = "2020-01-01T00:00:00+00:00"
        _write_json(state / "state.json", saved_state)
        dispatcher, dispatches = _write_dispatcher(self.root)
        config_obj = json.loads(config.read_text())
        config_obj["dispatcher"] = [sys.executable, str(dispatcher), str(dispatches)]
        _write_json(config, config_obj)

        result = _invoke(config, state)

        self.assertEqual(result.returncode, 2)
        self.assertEqual(_receipt(result)["decision"], "error")
        self.assertFalse(_receipt(result)["dispatch_attempted"])
        self.assertEqual(_dispatches(dispatches), [])
        self.assertEqual(json.loads((state / "state.json").read_text())["pending"]["event_id"], event_id)

    def test_corrupt_or_wrong_job_state_fails_closed(self) -> None:
        values = (
            ("corrupt", "{bad-json"),
            ("wrong-version", '{"version":2,"job":"test-local-job"}'),
            ("wrong-job", '{"version":1,"job":"other-job"}'),
            ("empty-pending", '{"version":1,"job":"test-local-job","pending":{}}'),
            ("invalid-sequence", '{"version":1,"job":"test-local-job","sequence":"1"}'),
        )
        for name, state_contents in values:
            with self.subTest(state=name):
                directory = self.root / name
                config, state, observation, _, dispatches = _make_job(directory)
                _write_json(observation, _observation(status="attention", signal={"incident": "x"}))
                state.mkdir(parents=True)
                (state / "state.json").write_text(state_contents, encoding="utf-8")

                result = _invoke(config, state)

                self.assertEqual(result.returncode, 2)
                self.assertFalse(_receipt(result)["dispatch_attempted"])
                self.assertEqual(_dispatches(dispatches), [])

    def test_overlapping_invocation_skips_while_job_lock_is_held(self) -> None:
        config, state, observation, collector_calls, dispatches = _make_job(
            self.root, collector_delay=1.0
        )
        _write_json(observation, _observation())
        first = subprocess.Popen(
            [sys.executable, str(JOB_SCRIPT), "run", "--config", str(config), "--state-dir", str(state)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        deadline = time.monotonic() + 5
        while not collector_calls.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue(collector_calls.exists(), "first invocation never entered collector")

        overlapping = _invoke(config, state)
        stdout, stderr = first.communicate(timeout=5)

        self.assertEqual(first.returncode, 0, stderr)
        self.assertEqual(_receipt(overlapping)["decision"], "overlap")
        self.assertEqual(_receipt(subprocess.CompletedProcess([], 0, stdout, stderr))["decision"], "quiet")
        self.assertEqual(_dispatches(dispatches), [])

    def test_prepared_request_survives_restart_and_later_adapter_install(self) -> None:
        config, state, observation, collector_calls, dispatches = _make_job(self.root, dispatcher=False)
        _write_json(observation, _observation(status="attention", signal={"incident": "x"}))

        prepared = _invoke(config, state)
        event_id = _receipt(prepared)["event_id"]
        config_obj = json.loads(config.read_text())
        dispatcher, dispatches = _write_dispatcher(self.root)
        config_obj["dispatcher"] = [sys.executable, str(dispatcher), str(dispatches)]
        _write_json(config, config_obj)
        after_restart = _invoke(config, state)

        self.assertEqual(_receipt(prepared)["decision"], "pending_adapter")
        self.assertEqual(_receipt(after_restart)["decision"], "accepted")
        self.assertEqual(_receipt(after_restart)["event_id"], event_id)
        self.assertEqual(len(collector_calls.read_text().splitlines()), 1)
        self.assertEqual(len(_dispatches(dispatches)), 1)

        repeated = _invoke(config, state)
        self.assertEqual(_receipt(repeated)["decision"], "unchanged")
        self.assertEqual(len(_dispatches(dispatches)), 1)

    def test_policy_revision_reopens_condition_but_transport_changes_do_not(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root)
        _write_json(observation, _observation(status="attention"))
        self.assertEqual(_receipt(_invoke(config, state))["decision"], "accepted")
        data = json.loads(config.read_text())
        data["timeout_seconds"] = 10
        _write_json(config, data)
        self.assertEqual(_receipt(_invoke(config, state))["decision"], "unchanged")
        data["policy_version"] = "2"
        _write_json(config, data)
        self.assertEqual(_receipt(_invoke(config, state))["decision"], "accepted")
        self.assertEqual(len(_dispatches(dispatches)), 2)

    def test_post_dispatch_persistence_failure_preserves_attempt_evidence(self) -> None:
        config, state, observation, _, dispatches = _make_job(self.root)
        _write_json(observation, _observation(status="attention"))
        harness = self.root / 'fault.py'
        harness.write_text(
            "import importlib.util, pathlib, sys\n"
            "spec = importlib.util.spec_from_file_location('job', sys.argv[1])\n"
            "job = importlib.util.module_from_spec(spec); spec.loader.exec_module(job)\n"
            "original = job.atomic_json\n"
            "writes = 0\n"
            "def fail_third(path, value):\n"
            "    global writes\n"
            "    if path.name == 'state.json':\n"
            "        writes += 1\n"
            "        if writes == 3: raise OSError('injected persistence failure')\n"
            "    return original(path, value)\n"
            "job.atomic_json = fail_third\n"
            "raise SystemExit(job.main(sys.argv[2:]))\n"
        )
        result = subprocess.run([sys.executable, str(harness), str(JOB_SCRIPT),
                                 'run', '--config', str(config), '--state-dir', str(state)],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 2)
        receipt = _receipt(result)
        self.assertTrue(receipt['dispatch_attempted'])
        self.assertEqual(len(_dispatches(dispatches)), 1)
        self.assertEqual(json.loads((state / 'state.json').read_text())['pending']['status'], 'uncertain')
        repeated = _invoke(config, state)
        self.assertEqual(_receipt(repeated)['decision'], 'delivery_uncertain')
        self.assertEqual(len(_dispatches(dispatches)), 1)


if __name__ == "__main__":
    unittest.main()
