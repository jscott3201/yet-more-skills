---
name: rust-build-diagnostics
description: "Diagnose Rust compiler, linker, feature, or slow-build problems. Use for failing or inefficient builds; preserve useful caches and do not suppress correctness checks."
license: MIT OR Apache-2.0
---

# Rust Build Diagnostics

Reproduce the smallest failing or slow build before changing its environment. Respect repository toolchain and gate scripts. A build-tool failure is not automatically a source defect, and a source defect is not fixed by weakening the gate.

## Establish the failing stage

Record the actual command, package/features, compiler, target/host, profile, relevant environment, and first meaningful diagnostic. Distinguish dependency resolution, macro expansion, type checking, code generation, linking, test discovery, and runtime test failure. `cargo check` does not establish a successful link or a passing executable test.

Inspect workspace membership, cfg/feature gates, generated files, build scripts, native library requirements, and toolchain configuration. Match documentation to installed versions. Use compiler explanations, rust-analyzer navigation, and expanded diagnostics where helpful; do not rewrite an API to satisfy a guessed error.

## Repair the cause

For borrow errors, identify the real owner and use site; consider smaller scopes, separate phases, moving ownership, or splitting fields before cloning or introducing shared mutation. For trait errors, inspect bounds and auto-trait changes at the caller; an unsafe impl is not a compiler-error repair.

For feature errors, trace the actual enabling dependency and normal/build/dev graph. For linker/FFI errors, verify interpreter/native library and ABI selection before changing Rust logic. For stale generated code, run the documented generator rather than editing derived output alone.

Do not delete caches, lockfiles, or the entire target directory as the first diagnostic. A clean build is useful when testing a specific stale-artifact hypothesis, but it is costly and can destroy evidence. Avoid globally adding permissive lint flags, increasing limits, or downgrading dependencies without a supported cause.

## Investigate build time separately from runtime

Distinguish clean builds, incremental rebuilds, link time, and test execution. Use Cargo timing output on the relevant build. Inspect repeated compilation due to differing feature sets, flags, profiles, toolchains, or target directories; heavy build scripts; procedural macros; generic expansion; and unnecessarily broad workspace gates.

Prefer reusing compatible artifacts and narrowing local feedback to the affected crate. Do not conflate narrow feedback with the final required validation. Coordinate Cargo use among agents so memory pressure and duplicate work do not masquerade as slow code.

Evaluate profile changes, linker selection, generic versus dynamic dispatch, and dependency reduction against build time, runtime, code size, portability, and maintenance. Verify toolchain/platform support first. Do not prescribe a particular linker or cache service for every platform.

## Verify and return

Rerun the original failing command after the fix, plus the focused regression/consumer checks the change requires. When investigating speed, compare like-for-like warm/cold states and report the measured stage. A single faster warm run after a cold run is not a build optimization.

Return the root cause, minimal change, commands/results, and any remaining environment limitation. Label failures that could not be reproduced rather than claiming a speculative repair worked.

Read [diagnostic recipes](references/diagnostics.md) for a low-cost starting point.
