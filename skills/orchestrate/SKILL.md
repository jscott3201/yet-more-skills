---
name: orchestrate
description: Deliver one repository or PR-sized code change through grounding, bounded implementation, immutable review, exact-head gates, merge authorization, and handoff. Use for end-to-end delivery; not for explanation-only work or a user-requested direct local edit.
license: MIT OR Apache-2.0
metadata:
  category: delivery
  phase: orchestration
---

# Orchestrate

The primary session coordinates one bounded PR lifecycle at a time. Keep a compact ledger of repository, Codebase Memory project/root and coverage, exact base/head SHAs, phase, dispatched agents, owner decisions, milestone hard stops, gate state, PR state, review cycle, authorization, and next action. Use configured agent models rather than prescribing them here. Treat revisions as integrity anchors at phase transitions, not a polling loop. Do not edit product code during an orchestrated delivery. Personal configuration or skill maintenance uses direct local edits unless repository delivery was requested.

This is the serial route. When the user explicitly invokes `parallel-portfolio` and repository instructions permit it, use that skill as the delivery coordinator instead; do not run both coordinators or admit a portfolio merely to speed up ordinary work.

## Workflow

1. Resolve Codebase Memory project/index state once for the canonical absolute repository root. Call `index_repository` only when the repository is absent or a real state change requires it. Record the project identity and known coverage gaps for every dispatched packet.
2. Load `repository-grounding` and establish the exact revision, instructions, prerequisites, worktree state, source ownership, and real gates. Ground locally when this is the immediate dependency; use `research_grounding` when it can work independently alongside useful root work. Reuse the resulting `GROUNDING_RECORD`; refresh only changed fields. Use native Git/GitHub/file tools for exact state.
3. Spawn only the independent read-only research agents the decision needs, concurrently when useful:
   - `research_evidence` for external APIs, specifications, versions, and primary-source feasibility;
   - `research_ecosystem` for integrations, portability, operations, alternatives, and downstream consequences;
   - `research_architecture` for ownership, invariants, lifecycle, sequencing, coupling, and scope; ask it to load `module-design` for interface/seam/refactor analysis and `domain-language` only when naming or domain meaning is part of the question;
4. Load `owner-decision-gate` when a material PR, milestone, contract, infrastructure, acceptance, or authority choice remains unresolved. Proceed on routine reversible details with reasonable assumptions. Ask through the mechanism permitted by the active harness and pause only dependent work. Record actual answers and validity conditions. Defer merge approval until the reviewed result is ready; lack of merge approval does not block authorized implementation and review.
5. Load `bounded-pr-slice`, synthesize one coherent brief, and spawn exactly one `implementer`. Do not launch concurrent writers or edit around a failed implementer. Resume the same agent once when possible; otherwise independently verify the complete worktree and gates or return `REPLAN_REQUIRED`.
6. Inspect scope and validation, preserve unrelated work, then own the authorized Git/GitHub delivery actions: one cohesive commit, non-force push, and one PR against the proven base. Verify each mutation from live state.
7. Load `pr-gate-loop`, which owns review-cycle procedure. Spawn `review_holistic` and `review_dataflow` concurrently with the same complete immutable `REVIEW_TARGET`; run required CI in parallel and reuse results across roles. Follow that skill's bounded repair and re-review rules.
8. Follow `pr-gate-loop` through pending checks, any allowed repair, and its final live-state and merge-authorization transition. Keep completed source reviews when only check status changes on the same target; never treat a reviewer PASS as the overall gate result.
9. Load `handoff-continuity` and close the cycle at `MERGED`, `READY_TO_MERGE`, or `REPLAN_REQUIRED`. If the user has already authorized continued execution, a new coherent slice may begin in the same root session only after the handoff, fresh grounding, resolution of any milestone hard stop, and a user-visible transition update; never overlap implementation cycles.

Keep agent prompts bounded to the exact question, revision, paths/symbols, exclusions, relevant owner decisions, and requested result. Use self-contained forks and reuse agents for related follow-up under the global delegation contract. Require compact evidence packets rather than raw tool output. Mark unresolved facts `UNKNOWN`; replan only when a decision-critical prerequisite, scope boundary, or required validation cannot be proven.
