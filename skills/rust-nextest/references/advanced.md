# Advanced nextest use

Use these only when they answer the current problem. Verify the installed version and help first; newer nextest documentation is not a promise about an older CI binary.

**Stress:** A bounded `--stress-count` or `--stress-duration` run can investigate a selected concurrency failure. Keep retries off while diagnosing, preserve the original failure, and state the number of executions. A stress pass is not exhaustive interleaving coverage. Use a Loom model when the synchronization question warrants it.

**Record/replay:** Recorded output can support diagnosis without another execution. Replaying a saved run does not validate changed code. Treat logs and recordings as potentially sensitive. Keep them local unless upload is authorized.

**Archives/shards:** An archive reuses compiled artifacts; sharding divides selected tests. Neither performs a new build. Verify compatible native platform, runtime libraries, feature/codegen settings, and fixture access before reusing artifacts. An archive is not permission to cross-compile or emulate. Coordinate external resources across shards explicitly.

**Coverage:** `cargo llvm-cov nextest` is a separate instrumented path, useful to find unexecuted code. Doctest coverage has its own toolchain constraints; unit coverage does not silently include it. Keep measurement builds separate from performance comparison builds.

**Criterion smoke mode:** Current docs require compatible Criterion (0.5 or newer) for nextest test-mode integration. `cargo nextest run --benches` exercises compatible bench targets without producing performance measurements. Do not enable all targets blindly when that includes expensive or hardware-dependent harnesses.

**Benchmark measurement:** As reviewed 2026-09-05, `cargo nextest bench` is experimental, introduced in 0.9.117. It uses an explicit experimental switch and benchmark-specific timeouts. Existing `cargo bench`/Criterion workflows remain the default for this pack.

Sources: [stress tests](https://nexte.st/docs/features/stress-tests/), [archiving](https://nexte.st/docs/ci-features/archiving/), [Criterion integration](https://nexte.st/docs/integrations/criterion/), [benchmark measurement](https://nexte.st/docs/features/benchmarks/), [coverage](https://nexte.st/docs/integrations/test-coverage/), [cargo-llvm-cov](https://github.com/taiki-e/cargo-llvm-cov).
