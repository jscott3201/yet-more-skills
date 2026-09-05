---
name: rust-numerics-simd
description: "Optimize or validate Rust numerical kernels, SIMD, vector scoring, and deterministic floating-point behavior. Use for arithmetic/data-parallel changes, not generic performance work."
license: MIT OR Apache-2.0
---

# Rust Numerics and SIMD

Define numerical correctness before selecting a faster implementation. Respect local unsafe-code and cross-platform policies. Safe SIMD libraries can be appropriate; new dependencies and target-specific paths still need evidence.

## State the result contract

Identify input domain, dimensionality, accumulator precision, zero/NaN/infinity behavior, signed-zero policy, tie-breaking, and whether the output requires bitwise identity or a documented error bound. An error bound must be justified by the product, not invented to pass a test.

Keep exact integer work in an exact representation. Converting large integers through `f64` can change comparisons or equality. For floating-point work, reassociation, parallel reductions, fused operations, and accumulator changes can alter results even when algebra looks equivalent. Deterministic behavior and mathematical accuracy are separate properties.

For vector retrieval, specify score direction and quality requirements, including recall or task-level quality. A faster approximate score is not equivalent to a faster exact score. Preserve independent or exact reference results for evaluation.

## Optimize in a useful order

Remove invariant work first: bind query norms, precompute reusable state, batch compatible operations, and avoid duplicate conversions or scans. Confirm the lifetime and invalidation of cached data. Then inspect the compiler's optimized code or profile to determine whether vectorization or multiple accumulators would address the measured bottleneck.

Use safe chunks and explicit scalar tails. Check equal lengths before zip-based kernels if the contract rejects mismatches; `zip` otherwise stops at the shorter input. Test dimension zero, lane-minus-one, lane, lane-plus-one, and threshold neighbors. Include long vectors and mixed magnitudes that stress cancellation and intermediate range.

Choose size-based dispatch only when evidence shows a crossover. Tiny inputs can lose to setup cost; wider vectors or more unrolling can increase register pressure and code size. Do not copy another implementation's thresholds into an unrelated algorithm or CPU without a measurement.

## Preserve portable deployment

Distinguish compile-time target features from runtime dispatch. A runtime CPU check is not evidence that another part of a globally specialized binary is portable. Do not publish general binaries compiled with `target-cpu=native`. Keep a baseline path and native tests on the architectures actually supported; record missing native coverage instead of substituting QEMU or cross-compilation in this workflow.

Respect a `forbid(unsafe_code)` workspace. Do not introduce raw intrinsics or weaken that policy for a speculative win. Verify stabilization and API availability against the project's pinned toolchain rather than assuming a proposed SIMD API is stable.

## Verify and return

Compare numerical behavior, deterministic ordering, tail handling, quality, and performance independently. Run end-to-end retrieval/control tests when a kernel feeds those systems. Reject a speedup that changes the required semantics. Report tested dimensions/architectures, result agreement policy, timing uncertainty, and unsupported claims.

Read [numerical examples](references/examples.md) for the reviewed codebases.
