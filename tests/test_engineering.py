"""Structural coverage checks, not execution of the authored agent scenarios."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EngineeringCoverageTests(unittest.TestCase):
    def test_scenarios_cover_activation_boundary_and_behavior(self):
        data = json.loads((ROOT/'evals/engineering-scenarios.json').read_text())
        self.assertEqual(data['status'], 'authored_not_executed')
        names = data['skills_under_review']
        self.assertTrue(names)
        self.assertEqual(len(names), len(set(names)))
        catalog = {row['name'] for row in json.loads((ROOT/'catalog.json').read_text())['skills']}
        self.assertTrue(set(names) <= catalog)
        coverage = {name: set() for name in names}
        for row in data['scenarios']:
            self.assertTrue(row['case'])
            for field in ('prompt', 'expected', 'avoid', 'skills'):
                self.assertTrue(row[field])
            self.assertIn(row['kind'], ('activation', 'boundary', 'behavior'))
            for name in row['skills']:
                self.assertIn(name, coverage)
                coverage[name].add(row['kind'])
        for name, kinds in coverage.items():
            self.assertEqual(kinds, {'activation', 'boundary', 'behavior'}, name)

    def test_case_names_do_not_collide_with_other_suites(self):
        ids = []
        for path in (ROOT/'evals').glob('*scenarios.json'):
            ids.extend(row['case'] for row in json.loads(path.read_text())['scenarios'])
        self.assertEqual(len(ids), len(set(ids)))

    def test_additive_sets_and_existing_agent_set(self):
        spec = importlib.util.spec_from_file_location('engineering_install', ROOT/'install.py')
        install = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(install)
        self.assertEqual(set(install.SETS['engineering-additions']), {
            'agent-cli-design', 'typescript-package-boundaries',
            'cross-language-contracts', 'ui-agent-collaboration',
        })
        self.assertEqual(install.SETS['agent-systems'], ('agent-tool-boundaries', 'memory-context-hygiene'))
        self.assertEqual(set(install.SETS['agent-experience']), {
            'agent-tool-boundaries', 'memory-context-hygiene',
            'agent-cli-design', 'ui-agent-collaboration',
        })
        self.assertEqual(install.SETS['typescript-packages'], ('typescript-contracts', 'typescript-package-boundaries'))
        self.assertEqual(set(install.SETS['cross-language']), {
            'rust-api-design', 'python-api-typing', 'typescript-contracts', 'cross-language-contracts',
        })
        for name, values in json.loads((ROOT/'subsets.json').read_text()).items():
            self.assertEqual(list(install.SETS[name]), values)

    def test_new_skills_have_self_contained_references(self):
        for name in ('agent-cli-design', 'typescript-package-boundaries',
                     'cross-language-contracts', 'ui-agent-collaboration'):
            folder = ROOT/'skills'/name
            self.assertTrue((folder/'SKILL.md').is_file())
            self.assertTrue((folder/'agents/openai.yaml').is_file())
            self.assertTrue(list((folder/'references').glob('*.md')))
            for license_name in ('LICENSE-MIT', 'LICENSE-APACHE'):
                self.assertEqual((folder/license_name).read_bytes(), (ROOT/license_name).read_bytes())


if __name__ == '__main__':
    unittest.main()
