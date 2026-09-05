---
name: diagnosis-loop
description: Diagnose hard bugs and performance regressions with a symptom-specific feedback loop, minimized reproduction, falsifiable hypotheses, and bounded evidence. Use for diagnosis or debugging requests; stop before fixing unless the user also requested a fix.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex and OpenCode 1.x"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Diagnosis Loop

Produce an evidence-backed cause analysis. A diagnosis-only request authorizes inspection and reversible runtime checks, not tracked edits, a fix, a commit, or an external mutation.

## Establish the target

- Read applicable instructions and reuse the current grounding record when one exists.
- State the exact symptom, expected behavior, affected environment or revision, and the observable signal that distinguishes failure from success.
- Use Codebase Memory first for structural paths and callers. Read exact source and check index coverage before an exhaustive or negative claim.
- Protect credentials, session data, captures, and logs. Retain only the smallest redacted excerpt that carries the signal.

## Build the feedback loop

Prefer the narrowest existing command that exercises the real symptom: a focused test, CLI invocation, request replay, browser scenario, benchmark, or trace query. Run it at least once and record its exact verdict.

A useful loop is:

- **symptom-specific**: it can fail for the reported problem rather than any nearby error;
- **repeatable**: deterministic, or measured over enough trials to expose a known flake rate;
- **bounded**: fast enough to rerun after each probe;
- **safe**: it does not touch production, credentials, or durable external state without separate authority.

If the environment cannot reproduce the issue, continue with bounded static evidence. Label conclusions `INFERENCE` or `UNKNOWN`, explain what observation is missing, and name one concrete way to obtain it. Do not invent a reproduction.

## Minimize and hypothesize

1. Remove one input, caller, configuration value, or step at a time while preserving the symptom. Keep only load-bearing elements.
2. Write two to five ranked, mutually distinguishable hypotheses. For each, state a prediction that would falsify it.
3. Test the cheapest high-information prediction first. Change one variable per probe.
4. Prefer debugger, profiler, query plan, or existing structured telemetry over broad logging. Temporary instrumentation that changes tracked files belongs to an authorized implementation lane; otherwise propose it and stop.
5. Update the ranking after every observation and explicitly retire disproved hypotheses.

For performance regressions, establish a comparable baseline and distribution before changing anything. Separate latency, throughput, allocation, I/O, and contention evidence rather than treating “slow” as one cause.

## Stop at the requested boundary

- For **diagnose/explain** requests, stop once the root cause is proven or the remaining gap is `UNKNOWN`.
- For **fix** requests, hand the diagnosis packet and proposed regression seam into the authorized implementation workflow. The sole writer owns code and test changes.
- Clean up task-owned runtime state and verify that diagnostic commands did not alter tracked files.

Return a compact packet:

```text
DIAGNOSIS_RESULT
symptom and target:
feedback loop and observed verdict:
minimal reproduction:
confirmed cause: FACT | INFERENCE | UNKNOWN
evidence:
disproved alternatives:
proposed regression seam:
fix boundary and required authority:
remaining unknowns:
END_DIAGNOSIS_RESULT
```
