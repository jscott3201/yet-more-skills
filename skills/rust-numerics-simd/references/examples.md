# Numerical examples

For vector scoring, distinguish input precision from accumulator and result precision. Consider query-only cached state, vectorized chunks, independent accumulators, and explicit scalar tails only against a representative workload and accuracy contract.

An oracle that calls the optimized kernel cannot independently validate that kernel. Compare with an appropriately implemented reference and analyze the required result contract. Bitwise equality may be required against an established algorithm even where a different summation order would be numerically reasonable.

Distinguish bit-exact results from narrowly named tolerance exceptions. Preserve exact integer comparisons rather than routing large integers through floating point. Do not generalize a transcendental tolerance to every output.

For retrieval, evaluate changes to candidate generation separately from exact scoring. Report recall/quality at the same dataset, query set, filters, and search parameters; keep final ordering and ties consistent. Query-speed improvements that weaken candidate coverage need explicit product approval.

Sources: [Rust floating-point primitive](https://doc.rust-lang.org/std/primitive.f64.html), [target features](https://doc.rust-lang.org/reference/attributes/codegen.html), [wide](https://docs.rs/wide/latest/wide/), [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html).
