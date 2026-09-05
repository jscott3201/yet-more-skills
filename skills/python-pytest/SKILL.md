---
name: python-pytest
description: "Select, run, configure, or diagnose Python tests with pytest. Covers collection, plugins, asyncio scopes, resource isolation, installed-package imports, and truthful results; not test design alone."
license: MIT OR Apache-2.0
---

# Python Pytest

Inspect the project's pytest version, configuration, conftest.py files, plugins, testpaths, and interpreter before choosing a command. Preserve existing modes and gate scripts. Do not assume latest-only flags or that pytest-xdist, pytest-asyncio, coverage, or timeout plugins are installed.

## Select tests deliberately

Use explicit paths or node IDs for a focused change and `--collect-only -q` when discovery is uncertain. Reuse the same config, markers, and selection for collection and execution. Expand to relevant consumers, then the intended gate. `--lf` is useful feedback, not evidence that a changed surface is covered.

Distinguish failures, collection errors, deselection, skips, xfails, and passes. Exit code 5 means no tests collected; do not convert it to success in a required lane. A zero exit with all required tests skipped is not a pass for the promised feature. An expected failure needs a bounded reason and strict unexpected-pass handling where supported. Never add retries or importorskip to hide a missing required extension.

## Control imports and plugins

Run with the selected interpreter (`python -m pytest` or the existing project runner). That alone does not prevent source shadowing. For artifact evidence, use a clean environment and a working directory outside the checkout, inspect the imported module origin, and inspect any conftest/pythonpath manipulation. `--import-mode=importlib` is useful where compatible but not magic isolation.

If collection changes unexpectedly, inspect loaded plugins and configuration. Disabling plugin autoload is a diagnostic option, not a default fix: explicitly load required plugins when doing so. Do not remove a warnings policy to silence unawaited coroutines or resource leaks.

## Async and parallel execution

Keep pytest-asyncio strict/auto mode intentional. Async fixture caching scope and loop scope are different; the loop must outlive loop-bound resources and cleanup. Verify the installed plugin's supported syntax instead of pasting obsolete event_loop fixture overrides.

Use xdist only when fixtures and resources are safe to parallelize. A session fixture may run once per worker, not once globally. Isolate ports, filesystem paths, databases, interpreter state, and native runtimes. Start serially when diagnosing order sensitivity. Do not run latency benchmarks with workers or competing Cargo builds.

Return the exact command, environment, selected/collected and executed scope, outcomes, and untested lanes. A required native test lane should fail clearly when its module is absent.

Read [commands and pitfalls](references/runner.md) before changing runner configuration.
