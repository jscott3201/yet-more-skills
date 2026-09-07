"""Exercise the installed script interface with temporary destinations only."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name)
        self.dest = self.base/'a destination with spaces'/'skills'

    def run_cli(self, *args: str, script: Path | None = None):
        return subprocess.run(
            [sys.executable, str(script or ROOT/'install.py'), '--dest', str(self.dest), *args],
            input='', text=True, encoding='utf-8', capture_output=True, timeout=20,
        )

    def test_json_listing_is_complete_sorted_and_read_only(self):
        result = self.run_cli('--list', '--json')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        data = json.loads(result.stdout)
        catalog = json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
        self.assertEqual(data['pack'], catalog['pack'])
        self.assertEqual(data['skills'], sorted(catalog['skills'], key=lambda row: row['name']))
        self.assertFalse(self.dest.parent.exists())

    def test_filtered_listing_and_additional_skill_deduplicate(self):
        result = self.run_cli('--list', '--json', '--set', 'typescript-packages',
                              '--skill', 'typescript-contracts', '--skill', 'agent-cli-design')
        self.assertEqual(result.returncode, 0, result.stderr)
        names = [row['name'] for row in json.loads(result.stdout)['skills']]
        self.assertEqual(names, ['agent-cli-design', 'typescript-contracts', 'typescript-package-boundaries'])
        self.assertFalse(self.dest.exists())

    def test_single_skill_does_not_load_core(self):
        result = self.run_cli('--list', '--json', '--skill', 'agent-cli-design')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([row['name'] for row in json.loads(result.stdout)['skills']], ['agent-cli-design'])

    def test_text_listing_exposes_explicit_policy(self):
        result = self.run_cli('--list', '--skill', 'ui-design-review')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('ui-design-review [explicit-only]', result.stdout)
        self.assertIn('preserve established product tokens', result.stdout)
        self.assertNotIn('Preview only', result.stdout)
        self.assertFalse(self.dest.exists())

    def test_listing_does_not_preflight_or_touch_destination(self):
        self.dest.parent.mkdir(parents=True)
        self.dest.write_text('not a skills directory', encoding='utf-8')
        result = self.run_cli('--list', '--json', '--set', 'core')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)['skills']), 6)
        self.assertEqual(self.dest.read_text(encoding='utf-8'), 'not a skills directory')

    def test_listing_works_with_existing_customized_skill(self):
        marker = self.dest/'agent-cli-design'/'SKILL.md'
        marker.parent.mkdir(parents=True)
        marker.write_text('keep customization', encoding='utf-8')
        result = self.run_cli('--list', '--json', '--skill', 'agent-cli-design')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(marker.read_text(encoding='utf-8'), 'keep customization')
        self.assertEqual([p.name for p in self.dest.iterdir()], ['agent-cli-design'])

    def test_invalid_mode_combinations_do_not_write(self):
        for args in [('--json',), ('--json', '--apply'), ('--list', '--apply'),
                     ('--list', '--json', '--apply')]:
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, '')
                self.assertTrue(result.stderr)
                self.assertFalse(self.dest.exists())

    def test_unknown_skill_is_not_an_empty_success(self):
        result = self.run_cli('--list', '--json', '--skill', '../not-a-skill')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')
        self.assertIn('Unknown skill', result.stderr)
        self.assertFalse(self.dest.exists())

    def test_broken_catalog_fails_without_partial_json(self):
        copied = self.base/'pack'
        skill = 'agent-cli-design'
        shutil.copytree(ROOT/'skills'/skill, copied/'skills'/skill)
        shutil.copy2(ROOT/'install.py', copied/'install.py')
        catalog = copied/'catalog.json'
        valid_row = next(row for row in json.loads((ROOT/'catalog.json').read_text())['skills']
                         if row['name'] == skill)
        invalid_inputs = [
            '{not json',
            json.dumps({'pack': 'test', 'skills': []}),
            json.dumps({'pack': 'test', 'skills': [valid_row, valid_row]}),
            json.dumps({'pack': 'test', 'skills': [dict(valid_row, implicit='false')]}),
        ]
        for text in invalid_inputs:
            with self.subTest(text=text[:40]):
                catalog.write_text(text, encoding='utf-8')
                result = self.run_cli('--list', '--json', script=copied/'install.py')
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, '')
                self.assertIn('Cannot list skills from catalog.json', result.stderr)
                self.assertFalse(self.dest.exists())

    def test_unicode_metadata_round_trips(self):
        copied = self.base/'unicode pack'
        skill = 'agent-cli-design'
        shutil.copytree(ROOT/'skills'/skill, copied/'skills'/skill)
        shutil.copy2(ROOT/'install.py', copied/'install.py')
        row = next(row for row in json.loads((ROOT/'catalog.json').read_text())['skills']
                   if row['name'] == skill)
        row['description'] = 'Inspect caf\u00e9 data without guessing \u2014 read only.'
        (copied/'catalog.json').write_text(json.dumps({'pack': 'test', 'skills': [row]}), encoding='utf-8')
        result = self.run_cli('--list', '--json', script=copied/'install.py')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['skills'][0]['description'], row['description'])

    def test_default_preview_still_selects_core(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Preview only: 6 skills', result.stdout)
        self.assertFalse(self.dest.exists())

    def test_new_additions_install_with_licenses(self):
        result = self.run_cli('--set', 'engineering-additions', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.dest.iterdir()}, {
            'agent-cli-design', 'typescript-package-boundaries',
            'cross-language-contracts', 'ui-agent-collaboration',
        })
        for skill in self.dest.iterdir():
            for name in ['LICENSE-MIT', 'LICENSE-APACHE']:
                self.assertEqual((skill/name).read_bytes(), (ROOT/name).read_bytes())
            for source in (ROOT/'skills'/skill.name).rglob('*'):
                if source.is_file() and '__pycache__' not in source.parts:
                    self.assertEqual(source.read_bytes(), (skill/source.relative_to(ROOT/'skills'/skill.name)).read_bytes())

    def test_collision_still_prevents_partial_install(self):
        marker = self.dest/'ui-agent-collaboration'/'SKILL.md'
        marker.parent.mkdir(parents=True)
        marker.write_text('keep existing skill', encoding='utf-8')
        result = self.run_cli('--set', 'engineering-additions', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('will not be overwritten', result.stderr)
        self.assertEqual(marker.read_text(), 'keep existing skill')
        self.assertEqual([p.name for p in self.dest.iterdir()], ['ui-agent-collaboration'])


if __name__ == '__main__':
    unittest.main()
