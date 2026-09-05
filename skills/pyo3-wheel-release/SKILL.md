---
name: pyo3-wheel-release
description: "Use explicitly for PyO3/maturin wheels, source distributions, Python ABI compatibility, stubs, native interpreter matrices, and artifact release checks. Not ordinary pure-Python installation or permission to publish."
license: MIT OR Apache-2.0
---

# PyO3 Wheels and ABI

Read Cargo.toml, pyproject.toml, the actual lock/toolchain, maturin version, workspace exclusions, and existing release policy. Identify the Python distribution name separately from the import module name and Rust crate name. Keep published version metadata consistent with the chosen source of truth.

## Define the compatibility promise

Separate minimum supported Python, tested versions, interpreter implementation, ordinary versus free-threaded build, ABI flavor, OS/architecture, libc/deployment target, and CPU feature baseline. Classifiers do not prove compatibility and requires-python does not prove all allowed versions have usable wheels. Do not drop an existing Python floor or add prerelease support without a product decision.

Use version-matched ABI guidance. Current PyO3 distinguishes ordinary `abi3`, version-specific free-threaded wheels for Python 3.14t, and `abi3t` for Python 3.15+ across GIL-enabled/free-threaded variants. These are not interchangeable. The backend, dependency APIs, selected interpreter, and actual wheel tags must agree. A Cargo feature named abi3 does not make every emitted artifact ABI-stable.

Stable-ABI compatibility is not numerical, thread-safety, NumPy C-API, or OS compatibility. Verify native dependency support independently. Do not copy a generic CI matrix using emulation, QEMU, cross-compilation, or a universal target when this workflow calls for native builds and tests. Use appropriate native hosts/containers and clearly state untested platforms.

## Build and inspect

Use the repository's maturin configuration and explicit interpreter with the intended Rust release profile. Inspect module naming, extension initialization, included Python files, stubs, package data, licenses, shared-library dependencies, and ABI/platform tags. A developer's installed tool being newer than build-system.requires can hide a too-low build-backend floor; test the isolated build requirements that consumers will actually use.

Build the sdist and reconstruct a wheel from it in a clean directory. Watch for path dependencies outside the source artifact, untracked/generated files, workspace-only assumptions, and stale artifacts selected by a broad wildcard. Select the explicit artifact produced by the intended build.

## Exercise an installed consumer

Install into a clean environment, use a scratch working directory, verify module.__file__, and run public imports, exceptions, async/context-manager behavior, and representative operations. Do not let uv/project synchronization replace the wheel with an editable source install. Test the minimal runtime dependency set, not only a fully populated development environment.

Verify.pyi layout and actual type-checker discovery; a py.typed file in the source does not establish installed typing support. Exercise top-level and registered submodule imports. For free-threaded artifacts, record GIL state after normal imports and test concurrency separately. Keep Rust unit tests/doctests and Python artifact tests distinct.

Report artifacts and environments actually exercised, metadata/API differences, rejected assumptions, and release gaps. No publication, tagging, or workflow expansion occurs without explicit authorization.

Read [ABI and wheel checks](references/wheels.md).
