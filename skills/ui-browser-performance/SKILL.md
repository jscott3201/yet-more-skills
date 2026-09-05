---
name: ui-browser-performance
description: Investigate or optimize browser interaction latency, network waterfalls, layout, bundles, retained memory, and large-data rendering. Requires measured evidence; not a generic micro-optimization checklist.
license: MIT OR Apache-2.0
---
# Browser UI Performance

## Define the workload

Name a real user operation, representative data size, browser/device class, and build mode.
Capture a reproducible baseline using available browser profiling. Separate network, parsing,
computation, framework work, layout, paint, and idle/wait time. Do not label a local test timing
as field INP or a microbenchmark as a complete user experience result.

Prioritize expensive avoidable work: serial independent requests, unnecessary payloads, eager
optional bundles, repeated computation, broad subscriptions, large DOM trees, and memory retained
after navigation. Investigate the bottleneck before adding caches or a new rendering framework.

## Choose bounded improvements

Lazy-load optional features with usable fallbacks. Keep critical interaction paths responsive
while limiting background work. Avoid preloading everything on hover or turning an import
cleanup into unsupported deep package imports. Measure both initial and subsequent interactions.

Use virtualization, workers, chunked computation, or batching when evidence supports them.
Account for worker startup and data transfer, main-thread result handling, accessibility, and
cancellation. Rendering less often must not erase audit events or misrepresent data freshness.
Bound caches, subscriptions, and telemetry retention; test repeated open/close/navigation cycles.

Avoid layout thrashing by understanding read/write sequences, but do not rewrite readable code
into low-level loops without a measurable effect. Check animations, reduced motion, large
overlays, and sticky elements when paint/layout dominates.

## Compare honestly

Run equivalent before/after workloads repeatedly without competing builds, browser jobs, or
thermal/resource contention. Record the changed metric and meaningful tradeoffs, including
correctness and memory. Treat results within observed variance as inconclusive.

Validate on the browser/device classes that matter or state them as untested. A smaller bundle,
faster synthetic loop, or smoother local animation is useful evidence, not proof of improved
field performance across all deployments. Keep profiling artifacts bounded and free of secrets.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
