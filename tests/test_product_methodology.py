from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSET_SCRIPTS = ROOT / ".agents/skills/setup-methodology/assets/product/scripts"
COMPILER = ASSET_SCRIPTS / "methodology_graph.py"
FACTS = ASSET_SCRIPTS / "triage_facts.py"


class ProductMethodologyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        docs = self.root / "docs"
        (docs / "methodology").mkdir(parents=True)
        (docs / "stories").mkdir()
        (docs / "ideal.md").write_text(
            "# A Real Product Ideal\n\nPeople can complete their work with confidence and understand what happened.\n",
            encoding="utf-8",
        )
        (docs / "spec.md").write_text(
            "# Product Spec\n\n## spec:1 Core experience\n\n### spec:1.1 Clear results\n",
            encoding="utf-8",
        )
        self.write_state()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_state(self, *, lanes: dict | None = None) -> None:
        state = {
            "project": {"name": "Sample Product", "mission": "Help people do useful work."},
            "categories": {
                "core": {"spec_ref": "spec:1", "substrate": "missing", "phase": "hold", "summary": "Initial product area."}
            },
            "lanes": lanes or {},
        }
        (self.root / "docs/methodology/state.yaml").write_text(json.dumps(state, indent=2), encoding="utf-8")

    def write_story(self, filename: str = "story-001-first-slice.md", *, spec_ref: str = "spec:1.1", depends_on: str = "[]") -> None:
        text = f'''---
title: "First useful slice"
status: "Pending"
priority: "High"
spec_refs:
  - "{spec_ref}"
category_refs:
  - "core"
depends_on: {depends_on}
---

# First useful slice
'''
        (self.root / "docs/stories" / filename).write_text(text, encoding="utf-8")

    def compiler(self, command: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(COMPILER), command, "--root", str(self.root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def facts(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(FACTS), "--json", "--root", str(self.root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_compiles_empty_product_and_checks_deterministic_relative_outputs(self) -> None:
        compiled = self.compiler("compile")
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        graph_path = self.root / "docs/methodology/graph.json"
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        self.assertEqual(graph["project"]["name"], "Sample Product")
        self.assertEqual(graph["stories"], [])
        self.assertNotIn(str(self.root), graph_path.read_text(encoding="utf-8"))
        self.assertIn("No stories yet.", (self.root / "docs/stories.md").read_text(encoding="utf-8"))
        self.assertEqual(self.compiler("check").returncode, 0)
        (self.root / "docs/stories.md").write_text("stale\n", encoding="utf-8")
        self.assertEqual(self.compiler("check").returncode, 1)

    def test_installed_scripts_resolve_the_target_root_from_their_own_location(self) -> None:
        scripts = self.root / "scripts"
        scripts.mkdir()
        shutil.copy2(COMPILER, scripts / "methodology_graph.py")
        shutil.copy2(ASSET_SCRIPTS / "triage_facts.py", scripts / "triage_facts.py")
        compiled = subprocess.run(
            [sys.executable, str(scripts / "methodology_graph.py"), "compile"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        facts = subprocess.run(
            [sys.executable, str(scripts / "triage_facts.py"), "--json"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(facts.returncode, 0, facts.stderr)
        self.assertEqual(json.loads(facts.stdout)["project"]["name"], "Sample Product")

    def test_story_refs_and_metadata_are_checked(self) -> None:
        self.write_story(spec_ref="spec:404")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown spec spec:404", result.stderr)

        self.write_story(spec_ref="spec:1.1")
        story = self.root / "docs/stories/story-001-first-slice.md"
        story.write_text(story.read_text(encoding="utf-8").replace('"core"', '"unowned"'), encoding="utf-8")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("unknown category unowned", result.stderr)

        self.write_story(spec_ref="spec:1.1")
        story = self.root / "docs/stories/story-001-first-slice.md"
        story.write_text(story.read_text(encoding="utf-8").replace('priority: "High"\n', ""), encoding="utf-8")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("requires non-empty priority", result.stderr)

    def test_duplicate_story_ids_and_missing_dependencies_fail(self) -> None:
        self.write_story()
        self.write_story("story-001-second-slice.md")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate story ID", result.stderr)

        (self.root / "docs/stories/story-001-second-slice.md").unlink()
        self.write_story(depends_on='["story-009"]')
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("depends on unknown story 9", result.stderr)

    def test_malformed_state_is_reported_as_invalid_json(self) -> None:
        (self.root / "docs/methodology/state.yaml").write_text("categories: [", encoding="utf-8")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("JSON-compatible YAML (JSON syntax)", result.stderr)

    def test_category_state_alignment_requires_every_top_level_category_once(self) -> None:
        (self.root / "docs/spec.md").write_text(
            "# Product Spec\n\n## spec:1 Core experience\n\n### spec:1.1 Clear results\n\n## spec:2 Another category\n",
            encoding="utf-8",
        )
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("missing top-level spec categories: spec:2", result.stderr)

        state_path = self.root / "docs/methodology/state.yaml"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["categories"]["another"] = {
            "spec_ref": "spec:2", "substrate": "missing", "phase": "hold", "summary": "Second area."
        }
        state_path.write_text(json.dumps(state), encoding="utf-8")
        self.assertEqual(self.compiler("compile").returncode, 0)

        state["categories"]["duplicate"] = {
            "spec_ref": "spec:1", "substrate": "missing", "phase": "hold", "summary": "Duplicate mapping."
        }
        state_path.write_text(json.dumps(state), encoding="utf-8")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("multiple state categories map to spec:1", result.stderr)

    def test_phase_enum_and_deferred_lane_trigger_are_enforced(self) -> None:
        state_path = self.root / "docs/methodology/state.yaml"
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["categories"]["core"]["phase"] = "wait"
        state_path.write_text(json.dumps(state), encoding="utf-8")
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("phase must be climb, hold, or converge", result.stderr)

        self.write_state(lanes={
            "model_eval": {"status": "deferred", "reason": "No current model question."}
        })
        result = self.compiler("compile")
        self.assertEqual(result.returncode, 2)
        self.assertIn("requires a concrete trigger", result.stderr)

    def test_sparse_facts_keep_absent_and_deferred_lanes_and_optional_aliases_distinct(self) -> None:
        self.write_state(lanes={
            "ui_scout": {"status": "absent", "reason": "No interface exists yet."},
            "model_eval": {
                "status": "deferred",
                "reason": "No AI capability question is active.",
                "trigger": "Reconsider when the product adds an AI-dependent capability.",
            },
        })
        self.assertEqual(self.compiler("compile").returncode, 0)
        result = self.facts()
        self.assertEqual(result.returncode, 0, result.stderr)
        facts = json.loads(result.stdout)
        self.assertEqual(facts["stories"], {"total": 0, "by_status": {}})
        self.assertEqual(facts["lanes"]["ui_scout"]["status"], "absent")
        self.assertEqual(facts["lanes"]["model_eval"]["status"], "deferred")
        self.assertEqual(facts["evals"], {"status": "absent", "total": 0})
        self.assertEqual(facts["skills"]["canonical"]["status"], "absent")
        self.assertEqual(facts["skills"]["command_aliases"]["status"], "absent")
        self.assertEqual(facts["skills"]["compatibility_links"]["status"], "absent")

    def test_compatibility_link_facts_distinguish_valid_links_absence_and_drift(self) -> None:
        (self.root / ".agents/skills").mkdir(parents=True)
        (self.root / ".claude").mkdir()
        (self.root / ".cursor").mkdir()
        (self.root / ".claude/skills").symlink_to("../.agents/skills")
        (self.root / ".cursor/skills").symlink_to("../.agents/skills")
        (self.root / "skills").symlink_to(".agents/skills")
        self.assertEqual(self.compiler("compile").returncode, 0)
        facts = json.loads(self.facts().stdout)
        self.assertEqual(facts["skills"]["compatibility_links"]["status"], "present")

        (self.root / ".cursor/skills").unlink()
        (self.root / ".cursor/skills").symlink_to("../.agents/not-skills")
        facts = json.loads(self.facts().stdout)
        self.assertEqual(facts["skills"]["compatibility_links"]["status"], "drift")
        self.assertEqual(facts["skills"]["compatibility_links"]["links"][".cursor/skills"]["status"], "drift")

        (self.root / ".cursor/skills").unlink()
        (self.root / ".cursor/skills").symlink_to("../.agents/skills")
        (self.root / "skills").unlink()
        (self.root / "skills").mkdir()
        facts = json.loads(self.facts().stdout)
        self.assertEqual(facts["skills"]["compatibility_links"]["status"], "drift")
        self.assertEqual(facts["skills"]["compatibility_links"]["links"]["skills"]["status"], "drift")

    def test_malformed_optional_eval_registry_is_not_reported_as_empty(self) -> None:
        self.assertEqual(self.compiler("compile").returncode, 0)
        evals = self.root / "docs/evals/registry.yaml"
        evals.parent.mkdir(parents=True)
        evals.write_text("evals: [", encoding="utf-8")
        result = self.facts()
        self.assertEqual(result.returncode, 1)
        facts = json.loads(result.stdout)
        self.assertEqual(facts["status"], "invalid")
        self.assertEqual(facts["evals"]["status"], "invalid")
        self.assertIn("JSON-compatible YAML (JSON syntax)", facts["errors"][0])

    def test_malformed_graph_is_reported_as_invalid_not_zero_stories(self) -> None:
        (self.root / "docs/methodology/graph.json").write_text('{"stories": [null]}', encoding="utf-8")
        result = self.facts()
        self.assertEqual(result.returncode, 1)
        facts = json.loads(result.stdout)
        self.assertEqual(facts["inputs"]["graph"], "invalid")
        self.assertEqual(facts["status"], "invalid")
        self.assertTrue(any("malformed story record" in item for item in facts["errors"]))


if __name__ == "__main__":
    unittest.main()
