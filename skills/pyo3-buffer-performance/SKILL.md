---
name: pyo3-buffer-performance
description: "Use for measured Python/Rust boundary overhead, batching, Bytes/memoryview/NumPy exchange, zero-copy ownership, and native thread oversubscription. Not an instruction to replace correct copies with unsafe views."
license: MIT OR Apache-2.0
---

# PyO3 Buffers and Performance

Identify a real workload and measure the Python-visible operation before changing its representation. Separate Python call dispatch, argument extraction, allocation/copies, native kernel work, result construction, and I/O. A Rust-only microbenchmark does not measure the Python boundary.

## Choose the cheapest safe crossing

First consider fewer calls, batching, moving invariant conversion out of loops, reusing owned native objects, and returning a compact result. Avoid adding a framework or dependency for a small unmeasured gain. Preserve latency, cancellation granularity, memory bounds, units, precision, and public result semantics while batching.

For each buffer, record exporter/owner lifetime, dtype/item size, alignment, byte order, shape/strides, contiguity, writeability, overlapping views, and possible concurrent mutation. Validate dimensions and lengths with overflow-safe arithmetic before indexing or allocation. Do not reinterpret arbitrary bytes as typed aligned Rust slices or treat object-dtype arrays as plain numeric memory.

A read-only view is not proof that the backing allocation is immutable. rust-numpy borrow guards constrain cooperating Rust borrows; they do not synchronize arbitrary Python/C/Fortran mutation. Keeping an owner alive prevents deallocation but does not prevent resize or mutation through another alias. Detaching over externally mutable storage requires a valid exclusion/lifetime argument. When that cannot be established, make a bounded owned copy before detached work. Do not manufacture a runtime race to test known unsafe aliasing inside the main test process.

Use supported ownership-transfer/conversion APIs for outputs. An exposed view must keep storage alive after the temporary producer or input object is deleted. Remember that a tiny view may retain a large native allocation. Shared buffers, native caches, and reference cycles can dominate memory even when Python allocation tracing looks small.

## Measure fairly

Compare equivalent interpreter/build/GIL modes and release-built native artifacts with identical input distributions. Measure small and large payloads, contiguous and strided inputs, aligned/misaligned or rejected inputs, and conversion-inclusive end-to-end performance. Record retained/process memory as well as allocation counts when relevant. tracemalloc alone does not account for arbitrary Rust/native allocations.

Avoid multiplying Python executors, Tokio workers, Rayon threads, and BLAS/OpenMP pools. Establish a whole-process concurrency budget before increasing any one pool. Do not change process-wide threading knobs invisibly or benchmark while other agents build.

Leave PyO3 reference-pool disabling, raw-pointer shortcuts, unchecked conversion, and specialized CPU flags out unless explicit evidence and safety review justify them. Some such options turn off-thread reference destruction into process aborts rather than a harmless speed tradeoff.

Report the boundary bottleneck, ownership/synchronization argument, measured change and variance, numerical/behavioral checks, and any workload regression.

Read [buffer decisions](references/buffers.md).
