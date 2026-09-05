---
name: pr-gate-loop
description: "Run the authoritative PR gate: one immutable review cycle, one optional batched repair, and one final cycle before mandatory re-planning."
license: MIT OR Apache-2.0
metadata:
  category: review
  phase: gate
---

# PR Gate Loop

This skill is the sole authority for review-cycle state and limits. Use `immutable-pr-review` for the shared reviewer protocol. Keep separate counters for each lane PR and integration PR in an admitted portfolio; portfolio integration forbids code/glue repair and replans instead.

## State machine

1. `TARGETED` — the orchestrator records the PR, exact base/head SHAs, required checks, and grounding-record reference.
2. `CYCLE_1` — `review_holistic` and `review_dataflow` independently inspect that same immutable head.
3. `PASS` — both packets are blocker/major-clean and required exact-head checks are green. Stop reviewing.
4. `AWAITING_REQUIRED_CHECKS` — source review is clean but required checks remain pending or temporarily unavailable. Keep the completed review packets for this unchanged target. Use bounded status waits; investigate environmental failures and retry only within existing authority. Do not restart source review, spend the repair batch, declare PASS, or waive a required check merely to finish.
5. `REPAIR` — for confirmed repairable blocker/major findings or a required-check failure proven introduced by this PR, deduplicate root causes and send one batched repair brief to the same original writer (`implementer` for serial delivery or `lane_implementer` for an admitted portfolio lane). Include check/reproduction evidence when a failure was found by validation rather than a reviewer. A pending check, infrastructure failure, incomplete target, or moved head is not itself a product-code repair request; resolve it or report the specific blocker.
6. `RETARGETED` — the orchestrator verifies the repair, records the new head, and reruns required checks. A moved head is always retargeted explicitly.
7. `CYCLE_2_FINAL` — the same review roles recheck prior finding IDs and repair-caused regressions on the new immutable head. Pending checks still use `AWAITING_REQUIRED_CHECKS` without resetting the cycle counter.
8. `PASS` or `REPLAN_REQUIRED` — pass only when both packets and required checks are clean. After the one repair, a confirmed blocking code defect or an unresolvable required-validation blocker requires re-planning. Never launch cycle three.

Reviewer PASS is review-clean status, not overall gate status. Record check names, reviewed-head association, and GREEN | PENDING | FAILED | UNAVAILABLE explicitly. Confirmed failures already present at the base remain pre-existing evidence; they do not silently broaden the repair scope or waive required gates.

When posting is authorized under the active harness's rules, the orchestrator posts at most one deduplicated comment per cycle. Otherwise keep the summary local. Minor/nit findings are deferred and do not trigger repair.

Required CI and both review lenses may run concurrently against the frozen head. The exact-head check result is shared evidence: each role may confirm its head association, but should not rerun the same broad suite. Run focused diagnostics only to investigate a finding, resolve conflicting evidence, or replace unavailable CI.

## Merge authorization

After `PASS`, the orchestrator uses one consolidated live read to verify the reviewed head, checks, repository policy, and clean delivery state. Request merge authorization only when no valid approval already covers that exact reviewed head. It does not repeat already-successful authoritative validation without a concrete reason. Without per-PR or active session authorization, stop at `READY_TO_MERGE` with a concrete reviewed result.

Standing authorization is root-session-only, applies only to exact reviewed heads that pass every gate, may be revoked at any time, and never enables auto-merge. Record it in the orchestrator ledger.
