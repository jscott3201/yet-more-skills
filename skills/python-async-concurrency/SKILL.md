---
name: python-async-concurrency
description: "Design or debug Python asyncio tasks, deadlines, cancellation, backpressure, async resource ownership, and shutdown. Use pyo3-async-lifecycle for the Rust bridge itself."
license: MIT OR Apache-2.0
---

# Python Async and Cancellation

Map who owns the event loop, tasks, client sessions, queues, and shutdown. Identify the supported Python version and any AnyIO/Trio use; do not introduce a second async framework or call asyncio.run from a library function inside an active loop.

## Make task lifetime explicit

Use an existing structured-concurrency pattern or TaskGroup when the supported floor and failure semantics fit. A task group's sibling-cancellation behavior is a design decision, not interchangeable with gather. Retain and supervise tasks created outside a group; do not lose exceptions in fire-and-forget work. Handle ExceptionGroup deliberately at an appropriate boundary.

Use try/finally and async context managers for cleanup. When catching CancelledError for cleanup, normally re-raise it. Cancellation is not an ordinary recoverable request error. Shield only an intentionally owned bounded operation and keep its task handle; shielding without supervising completion leaves orphan work.

## Define admission, time, and overload

Bound both queued and active work. Placing a semaphore inside a task does not bound the number of tasks already created. Prefer bounded queues or bounded producers, with an explicit full-queue policy. Specify one logical deadline and how retries consume it; do not reset the total budget at every layer.

Cancellation before admission, during I/O, after a remote write, and during shutdown have different consequences. Preserve idempotency and unknown-outcome semantics. A timeout is not proof that a device write did not occur. Reject blanket retry of mutating operations.

Use monotonic time for elapsed budgets. Distinguish connection, read, and whole-operation timeouts. Timer cancellation is cooperative; do not promise a hard wall-clock bound for code that blocks the loop or suppresses cancellation.

## Keep the event loop responsive

Do not call blocking I/O or long native work directly on the loop thread. Use an existing async API or a justified worker seam. Cancelling a to_thread await does not forcibly stop the worker; bound and own that work. Asyncio objects are not general cross-thread primitives: schedule through the loop's supported thread-safe entry points.

Test readiness, overload, cancellation races, partial construction, close twice, and cleanup errors using controlled local fixtures. Verify that shutdown observes every owned task and does not wait while holding a resource those tasks need. For native awaitables, inspect the bridge rather than assuming coroutine semantics.

Return the lifecycle contract, changed behavior, tests, and any remaining inability to cancel or stop work.

Read [async cases](references/lifecycle.md) for focused diagnostics.
