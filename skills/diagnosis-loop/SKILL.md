---
name: diagnosis-loop
description: Diagnose a difficult bug or performance regression through a symptom-specific reproduction and falsifiable hypotheses. Fix only when requested; not an automatic architecture rewrite.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Diagnosis Loop

Explain the cause using evidence. A diagnosis-only task authorizes inspection and safe checks, not an unrequested tracked code change or remote mutation. A request to fix the problem can include implementation after diagnosis without requiring a separate agent.

## Build a useful feedback loop

State the expected behavior, actual symptom, affected environment, and observable failure signal. Inspect the relevant source and callers. Use an available index or memory service when helpful, with a focused file-search fallback.

Choose the narrowest existing test, request replay, browser scenario, CLI invocation, benchmark, or trace that exercises the symptom. Run it when safe and available. Preserve the first failure signal and protect credentials, personal data, device captures, and logs. Do not reproduce an issue against production or physical equipment without the necessary authority.

A useful loop distinguishes this bug from an unrelated setup failure. Minimize the input or sequence while preserving the symptom. If reproduction is unavailable, continue with bounded static reasoning and label the missing runtime evidence.

## Test competing explanations

Keep as many hypotheses as the uncertainty needs; do not manufacture alternatives for an obvious proven defect. For each plausible cause, identify an observation that would falsify it. Try the cheapest high-information probe, change one variable at a time, and retire explanations contradicted by the evidence.

Prefer existing telemetry, debuggers, profilers, and focused checks over broad logging. Add temporary tracked instrumentation only when edits are in scope, and remove task-owned instrumentation before closing. For a performance regression, compare equivalent workloads and environments and separate CPU, I/O, contention, allocation, and tail latency.

## Stop at the right boundary

For diagnosis, return the cause or bounded uncertainty, reproduction, supporting evidence, and a proposed regression seam. For an authorized fix, correct the root cause and verify the relevant failure path rather than patching only one symptom.

Do not promote an untested theory to fact, erase a flaky result with retries, or turn a local defect into a modernization program. Clean up task-owned runtime state and report remaining gaps plainly.
