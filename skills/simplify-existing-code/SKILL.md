---
name: simplify-existing-code
description: Simplify a requested code path by deleting unnecessary work, reusing existing behavior, or reducing caller complexity. Use explicitly for cleanup; not permission to weaken contracts, checks, or requested features.
license: MIT OR Apache-2.0
---

# Simplify Existing Code

Make the requested behavior easier to own without making it less correct. Simplicity is reduced coordination and maintenance cost—not the shortest line, smallest test count, or fewest files at any price.

## Understand before removing

Read the actual path, callers, tests, and user goal. Identify what each layer or dependency does today, including failures and cleanup. Separate dead or speculative behavior from requirements that look inconvenient. A one-implementation abstraction may still enforce a useful boundary; judge its purpose, not its count.

First ask whether redundant work can disappear. Then consider an existing helper, language/runtime facility, native platform behavior, or installed dependency that meets the same contract. Adding a small correct local implementation can be simpler than forcing an ill-fitting package; using a mature existing dependency can be simpler than maintaining a risky reinvention. Explain only consequential tradeoffs.

## Preserve the important costs and guarantees

Keep input validation, authentication, authorization, data-loss prevention, resource bounds, accessibility, and required error handling. Do not replace a cancellable or bounded operation with an unbounded convenience call. In protocols, storage, and bindings, preserve timing, durability, ownership, and error semantics.

Avoid incidental API redesign, broad formatting churn, clever compression, and permanent “simplification modes.” For a diagnosis-only request, propose the change without applying it. For authorized cleanup, make the smallest coherent change that removes a real source of complexity.

## Prove the same behavior still works

Use the existing test framework and meaningful behavioral checks. Do not impose a one-test ceiling, delete fixtures for aesthetic reasons, or replace a suite with a self-check. Add a targeted regression for an uncovered contract when needed.

Compare public results and failure paths before and after. Measure performance only when it is part of the goal; fewer lines do not prove lower latency or less memory. Report removed responsibility, preserved behavior, actual checks, and any remaining tradeoff.

This is an explicit task, not an always-on hook or authority to challenge settled user requirements repeatedly.
