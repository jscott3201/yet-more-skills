---
name: rust-async-concurrency
description: "Design or debug Rust async lifecycles, cancellation, deadlines, locks, channels, and backpressure. Use for concurrent behavior; not a blanket conversion to async."
license: MIT OR Apache-2.0
---

# Rust Async and Concurrency

Map the operation's lifecycle before changing synchronization. Follow the repository runtime and ownership model; this skill does not authorize more writers, runtime replacement, or automatic retries.

## Identify ownership and state transitions

Find the admission authority, logical-operation lifetime, per-attempt lifetime, in-flight resources, completion authority, shutdown owner, and task handles. Explain what happens if the caller disappears at each await. Distinguish a timeout from rollback: a request may already have reached the peer or mutated state.

Keep permits, registrations, timers, buffers, and cleanup attached to the lifetime they actually govern. Use RAII or an equally explicit cleanup owner so early returns and cancellation cannot strand resources. Check exact request identity before completing or freeing a reused slot. A modular slot number alone is not identity.

## Bound work and waiting

Bound both queued and active work where the product needs bounded resources. A semaphore on active operations does not bound an unbounded input queue or tasks waiting to acquire it. Define overload behavior and whether deadlines include queueing. Preserve one absolute deadline when a total operation budget is intended, rather than resetting a timeout at every stage or retry.

Do not automatically retry non-idempotent writes or reinterpret ambiguous completion as no effect. Distinguish logical requests from attempts for permits, telemetry, and shutdown accounting. Use the protocol's retry/error classification and caller policy.

Choose synchronization from ownership and contention. Short, low-contention synchronous critical sections can be appropriate in async code; do not replace every mutex with an async mutex. Keep blocking guards and large CPU work out of await paths. Async mutexes can still create deadlocks or long serialized queues. Preserve lock order and avoid callbacks while holding locks when they can re-enter.

## Review cancellation and scheduling

Inspect each `select!` branch for cancellation safety and lost partial progress. A dropped future does not undo bytes written or state already changed. Retain framing/progress state across cancellation where required. Check fairness and shutdown responsiveness rather than assuming a busy ready branch will yield appropriately.

Move blocking work only when needed. A started `spawn_blocking` task cannot simply be aborted; use bounded concurrency and cooperative stop design for long-running work. Do not offload every tiny function or create a new runtime per request. Keep background tasks owned and their failures observable.

For custom atomics, write down what data an atomic publishes and which synchronization establishes visibility. An atomic counter used only for identity allocation is different from publishing initialized state. Prefer a simple lock until a measured reason and a sound ordering argument justify complexity.

## Shutdown and verification

Seal admission, let admitted work drain according to policy, signal cancellation when appropriate, and join owned tasks within the intended deadline. Preserve response/deadline processing during drain if admitted requests still depend on it. `Drop` is not an async graceful-shutdown mechanism.

Test cancellation before/after admission, mid-I/O, completion racing expiry, shutdown under load, task panic, stale replies, and resource recovery. Use deterministic clocks and a focused concurrency model where practical, plus real runtime integration. Return lifecycle invariants, tests, resource bounds, and unresolved interleavings.

Read [concurrency cases](references/cases.md) when selecting tests.
