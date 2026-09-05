"""Authoring validator regressions; requires PyYAML."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate_metadata import validate

ROOT = Path(__file__).resolve().parents[1]


class MetadataTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        name = 'orchestrate'
        shutil.copytree(ROOT/'skills'/name, self.root/'skills'/name)
        for license_name in ('LICENSE-MIT', 'LICENSE-APACHE'):
            shutil.copy2(ROOT/license_name, self.root/license_name)
        rows = json.loads((ROOT/'catalog.json').read_text())['skills']
        (self.root/'catalog.json').write_text(json.dumps({'skills': [r for r in rows if r['name'] == name]}))

    def test_valid(self):
        self.assertEqual(validate(self.root), 1)

    def test_description_drift(self):
        path = self.root/'catalog.json'
        data = json.loads(path.read_text())
        data['skills'][0]['description'] = 'drift'
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'frontmatter mismatch'):
            validate(self.root)

    def test_duplicate_yaml_key(self):
        path = self.root/'skills/orchestrate/agents/openai.yaml'
        path.write_text(path.read_text() + '\npolicy:\n  allow_implicit_invocation: false\n')
        with self.assertRaisesRegex(ValueError, 'Duplicate YAML key'):
            validate(self.root)

    def test_explicit_only_cannot_drift_together(self):
        path = self.root/'skills/orchestrate/agents/openai.yaml'
        path.write_text(path.read_text().replace('allow_implicit_invocation: false', 'allow_implicit_invocation: true'))
        path = self.root/'catalog.json'
        data = json.loads(path.read_text())
        data['skills'][0]['implicit'] = True
        path.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'must remain explicit-only'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
