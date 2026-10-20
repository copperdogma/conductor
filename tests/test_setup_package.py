from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / '.agents/skills/setup-methodology/scripts/package.py'


class SetupPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='conductor-package-test-')
        self.target = Path(self.temp.name).resolve()
        (self.target / 'docs').mkdir()
        self.ideal = b'# Errands Ideal\n\nI can capture errands naturally and get a clear list without losing anything.\n'
        self.spec = b'# Errands Spec\n\n## spec:1 Capture\n\nThe first proof is offline text capture; product implementation is not present.\n'
        (self.target / 'docs/ideal.md').write_bytes(self.ideal)
        (self.target / 'docs/spec.md').write_bytes(self.spec)

    def tearDown(self):
        self.temp.cleanup()

    def run_package(self, command, *extra):
        return subprocess.run([sys.executable, str(HELPER), command, '--target', str(self.target), *extra],
                              text=True, capture_output=True)

    def assert_truth(self):
        self.assertEqual((self.target / 'docs/ideal.md').read_bytes(), self.ideal)
        self.assertEqual((self.target / 'docs/spec.md').read_bytes(), self.spec)
        self.assertFalse((self.target / 'projects.yaml').exists())
        self.assertFalse((self.target / 'docs/methodology/state.yaml').exists())

    def test_plan_has_no_mutation_and_install_preserves_truth_with_product_variants(self):
        before = sorted(p.relative_to(self.target).as_posix() for p in self.target.rglob('*'))
        plan = self.run_package('plan')
        self.assertEqual(plan.returncode, 0, plan.stderr)
        self.assertEqual(sorted(p.relative_to(self.target).as_posix() for p in self.target.rglob('*')), before)
        installed = self.run_package('install')
        self.assertEqual(installed.returncode, 0, installed.stderr)
        self.assert_truth()
        receipt = json.loads((self.target / 'docs/methodology/package.json').read_text())
        self.assertEqual(receipt['variant'], 'product')
        self.assertEqual(receipt['modules'], ['core', 'evidence'])
        product_triage = (self.target / '.agents/skills/triage/SKILL.md').read_bytes()
        self.assertEqual(product_triage, (ROOT / '.agents/skills/setup-methodology/assets/product/skills/triage.md').read_bytes())
        self.assertNotEqual(product_triage, (ROOT / '.agents/skills/triage/SKILL.md').read_bytes())
        self.assertEqual(self.run_package('install').returncode, 0)

    def test_missing_intake_and_existing_conflicts_refuse_before_copying(self):
        (self.target / 'docs/ideal.md').unlink()
        result = self.run_package('install')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.target / '.agents').exists())
        (self.target / 'docs/ideal.md').write_bytes(self.ideal)
        (self.target / 'AGENTS.md').write_text('Project-owned rules must stay.\n')
        result = self.run_package('install')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('AGENTS.md', result.stderr)
        self.assertFalse((self.target / '.agents').exists())
        self.assertEqual((self.target / 'AGENTS.md').read_text(), 'Project-owned rules must stay.\n')
        self.assert_truth()

    def test_symlink_destination_is_refused_without_writing_through(self):
        with tempfile.TemporaryDirectory(prefix='conductor-package-outside-') as outside:
            (self.target / '.agents').symlink_to(Path(outside).resolve(), target_is_directory=True)
            result = self.run_package('install')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('symlink', result.stderr)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_optional_module_selection_does_not_force_all_lanes(self):
        result = self.run_package('install', '--modules', 'core', 'ui')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.target / '.agents/skills/ui-scout/SKILL.md').is_file())
        self.assertFalse((self.target / '.agents/skills/create-eval').exists())
        self.assertFalse((self.target / '.agents/skills/triage-architecture').exists())
        self.assertFalse((self.target / 'docs/evals/registry.yaml').exists())
        receipt = json.loads((self.target / 'docs/methodology/package.json').read_text())
        self.assertEqual(receipt['modules'], ['core', 'ui'])

    def test_skill_sync_preserves_existing_real_directory(self):
        self.assertEqual(self.run_package('install', '--modules', 'core').returncode, 0)
        protected = self.target / '.cursor/skills'
        protected.mkdir(parents=True)
        (protected / 'keep.txt').write_text('keep')
        result = subprocess.run(['bash', 'scripts/sync-agent-skills.sh'], cwd=self.target, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Refusing to replace', result.stderr)
        self.assertEqual((protected / 'keep.txt').read_text(), 'keep')
        self.assertFalse((self.target / '.claude').exists())

    def test_skill_sync_refuses_symlinked_parent_without_touching_external_links(self):
        self.assertEqual(self.run_package('install', '--modules', 'core').returncode, 0)
        with tempfile.TemporaryDirectory(prefix='conductor-link-parent-') as outside:
            external = Path(outside).resolve()
            foreign = external / 'skills'
            foreign.symlink_to('keep-foreign-target')
            (self.target / '.claude').symlink_to(external, target_is_directory=True)
            result = subprocess.run(['bash', 'scripts/sync-agent-skills.sh'], cwd=self.target, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('unsafe compatibility parent', result.stderr)
            self.assertEqual(str(foreign.readlink()), 'keep-foreign-target')
            self.assertFalse((self.target / '.cursor').exists())

    def test_installed_source_audit_and_story_helper_work_without_source_checkout(self):
        result = self.run_package('install')
        self.assertEqual(result.returncode, 0, result.stderr)
        audit = subprocess.run([sys.executable, '.agents/skills/setup-methodology/scripts/package.py', 'audit'],
                               cwd=self.target, capture_output=True, text=True)
        self.assertEqual(audit.returncode, 0, audit.stderr)
        self.assertEqual(json.loads(audit.stdout)['status'], 'ok')
        story = subprocess.run(['bash', '.agents/skills/create-story/scripts/start-story.sh', 'first-capture'],
                               cwd=self.target, capture_output=True, text=True)
        self.assertEqual(story.returncode, 0, story.stderr)
        path = self.target / 'docs/stories/story-001-first-capture.md'
        self.assertTrue(path.is_file())
        for command in re.findall(r'`make ([a-z-]+)`', path.read_text()):
            dry_run = subprocess.run(['make', '-n', command], cwd=self.target, capture_output=True, text=True)
            self.assertEqual(dry_run.returncode, 0, f'Generated story requires unavailable gate {command}: {dry_run.stderr}')


if __name__ == '__main__':
    unittest.main()
