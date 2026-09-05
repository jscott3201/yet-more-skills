---
name: repository-grounding
description: Establish and reuse an exact repository, revision, prerequisite, instruction, worktree, and validation baseline before repository work.
license: MIT OR Apache-2.0
metadata:
  category: workflow
  phase: preflight
---

# Repository Grounding

Create one grounding record before work that depends on a live repository, pull request, branch, milestone, or handoff. Reuse that record while the target revision, applicable instructions, and prerequisite state remain unchanged. Do not launch a second grounding pass as a planning or review ritual.

## Establish the baseline

- Read the applicable repository instructions and task or milestone handoff.
- Record repository identity, branch, exact base/head SHAs, remote, and worktree state. Preserve unrelated work.
- Resolve prerequisites and overlapping pull requests to live states and the immutable identifiers needed for the decision; prose such as "done" is not evidence.
- Distinguish immutable revision-bound contracts and provenance from mutable workflow status. Read current status from its live authority and never use an older pin as a fallback for eligibility.
- Verify referenced paths, symbols, contracts, tests, validators, and gate commands against live source.
- The root resolves the Codebase Memory project/root and coverage once under the global tool-routing rule. Delegated agents consume that record without project discovery or index management. Use focused read tools for referenced paths, symbols, and minimum dependency edges before broad native search, check coverage before exhaustive claims, and read exact source for flagged or missing coverage. This repository-specific skill does not require inventing a repository for personal configuration or external research.
- Classify conclusions as `FACT`, `INFERENCE`, `UNKNOWN`, or `RECOMMENDATION` and name stop/replan conditions.

Use bounded source inspection and exact-revision remote evidence. Do not paste command output, full diffs, or large source excerpts into the record.

## Reuse and refresh

- Pass the record by reference to planning, implementation, and review roles.
- If only a volatile field changes, verify and amend that field while preserving the rest of the record.
- Rebuild the record only when a revision, prerequisite, instruction, or ownership change invalidates its baseline.
- Recheck revisions at phase transitions or after an observed state change, not on a timer or as a repeated planning ritual.
- If the baseline cannot be proven, return `REPLAN_REQUIRED`; never fabricate it.

## Required record

```text
GROUNDING_RECORD
owner/repo:
root:
Codebase Memory project/root and coverage:
instructions:
default branch:
current branch:
base ref/SHA:
head ref/SHA:
working tree:
prerequisites:
overlapping PRs:
owner decisions and milestone hard stops:
authoritative paths/symbols:
gate commands:
unrelated WIP:
facts:
inferences:
unknowns:
stop conditions:
signal: GROUNDED | REPLAN_REQUIRED
END_GROUNDING_RECORD
```
