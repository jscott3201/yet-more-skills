---
name: rust-api-design
description: "Design or refactor Rust APIs, ownership, traits, and error boundaries. Use for semantic interface changes, not test-runner configuration or speculative optimization."
license: MIT OR Apache-2.0
---

# Rust API and Ownership

Start from the call sites and the invariant the API should make easy to preserve. Follow repository policy before applying general style preferences; this skill does not authorize a breaking release or a rewrite.

## Design from use

Read the implementation, two representative callers, public documentation, feature gates, and existing error types. Identify who owns data, how long a view may live, whether work crosses a thread/task boundary, and whether results must survive mutation or buffer reuse.

Use slices and borrowed views for temporary access, owned values for independent lifetime, and shared ownership where there are real independent owners. Do not clone merely to silence the borrow checker; first shorten a borrow, split a phase, move the owner, or separate fields. Conversely, one bounded copy at an API boundary can be simpler and cheaper than pervasive lifetimes or reference-count churn. Avoid introducing `Arc<Mutex<_>>` as a universal ownership escape hatch.

Prefer constructors and validated newtypes where invalid values create real failure modes: IDs, lengths, bounded quantities, deadlines, units, or lifecycle capabilities. Avoid a generic typestate framework when a small enum or checked constructor communicates the contract. Make destructive actions and expensive conversions visible in naming and ownership.

## Trait and error decisions

Choose generics, enums, or dynamic dispatch from the required extension boundary, code size, compile time, and profiling evidence. Preserve intentional static dispatch in protocol transports. Native async/RPITIT trait methods do not automatically become usable through `dyn`; inspect current trait constraints and actual consumers before promising that interface. Do not add `async_trait` just to follow an old recipe.

Keep expected input, I/O, and domain failures typed where callers act on them. Preserve source errors and useful context at boundaries, without erasing actionable variants into strings throughout a library. Reserve panics for genuinely internal violated assumptions under repository policy; do not hide malformed-input failures behind `unwrap` or default values. An explicit `expect` with an established invariant can be more honest than a fabricated fallback.

Preserve trait laws and semantic contracts: `Eq`/`Hash`, ordering, iterator behavior, units, absence versus zero, null versus missing, and cancellation effects. Do not derive traits for values whose semantics do not satisfy them.

## Make the change

Keep the public surface minimal and dependency direction intact. Write rustdoc examples for the real caller workflow and document relevant errors, panics, safety, allocation, and lifecycle behavior. Use established naming/conversion conventions rather than mechanically enforcing every optional guideline.

Add a regression or compile-time example demonstrating the intended use. Validate affected consumers, feature combinations, and doctests separately. Run rustfmt and the repository's Clippy scope; fix causes before adding a narrowly justified lint allowance. Do not blanket-enable every pedantic/restriction lint or reformat unrelated code.

## Return

Explain the ownership or semantic improvement, compatibility impact, affected callers, and evidence. For a hot-path refactor, avoid claiming faster code without measurement. For greenfield code, favor a clean contract rather than preserving accidental internal APIs.

Read [design checks](references/design-checks.md) for boundary-specific questions.
