---
name: pyo3-ownership-errors
description: "Use for PyO3 Python/Rust conversions, object lifetime, pyclass borrows, callbacks, exception mapping, and signature/stub consistency. For ABI packaging or async runtime teardown use the corresponding specialist."
license: MIT OR Apache-2.0
---

# PyO3 Ownership and Errors

Start from the actual PyO3 version, Python floor, generated module layout, and Rust crate policy. Keep Python-independent logic in the Rust core and Python conversion/exception policy in the binding. Do not weaken safe-core lints just because PyO3 macros need a separate boundary crate.

## Map each crossing

For each changed argument, result, callback, or stored object, name the owner, borrow duration, mutability, thread/interpreter affinity, and error behavior. `Bound<'py, T>` is tied to an interpreter attachment lifetime; `Py<T>` owns a Python reference but does not make the object immutable, interpreter-independent, or safe to use without attachment. Do not extend lifetimes, store borrowed pointers in workers, or add unsafe Send/Sync to silence compiler constraints.

Convert or retain owned inputs before detaching or moving work into an async task. A safe owned copy is often the right boundary; eliminate it only with a proven lifetime and synchronization model plus performance evidence. Drop pyclass borrow guards before reentrant Python callbacks. Rust locks and Python attachment are separate resources with a lock order; avoid calling user code while holding a core lock.

A frozen pyclass can simplify ordinary field mutation but is not a blanket proof for interior mutability, native handles, caches, or callbacks. An unsendable class is an explicit thread-affinity contract, not an automatic fix for sharing. Keep extension module and interpreter lifetime in mind for globals and caches; use the version's interpreter-aware initialization facilities when warranted.

## Preserve Python behavior

Choose explicit signatures/defaults and meaningful exceptions. Distinguish bad Python types, out-of-range values, invalid protocol data, transport failures, cancellation, and internal defects. Preserve native error context and public exception inheritance. Do not flatten every error into RuntimeError or turn a Rust panic into normal domain control flow. Panic handling does not make undefined behavior recoverable.

Test numeric narrowing, bool/int, missing/None, nested conversion, Unicode, and domain-specific sentinels. Conversion methods may execute Python and reenter the extension. Match `.pyi` files to runtime imports, classes, positional/keyword arguments, defaults, awaitables, context managers, and exceptions. Prefer real consumer tests when native signature introspection is incomplete.

## Validate at both sides

Run relevant core tests plus installed Python consumer tests. Include repeated object creation/destruction, callback exceptions/reentry, invalid conversions, and explicit close. For resource-owning objects, verify ownership after owner deletion and avoid relying on garbage collection timing for correctness.

Report ownership decisions, failure contracts, tested Python surface, and unresolved lifetime or interpreter assumptions. Ask for policy guidance when supporting subinterpreters or changing public coercion rules would broaden the product.

Read [boundary checks](references/ownership.md) for examples and source links.
