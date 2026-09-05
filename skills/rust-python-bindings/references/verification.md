# Binding verification

Start with the real package root, interpreter, and pinned tools. The sampled repositories differ: Modbus declares Python 3.14+; BACnet and Haystack declare 3.11+. Preserve the applicable policy and verify actual Cargo/Python metadata before using these observations.

Use focused Rust tests and Python tests for behavior. For a distribution change, separately build with maturin, install the explicit wheel into a clean environment, change outside the checkout, inspect module origin, and run public consumer tests. Do not allow uv/project synchronization to reinstall an editable package over the wheel.

For free-threaded claims, observe build marker plus runtime GIL state after normal extension/dependency imports, then run concurrency tests. The pyo3-free-threading skill includes an optional bounded interpreter probe. Missing introspection, ordinary CPython tests, or a forced-disabled startup do not prove voluntary module compatibility.

For ABI decisions use the pinned PyO3 feature/distribution pages. The 0.29.2 feature reference distinguishes abi3, 3.14t version-specific artifacts, and abi3t for 3.15+. Some general free-threading documentation retains an older limited-API caveat; verify the specific ABI/toolchain rather than copying it as a universal restriction.

Sources: [PyO3 types](https://pyo3.rs/v0.29.2/types), [free-threading](https://pyo3.rs/v0.29.2/free-threading), [ABI features](https://pyo3.rs/v0.29.2/features), [Maturin](https://www.maturin.rs/bindings.html), [CPython runtime evidence](https://docs.python.org/3.14/howto/free-threading-python.html).
