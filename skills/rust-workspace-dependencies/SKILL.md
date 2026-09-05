---
name: rust-workspace-dependencies
description: "Change or investigate Cargo workspaces, feature graphs, dependencies, MSRV, no_std, and crate boundaries. Use for build graph or compatibility work, not automatic mass updates."
license: MIT OR Apache-2.0
---

# Rust Workspace and Dependencies

Read the manifests and toolchain configuration instead of inferring them from Rust edition or repository age. The goal is a coherent supported build graph, not the largest dependency version bump.

## Inventory actual support

Identify members, default-members, excludes, resolver, inherited dependencies/lints, `rust-version`, build scripts, target-specific dependencies, and optional features. Inspect the lockfile policy and native platforms. A pinned stable compiler, edition, resolver, and advertised MSRV are separate choices.

Use Cargo metadata and `cargo tree` to understand the relevant graph. `cargo tree -e features -i <dependency>` can explain who enables a feature; inspect the actual graph rather than assuming `default-features = false` at one declaration disables defaults everywhere. Separate normal, build, and development dependencies when evaluating footprint or feature leakage.

## Keep boundaries intentional

Preserve foundational `no_std` and `no_alloc` constraints. A host test build can use a std-based harness while hiding production dependency leakage. Check the foundation's normal dependency graph and supported feature configurations separately. A native no-default check is useful evidence, not proof of every embedded target.

Use additive feature design where possible. Avoid mutually incompatible features in a reusable crate unless the product requires that design and validation covers it. `--all-features` can be invalid or hide a missing gate; it does not prove default, minimal, or each-feature behavior.

Maintain dependency direction and public facade intent. Do not make lower-level data types depend on a runtime, binding, query language, or application layer for convenience. Avoid leaking implementation dependencies into a public API unless that is a deliberate supported contract.

## Evaluate a dependency change

Compare an existing solution, a small local implementation, and a maintained dependency. Consider runtime cost, code/build size, maintenance, licensing, unsafe/FFI footprint, security updates, and platform support. Prefer fewer justified dependencies, not hand-rolled cryptography, TLS, async runtimes, or complex serialization to chase a dependency count.

Consult official release notes, advisories, and version-matched APIs for an update. Check MSRV, default feature changes, native library requirements, and transitive impacts. Keep updates scoped to the task. Preserve the repository's rustls/license policy and do not silence audit findings with unexplained ignores.

Update manifests and lockfiles together when required. Use `--locked` for verification after an intentional resolution change; do not use it to pretend a needed lockfile update is impossible. Do not delete the lockfile or use `--ignore-rust-version` as the default fix.

## Validate useful combinations

Start with affected default and minimal configurations, then the changed feature and supported aggregate configurations. Include consumers and excluded binding crates when impacted. Use an existing feature-matrix tool such as cargo-hack for a targeted gap; do not run the full powerset on every small PR. Test the declared MSRV deliberately when compatibility is part of the change, without assuming a newer compiler proves it.

Return the graph change, dependency rationale, supported combinations actually checked, lockfile/compatibility impact, and deferred broader checks. Do not silently raise MSRV or change resolver as cleanup.

Read [feature recipes](references/features.md) when planning validation.
