---
name: module-design
description: Analyze or improve module boundaries, interfaces, ownership, and test seams for a requested design or refactor. Prefer simpler callers and local invariants; not automatic abstraction or permission to rewrite.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Module Design

Seek interfaces that give callers useful behavior without making them coordinate internal details. Keep related state, invariants, failure handling, and change together. This is design guidance, not a mandate to create architecture documents.

## Inspect the current pressure

Read the relevant source, consumers, tests, and repository terminology. Use code-index tools when available and useful; direct source inspection is a complete fallback. Identify the specific cost: duplicated decisions, leaky lifecycle rules, difficult testing, tightly coupled changes, or surprising failure behavior.

List what callers currently need to know: types, ordering, ownership, errors, configuration, and important performance promises. Ask what would happen if the module disappeared. Would complexity disappear with it, or merely move into every caller?

## Compare proportionate alternatives

Consider deletion, consolidation, a clearer concrete API, or an adapter at a real variation boundary before adding generic machinery. One implementation does not automatically forbid an interface; a faithful test adapter or likely independent consumer can justify a seam. Conversely, an imagined future consumer does not automatically justify one.

Put invariants with the state that owns them. Keep volatile integration details behind an appropriate boundary while preserving required control, observability, recovery, and portability. Avoid hiding blocking behavior, ownership transfers, or durability tradeoffs behind a superficially small API.

For a material open interface choice, compare genuinely different options and explain the tradeoff. For an obvious local cleanup, act within the authorized scope rather than inventing alternatives or a formal design approval.

## Ground the proposal in evidence

Identify the affected callers, preserved behavior, useful test seam, and any migration needed. Distinguish current pain from a speculative benefit. Demonstrate performance claims with representative measurements; interface elegance alone is not a benchmark.

Return a concise recommendation and the decisions that remain. Write a design note only when requested or when a consequential tradeoff needs durable context in the existing project format. Do not implement, change public compatibility, or broaden scope merely because this skill was invoked.
