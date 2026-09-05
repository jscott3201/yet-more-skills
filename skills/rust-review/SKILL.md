---
name: rust-review
description: "Review a Rust patch for concrete correctness, performance, API, and test gaps. Use for code review; do not create extra approval loops or rewrite code without authorization."
license: MIT OR Apache-2.0
---

# Rust Semantic Review

Review the patch in context, not just the changed lines. Respect repository reviewer roles, severity vocabulary, and stopping rules. This skill supplies technical findings; it does not add an approval panel or authorize editing, merging, or publishing.

## Understand the change

Read the intended outcome, diff, applicable instructions, affected callers, and relevant tests. Trace one real operation through the changed path. Identify the invariants that were previously enforced and whether the patch moves, removes, or duplicates their authority.

Separate confirmed behavior from assumptions. Repository documentation and agent summaries are navigation aids; confirm decisive claims in source or executed evidence. A code graph can identify callers but does not replace reading the actual branch/feature behavior.

## Follow failure paths

Check malformed input, numeric boundaries, ownership and borrowing, cancellation, partial mutation, resource cleanup, and concurrency. Look for accidental type-domain conversion, stale IDs, length arithmetic overflow, unbounded allocations/queues, swallowed errors, or silently changed defaults. Review `Drop`, early return, and panic paths where they own resources.

At API boundaries, inspect behavior and compatibility, not only signature changes. At protocol boundaries, preserve wire identity and authoritative specification meaning. At storage boundaries, inspect acknowledge/recovery ordering and derived-index invalidation. At numerical boundaries, apply the documented exact/tolerance contract rather than a generic epsilon.

If unsafe or FFI is involved, review reachable safe callers and safety invariants. Do not accept `Send`/`Sync` or layout assumptions merely because the code compiles. Use the relevant specialist only for a real question, not a mandatory checklist expansion.

## Test the evidence

Confirm that the selected test commands actually include the affected crate, feature, and consumer path. Separate nextest from doctests, excluded bindings, and hardware/OS qualification. Read assertions: a test name, snapshot, or high coverage percentage does not show that the suspected bug would be detected.

For performance claims, verify equivalent workload and semantics, timing boundaries, host/codegen settings, and uncertainty. A benchmark smoke pass is not performance evidence. Ask whether the improvement transfers from the microkernel to the stated product metric; require no broader claim than the measurements support.

Try to disprove each suspected defect with existing guards and caller constraints before reporting it. When practical, run a small reproducer or regression under the permitted role. Do not run duplicate heavy builds already coordinated by the parent or perturb a benchmark host.

## Report actionable findings

For a confirmed finding, give the severity in the repository's vocabulary, exact file/symbol, triggering input or schedule, consequence, and minimal repair/test. Rank by impact, not confidence of phrasing. Label an unverified risk or design question rather than presenting it as a defect.

Avoid style-only noise, speculative redesign, blanket dependency objections, and requests for tests unrelated to the changed risk. If no actionable issues remain, say so with the reviewed scope and unrun checks. Do not demand endless rounds after the existing stopping rule is met.

Read [review prompts](references/prompts.md) for focused adversarial questions.
