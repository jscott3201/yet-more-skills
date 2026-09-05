---
name: rust-workflow
description: "Orient a substantial Rust task: map the workspace, choose validation and specialist skills, and coordinate agent work. Explicit entry point; not required for tiny edits."
license: MIT OR Apache-2.0
---

# Rust Workflow

Use this as an entry point, not a mandatory ceremony. For a small correction, inspect the relevant code and act. For substantial work, establish the boundary of the change before choosing specialists.

## Establish context

Read applicable `AGENTS.md`, task instructions, the nearest `Cargo.toml`, workspace manifest, toolchain pin, testing scripts, and relevant nextest configuration. Distinguish workspace members, default members, excluded crates, feature sets, generated code, and native/FFI boundaries. Consult repo-local compatibility policy: a greenfield engine and a published protocol library need different API decisions.

Use the installed language server or repository code graph for callers and dependency direction when available; verify its coverage and confirm decisive claims in source. Do not require a memory service, a particular MCP, or a machine-specific path. With no graph tool, use targeted search and Cargo metadata.

Start with cheap inspection. `cargo metadata --no-deps --format-version 1` identifies workspace packages; use `--locked` where a lockfile is authoritative. Metadata without dependencies is not a transitive dependency analysis. Cargo commands can resolve dependencies or invoke build scripts later: respect network and execution permissions.

## Choose the smallest useful workflow

Translate the task into an observable outcome and the few invariants it could disturb. For example: reduce response copies while preserving transaction identity, errors, and retained-memory bounds. State a short plan only when it resolves real coordination or design uncertainty.

Use the specialist matching the difficult part; usually one or two are enough:

| Work | Specialist |
|---|---|
| Public interfaces and ownership | `$rust-api-design` |
| Selecting/running tests | `$rust-nextest` |
| Missing or weak behavioral evidence | `$rust-test-design` |
| Measured runtime improvement | `$rust-performance`, then memory or SIMD as relevant |
| Cancellation, contention, task ownership | `$rust-async-concurrency` |
| Wire/state-machine semantics | `$rust-protocol-codecs` |
| WAL, recovery, indexes | `$rust-storage-durability` |
| Binding or unsafe boundary | `$rust-python-bindings` or `$rust-unsafe-ffi` |
| Features, dependencies, slow builds | Workspace or build-diagnostics skill |

Skills are independent; an uninstalled specialist is not a blocker. Load only the references relevant to the current question.

## Execute and verify

Follow the existing implementer/reviewer split. Delegate independent source questions only when they save useful root work. Give readers one question, paths, constraints, and expected evidence. Do not create extra approval panels, nested delegation, or multiple product writers merely because more agents are available.

Coordinate expensive Cargo builds, shared fixtures, ports, and benchmark hosts. A separate worktree does not isolate machine load or external services. Keep performance runs free of competing work. A skill never grants permission to commit, push, merge, publish, access hardware, or change CI.

Implement the smallest coherent change, including its regression test. Run the relevant package/consumer checks, then the repo's required gate. Preserve `no_std`, `no_alloc`, unsafe-code policy, deterministic behavior, and wire/persistence contracts. Do not silently upgrade the compiler, dependency graph, or MSRV to make a patch easier.

## Finish

Return the outcome, important design tradeoff, actual commands/results, and unverified areas. A skipped command is unrun, not passing. Distinguish a source-based hypothesis, a compiled result, a test result, and a measured performance result. Keep handoffs short and integrate with existing review/stopping rules.

Read [repository adaptation](references/repository-adaptation.md) when entering one of the reviewed workspaces.
