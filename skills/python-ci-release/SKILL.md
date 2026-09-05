---
name: python-ci-release
description: "Use explicitly for Python CI, test gates, native release matrices, package artifacts, and release readiness. Preserve existing workflows; do not publish or add CI without authorization."
license: MIT OR Apache-2.0
---

# Python CI and Release

Read existing workflows, release policy, package roots, and the requested scope first. This skill is a delivery specialist, not permission to add workflows, publish packages, change branch protection, or broaden supported platforms.

## Separate everyday feedback from release qualification

Keep PR work focused: existing formatting/lint/type checks, affected behavioral tests and consumers, and a relevant native binding smoke when needed. A Rust core change that affects exposed behavior can require Python tests even if no.py file changed. Avoid path filters that silently exclude Cargo files, shared sources, stubs, or build metadata used by the binding.

Reserve expanded interpreter/platform/feature matrices, sdist reconstruction, free-threading stress, exhaustive compatibility, and long benchmarks for the established staged-release lane. This does not excuse skipping the tests necessary for the changed behavior locally. Report the light gate's actual scope instead of calling it full coverage.

Reuse repository scripts and pinned tool versions. Keep check-mode commands non-mutating: for an existing Ruff setup use `ruff check --no-fix` and `ruff format --check`; do not enable unsafe fixes or run an autoformatter across unrelated work. Use the selected type checker, not three competing checkers. Preserve exit codes through shell pipelines and distinguish collection errors, no tests, skipped tests, and expected failures.

## Build the product that users install

Use an isolated environment with the intended interpreter and backend. For extension changes, select native architecture, Rust build profile, Python ABI, and maturin features intentionally. No QEMU, emulation, cross-compilation, or universal-binary shortcut is a substitute for native qualification in this workflow. Run on native hosts/containers appropriate to each promised platform; Linux containers do not establish macOS behavior.

Install the explicit built wheel outside the checkout and inspect module origin. Verify runtime dependencies, public imports, native symbols through behavior, stubs/type consumers, entry points, and version metadata. Build from the source distribution in a clean directory before claiming source releases work. Keep debug editable builds out of performance claims.

Coordinate agents: one owner modifies an environment or build directory, fixed-port suites are not run concurrently, and performance runs have no competing builds. Use existing caching where safe; interpreter ABI, feature selection, OS/architecture, and toolchain differences must not reuse incompatible native outputs.

## Close with bounded evidence

List checks actually run, interpreter/platform/ABI, artifact tested, failures/skips, and release-only gaps. Dependency advisory scans and license checks should use the repo's established tools, not introduce an unsolicited security-tool stack. Keep credentials out of outputs and untrusted PR execution away from publication secrets.

Read [gate decisions](references/gates.md) before altering a matrix.
