---
name: python-performance
description: "Profile, benchmark, or optimize Python CPU, latency, throughput, allocations, startup, or native-call overhead. Requires a representative workload; not a blanket rewrite into Rust."
license: MIT OR Apache-2.0
---

# Python Performance Engineering

Define the user-visible workload and correctness contract first. Identify whether the bottleneck is Python execution, object conversion, native compute, I/O, queuing, startup, or memory retention. Reuse an existing benchmark before adding another framework.

## Establish a comparable baseline

Record the interpreter/build variant, GIL state after imports, extension build mode, relevant dependencies, input size, concurrency, and warm/cold conditions. Compare on the same native host without other benchmark or compilation jobs. Do not compare a debug extension to a release extension and attribute the difference to a code change.

Use a profiler to locate cost, then measure without profiling overhead. Standard-library cProfile and tracemalloc can answer Python questions, but Python allocation tracing does not automatically account for Rust Vec/Arc/allocator memory. Use native profiling or process-level measurements when the cost crosses that boundary, and distinguish live objects, allocator retention, mapped memory, and RSS.

Prefer a representative end-to-end case plus a focused microbenchmark. Use pyperf when already available or justified for repeated measurements; retain raw output and inspect instability. A single fastest timing, or an average with failures omitted, is not evidence. Measure completed operations and include error rate, payload shape, queue depth, and tail latency where relevant. Do not run privileged system tuning without explicit authorization.

## Optimize in a useful order

Remove repeated work and unnecessary protocol crossings first. Consider batching, parsing once, fewer intermediate objects, better algorithms, bounded caching, and reusing connections. Check retained memory and latency tradeoffs: streaming can defer errors, batching can delay small requests, and caching can serve stale data.

At a Rust boundary measure Python conversion, native computation, and result construction separately. Replacing many small calls with one batch may matter more than a faster kernel. Avoid unsafe zero-copy, unconditional detachment, wholesale vectorization, new allocators, or a Rust rewrite without measured need.

For free-threading, measure both single-call overhead and realistic parallel scaling. Bound Python workers, Rust/Tokio/Rayon workers, and any numerical-library pools as one CPU budget. Independent processes or fewer threads may outperform nested parallelism; measure rather than prescribe.

Run correctness tests before and after. Report baseline/candidate measurements, variance, relevant regressions, and one of keep, reject, or inconclusive. Microbenchmark improvement is not a product-wide speedup.

Read [measurement notes](references/measurement.md) for the boundary-specific questions.
