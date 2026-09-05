# Memory investigation notes

`Bytes` can share underlying storage across clones and slices. This is useful for moving protocol data through layers, but sharing also extends the allocation's lifetime. Check whether retaining a few bytes from a large frame is a sensible tradeoff for this workload. [Bytes API](https://docs.rs/bytes/latest/bytes/struct.Bytes.html).

When a core separates borrowed, allocation-free codecs from owned transport frames, preserve that boundary; do not introduce `Bytes`, `String`, or an allocator into the foundation just because a higher layer uses them.

For a vector/string optimization, look for repeated `collect`, temporary formatting, nested allocation, redundant conversion, and short-lived clone chains. First determine whether each is on a hot path. Lifetime-heavy rewrites can create more maintenance cost than their bounded copies save. [Heap allocations](https://nnethercote.github.io/perf-book/heap-allocations.html).

For a slot map or ring, smaller storage is only one goal. Stale handles must not alias a new occupant, cancellation must not free another request's slot, and compaction must maintain references or deliberately invalidate them. Use exact identity checks plus tests for generation/ID reuse.

Allocator profiling changes the workload and may need a separate binary or feature. Respect repository rules on permanent instrumentation and dependencies. Keep instrumentation out of a before/after wall-clock comparison unless both sides use the same setup. [Profiling](https://nnethercote.github.io/perf-book/profiling.html).
