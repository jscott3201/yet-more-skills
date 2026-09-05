"""Portable frontend package/installer checks; these do not execute a UI or an agent."""
from __future__ import annotations
import ast
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT/'catalog.json').read_text())
COMBINED = CATALOG['pack'] == 'yet-more-skills'
SUBSETS = json.loads((ROOT/'subsets.json').read_text())
NEW = set(SUBSETS['typescript-additions'])

class FrontendContentTests(unittest.TestCase):
    def test_total_and_unique_catalog(self):
        names=[x['name'] for x in CATALOG['skills']]
        expected=len(list((ROOT/'skills').glob('*/SKILL.md'))) if COMBINED else 22
        self.assertEqual(len(names),expected)
        self.assertEqual(len(set(names)),expected)
        self.assertEqual(set(names),{p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')})

    def test_new_skill_format(self):
        entries={x['name']:x for x in CATALOG['skills']}
        for name in NEW:
            with self.subTest(name=name):
                p=ROOT/'skills'/name
                text=(p/'SKILL.md').read_text()
                self.assertRegex(text,rf'\A---\nname: {name}\ndescription:')
                self.assertEqual(len(text.split('\n---\n',1)),2)
                self.assertIn('references/practice.md',text)
                self.assertGreater(len(text.split()),150)
                self.assertLess(len(text.split()),600)
                meta=(p/'agents/openai.yaml').read_text()
                self.assertIn('$'+name,meta)
                self.assertIn('allow_implicit_invocation: '+str(entries[name]['implicit']).lower(),meta)
                self.assertTrue((p/'references/practice.md').is_file())

    def test_frontend_subsets(self):
        self.assertEqual(len(NEW),22)
        self.assertEqual(len(SUBSETS['typescript-core']),8)
        self.assertEqual(len(SUBSETS['react-ui']),16)
        self.assertEqual(len(SUBSETS['svelte-ui']),16)
        self.assertEqual(len(SUBSETS['ui-review']),6)
        self.assertEqual(set(SUBSETS['typescript']),NEW)
        for values in SUBSETS.values():
            self.assertEqual(len(values),len(set(values)))
            self.assertTrue(set(values)<=NEW)

    def test_framework_subsets_do_not_cross_load(self):
        react=set(SUBSETS['react-ui'])
        svelte=set(SUBSETS['svelte-ui'])
        self.assertTrue({'react-components-state','react-performance','shadcn-react-components'}<=react)
        self.assertFalse(any(x.startswith(('svelte','shadcn-svelte')) for x in react))
        self.assertTrue({'svelte-components-runes','sveltekit-boundaries','shadcn-svelte-components'}<=svelte)
        self.assertFalse(any(x.startswith(('react-','shadcn-react')) for x in svelte))

    def test_installer_and_machine_subsets_agree(self):
        spec=importlib.util.spec_from_file_location('frontend_install',ROOT/'install.py')
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name,values in SUBSETS.items():
            self.assertEqual(list(module.SETS[name]),values)

    def test_local_links(self):
        for p in ROOT.rglob('*.md'):
            for target in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)',p.read_text()):
                if '://' in target or target.startswith(('#','mailto:')):
                    continue
                target=target.split('#')[0]
                if target:
                    self.assertTrue((p.parent/target).exists(),f'{p}: {target}')

    def test_python_311_syntax(self):
        for p in ROOT.rglob('*.py'):
            ast.parse(p.read_text(),filename=str(p),feature_version=(3,11))

    def test_scenarios_unique_authored_not_run(self):
        data=json.loads((ROOT/'evals/scenarios.json').read_text())
        cases=data['scenarios']
        self.assertEqual(data['status'],'authored_not_executed')
        self.assertTrue(cases)
        self.assertEqual(len({x['case'] for x in cases}),len(cases))
        self.assertEqual(sum(x['case'].startswith('ui-') for x in cases),56)
        for case in cases:
            self.assertTrue(case['prompt'])
            self.assertTrue(case['expected'])
            self.assertTrue(case['avoid'])

    def test_no_source_symlinks(self):
        self.assertFalse(any(p.is_symlink() for p in ROOT.rglob('*')))

class FrontendInstallerTests(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base=Path(temp.name)
        self.dest=self.base/'a destination with spaces'/'skills'

    def run_install(self,*args,script=None):
        return subprocess.run([sys.executable,str(script or ROOT/'install.py'),'--dest',str(self.dest),*args],
                              capture_output=True,text=True,timeout=20)

    def count(self):
        return len(list(self.dest.glob('*/SKILL.md')))

    def test_additions_preview_is_read_only(self):
        result=self.run_install('--set','typescript-additions')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('Preview only: 22 skills',result.stdout)
        self.assertFalse(self.dest.exists())

    def test_frontend_install_copies_only_new_skills(self):
        result=self.run_install('--set','typescript-additions','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual({p.name for p in self.dest.iterdir()},NEW)
        for name in NEW:
            for source in (ROOT/'skills'/name).rglob('*'):
                if source.is_file() and source.name != '.DS_Store' and '__pycache__' not in source.parts:
                    self.assertEqual(source.read_bytes(),(self.dest/source.relative_to(ROOT/'skills')).read_bytes())

    def test_additions_preserve_preexisting_customization(self):
        if COMBINED:
            for source in (ROOT/'skills').iterdir():
                if source.is_dir() and (source/'SKILL.md').is_file() and source.name not in NEW:
                    shutil.copytree(source,self.dest/source.name)
        else:
            # A standalone add-on need not contain the other package to coexist with it.
            (self.dest/'rust-python-bindings').mkdir(parents=True)
        marker=self.dest/'rust-python-bindings'/'SKILL.md'
        marker.write_text('user customization must remain')
        before={str(p.relative_to(self.dest)):p.read_bytes() for p in self.dest.rglob('*') if p.is_file()}
        result=self.run_install('--set','typescript-additions','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.count(),len(CATALOG['skills']) if COMBINED else 23)
        for path,content in before.items():
            self.assertEqual((self.dest/path).read_bytes(),content)

    def test_conflict_prevents_all_new_copies(self):
        marker=self.dest/'vite-build-tooling'
        marker.mkdir(parents=True)
        (marker/'SKILL.md').write_text('custom')
        result=self.run_install('--set','typescript-additions','--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual([p.name for p in self.dest.iterdir()],['vite-build-tooling'])
        self.assertEqual((marker/'SKILL.md').read_text(),'custom')

    def test_framework_sets(self):
        for choice in ('react-ui','svelte-ui'):
            with self.subTest(choice=choice):
                self.dest=self.base/choice
                result=self.run_install('--set',choice,'--apply')
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual({p.name for p in self.dest.iterdir()},set(SUBSETS[choice]))

    def test_one_skill_does_not_force_dependencies(self):
        result=self.run_install('--skill','shadcn-svelte-components','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.count(),1)

    def test_invalid_name_no_writes(self):
        result=self.run_install('--skill','../escape','--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertFalse(self.dest.exists())

    def test_default_is_documented(self):
        result=self.run_install()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn(f'Preview only: {6 if COMBINED else 8} skills',result.stdout)
        self.assertFalse(self.dest.exists())

    def test_full_is_archive_specific(self):
        result=self.run_install('--set','full','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.count(),len(CATALOG['skills']) if COMBINED else 22)

    def test_dangling_collision_rejected(self):
        self.dest.mkdir(parents=True)
        link=self.dest/'typescript-contracts'
        try:
            link.symlink_to(self.base/'absent',target_is_directory=True)
        except OSError:
            self.skipTest('This host cannot create symlinks')
        result=self.run_install('--skill','typescript-contracts','--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertTrue(link.is_symlink())

    def test_configuration_not_touched(self):
        marker=self.base/'.codex'/'config.toml'
        marker.parent.mkdir()
        marker.write_text('model = "keep-current"\n')
        instructions=self.base/'AGENTS.md'
        instructions.write_text('keep local policy')
        result=self.run_install('--set','typescript-core','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(marker.read_text(),'model = "keep-current"\n')
        self.assertEqual(instructions.read_text(),'keep local policy')

    def test_source_symlink_rejected(self):
        copy=self.base/'pack'
        shutil.copytree(ROOT/'skills'/'typescript-contracts',copy/'skills'/'typescript-contracts')
        shutil.copy2(ROOT/'install.py',copy/'install.py')
        link=copy/'skills'/'typescript-contracts'/'references'/'external'
        try:
            link.symlink_to(self.base/'outside')
        except OSError:
            self.skipTest('This host cannot create symlinks')
        result=self.run_install('--skill','typescript-contracts','--apply',script=copy/'install.py')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('contains a symlink',result.stderr)
        self.assertFalse(self.dest.exists())

if __name__=='__main__':
    unittest.main()
