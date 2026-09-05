---
name: rust-memory-layout
description: "Investigate Rust allocations, copies, buffer retention, collection layout, and cache locality. Use for measured memory or data-access bottlenecks, not blanket clone removal."
license: MIT OR Apache-2.0
---

# Rust Memory and Data Layout

Start with the ownership path and observed cost. Preserve the existing safety, API, and serialization contracts. Use `$rust-performance` for the overall experiment when available; this skill focuses on the memory mechanism.

## Trace data through the operation

Map input ownership, parsing, intermediate values, queues/caches, output ownership, and destruction. Identify actual allocations and deep copies separately from shallow handles. Measure allocations per operation, bytes allocated, peak live memory, and retained memory under representative steady-state and burst load. RSS is useful but is not identical to live heap bytes or a leak.

Examine common and worst-case sizes and lifetimes. A small borrowed view or `Bytes` slice may retain a much larger owner. A buffer pool may lower allocation count while raising high-water memory. A change is not better merely because `.clone()` disappears or an allocation counter falls.

## Choose the simplest effective representation

Prefer moving existing ownership, writing into caller-owned buffers, reserving a justified capacity, or reusing scratch storage within a bounded lifetime. Validate input lengths before reserving; attacker-controlled lengths are not safe capacity hints. Use checked arithmetic for byte counts, offsets, multiplication, and conversion across integer widths.

Keep zero-copy boundaries honest. Distinguish no payload copy from no allocation, no reference-count operation, and no later consumer copy. Convert to ownership deliberately when a result must outlive input or enter a background task. A small copy can reduce retention and simplify aliasing.

Consider contiguous layouts, compact indices, inline small values, batching, or structure-of-arrays only for the observed access pattern. Include object size, cache misses, initialization, deletion, and index maintenance in the comparison. Do not assume an inline collection is always cheaper: unused capacity can inflate every object. Prefer existing types and small local code over a dependency without a measured need.

Choose maps and hashers according to adversarial input, deterministic output requirements, and lookup workload. Do not trade away hash-flooding resistance casually. Stable output ordering should be explicit; it must not depend on incidental randomized iteration order.

## Preserve safety and portability

Use safe slice/chunk APIs before unchecked indexing or representation casts. Never change `repr`, field layout, packed access, or byte interpretation merely to silence padding reports; Rust memory layout is not a wire format. Do not bypass a crate's `forbid(unsafe_code)` policy for a microbenchmark.

For long-lived caches and arenas, define the retention boundary and invalidation owner. Inspect stale IDs and generation checks after deletion or compaction. Avoid making every request retain an entire graph snapshot when a smaller result suffices.

## Validate and return

Run behavioral tests and realistic burst/steady-state measurements. Check tiny inputs, large payloads, high concurrency, and repeated clear/reuse cycles. Compare latency and memory together. Report which copy/allocation was removed, the ownership lifetime before and after, measured costs, and any increased retained memory or complexity.

Read [memory investigation notes](references/investigation.md) for implementation-specific questions.
