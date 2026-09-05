"""Test probe mechanics, not native extension or free-threading correctness."""
from pathlib import Path
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT/'skills/pyo3-free-threading/scripts/interpreter_probe.py'
spec = importlib.util.spec_from_file_location('interpreter_probe', PROBE)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

class ProbeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cwd = Path(self.temp.name)

    def run_probe(self, *args):
        return subprocess.run([sys.executable, str(PROBE), *args], text=True,
                              capture_output=True, cwd=self.cwd, timeout=10)

    def test_real_interpreter_and_origin(self):
        result = self.run_probe('--python', sys.executable, '--module', 'json', '--isolated')
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data['executable'], sys.executable)
        self.assertTrue(data['imports'][0]['ok'])
        self.assertTrue(data['imports'][0]['origin'].endswith('json/__init__.py'))
        self.assertTrue(data['isolated'])

    def test_missing_import_is_failure(self):
        result = self.run_probe('--module', 'does_not_exist_astra_probe_93')
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertEqual(json.loads(result.stdout)['status'], 'import_failed')

    def test_import_sequence_preserves_failure(self):
        result = self.run_probe('--module', 'json', '--module', 'does_not_exist_astra_probe_93',
                                '--module', 'math')
        data = json.loads(result.stdout)
        self.assertEqual([x['ok'] for x in data['imports']], [True, False, True])
        self.assertEqual(result.returncode, 1)

    def test_missing_executable_is_structured_failure(self):
        result = self.run_probe('--python', str(self.cwd/'missing-python'), '--module', 'json')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['status'], 'probe_error')

    def test_rejects_code_as_module(self):
        result = self.run_probe('--module', 'json;print(1)')
        self.assertEqual(result.returncode, 2)
        self.assertIn('dotted import module', result.stderr)

    def test_requires_module(self):
        result = self.run_probe()
        self.assertEqual(result.returncode, 2)

    def test_invalid_timeouts_rejected(self):
        for value in ['0', '-1', 'nan', 'inf']:
            with self.subTest(value=value):
                result = self.run_probe('--module', 'json', '--timeout', value)
                self.assertEqual(result.returncode, 2)

    def test_output_noise_does_not_corrupt_json(self):
        # PYTHONPATH is explicit here to provide the test-only module in the child.
        (self.cwd/'probe_noise.py').write_text('print("not JSON")\n')
        with patch.dict(os.environ, {'PYTHONPATH': str(self.cwd)}):
            result = self.run_probe('--module', 'probe_noise')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('not JSON', json.loads(result.stdout)['child_stdout_excerpt'])

    def test_isolated_mode_ignores_pythonpath(self):
        (self.cwd/'probe_only_local.py').write_text('value = 1\n')
        with patch.dict(os.environ, {'PYTHONPATH': str(self.cwd)}):
            result = self.run_probe('--module', 'probe_only_local', '--isolated')
        self.assertEqual(result.returncode, 1)

    def test_hanging_import_is_bounded(self):
        (self.cwd/'probe_sleep.py').write_text('import time\ntime.sleep(30)\n')
        with patch.dict(os.environ, {'PYTHONPATH': str(self.cwd)}):
            result = self.run_probe('--module', 'probe_sleep', '--timeout', '0.3')
        self.assertEqual(result.returncode, 1)
        self.assertIn('timed out', json.loads(result.stdout)['error'])

    def test_import_system_exit_is_not_success(self):
        (self.cwd/'probe_exit.py').write_text('raise SystemExit(0)\n')
        with patch.dict(os.environ, {'PYTHONPATH': str(self.cwd)}):
            result = self.run_probe('--module', 'probe_exit')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['status'], 'probe_error')

    def fixture(self, build=True, before=False, after=False):
        return {'free_threaded_build': build, 'gil_before_imports': before,
                'gil_after_imports': after,
                'imports': [{'ok': True, 'gil_before': before, 'gil_after': after}]}

    def test_simulated_disabled_observations_pass(self):
        self.assertEqual(probe.assess(self.fixture(), True), (0, 'observed_disabled_gil'))

    def test_simulated_reenabled_gil_fails(self):
        self.assertEqual(probe.assess(self.fixture(after=True), True)[0], 2)

    def test_unknown_states_are_not_disabled(self):
        for data in [self.fixture(build=None), self.fixture(before=None), self.fixture(after=None)]:
            self.assertEqual(probe.assess(data, True)[0], 2)

    def test_regular_build_is_not_free_threaded(self):
        self.assertEqual(probe.assess(self.fixture(build=False), True)[0], 2)

    def test_real_strict_result_matches_observation(self):
        result = self.run_probe('--module', 'json', '--isolated', '--require-gil-disabled')
        data = json.loads(result.stdout)
        code, status = probe.assess(data, True)
        self.assertEqual(result.returncode, code)
        self.assertEqual(data['status'], status)

    def test_missing_introspection_is_unknown(self):
        with patch.object(probe.sys, '_is_gil_enabled', None, create=True):
            self.assertIsNone(probe.gil_enabled())

    def test_bad_introspection_is_unknown(self):
        with patch.object(probe.sys, '_is_gil_enabled', lambda: 'false', create=True):
            self.assertIsNone(probe.gil_enabled())

if __name__ == '__main__':
    unittest.main()
