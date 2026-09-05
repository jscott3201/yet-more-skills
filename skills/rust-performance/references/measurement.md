# Measurement recipes

Reuse a checked-in Criterion benchmark target. Replace the example package and target below with discovered names. In an authorized baseline checkout:

```bash
cargo bench -p example-benchmarks --bench codec --locked -- --save-baseline before
```

In the candidate state with the same Criterion results available:

```bash
cargo bench -p example-benchmarks --bench codec --locked -- --baseline before
```

`--baseline` compares without replacing the named baseline; `--save-baseline` writes it. Separate worktrees/target directories need deliberate baseline result availability. Do not silently compare unrelated cached results. Select the named Criterion bench so libtest does not consume unsupported Criterion arguments. Source: [Criterion CLI](https://bheisler.github.io/criterion.rs/book/user_guide/command_line_options.html).

For a mutating benchmark, reset meaningful state per iteration or batch. Inspect `iter`, `iter_batched`, and `iter_batched_ref` timing/drop behavior. If production performs the setup every request, excluding it answers a narrower question. Limit batch size to avoid accidentally benchmarking allocator pressure or exhausting memory. Source: [Criterion Bencher](https://docs.rs/criterion/latest/criterion/struct.Bencher.html).

Use `std::hint::black_box` where constant inputs or discarded outputs would create unrealistic optimization. It is a best-effort optimizer barrier, not a correctness, constant-time, or security guarantee. Source: [black_box](https://doc.rust-lang.org/std/hint/fn.black_box.html).

For profiling, use available native tooling: Linux perf/heap tools, macOS Instruments, or an appropriate sampler such as samply. Symbol information can be enabled in an optimized profile. Frame pointers may improve stacks but alter codegen; do not compare an instrumented A with an uninstrumented B. Source: [profiling](https://nnethercote.github.io/perf-book/profiling.html).

A compact result table is enough: workload/scale, metric, before, after, uncertainty, and caveat. State whether percent change means latency reduction or throughput increase. Report errors and resource costs beside service-level results. Preserve raw output locally so another reader can inspect the interpretation.
