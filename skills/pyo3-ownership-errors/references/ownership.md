# Boundary checks

Prefer three phases for a blocking operation: validate/extract while attached; perform Python-independent work while detached using owned or correctly synchronized data; reattach to construct Python results. `detach` does not sanitize captured raw pointers, mutable buffers, or Python references. Conversely, retaining a Py handle while detached can preserve ownership, but accessing its Python API still requires valid attachment to the owning interpreter.

Expose stable domain errors through the binding's exception hierarchy. For example, the sampled Modbus wrapper uses a central client_error_to_pyerr mapping; test that sync and async APIs preserve consistent public categories. Distinguish an invalid Python argument from an actual device exception. Keep useful causal information without revealing credentials or raw sensitive payloads.

Native text signatures aid inspection, but metadata is not behavior. Call methods with positional and keyword variants, omitted optional values, and wrong inputs. A returned Future is awaitable but not necessarily a coroutine object; test consumer scheduling behavior and type annotations accordingly.

Python callbacks stored in Rust objects may form reference cycles. Where Python-owned references participate in cycles, inspect the version's GC integration protocol; do not implement a generic destructor or global cache as a substitute. Never assume process-global Python objects can be reused across independent interpreters or after shutdown.

Primary references: [PyO3 types](https://pyo3.rs/v0.29.2/types), [thread safety](https://pyo3.rs/v0.29.2/class/thread-safety), [exceptions](https://pyo3.rs/v0.29.2/exception), [function signatures](https://pyo3.rs/v0.29.2/function/signature), [Python protocols](https://pyo3.rs/v0.29.2/class/protocols), [synchronization](https://pyo3.rs/main/doc/pyo3/sync/index.html).
