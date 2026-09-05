"""Portable structural checks. Authoring also parses YAML with PyYAML separately."""
import ast
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PackTests(unittest.TestCase):
    def test_catalog_and_files_match(self):
        skills = json.loads((ROOT/'catalog.json').read_text())['skills']
        names = [x['name'] for x in skills]
        self.assertEqual(len(names), 70)
        self.assertEqual(len(set(names)), 70)
        self.assertEqual(set(names), {p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')})
        for name in names:
            self.assertRegex(name, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
            self.assertTrue((ROOT/'skills'/name/'agents/openai.yaml').is_file())

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            for link in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', path.read_text()):
                if '://' in link or link.startswith(('#', 'mailto:')):
                    continue
                target = link.split('#')[0]
                if target:
                    self.assertTrue((path.parent/target).exists(), f'{path}: {target}')

    def test_python_syntax_supports_declared_floor(self):
        for path in ROOT.rglob('*.py'):
            ast.parse(path.read_text(), filename=str(path), feature_version=(3, 11))

    def test_evaluation_cases_are_unique_and_unexecuted(self):
        data = json.loads((ROOT/'evals/scenarios.json').read_text())
        self.assertEqual(data['status'], 'authored_not_executed')
        self.assertEqual(len(data['scenarios']), 140)
        self.assertEqual(len({x['case'] for x in data['scenarios']}), 140)
        for row in data['scenarios']:
            self.assertTrue(row['prompt'])
            self.assertTrue(row['expected'])
            self.assertTrue(row['avoid'])

    def test_install_sets_select_existing_skills(self):
        spec = importlib.util.spec_from_file_location('pack_install', ROOT/'install.py')
        install = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(install)
        for names in install.SETS.values():
            self.assertEqual(len(names), len(set(names)))
            for name in names:
                self.assertTrue((ROOT/'skills'/name/'SKILL.md').is_file())
        self.assertEqual(set(install.SETS['python-additions']),
                         {p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')
                          if p.parent.name.startswith(('python-', 'pyo3-'))})

    def test_pack_has_no_symlinks(self):
        self.assertFalse(any(p.is_symlink() for p in ROOT.rglob('*')))

if __name__ == '__main__':
    unittest.main()
