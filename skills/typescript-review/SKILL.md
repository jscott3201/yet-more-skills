---
name: typescript-review
description: Perform a focused TypeScript/UI correctness review or review a frontend diff for reachable defects, missing evidence, data races, accessibility, and contract drift. Not a new PR approval gate.
license: MIT OR Apache-2.0
---
# TypeScript and UI Review

## Read the change in context

Establish the requested review scope and repository rules. Trace affected callers, state owners,
generated contracts, and tests. Distinguish the intended behavior from current implementation
and source comments. Review a coherent outcome; do not turn a focused patch into an unrelated
frontend modernization program.

## Look for consequential defects

Inspect unsafe narrowing, hidden null/undefined states, precision loss, changed serialization,
unknown discriminator handling, and edits to generated files. Follow async results through
changing props, route/site/session identity, unmount, cancellation, and revision conflict.
Check resource cleanup and repeated use, not only first render.

Use framework-correct reasoning: React hooks/effects and Svelte runes/ownership are different.
Match shadcn component APIs to the actual primitive backend and installed source. Check form
submit semantics, focus, labels, keyboard behavior, and browser/server separation.

For operational screens, verify that stale/unknown evidence is not shown as normal, a local
interaction is not treated as backend authority, and an accepted command is not presented as
a confirmed physical result. Assess performance claims against measured workloads rather than
endorsing speculative memoization or loop rewrites.

## Verify evidence and report

Inspect which package, test filter, environment, and build actually ran. Type checks, component
tests, browser tests, and visual inspection are separate evidence. Confirm that a new test
would fail for the original defect. Do not accept empty selections, automatic golden updates,
disabled checks, or broad retries as proof.

Report each actionable finding with location, reachable trigger, impact, and a focused remedy
or regression. Label uncertainty and unrun checks. Keep stylistic preferences separate from
correctness issues and use the repository's severity language.

Follow the existing review and delivery loop. This skill does not add an approval cycle,
authorize changes/merges, or override another role's ownership. A clean review is bounded to
the inspected scope; do not claim exhaustive certification.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
