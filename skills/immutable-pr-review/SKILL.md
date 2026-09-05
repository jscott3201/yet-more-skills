---
name: immutable-pr-review
description: Apply the shared read-only review protocol to one pull request at exact base/head SHAs and return a compact evidence-backed packet.
license: MIT OR Apache-2.0
metadata:
  category: review
  phase: verification
---

# Immutable PR Review

This skill owns the protocol shared by every review role. A role adds only its review lens; it must not redefine targeting, evidence, severity, permissions, or output rules.

## Target contract

Review only a complete target supplied in this form:

```text
REVIEW_TARGET
owner/repo:
pull request:
base SHA:
head SHA:
cycle: 1 | 2
prior finding IDs: N/A | IDs with expected repair state
required exact-head checks: names, head association, and GREEN | PENDING | FAILED | UNAVAILABLE status
grounding and evidence references:
Codebase Memory project/root and coverage:
scope and exclusions:
END_REVIEW_TARGET
```

Return `INCOMPLETE_TARGET` if a required identity, revision, cycle, or check field is absent. Return `HEAD_MOVED` if live state no longer matches either supplied SHA. Do not infer or silently retarget missing fields.

## Protocol

1. Verify owner/repo, PR number, base SHA, head SHA, cycle number, and exact-head checks.
2. Return `HEAD_MOVED` when the current target differs; never silently review a newer head.
3. Inspect the full diff plus the surrounding source, ownership boundary, and relevant tests. Consume the supplied Codebase Memory project identity without project discovery, status polling, or index management. Use focused graph tools for cross-file flows, diff impact, and blast radius before broad native search, and check index coverage before exhaustive claims. Patch fragments alone are insufficient.
4. Use exact-revision remote evidence. Local inspection or focused validation is valid only when local `HEAD` equals the target and the tracked worktree is clean before and after.
5. Record each required check as GREEN, PENDING, FAILED, or UNAVAILABLE and confirm its head association. Pending checks do not prevent source review. Treat supplied results as shared evidence; do not rerun the same broad suite. Use focused diagnostics only for a concrete finding, conflicting evidence, or an authorized substitute for unavailable CI. Report substitute validation separately; it does not waive a required check.
6. Remain independent and source-read-only: do not fetch, checkout, edit, stage, commit, push, rewrite refs, post, delegate, approve, request changes, or merge.
7. Report a blocker/major only with a stable ID, exact location, concrete failure, direct evidence, introduced-versus-pre-existing classification, shipping impact, smallest correction, and regression test.
8. Treat unsupported concerns, preferences, optional hardening, and unrelated pre-existing defects as non-blocking. A missing test blocks only when tied to a demonstrated unprotected contract failure.
9. Report each root cause once and defer minor/nit findings. Do not include raw logs, full diffs, or source dumps.
10. In the final review cycle, recheck prior IDs and repair-caused regressions without broadening scope.

Return the compact block directly; use `none` rather than omitting an empty field. Each blocker/major entry must carry its stable ID, severity, exact location, failure scenario and impact, evidence and introduced-by-PR proof, smallest correction, and regression test.

```text
REVIEW_RESULT
lens: holistic | dataflow
cycle: 1 | 2
reviewed base SHA:
reviewed head SHA:
signal: PASS | FIX | REPLAN_REQUIRED | HEAD_MOVED | INCOMPLETE_TARGET | WORKTREE_MUTATED
blocker/major findings: none | stable-ID entries
minor/nit deferred: none | compact entries
prior finding recheck: N/A | per-ID status
exact-head checks:
evidence and local validation:
confidence and remaining unknowns:
END_REVIEW_RESULT
```

Reviewer `PASS` means no blocker/major survives the review evidence threshold. It does not mean required checks are green or authorize merge; only `pr-gate-loop` can declare the overall gate passed. Preserve each check's actual status even in a clean review packet. Return `FIX` for a repairable blocker/major in cycle one, `REPLAN_REQUIRED` when the bounded review cannot converge, `HEAD_MOVED` for a changed target, or `WORKTREE_MUTATED` when local validation altered tracked state. The orchestrator deduplicates packets and owns any authorized remote posting.
