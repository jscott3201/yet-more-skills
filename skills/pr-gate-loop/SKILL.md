---
name: pr-gate-loop
description: Use explicitly to coordinate PR findings, focused repairs, and required checks. Preserve existing repository gates; not an automatic extra approval loop or authority to merge.
license: MIT OR Apache-2.0
---

# PR Review and Validation

Repository rules and user instructions define the gate. This skill helps interpret review and test evidence; it is not a new source of approval policy.

## Review and checks answer different questions

Inspect the requested change and enough surrounding behavior to assess it. Review may proceed while CI is pending. A clean source review does not mean required checks passed, and successful tests do not prove the review found every defect.

Use existing review requirements. Add a second independent lens when the risk warrants it or policy requires it, not as an invariant agent count. Share trustworthy test results instead of running the same broad suite for every reviewer. Run a focused diagnostic when a finding needs investigation.

Keep check outcomes distinct: passed, failed, pending, unavailable, and not run. Investigate whether a failure is introduced, pre-existing, or environmental. Do not waive a required check, suppress a flake, accept an empty selection, or silently substitute a narrower suite to finish.

## Repair without a ritual

Combine duplicate findings by root cause and prioritize consequential defects. Explain the failure path and expected behavior. Implement authorized corrections, add a useful regression where appropriate, and rerun affected checks. Recheck previous findings and anything materially affected by the repair. Do not reopen unrelated style questions after a clean focused correction.

There is no universal one-repair limit. Continue while changes are bounded and producing evidence. Stop and explain the blocker when the approach is cycling, scope changes materially, required evidence cannot be obtained, or a decision belongs to the user. Do not create an endless review loop.

Review evidence applies to the code inspected. When the patch materially changes, reassess the affected portions; do not present an earlier review as proof of unseen changes. Use the hosting service's ordinary PR/check association and repository policy rather than adding manual revision tracking.

## Report readiness separately from permission

Summarize actionable findings, required check results, and unresolved risks. Merge only under actual user authorization and applicable repository protections. Without it, leave the reviewed result ready for the next authorized action. Do not post review comments or change branch protections merely because this skill was loaded.
