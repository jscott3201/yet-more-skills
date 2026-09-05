---
name: rust-unsafe-ffi
description: "Audit Rust unsafe blocks, raw pointers, FFI, layout, and synchronization soundness. Use when a boundary exists or is proposed; never bypass a repository ban on unsafe code."
license: MIT OR Apache-2.0
---

# Rust Unsafe and FFI Review

Begin with the repository's unsafe policy. Where unsafe code is forbidden, preserve that policy and pursue safe APIs or an approved dependency boundary. This skill is an audit workflow, not permission to add unsafe code, relax lints, or assert thread safety.

## Find the actual unsafe boundary

Inspect unsafe blocks/functions/impls, FFI declarations, generated code, dependency wrappers, allocation owners, callbacks, and the safe entry points exposing them. Distinguish project-authored unsafe code from generated/dependency internals without assuming either is sound merely because it compiles.

For each operation, identify the caller obligations, invariants established before entry, and invariants the implementation must maintain. A safe wrapper must uphold its guarantees for all inputs reachable through its safe API, including error paths, panic/unwind behavior, reentrancy, and concurrent calls.

## Review memory and representation

Check provenance, bounds, allocation lifetime, alignment, initialization, aliasing/exclusivity, valid values, and drop ownership. A non-null pointer is not automatically valid to dereference. A buffer's capacity is not its initialized length. A zeroed byte pattern is not a valid instance of every Rust type. Do not infer stable FFI layout from ordinary Rust struct layout.

Review raw slice construction and pointer arithmetic at zero-length and overflow boundaries. Verify that pointer/length pairs describe the same live allocation. Preserve the distinction between an unaligned read and creating an invalid aligned reference. Check that owning pointers are released exactly once by the matching allocator/foreign API.

For concurrent code, inspect `Send`/`Sync` assumptions, atomics, interior mutability, and foreign thread affinity. An unsafe impl is a semantic promise, not a way to satisfy a compiler error. Keep publication/visibility and object lifetime reasoning separate.

## Review control flow across FFI

Define how panics and foreign exceptions interact with the chosen ABI. Do not assume `catch_unwind` catches aborts or arbitrary foreign exceptions. Keep callbacks' lifetimes, user-data ownership, thread constraints, and reentrancy explicit. Do not hold a Rust lock across a callback that can re-enter the protected API unless the design handles it.

Prefer small unsafe islands behind clear safe abstractions. Put a useful safety explanation next to the operation, stating the established invariant rather than repeating that it is safe. Do not expand an unsafe block to cover unrelated work or perform speculative unsafe optimization.

## Build complementary evidence

Use targeted Miri tests for supported pure-Rust paths when the toolchain is available and permitted. Use sanitizers or native FFI tests for relevant unsupported/external paths, and a bounded concurrency model when appropriate. These tools find classes of failures on exercised paths; passing them is not a proof of soundness. Do not disable isolation or widen permissions merely to force a test through.

Exercise malformed inputs, zero/large sizes, failed construction, early drop, callback reentry, and concurrent teardown. Keep the safe alternative as a differential baseline when useful.

## Return

List the safety invariant, evidence, concrete unsound path if found, and the smallest repair. State tooling/platform gaps explicitly. A speculative concern without a reachable violation should be labeled as such, not promoted to a confirmed defect.

Read [tool limits](references/tool-limits.md) when choosing evidence.
