# Gate adaptation

Preserve explicit retry, flake, leak, timeout, and JUnit policies in the repository test configuration. The local gate and test contract define the required breadth; a generic starter workflow must not weaken them.

Separate everyday PR validation from broader release qualification, including any separately packaged bindings. Read actual workflows and manifests before changing policy.

Follow repository authority for CI changes. Technical skill guidance can improve local tests and evidence without creating a new workflow.

Use Cargo packaging inspection for the actual crate and installed-wheel/binary smoke tests for bindings/tools. `cargo package --list` is inspection, not a full package build; `--no-verify` deliberately omits a verification step and must not be reported as equivalent evidence. [Cargo package](https://doc.rust-lang.org/cargo/commands/cargo-package.html).

For supply chain, preserve the existing split between license/source/ban checks and advisory checks. Do not make every repository adopt another tool solely for consistency. Sources: [cargo-deny](https://embarkstudios.github.io/cargo-deny/), [cargo-audit](https://github.com/rustsec/rustsec/tree/main/cargo-audit).
