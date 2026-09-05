---
name: rust-nextest
description: "Select, run, diagnose, or configure Rust tests with cargo-nextest. Covers profiles, filters, resource limits, doctests, and truthful test results; not test design alone."
license: MIT OR Apache-2.0
---

# Rust Nextest

Use the repository's wrapper or documented gate before inventing an equivalent command. Read its flags rather than dropping inconvenient ones. This skill changes neither test requirements nor CI policy.

## Resolve what will run

Inspect Cargo members/default-members/excludes, test targets and `required-features`, `.config/nextest.toml`, relevant environment overrides, toolchain, and installed `cargo nextest --version`. Compare the runner version with the configuration keys actually used. A recommended version is not an enforced minimum. Unsupported settings or warnings require investigation, not suppression.

Choose the changed package and the consumer tests that exercise its behavior. List the selected tests with the same features, target selection, filter, and profile before a complex run. Cargo package selection decides what is built; nextest filtersets select from that built universe. An `rdeps(...)` filter cannot restore packages excluded by `-p`.

Respect default filters and ignored/hardware suites. Do not use `--ignore-default-filter` or `--run-ignored all` just to increase counts. Check why tests were excluded and whether their prerequisites and permissions exist. Fail a gate that was expected to run tests but selected none; use `--no-tests=fail` where supported and preserve it in existing gates.

## Run the correct configurations

Nextest's `--profile ci` chooses runner policy. It does not select optimized Cargo code generation; use `--release` or a verified `--cargo-profile` separately. Keep feature and package scope consistent across a comparison.

Run doctests separately with the repository's `cargo test --doc` command. Neither a successful nextest run nor `--all-targets` establishes doctest success. Excluded binding crates and external language tests also need their own path.

Distinguish benchmark smoke tests from measurements. Compatible Criterion targets can run in nextest test mode; one successful iteration proves neither speed nor statistical improvement. Current nextest also offers experimental benchmark measurement, but do not enable it by default or bypass the existing harness.

## Diagnose without hiding failures

On failure, keep the first output and reproduce the smallest relevant selection. Check fixture isolation, child processes, deadlines, feature gates, and runtime flavor before broadening timeouts. A retry can gather information; it does not erase a flaky result or justify adding gate retries.

Budget build parallelism separately from test-process concurrency and each test's own workers. Use per-test weights/groups for known heavy or mutually exclusive tests instead of serializing the entire suite. Groups coordinate one nextest invocation, not another agent or CI job. Prefer per-test temporary directories and ephemeral ports where the protocol permits.

Terminate hung work through the documented timeout policy and inspect cleanup. A passing process with leaked child handles is not automatically healthy. Treat test-count reductions as a question to resolve, not a performance win.

## Report

Give the exact command, packages/features, Cargo codegen profile, nextest profile, selected/run/passed/failed/skipped counts available from output, and unrun suites. Explain whether the result is focused, a PR gate, or full release evidence. Never substitute a different runner silently when nextest is unavailable.

Use [command recipes](references/commands.md), [configuration and versions](references/configuration.md), or [advanced diagnostics](references/advanced.md) as needed.
