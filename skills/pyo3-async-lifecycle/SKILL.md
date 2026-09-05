---
name: pyo3-async-lifecycle
description: "Use for pyo3-async-runtimes, Tokio/asyncio bridges, synchronous wrappers over async Rust, callbacks, cancellation, and close/drop behavior. Not generic async Python with no native boundary."
license: MIT OR Apache-2.0
---

# PyO3 Async Lifecycle

Read the installed pyo3-async-runtimes/PyO3 APIs and trace ownership across the Python loop, Tokio runtime, native client, task handles, and Python object. Reuse the repository's bridge; do not create a new runtime per request or nest runtime drivers indiscriminately.

## Define the lifecycle before editing

Identify who starts the runtime, admits operations, retains in-flight work, rejects new work during close, drains/cancels remaining work, joins tasks, and finally destroys the runtime. Separate graceful asynchronous close, immediate non-waiting abort, final object drop, and interpreter exit. A destructor cannot be assumed to await cleanup or run on a convenient thread.

Python awaitables and asyncio objects belong to their loop. Do not create bridge futures during import or before the intended loop exists, cache them across loops, or invoke asyncio.run inside an already-running loop. A bridge can return an asyncio Future: do not label every awaitable as a coroutine or assume create_task accepts it on all supported Python versions. Native workers must dispatch into the Python loop through the bridge or documented thread-safe facilities.

Clone the required native ownership and release temporary Python/pyclass borrows before crossing an await. Keep synchronous Rust waits detached from Python when the pinned API permits it. Detach does not resolve wrong-thread runtime destruction, unsupported nested block_on, or callbacks under a core mutex.

## Follow cancellation all the way down

The documented future_into_py bridge propagates Python Future cancellation to its wrapped Rust future. Determine what dropping that future actually cancels. Separately spawned tasks, blocking work, transport sends, and committed database writes may continue. Preserve protocol identity and cleanup guards; never describe a timeout as proof that no external side effect happened or retry a write blindly.

Use one close deadline, stop admission before draining, and keep response/timeout processing alive while needed. Make repeated close and abort-after-close behavior explicit. Ensure cancellation during close does not leak the runtime or leave hidden admitted work. Do not shield entire operations just to make cancellation tests green.

Treat context propagation deliberately. The bridge documents contextvars handling for converted asynchronous Python calls; synchronous callbacks from Rust do not automatically inherit that context. Use the documented explicit context mechanism where required and test it rather than depending on thread-local coincidence.

## Validate the seam

Test normal completion, Python cancellation, native error, close with in-flight work, repeated close, callback exception/reentry, multiple supported event loops, and interpreter/process exit. Bound hang-prone cases with a supervising subprocess. Recheck task/permit/socket cleanup, not just the awaited exception.

Report the operation and teardown contract, surviving work after cancellation, commands, and untested runtime/interpreter cases.

Read [lifecycle cases](references/lifecycle.md).
