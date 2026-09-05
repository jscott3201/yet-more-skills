---
name: immutable-pr-review
description: Review a requested PR, patch, or working-tree diff read-only for concrete failures and contract gaps. Use surrounding source and tests; not a demand for a revision packet or authority to edit.
license: MIT OR Apache-2.0
---

# Evidence-Based PR Review

The directory name remains for existing callers. Review the actual requested change without requiring a special packet, a clean unrelated worktree, a particular agent role, or a revision ledger.

## Establish the scope

Identify the PR, supplied patch, or local changes under review. Read applicable instructions, the relevant diff, surrounding implementations, callers, and tests. Inspect missing context with available read tools. An optional code index can help trace dependencies, but source remains the basis for consequential findings.

For a working-tree review, include the requested uncommitted changes and preserve unrelated work. If unrelated edits make attribution ambiguous, state that limitation rather than resetting them. For a patch-only review without surrounding code, narrow the conclusions accordingly.

Remain read-only by default. Focused execution is appropriate when authorized, safe, and unlikely to alter user data; otherwise reason from source and explain what remains untested. Do not edit, post, approve, commit, push, or merge without separate scope.

## Follow the failure path

Look for reachable incorrect behavior: ownership/lifetime errors, cancellation and cleanup gaps, lost or duplicated data, invalid contracts, security boundaries, silent error suppression, and missing consumer coverage. Use the relevant language specialist when needed. Assess performance claims against measurements rather than intuition alone.

A useful finding gives its location, triggering input or state, why the behavior fails, its impact, and the smallest correction or regression test. Direct source reasoning can establish a defect even when reproducing it is unsafe or unavailable; label that evidence honestly. Do not demand a runtime exploit or an observed production failure.

Separate introduced defects from pre-existing issues. Report a root cause once. Keep preferences, speculative hardening, and nits distinct from blockers. A missing test is most meaningful when tied to a specific unprotected behavior.

## Return a bounded result

Lead with actionable findings, then confidence, validation performed, and material limits. A clean review means no supported issue was found in the inspected scope—not certification, passing CI, or merge permission. If the change moves materially during review, state what was inspected and reassess affected work rather than claiming coverage of unseen code.
