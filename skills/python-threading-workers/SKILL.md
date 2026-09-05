---
name: python-threading-workers
description: "Design or debug Python thread/process workers, shared-state synchronization, free-threaded Python behavior, and native thread-pool budgets. Not asyncio-only scheduling or PyO3 module auditing."
license: MIT OR Apache-2.0
---

# Python Threads and Workers

Identify the actual interpreter, GIL runtime state, process start method, native dependencies, and source of parallelism. Decide whether the work is I/O-bound, Python CPU-bound, or native CPU-bound before choosing threads or processes. Existing pools are part of the budget; more workers are not inherently faster.

## Shared state and ownership

Protect application invariants across compound operations, not just individual dict/list accesses. Do not use historical GIL behavior or built-in container locks as a transaction guarantee. Prefer explicit ownership, immutable snapshots, queues, or narrow locks. A frozen wrapper does not freeze its contained list or native handle.

Keep lock order consistent. Avoid calling user callbacks while holding non-reentrant locks; snapshot required state and invoke callbacks outside the critical section. Bound submissions, memory, and outstanding results. Define what happens to queued work during cancellation or failure.

For free-threaded execution audit module globals, caches, lazy initialization, iterators, context propagation, and third-party native state. Check the GIL after relevant imports. Separate same-object thread safety from independent-object parallelism. Do not declare subinterpreter support from free-threading evidence; interpreter isolation and module state are different requirements.

## Processes and native runtimes

Do not assume fork is the default or a safe shortcut. Inspect the selected platform and Python version. Allow callers to provide an appropriate multiprocessing context instead of globally changing a library user's start method. Worker entry functions and payloads must meet the selected context's serialization/import requirements.

Create native clients, runtimes, connections, and locks inside workers unless a specific cross-process transfer is supported. Do not fork an initialized Tokio or other multithreaded runtime and reuse its inherited handle. Guard application entry points and avoid spawning pools at import time.

Cancellation of an executor Future does not necessarily stop a running function. Provide cooperative cancellation for long work where required; an externally bounded subprocess may be needed for a hard operational boundary. Own worker shutdown and do not rely on daemon threads to flush durable work.

## Evidence

Use barriers/events with bounded joins for race tests and fresh processes for hang tests. Stress same-instance and separate-instance access, failure propagation, overload, and repeated create/close. Test the actual GIL-disabled configuration and native host combinations promised by the change. Report CPU/thread counts and untested interpreter isolation claims.

Read [worker checks](references/workers.md) for version and platform considerations.
