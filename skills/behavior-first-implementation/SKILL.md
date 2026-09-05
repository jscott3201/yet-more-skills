---
name: behavior-first-implementation
description: Implement an authorized change with test-first vertical red-green-refactor cycles when TDD is requested or required. Use observable behavior; not diagnosis-only work or a mandate to replace existing tests.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Behavior-First Implementation

Use TDD inside the requested change. An explicit request to fix or implement supplies the task scope; a separate planning packet or orchestrator is not required. Follow repository test conventions and preserve unrelated work.

## Choose the observable behavior

Find a stable seam where a caller can observe the requested result, error, or state transition. Read the implementation and consumers before inventing an interface. Prefer meaningful existing unit, integration, or contract seams over forcing every check into the highest possible layer.

Derive expected results from a specification, independently worked example, trustworthy fixture, or independent implementation. A round-trip or duplicated algorithm can agree with the same bug. Use test doubles at true external boundaries or to control nondeterminism, not to lock tests to private call order.

## Work vertically

For one behavior, write the smallest useful failing test and run it. Confirm it fails for the intended missing behavior, not a broken fixture, import error, or unrelated environment problem. Make the smallest correct production change, rerun the focused test, and refactor within scope while it remains green.

Then add the next behavior the implementation has made clear. Avoid a large speculative batch of tests for interfaces that are still being designed. For legacy behavior, a characterization test may begin green; label it honestly rather than claiming a red-green cycle occurred.

Test relevant failure and lifecycle cases as well as the happy path. Reuse deterministic fixtures and the repository's runner. For Rust, preserve nextest selection semantics and separate required doctests. For bindings, include Python-visible evidence rather than only native tests.

## Finish with evidence

Run focused acceptance checks and the appropriate repository-required broader validation. Report what actually ran and what remains unrun. Do not disable flaky checks or overwrite expected results merely to obtain green output.

Ask only when a consequential public contract or owner decision remains unresolved. Routine implementation discoveries do not require a new approval loop. Commit, publish, or merge only when separately covered by the request and policy.
