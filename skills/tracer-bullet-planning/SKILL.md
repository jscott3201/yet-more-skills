---
name: tracer-bullet-planning
description: Decompose a large plan or specification into serial PR-sized vertical slices with explicit blockers, acceptance evidence, and expand-migrate-contract handling. Use for multi-PR planning; draft before tracker publication.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex and OpenCode 1.x"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Tracer Bullet Planning

Turn a large outcome into a dependency graph of coherent future delivery cycles. Planning is read-only by default: issue creation, labels, roadmap updates, and local planning files require explicit scope and live-state verification.

## Ground before slicing

- Read the source plan/specification, applicable instructions, existing roadmap or tracker state, and repository architecture records.
- Reuse a grounding record when available. Use Codebase Memory to identify source ownership, callers, shared contracts, and blast radius; check coverage before claiming a slice is independent.
- State the destination, current prerequisites, out-of-scope work, and material unknowns. Resolve owner choices before encoding them as ticket assumptions.

## Draft vertical slices

Each slice should:

- deliver one observable behavior or verifiable capability through the relevant layers;
- fit one reviewable PR with one source-of-truth story and one sole writer;
- remain green and useful after it lands, or be an explicitly named compatibility step in a proven migration;
- declare blockers, owned contracts, likely source surface, exclusions, and executable acceptance evidence;
- expose a concrete `REPLAN_REQUIRED` trigger when its prerequisite or ownership claim becomes false.

Prefer a thin end-to-end tracer bullet over horizontal “all schema, then all API, then all UI” batches. Prefactoring is its own slice only when it leaves the repository green and measurably enables later behavior.

Ordinary execution is serial: only one implementation cycle is active. A graph may reveal several unblocked slices, but it does not authorize concurrent writers. Parallel work requires the separately admitted portfolio workflow and disjoint ownership proof.

For wide compatibility changes that cannot land as one vertical slice, read [expand-migrate-contract.md](references/expand-migrate-contract.md).

## Review the plan

Present the draft in dependency order and identify the current frontier. Recommend merges or splits where a slice lacks independent value, exceeds one PR, or hides a shared-authority change. Use the owner-decision gate only for material choices; do not require approval for a clearly dominant reversible decomposition detail.

Publish only when requested. Tracker writes must preserve parent issues and existing state, use native dependency links when available, and verify the resulting live graph. Do not label work implementation-ready until its own fresh grounding and bounded slice qualify it.

Use this per-slice record:

```text
SLICE
title and outcome:
blocked by:
user-visible or verifiable behavior:
contracts and ownership:
likely change surface:
acceptance evidence:
explicit exclusions:
risks and replan triggers:
readiness: PLANNED | NEEDS_DECISION | NEEDS_GROUNDING
END_SLICE
```
