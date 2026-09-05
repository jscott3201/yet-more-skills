---
name: bounded-pr-slice
description: Convert a grounding record into one coherent PR-sized implementation cycle with explicit scope, ownership, evidence, gates, and replan triggers.
license: MIT OR Apache-2.0
metadata:
  category: delivery
  phase: planning
---

# Bounded PR Slice

A valid slice has one objective, one source-of-truth story, a small owned change surface, executable acceptance evidence, and no hidden prerequisite.

Under ordinary serial delivery, one root session owns only one active PR cycle at a time: plan, implementation, delivery, the bounded review gate, and a terminal handoff. After `MERGED`, `READY_TO_MERGE`, or `REPLAN_REQUIRED`, close that cycle. A next explicitly authorized slice may begin in the same session only after a user-visible transition, fresh grounding, and any milestone hard stop or owner decision is resolved.

For an explicitly admitted `parallel-portfolio`, use this brief per lane; the portfolio skill owns concurrency, isolated ownership, integration, and terminal state. This skill alone never authorizes concurrent writers.

Before finalizing the brief, identify assumptions that affect scope, acceptance, authority, or compatibility. Use `owner-decision-gate` for material unresolved choices; use reasonable documented assumptions for routine reversible details. Do not turn review into design negotiation.

## Brief template

1. Objective and user-visible outcome.
2. Grounding-record reference with exact base SHA, prerequisites, and resolved Codebase Memory project/root plus coverage notes.
3. Owner-decision record, milestone boundary, and authorization state.
4. In-scope and explicitly excluded work.
5. Contracts, invariants, source ownership, and likely change surface.
6. Ordered implementation steps and focused acceptance evidence.
7. Failure, hostile-repetition, cleanup/reclaim, and platform cases that apply.
8. Required local/native gates plus any explicitly justified hosted or platform gates.
9. Low-risk assumptions, risks, and concrete `REPLAN` triggers.

Use Codebase Memory's focused graph tools to bound the source-of-truth path, implementation surface, and blast radius before finalizing the brief. Check index coverage before an exhaustive scope claim. Keep exact repository state and executable gates as separate evidence; the graph does not replace them.

For several already-authorized slices, select the first dependency-eligible coherent slice using recorded priorities. Ask only when credible alternatives leave a material scope, sequencing, or acceptance decision unresolved. Split or replan when work needs independent migrations, competing source owners, an unmerged prerequisite, or behavior that cannot be demonstrated in one reviewable PR. Review cycles verify an agreed design; they do not discover or negotiate it.
