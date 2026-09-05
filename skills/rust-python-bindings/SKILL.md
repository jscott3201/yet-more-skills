---
name: rust-python-bindings
description: "Plan or implement a mixed Rust/Python binding change: map PyO3 contracts and select ownership, async, free-threading, buffer, or wheel checks. Use for the boundary as a whole, not pure Rust or pure Python work."
license: MIT OR Apache-2.0
---

# Rust Python Bindings

Read local instructions, the actual PyO3/async-bridge/maturin versions, Python support policy, and build path. Keep language-independent behavior in Rust and conversion, Python exceptions, and Python-facing lifecycle in the binding. This entry is the map for a mixed task, not a requirement to invoke every specialist.

## Map the exposed contract

Locate Cargo and Python manifests, workspace/default-member/excluded-crate status, module registration, public imports, stubs, interpreter selection, and existing tests. Separate distribution, Rust crate, and Python import names. A Rust workspace gate cannot validate an excluded binding, Python behavior, or installed package contents.

For each changed crossing, identify owner and borrow duration, thread/loop affinity, mutation, conversions, errors, and cleanup. Preserve domain identity, units, precision, null/sentinel distinctions, and protocol side-effect semantics. Do not remove a correct owned copy just to claim zero-copy, retain borrowed Python references beyond attachment, or weaken safe-core policy for binding macros.

## Select only relevant checks

When installed, use the specialist that matches the work:

| Concern | Skill |
|---|---|
| Bound/Py ownership, pyclass borrows, conversions, exceptions, stubs | pyo3-ownership-errors |
| Tokio/asyncio, blocking wrappers, cancellation, close/drop | pyo3-async-lifecycle |
| Module declarations, shared state, post-import GIL, concurrency | pyo3-free-threading |
| Boundary profiling, batching, NumPy/buffers, ownership and retention | pyo3-buffer-performance |
| Maturin, ABI, native wheels, sdist, installed typed consumers | pyo3-wheel-release |

They are optional depth, not mandatory dependencies. If unavailable, apply the relevant checks below and use primary documentation. Do not add new agents, model settings, approval rounds, or unrequested CI.

## Baseline safeguards

Extract or retain valid owned inputs before detached/async work, then attach to use Python APIs. Attachment is not application mutual exclusion on GIL-disabled Python. Release borrow guards and core locks before reentrant callbacks. Since PyO3 0.28 module support defaults changed; neither adding nor omitting gil_used=false is proof of concurrency correctness.

Trace each runtime's owner, admission/close, task cancellation, callbacks, and final destruction. The async bridge can cancel its wrapped Rust future, but already-sent writes, independently spawned tasks, and blocking work have their own lifetime. Keep immediate abort distinct from graceful shutdown and finalizer behavior.

Validate the actual Python interface: exceptions, arguments/defaults, returned awaitables, context managers, top-level/submodule imports, and type consumers. For support claims use the intended interpreter and verify post-import GIL state. Stable ABI, free-threading, and subinterpreters are distinct promises.

Build and test an explicit installed wheel outside the checkout when packaging or release claims matter. Use native hosts/containers for promised platforms, not emulation/cross-compilation as substitute evidence. Coordinate build ownership and keep expensive matrices in established release lanes.

Report the change, Rust and Python checks separately, artifact and interpreter evidence, and unrun platform/concurrency cases. Read [verification notes](references/verification.md).
