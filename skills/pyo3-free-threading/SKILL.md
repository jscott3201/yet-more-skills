---
name: pyo3-free-threading
description: "Use to audit or validate PyO3 on GIL-disabled CPython, including module declarations, synchronization, pyclass mutation, global initialization, and dependency imports. Do not infer support from a build flag alone."
license: MIT OR Apache-2.0
---

# PyO3 Free-Threading

Treat free-threading as a runtime and concurrency contract, not a compiler switch. Read the installed Python, PyO3, and native dependency versions before making compatibility claims. Preserve the repository's supported ordinary Python versions.

## Establish the environment

Record the executable, implementation/version, native architecture, free-threaded build marker, and actual GIL state before and after importing the extension and its normal dependencies. A free-threaded build can run with the GIL enabled; a dependency import can enable it. Missing runtime introspection is unknown, not proof of disabled execution.

Use [the interpreter probe](scripts/interpreter_probe.py) with explicit trusted module names and the intended executable. It runs imports in a bounded child process and reports their origins. It does not build the extension, establish thread safety, or force GIL-disabled mode. Use a scratch working directory and `--isolated` for an installed-wheel check when that matches the deployment. If the caller forces the GIL off externally, record that separately: it cannot demonstrate that modules voluntarily advertise compatibility.

## Audit the shared state

Since PyO3 0.28, generated modules default to declaring thread-safe support. Absence of `gil_used=false` is not a defect on those versions. An explicit declaration is still not a proof of application invariants. Inspect all exported submodules, dependencies, shared pyclasses, caches, callback registries, globals, and raw/unsafe assumptions.

`Python<'py>` denotes attachment, not exclusive access to application state on a GIL-disabled runtime. Pyclass borrow checking can reject simultaneous mutable access; it is not a queueing mutex. Define whether concurrent calls serialize, reject, or operate independently. Prefer immutable ownership or appropriately scoped synchronization over blanket unsafe Send/Sync or unsendable annotations.

Detach for long Python-independent work and blocking waits where the pinned API requires it; runtime-wide synchronization can still occur without the GIL. Check joins, one-time initialization, and lock acquisition that can block another thread needing Python. Use PyO3's version-supported PyOnceLock or synchronization helpers when appropriate, but still analyze lock order and reentrant callbacks. Never hold a core lock while invoking arbitrary Python merely because an interpreter-aware lock helper exists.

## Validate behavior, not just import

Test the same instance from multiple threads, independent instances, mixed read/write methods, callback exceptions, close during work, and repeated create/destroy. Use barriers/events for ordering and a subprocess timeout for hangs. Run representative ordinary and GIL-disabled variants, verify post-import state, and measure scaling separately from correctness.

Keep free-threading, subinterpreters, and embedded interpreter restart/finalization as distinct claims. Report exact exercised scope and unsupported dependencies. A compatibility opt-out can be honest temporary containment, not a performance success.

Read [validation details](references/free-threading.md).
