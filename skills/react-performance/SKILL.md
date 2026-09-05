---
name: react-performance
description: Measure and improve React rendering, subscriptions, expensive work, and route loading. Trigger on a concrete performance task, not ordinary React syntax or speculative memoization.
license: MIT OR Apache-2.0
---
# React Performance

## Measure the operation, not the component's reputation

Reproduce a slow user action with representative data, a defined browser/device class, and
the relevant production build. Separate network wait, JavaScript, React render/commit, layout,
and paint. Use the available profiler and browser tools; state explicitly when measurements
cannot be run. Development double rendering is not a production latency baseline.

Start with avoidable work: sequential independent requests, eager heavy routes, oversized
payloads, broad store subscriptions, repeated transformations, and excessive mounted UI.
Keep query state in its existing cache rather than mirroring it throughout a global store.
Select the smallest stable state slice a consumer needs.

## Choose the narrowest change

Memoize expensive work or stabilize references only when identity matters or profiling supports
it. Check whether React Compiler is actually enabled and which code it covers. Do not blanket
add or remove `memo`, `useMemo`, or `useCallback`. Keep hook dependencies correct.

Split heavy optional features using the application's supported lazy-loading path. A Vite SPA
does not use `next/dynamic`. Preserve useful loading/error fallbacks and avoid replacing one
waterfall with another. Keep imports within supported package exports.

Use deferred rendering or transitions for suitable non-urgent views without delaying controlled
input feedback or safety-critical status. These techniques schedule work; they do not make
expensive computation disappear. Virtualization and workers need their own accessibility,
ownership, and data-volume checks.

## Confirm the tradeoff

Compare before/after with equivalent data and conditions, including initial load, repeated
interaction, memory growth, and key correctness tests. Run performance measurements without
competing agent builds or browsers. An apparent win within run-to-run noise is inconclusive.
Reject changes that remove useful checks, hide stale data, lose keyboard focus, or weaken
backend confirmation just to make the interface appear faster.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
