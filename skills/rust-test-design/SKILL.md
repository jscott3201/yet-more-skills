---
name: rust-test-design
description: "Create or strengthen Rust regression, property, differential, fuzz, and concurrency tests. Use when evidence is missing or weak; use rust-nextest for runner mechanics."
license: MIT OR Apache-2.0
---

# Rust Behavioral Testing

Identify the behavior that could be wrong before choosing a test framework. Work within the existing test architecture; this skill does not require a new dependency, test service, or CI job.

## Build a small behavioral model

Read the contract, relevant call sites, implementation, and existing tests. Identify a concrete failure mode and the observable result that should distinguish it from correct behavior. Write the smallest regression first; confirm that it fails for the bug when practical, or explain why a pre-fix run is unavailable.

Cover representative boundaries rather than a long list of arbitrary examples: empty/one/max/over-limit inputs, zero and overflow, malformed nested data, exact deadline transitions, duplicate/stale messages, cancellation at resource acquisition, partial I/O, and cleanup after failure. Test the error variant and side effects, not just `is_err()`.

## Choose evidence for the risk

Use unit tests for local transformations and boundary arithmetic; integration tests for crate contracts and real lifecycle behavior. Property tests should generate valid domain values as well as deliberate invalid encodings, shrink failures, and retain actionable regressions. Bound generators so they can reach deep behavior rather than mostly reject input.

A round trip proves encoder/decoder agreement, not conformance: both can share a bug. Add independently derived vectors or a separately implemented reference model. A stored snapshot of the engine's own output is a regression/determinism check, not an independent correctness oracle. Record the origin of reference outputs and acknowledge shared formulas or kernels.

Use fuzzing for hostile bytes and bounded event sequences. Assert progress, resource limits, and semantic invariants, not merely absence of a panic. Promote interesting minimized inputs to ordinary regression tests. Use deterministic clocks or explicit timestamp events for timeout state machines; real sleeps alone are noisy and weak at exact boundaries.

For a synchronization change, consider a small Loom model using Loom synchronization types around the actual relevant algorithm. Model limits and uninstrumented dependencies restrict the claim. Add a real runtime integration test as a complementary check; neither is a substitute for the other.

## Challenge the test itself

Deliberately imagine or locally introduce one plausible incorrect implementation: swap a comparison, ignore an ID, skip invalidation, omit a tail, or acknowledge before persistence. Does the test detect it? A narrow mutation experiment can be more informative than a higher line-coverage percentage. Restore any experimental mutation immediately; never ship it or regenerate expectations to hide it.

Make parallel execution safe with unique temporary resources, explicit lifecycle ownership, and no implicit test ordering. Keep expensive fuzzing, exhaustive schedules, and broad coverage out of the ordinary PR path unless already required. Run focused tests now and describe deeper unrun validation honestly.

## Return

State the bug class, why these assertions would detect it, the test scope actually executed, and remaining blind spots. Do not equate test count, compilation, coverage, or a replayed golden with correctness.

Read [risk-to-test recipes](references/recipes.md) for this repository family.
