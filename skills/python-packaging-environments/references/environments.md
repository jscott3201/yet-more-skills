# Environment decisions

Use `python -m pip` with an explicitly selected interpreter when pip is the established installer. A uv-created environment may not include pip; use `uv pip install --python /path/to/python...` with the actual package arguments, or the project's normal uv workflow, rather than assuming pip exists. Never change global Python to repair a project.

For an established uv project, `uv sync --locked` validates the lock before syncing; `uv run --locked...` still may synchronize. For an artifact test, invoke the isolated environment directly, or use a documented no-project invocation. Do not permit project synchronization to put an editable install back over the wheel under test.

Installation recipe: create a separate venv using the intended interpreter, install the explicit wheel and approved test dependencies, change to a scratch directory, inspect module.__file__, then execute an installed-consumer test. Use the repository's actual module name. Dependency isolation does not mean `--no-deps` unconditionally: that can mask runtime requirements if the environment is prepopulated or simply leave it unusable. Test minimal runtime installation and development extras separately.

Maturin owns native package assembly in the sampled bindings. Keep its Python metadata and Cargo version decisions coherent rather than copying a pure-Python backend template into them. No package is published by these skills.

Primary references: [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/), [uv CLI](https://docs.astral.sh/uv/reference/cli/), [pyproject specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/), [build isolation](https://pip.pypa.io/en/stable/reference/build-system/), [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
