# Test quality

Use these checks when selecting or reviewing a test inside a red-green-refactor cycle.

## A durable test

- names a behavior a caller or user cares about;
- exercises the real public seam or repository-approved contract surface;
- fails when that behavior is absent or broken;
- uses an expected result independent of the production algorithm;
- remains valid when internal structure changes without changing behavior;
- controls time, randomness, network, and filesystem state when they affect the verdict.

One test may contain several assertions when they describe one outcome. Split it when failures would represent independent behaviors or require unrelated setup.

## Warning signs

- **Setup failure:** the test never reaches the behavior it claims to exercise.
- **Implementation coupling:** assertions depend on private methods, internal call counts, or incidental query order.
- **Tautology:** the test calculates the expected answer with the same rule as production.
- **Side-channel verification:** the test bypasses the supported interface without a contract-level reason.
- **Snapshot opacity:** a broad snapshot changes often and does not identify the protected behavior.
- **Flaky oracle:** uncontrolled time, concurrency, random data, or external services determine the verdict.

Repository conventions and proven contract tests outrank generic preferences. Replace existing coverage only when the new test demonstrably preserves its protected behaviors.
