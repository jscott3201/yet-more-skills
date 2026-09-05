---
name: handoff-continuity
description: Preserve exact repository and delivery state in a compact standalone handoff without replaying the completed session transcript.
license: MIT OR Apache-2.0
metadata:
  category: delivery
  phase: continuity
---

# Handoff Continuity

Finalize one handoff when the current PR reaches `MERGED`, `READY_TO_MERGE`, or `REPLAN_REQUIRED`. Do not draft a speculative next slice while an immutable head is under review.

Verify the final repository, PR, check, and merge state at exact SHAs. Reconcile stale paths or symbols against live source and reuse the grounding, evidence, and review records rather than reproducing them.

## Required standalone content

- purpose and expected next outcome;
- exact repository, branch, PR, merge, base/head SHA, and worktree state;
- prerequisite and dependency state;
- applicable instructions, source ownership, the resolved Codebase Memory project/root and coverage gaps, and links to durable grounding/evidence records;
- resolved owner decisions, milestone hard stops, and contracts that still constrain the next slice;
- remaining scope, explicit exclusions, likely paths/symbols, and first verification commands;
- gate commands with compact pass/fail results, not logs;
- material deferred findings, risks, unknowns, and replan triggers;
- required authorization or merge state.

Do not replay the transcript or embed raw tool output, full diffs, full review packets, discarded alternatives, or already-resolved discussion. The handoff must be sufficient to resume safely without inheriting the prior context window. End the current implementation cycle after the handoff. The same root session may begin a next explicitly authorized slice only after a user-visible transition, fresh grounding, and confirmation that no declared milestone hard stop applies; otherwise stop and preserve the handoff for a later session.
