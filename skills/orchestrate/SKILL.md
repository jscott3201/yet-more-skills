---
name: orchestrate
description: Coordinate an explicitly requested end-to-end implementation and review workflow. Use available agents only when useful; not for explanation, diagnosis-only requests, or routine direct edits.
license: MIT OR Apache-2.0
---

# Coordinate a Bounded Change

Guide one coherent requested outcome from source inspection through implementation, validation, and a useful handoff. Respect repository policy and the user's authority boundaries. No named agent, memory server, ledger, or remote PR is required by this skill.

## Choose the smallest effective workflow

Confirm the goal and inspect the affected source, instructions, and existing checks. Reuse context already established. For a small task, implement directly when authorized. For substantial work, form a compact outcome and acceptance brief; use specialist skills only for the boundaries actually involved.

Delegate only when independent work or context isolation repays setup, duplicated instructions, review, and integration. A small known-path lookup usually stays local. Give each worker one question or outcome, relevant paths, authority, exclusions, and the expected evidence; do not clone the entire conversation or ask every worker to survey the repository. Use configured roles and models, not hard-coded names or unauthorized cheaper-model switches.

Request conclusions with source pointers, actual checks, and unresolved issues rather than full transcripts. Verify consequential claims without repeating all discovery. Stop redundant exploration when its question is answered; preserve useful partial work. Judge total work across parent and workers, not just the coordinator's visible context. Without subagents, do the same work locally.

Avoid simultaneous writers to the same logical state. For intentional parallel implementation, agree on independent lanes and who integrates shared changes. Do not run competing implementations or contending performance measurements by default.

## Implement and check

Preserve unrelated work. Test observable behavior at the appropriate seam, run focused checks and required gates, and inspect the resulting diff. Distinguish introduced failures from pre-existing or environmental failures; report both honestly. Missing optional tooling does not excuse skipping a required check or claiming it passed.

Use proportionate review. A second lens is useful for independent risks such as lifecycle/data flow or public contracts; it is not an automatic two-agent ceremony. Deduplicate findings, fix demonstrated defects within scope, and recheck the correction. Change the approach when feedback stops producing progress or exposes a material design gap, not because a fixed number of review rounds elapsed.

## Close at the authorized boundary

Commit, push, open a PR, merge, publish, or deploy only when the request and active policy cover that action. Reuse valid authorization; do not re-ask unchanged questions. Never treat a review result as permission to merge.

Report the outcome, changed areas, actual checks, remaining gaps, and next useful action. Continue already-authorized work unless the user set a stop point. Leave a handoff when changing sessions or ownership, not after every minor step.
