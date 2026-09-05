---
name: rust-performance
description: "Profile, benchmark, or optimize Rust latency, throughput, CPU, or memory. Requires a workload and correctness contract; not a license for speculative rewrites."
license: MIT OR Apache-2.0
---

# Rust Performance Engineering

Treat optimization as an experiment with a reject option. If the repository already uses a performance A/B review skill, provide the Rust-specific work under that workflow instead of adding another review gate.

## Define the useful result

Name the workload, metric, baseline behavior, and allowed semantic change. Distinguish codec cost, end-to-end request latency, throughput at a given concurrency, tail latency under saturation, retained memory, and cold-start behavior. An improvement in one does not establish the others.

Inspect existing harnesses and the actual hot path. Capture compiler/toolchain, Cargo profile, important flags/features, hardware/OS, workload scale, seed or data source, and whether caches are warm. Use an ordinary short benchmark note and saved output; do not build a new tracking system. Do not claim historical README numbers are measurements from this task.

## Profile before redesign

Reproduce the issue in a native, representative build. Use CPU or allocation profiling according to the observed bottleneck. Inspect dominant work, allocation/copy boundaries, lock waits, queueing, repeated parsing, and invariant computation. Optimize algorithms, unnecessary work, data access, or ownership before reaching for instruction-level changes.

Prefer a small hypothesis: bind query-only state once, reuse a buffer within a clear lifetime, avoid a repeated lookup, batch work without violating ordering, or replace an unbounded structure with a justified bounded one. Estimate whether the hotspot is large enough to matter. Avoid blanket `inline(always)`, unsafe indexing, a new allocator, fast hashers, or global CPU flags without evidence.

## Compare fairly

Run correctness checks before and after. Preserve the workload, compiler, features, optimization settings, and timing boundary between A and B. When changing compiler or codegen is itself the experiment, vary that factor explicitly rather than attributing the change to source code.

Use repeated samples and an A/B/A or alternating order when host drift is plausible. Keep agents, builds, and unrelated benchmarks off the measurement host. Decide whether setup, destruction, allocation, scheduling, or persistence belongs inside the measured operation; do not remove real product costs just to improve the chart.

Inspect per-workload results and uncertainty, not only an average. For end-to-end services, include timeout/error rate, backlog, memory, and tail latency at the same offered load. Closed-loop clients can reduce offered load as the server slows; do not label their latency distribution as unconstrained service capacity.

For graph/vector work, evaluate quality against an exact or independent baseline as well as speed. Changing candidate coverage, scoring precision, or durability is not a free optimization. For SIMD, compare tiny, tail, and large inputs on available native architectures.

## Decide and stop

Keep a change when the relevant improvement is credible and complexity/regressions are acceptable. Reject or label inconclusive when effects are small, noisy, workload-specific, or bought by weaker semantics. Do not keep tuning merely to obtain a positive result.

Return the hypothesis, commands, correctness evidence, baseline/candidate results with units and uncertainty, tradeoffs, and unmeasured platforms. No speedup claim from a build, smoke benchmark, or generated code inspection alone.

Read [measurement recipes](references/measurement.md) or [optimization choices](references/choices.md) as needed.
