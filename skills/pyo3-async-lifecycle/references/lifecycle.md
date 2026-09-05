# Lifecycle cases

The sampled Modbus async wrapper clones an Arc-backed native client before creating bridge futures, provides shutdown and abort, and awaits shutdown from __aexit__. Its synchronous companion owns a Tokio Runtime and uses py.detach around blocking operations. These are distinct ownership paths: validating the async context manager does not validate synchronous finalization, and vice versa.

A bounded test can start a loopback server, admit a request, synchronize on server observation, cancel the Python Future, and verify the promised native cleanup. Avoid sleeps as the only ordering mechanism. Test cancellation before admission separately from cancellation after a request was sent. The expected device-side effect must reflect the actual protocol contract.

Closing an event loop before Rust callbacks finish can produce dropped delivery or errors; callbacks must not retain an obsolete loop indefinitely. A successful asyncio test in one loop does not prove multi-loop reuse or subinterpreter support. Import, construct, close, delete, and process exit should be tested in the combinations the public API promises.

Blocking threads cannot generally be force-cancelled safely. A dropped wrapper future may abandon a result while the underlying computation continues. Keep a cancellation token/cooperative stop or join policy at the work owner where needed. Do not infer stopped I/O from a cancelled await alone.

Primary references: [future_into_py cancellation/context behavior](https://docs.rs/pyo3-async-runtimes/latest/pyo3_async_runtimes/tokio/fn.future_into_py.html), [asyncio developer guidance](https://docs.python.org/3.14/library/asyncio-dev.html), [PyO3 parallelism](https://pyo3.rs/v0.29.2/parallelism), [Tokio runtime](https://docs.rs/tokio/latest/tokio/runtime/struct.Runtime.html).
