# Feature and compatibility recipes

Use actual discovered package names:

```bash
cargo metadata --no-deps --format-version 1 --locked
cargo tree -e features -i bytes --locked
```

The first is inventory, not a complete feature-resolution report. The second is an example for a dependency named `bytes`; multiple versions may require a package/version selector.

Inspect the actual facade manifest before testing supported minimal and full feature sets. Replace the example package and feature names below with discovered names.

```bash
cargo check -p example-package --no-default-features --locked
cargo check -p example-package --features full --locked
```

Run behavioral tests with the changed features as well. Compilation does not prove runtime behavior. Verify the foundation's normal dependencies and no-allocator contract independently.

When already installed and useful, cargo-hack can exercise individual features with `--each-feature`; `--no-dev-deps` avoids development dependencies masking feature isolation during appropriate checks. A feature powerset grows rapidly and should be restricted to meaningful supported combinations, usually deeper validation. Inspect current options before using them. [cargo-hack](https://github.com/taiki-e/cargo-hack).

Read an explicit workspace resolver independently of the edition and rust-version declarations. Edition alone is not evidence of the effective resolver.

Sources: [Cargo features](https://doc.rust-lang.org/cargo/reference/features.html), [resolver](https://doc.rust-lang.org/cargo/reference/resolver.html), [rust-version](https://doc.rust-lang.org/cargo/reference/rust-version.html), [Cargo tree](https://doc.rust-lang.org/cargo/commands/cargo-tree.html), [dependency declarations](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html).
