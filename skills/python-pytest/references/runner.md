# Runner recipes

These are command shapes; select real paths/node IDs from the repository and run in the intended environment. They are not a command queue.

```bash
python -m pytest --version
python -m pytest --collect-only -q tests/test_client.py
python -m pytest -q tests/test_client.py --durations=10
```

For uv repositories, use the established locked project command instead. Running ordinary `uv run` after installing a candidate wheel can resynchronize and replace it with the project; artifact checks should use a separate environment and its direct interpreter.

Register markers and enable supported strict marker/config behavior where the project permits. Pytest 9 adds aggregate strict configuration and native TOML syntax; do not paste those tables into an older project's pyproject.toml. Existing `[tool.pytest.ini_options]` and explicit supported settings remain useful. Inspect the installed version before changing `xfail_strict` versus newer strict-setting names.

Test fixture acquisition and cleanup separately. A yield fixture whose setup fails before yield never executes its post-yield cleanup; register cleanup immediately or use context managers/ExitStack for partial acquisition. Use observable readiness rather than fixed sleeps. A timeout from pytest-timeout can terminate the process, so do not rely on it to perform graceful native cleanup; use bounded subprocesses for hang/crash tests.

`pytest -n auto` is not a free speedup. Benchmark helpers may reserve fixed transport ports, so inspect resource ownership before enabling parallel execution.

Primary references: [exit codes](https://docs.pytest.org/en/stable/reference/exit-codes.html), [plugin behavior](https://docs.pytest.org/en/stable/how-to/plugins.html), [fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html), [pytest-asyncio concepts](https://pytest-asyncio.readthedocs.io/en/stable/concepts.html), [xdist worker fixtures](https://pytest-xdist.readthedocs.io/en/stable/how-to.html).
