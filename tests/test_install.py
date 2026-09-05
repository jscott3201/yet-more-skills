"""Installer behavior tests using temporary directories only. No Rust/Codex required."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT/'install.py'

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.dest = self.base/'installed'

    def run_install(self, *args, script=INSTALL):
        return subprocess.run([sys.executable, str(script), '--dest', str(self.dest), *args],
                              text=True, capture_output=True, timeout=20)

    def count(self):
        return len(list(self.dest.glob('*/SKILL.md')))

    def test_preview_makes_no_destination(self):
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Preview only: 6 skills', result.stdout)
        self.assertFalse(self.dest.exists())

    def test_core_install(self):
        result = self.run_install('--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 6)

    def test_full_install_preserves_file_contents(self):
        result = self.run_install('--set', 'full', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 70)
        for source in (ROOT/'skills').rglob('*'):
            if source.is_file() and source.name != '.DS_Store' and '__pycache__' not in source.parts:
                target = self.dest/source.relative_to(ROOT/'skills')
                self.assertEqual(target.read_bytes(), source.read_bytes())

    def test_workflow_install_retains_licenses(self):
        result = self.run_install('--set', 'workflow', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 16)
        for skill in self.dest.iterdir():
            for name in ('LICENSE-MIT', 'LICENSE-APACHE'):
                self.assertEqual((skill/name).read_bytes(), (ROOT/name).read_bytes())
        adapted = self.dest/'module-design'
        self.assertIn('Matt Pocock', (adapted/'LICENSE.mattpocock-skills').read_text())
        self.assertTrue((adapted/'NOTICE').is_file())

    def test_protocol_set(self):
        result = self.run_install('--set', 'protocol', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 10)

    def test_storage_set(self):
        result = self.run_install('--set', 'storage', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 11)

    def test_single_skill_only(self):
        result = self.run_install('--skill', 'rust-python-bindings', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 1)
        self.assertTrue((self.dest/'rust-python-bindings/references/verification.md').is_file())

    def test_set_plus_extra_deduplicates(self):
        result = self.run_install('--set', 'core', '--skill', 'rust-python-bindings',
                                  '--skill', 'rust-nextest', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 7)

    def test_add_uninstalled_skill_to_existing_core(self):
        first = self.run_install('--apply')
        self.assertEqual(first.returncode, 0, first.stderr)
        result = self.run_install('--skill', 'rust-python-bindings', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 7)

    def test_unknown_name_has_no_side_effects(self):
        result = self.run_install('--skill', '../unknown', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Unknown skill', result.stderr)
        self.assertFalse(self.dest.exists())

    def test_existing_directory_preflight_prevents_partial_copy(self):
        saved = self.dest/'rust-review'
        saved.mkdir(parents=True)
        (saved/'custom.txt').write_text('keep me')
        result = self.run_install('--set', 'full', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((saved/'custom.txt').read_text(), 'keep me')
        self.assertEqual(list(self.dest.iterdir()), [saved])

    def test_existing_file_is_not_replaced(self):
        self.dest.mkdir()
        saved = self.dest/'rust-nextest'
        saved.write_text('user file')
        result = self.run_install('--skill', 'rust-nextest', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(saved.read_text(), 'user file')

    def test_dangling_destination_symlink_is_not_replaced(self):
        self.dest.mkdir()
        saved = self.dest/'rust-nextest'
        try:
            saved.symlink_to(self.base/'missing', target_is_directory=True)
        except OSError:
            self.skipTest('Creating symlinks is not permitted on this test host')
        result = self.run_install('--skill', 'rust-nextest', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(saved.is_symlink())
        self.assertEqual(os.readlink(saved), str(self.base/'missing'))

    def test_destination_file_is_rejected(self):
        self.dest.write_text('not a directory')
        result = self.run_install('--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.dest.read_text(), 'not a directory')

    def test_source_symlink_is_rejected(self):
        copied = self.base/'pack'
        shutil.copytree(ROOT/'skills', copied/'skills')
        shutil.copy2(INSTALL, copied/'install.py')
        link = copied/'skills/rust-nextest/references/unexpected-link'
        try:
            link.symlink_to(self.base/'outside')
        except OSError:
            self.skipTest('Creating symlinks is not permitted on this test host')
        result = self.run_install('--skill', 'rust-nextest', '--apply', script=copied/'install.py')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('contains a symlink', result.stderr)
        self.assertFalse(self.dest.exists())

    def test_new_sets(self):
        for selection, count in [('python-core', 6), ('python', 11), ('bindings', 6),
                                 ('python-rust', 17), ('python-additions', 16)]:
            with self.subTest(selection=selection):
                self.dest = self.base/selection
                result = self.run_install('--set', selection, '--apply')
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.count(), count)

    def test_additions_preserve_existing_rust_skills(self):
        for source in (ROOT/'skills').glob('rust-*'):
            shutil.copytree(source, self.dest/source.name)
        marker = self.dest/'rust-python-bindings/SKILL.md'
        marker.write_text('Custom previously installed binding skill')
        result = self.run_install('--set', 'python-additions', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.count(), 32)
        self.assertEqual(marker.read_text(), 'Custom previously installed binding skill')

    def test_bindings_collision_is_not_silently_skipped(self):
        source = ROOT/'skills/rust-python-bindings'
        shutil.copytree(source, self.dest/source.name)
        result = self.run_install('--set', 'bindings', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.count(), 1)

    def test_python_additions_preview_no_changes(self):
        result = self.run_install('--set', 'python-additions')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Preview only: 16 skills', result.stdout)
        self.assertFalse(self.dest.exists())

if __name__ == '__main__':
    unittest.main()
