---
name: python-packaging-environments
description: "Diagnose or change Python environments, dependencies, pyproject metadata, imports, or packaging. Use for uv/pip/build-backend issues; use pyo3-wheel-release for native ABI and wheel qualification."
license: MIT OR Apache-2.0
---

# Python Packaging and Environments

Inspect the existing package manager, interpreter selectors, lock/requirements files, build backend, and source layout. Prefer the established uv or venv/pip workflow; do not migrate managers, add redundant lockfiles, or update unrelated dependencies for a small task.

## Resolve the actual environment

Record the executable and version used for installation, tests, and builds. A shell activation or pyproject requires-python field does not prove which interpreter ran. Inspect installed package versions and module origins when imports are surprising. Distinguish distribution names from import names and editable source from a built wheel.

For uv projects understand --locked, --frozen, and --no-sync before selecting one. --locked checks lock freshness; --frozen uses the existing lock without that check; --no-sync leaves the environment unchanged and can therefore leave it stale. Ordinary uv run/sync may change files or environments. Do not silently upgrade the interpreter or replace a candidate wheel during validation.

Keep virtual environments local and owned by one task/agent while modifying them. Do not use sudo pip, install into system Python, dump all environment variables, or expose private index credentials. Package installation and build backends execute code; use trusted declared sources and explicit network permission.

## Keep metadata and runtime consistent

Separate build dependencies, runtime dependencies, optional extras, and development groups. A test dependency present in the development environment can mask a missing runtime requirement. Retain library compatibility ranges while locking the development/application environment appropriately. Check the supported Python floor before upgrading syntax or libraries.

A build backend runs in its own environment under build isolation. Ensure native and generated files required to build are in the source distribution. Inspect dynamic version sources, package data, stubs, entry points, and licenses. Never infer the contents of a wheel from the source tree.

## Verify the artifact

Build with the intended backend and interpreter. Install the explicit new wheel in a fresh environment with declared runtime dependencies, run from outside the checkout, and inspect module origin. For release changes also build from the sdist in a clean directory; local path dependencies and generated files must not be accidentally supplied by the working tree.

For a native extension, use pyo3-wheel-release when available or independently verify ABI, native platform, and build dependencies. Editable/maturin develop success is development evidence only.

Report the environment problem, minimal changes, dependency effects, artifacts actually tested, and remaining platform gaps.

Read [environment decisions](references/environments.md) for concrete commands and limits.
