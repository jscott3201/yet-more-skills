# Risk-to-test recipes

**A byte parser:** truncate at every field boundary, vary advertised and actual lengths independently, exercise reserved values, and check that successful streaming output consumes bytes. Verify failure preserves or consumes the buffer according to its explicit contract. Round-trip tests accompany external vectors, not replace them.

**A transaction ring:** force an occupied modular slot, ID wrap/reuse, a stale response with the same slot index, wrong unit/function, duplicate completion, cancellation, and timeout racing completion. Assert the surviving request's identity and resource accounting, not only returned data.

**A clocked serial assembler:** generate byte and deadline events with explicit timestamps. Include before/at/after boundaries, stale deadline tokens, monotonicity errors, truncation, and quarantine recovery. Separate raw RTU frame/CRC checks from timestamped assembler checks: a byte-only harness does not establish timing behavior.

**A numerical kernel:** test scalar tails, threshold neighbors, zero norms, cancellation-prone values, finite extremes, and the chosen exact/tolerance policy. Preserve the documented treatment of signed zero and NaNs; do not widen a tolerance to accept a regression.

**A storage mutation:** compare live state, indexed results, replayed state, and checkpoint-restored state. Inject failure between steps and verify either the old or new committed state, never a silent mixture. Process termination alone does not emulate a power loss.

**Optional tools:** Use already adopted Proptest, cargo-fuzz, Loom, cargo-llvm-cov, or cargo-mutants. Add a tool only for a concrete evidence gap. Coverage answers where execution went; mutation asks whether assertions notice changed behavior. Neither proves specification completeness.

Sources: [Proptest](https://proptest-rs.github.io/proptest/proptest/index.html), [Rust fuzzing book](https://rust-fuzz.github.io/book/cargo-fuzz.html), [Loom](https://docs.rs/loom/latest/loom/), [cargo-llvm-cov](https://github.com/taiki-e/cargo-llvm-cov), [cargo-mutants](https://mutants.rs/).
