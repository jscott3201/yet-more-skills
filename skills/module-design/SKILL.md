---
name: module-design
description: Analyze or design module interfaces, seams, invariants, and dependency adapters for high leverage and locality. Use for architecture design, refactor planning, and testability questions; not as permission to implement.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex and OpenCode 1.x"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Module Design

Design for leverage at the interface and locality in the implementation. Use the repository's own terminology in user-facing output; the vocabulary below is an analytical aid, not a renaming mandate.

- **Module:** a unit with an interface and hidden implementation, at any scale.
- **Interface:** everything a caller must know—types, invariants, ordering, errors, configuration, and relevant performance behavior.
- **Seam:** a location where behavior can vary without changing the caller.
- **Adapter:** a concrete implementation at a seam.
- **Depth:** useful behavior available per unit of interface complexity.
- **Leverage:** how much capability callers gain from one learned interface.
- **Locality:** how well related knowledge, change, failure, and verification stay together.

## Ground the current shape

1. Read repository instructions, architecture records, and domain vocabulary.
2. Use Codebase Memory to locate authoritative symbols, callers/callees, ownership boundaries, and recent-change impact. Check coverage before claiming a complete call surface.
3. Read exact implementations and tests around the candidate. Record current interface obligations and which callers depend on each one.
4. Apply the deletion test: if the module vanished, would complexity disappear or merely scatter into callers? Treat the result as evidence, not a verdict by itself.

## Evaluate a design

Prefer designs that:

- reduce what callers must coordinate without hiding required control;
- place invariants and failure handling with the state or behavior that owns them;
- expose stable behavior while keeping volatile policy and integration detail local;
- create a testable contract at a real variation or ownership seam;
- preserve portability, observability, recovery, and migration needs.

Do not add an abstraction solely because one implementation exists today. Conversely, production plus a faithful local/test adapter may be a real variation. Judge the evidence and expected change, not a fixed adapter count.

Read [deepening.md](references/deepening.md) for dependency categories and safe consolidation. When a public interface is still open, read [alternatives.md](references/alternatives.md) and compare at least two genuinely different shapes before recommending one.

## Return a design record

Separate fact from recommendation. Include current pain, authoritative paths/symbols, callers and contracts, proposed interface including invariants/errors, hidden implementation, dependency strategy, migration shape, test seam, alternatives, tradeoffs, and unresolved owner decisions.

Material public-contract, persistence, compatibility, or migration choices go through the owner-decision gate before implementation. This skill does not edit code or architecture documents unless that change is separately in scope.
