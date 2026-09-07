---
name: handoff-continuity
description: Prepare a compact, self-contained handoff when work changes session or owner, including partial implementation or research. Capture useful state and next action; not a transcript or a mandatory PR-close ritual.
license: MIT OR Apache-2.0
---

# Handoff Continuity

Leave enough information to resume without replaying the conversation. A handoff can describe completed work, an incomplete local change, research, or a blocker; it does not require a merged PR or terminal workflow state.

## Preserve what matters

Explain the goal, what changed or was learned, and what remains. Name the relevant repository, working location, branch or PR when applicable, important source paths, and unrelated work to preserve. Use ordinary references; do not create revision ledgers.

Record actual checks and their outcomes, including failed, unavailable, or unrun evidence. Separate implementation from validation and validation from release readiness. A generated file, a green narrow test, or a remembered approval is not proof of everything downstream.

Carry forward only decisions that still constrain the task: public contracts, ownership, native-platform policy, user stop points, exclusions, and permission boundaries. Include a concrete next action and the minimum verification needed before taking it. Make a stale or unresolved prerequisite visible.

## Avoid stale authority

Confirm consequential current status when the next action depends on it. Do not turn an old handoff into proof that a PR merged, a release shipped, or an external operation succeeded. The next worker should inspect the relevant live authority rather than repeat a whole grounding ritual.

Memory or an index can supply context when available; it is not a prerequisite. Persistent memory writes require the active workflow's authority and should retain source pointers, not unsupported conclusions. Do not copy secrets, raw logs, customer captures, or full tool transcripts into a handoff.

## Use the smallest useful form

A short Markdown note with outcome, changed areas, evidence, open issues, and next action is usually enough. Lead with the next action and the few facts needed to take it; put deeper evidence behind usable file, symbol, section, or tool-resource references. Retain disproved hypotheses only when they prevent likely repeated work. Do not repeat full plans or source bodies already reachable from those pointers.

Verify that the recipient can actually retrieve a referenced artifact; an ephemeral path in one worker's sandbox may be inaccessible to another. Carry a minimal necessary excerpt when the source cannot travel, without exporting private material outside its permitted scope. Reuse an existing handoff rather than creating competing status documents. Write to a project or program repository only when that destination is part of the request.

Do not invent missing results, impose a stop after every small edit, or promise work that will happen outside the current execution. State exactly where the next person or agent should pick up.
