# Diagnostic recipes

Before Cargo work, inspect `rust-toolchain.toml`, `.cargo/config.toml`, and the local gate. Then use applicable commands rather than running a whole checklist:

```bash
rustc --version
cargo --version
cargo metadata --no-deps --format-version 1 --locked
```

For a chosen package, compare a focused check with the actual link/test stage required by the failure. Use `cargo build -p PACKAGE --locked --timings` for build timing after replacing `PACKAGE` with a discovered name. Do not put placeholder commands into a claimed executed-command report.

`RUSTFLAGS`, Cargo profile overrides, and target directories affect artifact reuse. Before adding profiling or sanitizer flags, plan a separate build path and avoid overwriting existing flags accidentally. Do not use `RUSTFLAGS="..."` in a wrapper without considering previously required flags and configuration.

A successful `cargo check` followed by an FFI linker failure calls for native-library/ABI investigation; repeatedly cleaning Rust artifacts rarely resolves the missing dependency. A successful compile followed by zero discovered tests calls for selection/configuration investigation.

Cargo's stable HTML timing report is different from unstable machine-readable timing options. Use only the mode supported by the installed Cargo. [Cargo build](https://doc.rust-lang.org/cargo/commands/cargo-build.html), [Cargo timings](https://doc.rust-lang.org/cargo/reference/timings.html), [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html), [rust-analyzer](https://rust-analyzer.github.io/book/).
