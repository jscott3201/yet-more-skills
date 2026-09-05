---
name: python-review
description: "Use to review a Python patch for reachable correctness, resource-lifetime, testing, typing, packaging, or native-boundary defects. Not a request for a rewrite, style-only critique, or an extra approval gate."
license: MIT OR Apache-2.0
---

# Python Correctness Review

Follow the repository's existing review and delivery rules. Remain read-only unless asked to repair code. Review the changed behavior and its callers; do not expand a bounded patch into a redesign or add an approval cycle.

## Establish the real execution context

Read the patch, relevant original code, tests, Python floor, environment and dependency declarations. Confirm whether the consumer runs a script, source checkout, editable package, installed wheel, or embedded/native extension. A module import resolving to the wrong copy can invalidate an otherwise convincing test report.

Identify input domain, normal and exceptional exits, state transitions, resource ownership, and observable return/exception contracts. Trace at least one reachable failure path before raising a defect. Separate source evidence, reproductions, hypotheses, and unrun checks.

## Review semantics before style

Look for truthiness replacing missing-value handling, bool/int or datetime/date confusion, mutable defaults and shared state, lossy numeric conversions, unbounded queues/caches, leaked files/tasks, swallowed cancellation, and invalid retry assumptions. Check error context without exposing secrets. Type annotations, successful imports, and high line coverage are not runtime guarantees.

For async work, trace loop affinity, every background task, cancellation after external side effects, and teardown. For worker pools, examine process creation and object serialization, shared-state synchronization, and multiplicative parallelism. Do not assume the GIL supplies application locking or that free-threading support implies subinterpreter compatibility.

For PyO3 work, inspect the Rust implementation and stubs together: owner lifetime, borrow guards, callbacks under locks, detach boundaries, exception mapping, returned awaitable type, interpreter finalization, and installed-wheel behavior. Use the relevant pyo3 specialist when present; a generic unsafe-code checklist does not replace boundary reasoning.

## Judge evidence and propose the smallest repair

Ask whether a failing regression would detect the alleged problem. A round trip through the same native implementation is not an independent oracle. Check no-tests/all-skipped outcomes, development-only dependencies hiding packaging errors, and ordinary CPython being mislabeled as a free-threaded run. Run focused reproductions only when permitted and safe.

Prefer a minimal fix plus regression test. Do not recommend broad except/pass, new blanket retries, blanket ignore rules, unsolicited framework swaps, or suppression of failing native checks. Performance claims need comparable measurements, not intuition about Python versus Rust.

Return only actionable findings with severity under the existing rubric, location, trigger, impact, evidence, and proposed correction. State no findings when appropriate, together with coverage limits. Do not manufacture an issue to fill a review template.

Read [review examples](references/review.md) for the evidence bar.
