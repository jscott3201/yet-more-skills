# High-value cases

For Modbus, use a loopback server that records which requests crossed the transport before cancellation. Check register widths and unit IDs at the Python boundary; ordinary Python integers can exceed the Rust target type. Cross-check exception attributes and the documented effect of shutdown versus abort. Avoid touching real control equipment for tests.

For Haystack, test bool before numeric coercion, null/Marker/NA/Remove, unit-bearing numbers, references, and HDateTime rules. Check that the converter distinguishes bool and enforces named-zone requirements where the contract calls for them. Check large integer and sub-microsecond conversion policy; do not assume losslessness merely because a round trip succeeds for ordinary values.

For graph/storage wrappers, test owner lifetime, close during a query, read-only versus mutating calls, errors after recovery, and snapshot/view invalidation. Apply these tests only when such a binding boundary exists.

Property examples: parsing an arbitrary truncated frame must not hang; cancellation never returns a resource permit twice; a rejected batch leaves state unchanged when atomicity is promised; offset and unit conversion preserve the declared meaning, not just a printable number.

Primary references: [Hypothesis strategies](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html), [stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html), [unittest.mock](https://docs.python.org/3.14/library/unittest.mock.html), [pytest parametrization](https://docs.pytest.org/en/stable/how-to/parametrize.html).
