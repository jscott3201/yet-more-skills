# Practical measurements

Choose cold import/startup, steady-state call latency, sustained ingestion, or shutdown as separate experiments. A loopback protocol test includes scheduling, serialization, and transport overhead; it is not a pure PyO3-call-cost measurement. Separate Python-client/Rust-server from Rust-client/Python-server workloads. Reuse existing direction-specific benchmarks before adding another harness.

Use the same public result checks outside the timed segment for both variants. Include small, typical, and large batches. Name whether conversions and result disposal are timed; moving destruction out of the loop changes the question. A percentile computed from a handful of samples is unstable. The load generator must not suppress requests during a slow response and then claim to represent externally paced traffic.

For an existing pyperf harness, run its normal output option into separate result files, then inspect with `python -m pyperf compare_to baseline.json candidate.json`. Inspect raw samples and benchmark warnings rather than treating the significance label as practical importance. Do not assume fixed iteration counts or cache state across interpreters.

`timeit` disables garbage collection by default; check whether that matches the workload before using its results for allocation-heavy code. Never disable production validation, TLS, or error reporting to manufacture a faster comparison. Preserve supported CPU portability in built extensions; local target-cpu=native results do not justify a portable release claim.

Primary references: [pyperf measurement](https://pyperf.readthedocs.io/en/latest/run_benchmark.html), [pyperf analysis](https://pyperf.readthedocs.io/en/latest/analyze.html), [tracemalloc](https://docs.python.org/3.14/library/tracemalloc.html), [timeit](https://docs.python.org/3.14/library/timeit.html), [cProfile](https://docs.python.org/3.14/library/profile.html).
