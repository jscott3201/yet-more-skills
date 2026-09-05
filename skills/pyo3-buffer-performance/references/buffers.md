# Buffer decisions

`bytes`, bytearray, memoryview, and NumPy arrays expose different contracts. A read-only memoryview over mutable storage does not freeze other aliases. Contiguous storage is not necessarily aligned for a Rust type or in native byte order. NumPy slicing can create negative strides, non-contiguous views, and overlaps; a kernel requiring contiguous input should either reject with a clear error or make an explicit measured copy.

For rust-numpy, inspect the installed crate's borrow APIs. Dynamic borrow checking does not block until other borrows finish and cannot police arbitrary unchecked external code. Do not defeat a rejected borrow using unsafe access solely because the desired views seem disjoint. Build an owned immutable boundary or prove the actual memory ranges and synchronization under the project's unsafe policy.

Useful tests include empty and singleton arrays, dimensions not divisible by SIMD width, wrong dtype, reversed/strided slices, non-native endian data, overlapping input/output, input deletion, repeated output-view creation, and large-allocation retention. Validate numerical semantics independently of throughput. Releasing Python attachment during a kernel is useful only when every captured reference remains valid and safe.

Separate Python-client/Rust-server, Rust-client/Python-server, and Python/Python benchmark directions. That end-to-end distinction helps locate bridge and serving overhead rather than attributing all latency to the kernel. Do not copy historic performance numbers as current evidence.

Primary references: [rust-numpy borrowing and limitations](https://docs.rs/numpy/latest/numpy/borrow/index.html), [NumPy thread safety](https://numpy.org/doc/stable/reference/thread_safety.html), [PyO3 parallelism](https://pyo3.rs/v0.29.2/parallelism), [PyO3 performance-oriented flags](https://pyo3.rs/v0.29.2/features), [Python memory tracing](https://docs.python.org/3.14/library/tracemalloc.html), [Python memoryview](https://docs.python.org/3.14/library/stdtypes.html#memoryview).
