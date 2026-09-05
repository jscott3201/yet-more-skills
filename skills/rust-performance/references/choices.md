# Optimization choices and tradeoffs

**Hoist work:** Cache query-specific invariant state when its lifetime and invalidation rules are clear. Measure whether this reduces meaningful repeated work.

**Use bounded structures intentionally:** A fixed transaction ring is not a drop-in faster map for an unbounded workload. Capacity, admission, collision, exact identity, cleanup, and ID reuse are part of the design.

**Separate kernel and product:** Measure the codec in isolation to locate cost, then verify the request path if the claim is end-to-end latency. A zero-copy decode can still retain a large backing allocation or feed a copying consumer.

**Tune codegen after evidence:** LTO, codegen units, inlining, panic strategy, and target features alter tradeoffs among build time, size, runtime, and deployment compatibility. Preserve existing flags and benchmark the proposed setting as its own change. PGO requires representative training and a separate holdout; training-set wins are not generalization evidence. No default `target-cpu=native` for distributed binaries. [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html), [Rust PGO](https://doc.rust-lang.org/rustc/profile-guided-optimization.html).

**Advanced counters:** Instruction/cache measurements can reduce wall-clock noise and explain changes, but simulated counters are not real latency. A tool such as Gungraun is optional and native-platform-dependent; do not introduce it merely to complete a checklist. [Performance Book benchmarking](https://nnethercote.github.io/perf-book/benchmarking.html).
