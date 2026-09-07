"""Entry-point regressions plus subprocess smoke tests; no model evaluation."""
from __future__ import annotations

import ast
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class ScopedDiscoveryTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name)
        self.pack = self.base/'fixture pack'
        self.pack.mkdir()
        self.dest = self.base/'destination with spaces'/'skills'
        self.script = self.pack/'install.py'
        shutil.copy2(ROOT/'install.py', self.script)
        self.rows = [
            dict(name='rust-workflow', title='Rust Workflow', description='Orient a Rust change.', group='core', implicit=False),
            dict(name='rust-async-concurrency', title='Rust Async', description='Cancellation and task ownership.', group='rust', implicit=True),
            dict(name='python-packaging-environments', title='Python Packaging', description='Inspect package environments.', group='python', implicit=True),
            dict(name='ui-design-review', title='Café UI Design', description='Literal [token] styles.', group='ui', implicit=False),
        ]
        for row in self.rows:
            folder = self.pack/'skills'/row['name']
            folder.mkdir(parents=True)
            (folder/'SKILL.md').write_text('DO NOT LOAD THIS BODY FOR DISCOVERY', encoding='utf-8')
        self.save_catalog()
        spec = importlib.util.spec_from_file_location('efficiency_fixture_install', self.script)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def save_catalog(self):
        (self.pack/'catalog.json').write_text(json.dumps({'pack': 'fixture', 'skills': self.rows}), encoding='utf-8')

    def run_cli(self, *args):
        # Exercise the real parser/entry point without paying process startup for
        # every option combination. Dedicated tests below cover process behavior.
        stdout, stderr = io.StringIO(), io.StringIO()
        argv = ['--dest', str(self.dest), *args]
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                code = self.module.main(argv)
            except SystemExit as error:
                code = error.code
        return subprocess.CompletedProcess(argv, code, stdout.getvalue(), stderr.getvalue())

    def run_external(self, *args):
        return subprocess.run([sys.executable, str(self.script), '--dest', str(self.dest), *args],
                              input='', text=True, encoding='utf-8', capture_output=True, timeout=20)

    def listing(self, *args):
        result = self.run_cli('--list', '--json', *args)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        self.assertNotIn('DO NOT LOAD', result.stdout)
        self.assertFalse(self.dest.exists())
        return json.loads(result.stdout)

    def test_external_no_tty_json_filter(self):
        result = self.run_external('--list', '--json', '--search', 'rust', '--limit', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, '')
        data = json.loads(result.stdout)
        self.assertEqual(data['total_matches'], 2)
        self.assertIs(data['truncated'], True)
        self.assertFalse(self.dest.exists())

    def test_external_invalid_input_has_nonzero_status(self):
        result = self.run_external('--list', '--json', '--limit', '0')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')
        self.assertIn('positive integer', result.stderr)
        self.assertFalse(self.dest.exists())

    def test_external_install_preserves_existing_skill(self):
        result = self.run_external('--skill', 'rust-workflow', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        marker = self.dest/'rust-workflow/SKILL.md'
        marker.write_text('keep customization')
        result = self.run_external('--skill', 'rust-workflow', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), 'keep customization')

    def test_unfiltered_json_contract_is_unchanged(self):
        self.assertEqual(self.listing(), {'pack': 'fixture', 'skills': sorted(self.rows, key=lambda row: row['name'])})

    def test_search_matches_all_words_across_fields(self):
        result = self.listing('--search', 'RUST   cancellation')
        self.assertEqual([row['name'] for row in result['skills']], ['rust-async-concurrency'])
        self.assertNotIn('truncated', result)

    def test_search_is_literal_not_regex(self):
        self.assertEqual([r['name'] for r in self.listing('--search', '[token]')['skills']], ['ui-design-review'])
        self.assertEqual(self.listing('--search', '.*')['skills'], [])

    def test_search_handles_unicode(self):
        self.assertEqual([r['name'] for r in self.listing('--search', 'CAFÉ')['skills']], ['ui-design-review'])

    def test_search_matches_group(self):
        self.assertEqual([r['name'] for r in self.listing('--search', 'core')['skills']], ['rust-workflow'])

    def test_limit_discloses_omitted_matches(self):
        data = self.listing('--limit', '2')
        self.assertEqual(data['total_matches'], 4)
        self.assertIs(data['truncated'], True)
        self.assertEqual([r['name'] for r in data['skills']], ['python-packaging-environments', 'rust-async-concurrency'])

    def test_limit_equal_to_count_is_not_truncated(self):
        data = self.listing('--limit', '4')
        self.assertEqual(data['total_matches'], 4)
        self.assertIs(data['truncated'], False)

    def test_filter_precedes_limit(self):
        data = self.listing('--search', 'rust', '--limit', '1')
        self.assertEqual(data['total_matches'], 2)
        self.assertIs(data['truncated'], True)
        self.assertEqual([r['name'] for r in data['skills']], ['rust-async-concurrency'])

    def test_empty_match_is_an_explicit_empty_success(self):
        data = self.listing('--search', 'not-present', '--limit', '2')
        self.assertEqual(data, {'pack': 'fixture', 'skills': [], 'total_matches': 0, 'truncated': False})
        result = self.run_cli('--list', '--search', 'not-present')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('No matching skills in the selected catalog scope.', result.stdout)

    def test_named_skill_scope_precedes_search_and_deduplicates(self):
        data = self.listing('--skill', 'rust-workflow', '--skill', 'rust-workflow', '--search', 'rust', '--limit', '1')
        self.assertEqual(data['total_matches'], 1)
        self.assertIs(data['truncated'], False)
        self.assertEqual([r['name'] for r in data['skills']], ['rust-workflow'])

    def test_named_set_scope_can_be_filtered_without_expanding(self):
        # Supply every core name so the actual existing selection remains valid.
        spec = importlib.util.spec_from_file_location('scoped_set_fixture', self.script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        known = {r['name'] for r in self.rows}
        for name in module.CORE:
            if name not in known:
                self.rows.append(dict(name=name, title=name, description='Core fixture.', group='core', implicit=True))
                folder = self.pack/'skills'/name
                folder.mkdir()
                (folder/'SKILL.md').write_text('fixture')
        self.save_catalog()
        data = self.listing('--set', 'core', '--search', 'async')
        self.assertEqual(data['skills'], [])

    def test_text_limit_is_visible_and_policy_is_retained(self):
        result = self.run_cli('--list', '--search', 'rust', '--limit', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Showing 1 of 2 matches', result.stdout)
        result = self.run_cli('--list', '--skill', 'rust-workflow')
        self.assertIn('rust-workflow [explicit-only]', result.stdout)

    def test_invalid_discovery_options_have_no_side_effects(self):
        for args in [('--search', 'rust'), ('--limit', '1'), ('--list', '--search', '  '),
                     ('--list', '--limit', '0'), ('--list', '--limit', '-1'),
                     ('--list', '--limit', '1.5'), ('--list', '--limit', '1', '--apply'),
                     ('--search', 'rust', '--apply'), ('--json', '--limit', '2')]:
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, '')
                self.assertTrue(result.stderr)
                self.assertFalse(self.dest.exists())

    def test_invalid_skill_is_not_hidden_by_search(self):
        result = self.run_cli('--list', '--search', 'none', '--skill', '../missing')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Unknown skill', result.stderr)
        self.assertEqual(result.stdout, '')

    def test_listing_ignores_unusable_destination(self):
        self.dest.parent.mkdir(parents=True)
        self.dest.write_text('keep this file')
        result = self.run_cli('--list', '--search', 'rust', '--limit', '1', '--json')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['total_matches'], 2)
        self.assertEqual(self.dest.read_text(), 'keep this file')

    def test_broken_catalog_cannot_be_hidden_by_filter(self):
        for content in ('not json', json.dumps({'pack': 'fixture', 'skills': self.rows + [self.rows[0]]})):
            with self.subTest(content=content[:30]):
                (self.pack/'catalog.json').write_text(content)
                result = self.run_cli('--list', '--json', '--search', 'absent', '--limit', '1')
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, '')
                self.assertFalse(self.dest.exists())

    def test_discovery_never_reads_instruction_bodies(self):
        spec = importlib.util.spec_from_file_location('scoped_read_fixture', self.script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = Path.read_text
        def guarded(path, *args, **kwargs):
            if path.name == 'SKILL.md':
                raise AssertionError('Discovery read a skill body')
            return original(path, *args, **kwargs)
        with patch.object(Path, 'read_text', guarded), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(module.main(['--list', '--json', '--search', 'rust', '--limit', '1']), 0)
        self.assertEqual(json.loads(output.getvalue())['total_matches'], 2)

    def test_search_and_limit_make_fixture_payload_smaller(self):
        full = self.run_cli('--list', '--json')
        scoped = self.run_cli('--list', '--json', '--search', 'cancellation', '--limit', '2')
        self.assertEqual(full.returncode, 0, full.stderr)
        self.assertEqual(scoped.returncode, 0, scoped.stderr)
        self.assertLess(len(scoped.stdout.encode('utf-8')), len(full.stdout.encode('utf-8')))
        self.assertEqual(len(json.loads(scoped.stdout)['skills']), 1)

    def test_installation_selection_and_no_overwrite_are_unchanged(self):
        result = self.run_cli('--skill', 'rust-async-concurrency', '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        marker = self.dest/'rust-async-concurrency/SKILL.md'
        marker.write_text('customized')
        result = self.run_cli('--skill', 'rust-async-concurrency', '--apply')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), 'customized')

    def test_new_skill_installs_with_references_and_licenses(self):
        name = 'context-efficiency'
        shutil.copytree(ROOT/'skills'/name, self.pack/'skills'/name)
        for filename in ('LICENSE-MIT', 'LICENSE-APACHE'):
            shutil.copy2(ROOT/filename, self.pack/filename)
        preview = self.run_cli('--skill', name)
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse(self.dest.exists())
        result = self.run_cli('--skill', name, '--apply')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.dest.iterdir()}, {name})
        self.assertTrue((self.dest/name/'references/recipes.md').is_file())
        for filename in ('LICENSE-MIT', 'LICENSE-APACHE'):
            self.assertEqual((self.dest/name/filename).read_bytes(), (ROOT/filename).read_bytes())


