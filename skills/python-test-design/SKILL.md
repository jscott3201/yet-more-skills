---
name: python-test-design
description: "Create Python regression, property, stateful, differential, and adversarial tests. Use for missing behavioral evidence and cross-language contracts; use python-pytest for runner mechanics."
license: MIT OR Apache-2.0
---

# Python Behavioral Testing

Write the test that would reject the wrong implementation. Begin with an observable contract, an input domain, and the failure mode—not a coverage percentage. Keep a small regression near the affected API and use the project's existing testing tools.

## Choose an honest oracle

Use hand-derived expectations, independent fixtures, a protocol specification, or a genuinely independent implementation as appropriate. A Python wrapper calling the same Rust routine as the expected-value generator is not an independent oracle. Round trips can preserve the same encoder/decoder bug; supplement them with known wire values and invalid input.

For numerics distinguish exact values, bitwise determinism, units, tolerances, and approximation quality. Never widen tolerances or regenerate goldens just because a refactor fails. Treat graph or protocol domain sentinels separately from None and zero.

## Exercise boundaries and state

Cover empty/singleton/large input, integer range and bool coercion, Unicode and bytes, missing versus explicit null, timestamps and timezone transitions, malformed nested structures, duplicate identifiers, and non-finite values where relevant. Test invalid input before and after valid calls to expose polluted state.

For lifecycle APIs test partial setup failure, close twice, operations after close, cancel before/after admission, timeout racing with completion, and exceptions during cleanup. Coordinate concurrency with events/barriers and bounded joins; sleeps can be a watchdog but should not be the synchronization argument. Assert no extra writes or leaked permits, not only the exception class.

Property-based tests are useful when the domain has broad combinations or state transitions. Reuse Hypothesis if present; define meaningful strategies, retain a minimized failing example, and bound expensive cases. Do not suppress health checks or eliminate adversarial inputs merely to make CI fast. Long randomized campaigns belong in a staged lane, with a small regression in ordinary tests.

## Keep evidence independent of test scaffolding

Patch the symbol where it is looked up and use constrained mocks. Mock clocks/transports at a stable seam, not the code under test. Include real local integration for framing, imports, and runtime transitions that a mock would erase. Native crash/deadlock cases belong in fresh subprocesses with an outer timeout.

Report the behavior each added test protects, the oracle and its limitations, and actual results. Use python-pytest for selection mechanics when installed; the test design stands on its own.

Read [domain cases](references/cases.md) for useful portfolio-shaped tests.