class EfficiencyStructureTests(unittest.TestCase):
    def test_each_reviewed_skill_has_activation_boundary_and_behavior(self):
        data = json.loads((ROOT/'evals/context-efficiency-scenarios.json').read_text())
        self.assertEqual(data['status'], 'authored_not_executed')
        names = data['skills_under_review']
        self.assertTrue(names)
        self.assertEqual(len(names), len(set(names)))
        catalog = {r['name'] for r in json.loads((ROOT/'catalog.json').read_text())['skills']}
        self.assertTrue(set(names) <= catalog)
        coverage = {name: set() for name in names}
        for case in data['scenarios']:
            for field in ('case', 'kind', 'skills', 'prompt', 'expected', 'avoid'):
                self.assertTrue(case[field])
            self.assertIn(case['kind'], ('activation', 'boundary', 'behavior'))
            for name in case['skills']:
                self.assertIn(name, coverage)
                coverage[name].add(case['kind'])
        for name, kinds in coverage.items():
            self.assertEqual(kinds, {'activation', 'boundary', 'behavior'}, name)

    def test_scenario_ids_are_globally_unique(self):
        ids = [row['case'] for path in (ROOT/'evals').glob('*scenarios.json')
               for row in json.loads(path.read_text())['scenarios']]
        self.assertEqual(len(ids), len(set(ids)))

    def test_changed_skill_references_resolve(self):
        data = json.loads((ROOT/'evals/context-efficiency-scenarios.json').read_text())
        for name in data['skills_under_review']:
            folder = ROOT/'skills'/name
            self.assertTrue((folder/'SKILL.md').is_file())
            self.assertTrue((folder/'agents/openai.yaml').is_file())
            front = (folder/'SKILL.md').read_text().split('\n---\n', 1)[0]
            self.assertIn('\nlicense: MIT OR Apache-2.0', front)
            for path in folder.rglob('*.md'):
                for link in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', path.read_text()):
                    if '://' not in link and not link.startswith(('#', 'mailto:')):
                        self.assertTrue((path.parent/link.split('#')[0]).exists(), f'{path}: {link}')

    def test_changed_python_supports_declared_syntax_floor(self):
        for path in (ROOT/'install.py', Path(__file__)):
            ast.parse(path.read_text(), filename=str(path), feature_version=(3, 11))


if __name__ == '__main__':
    unittest.main()
