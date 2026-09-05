---
name: rust-ci-release
description: "Plan or review Rust PR gates, native test matrices, packaging, or release evidence. Explicit workflow; does not authorize CI changes, publishing, tags, or merges."
license: MIT OR Apache-2.0
---

# Rust CI and Release Validation

Read the existing workflow scripts, CI definitions, testing contract, publication policy, and supported platforms. This is a validation skill, not authorization to add CI or release anything. Preserve the user's native-only policy: no QEMU and no cross-compilation locally or in GitHub workflows.

## Separate feedback from qualification

Use a short local edit loop for the affected package and a small regression selection. Keep the existing PR gate fast: formatting, relevant lint/build/test scope, required doctests, and already mandated policy checks. Do not add a full feature powerset, long fuzz campaign, exhaustive concurrency exploration, or timing-sensitive performance gate to every PR.

A narrow PR gate is not full product validation. When a changed crate is outside it, run that crate's meaningful checks and report the additional evidence. Preserve the broader staged-release gate for supported native OS/architectures, features, bindings, packaging, recovery/failure testing, and performance where applicable.

## Maintain reliable test semantics

Preserve `--locked`, documented warning policy, nonempty-test requirements, timeout/leak/flaky handling, and effective nextest profiles. Keep doctest and external-language results separate. Do not use retries or broad ignores to turn an unstable gate green. Do not silently skip missing tools and print a success summary.

Use native hosts for the OS/architecture being qualified. A same-architecture Linux container can validate its Linux environment; it does not establish macOS behavior because the physical host is a Mac. Container image selection must not invoke transparent emulation. When a required native environment is unavailable, report that lane unrun.

Coordinate test resources across jobs and agents; nextest groups do not provide cross-job locks. Avoid duplicating expensive builds or benchmarking on a contended runner. An archive or cache may accelerate a compatible run but does not replace source compilation when the build inputs differ.

## Validate packaging and release inputs

For a packaging task, inspect the actual package contents and dependencies, license/attribution files, generated assets, executable permissions, version alignment, and installation behavior. Test a consumable crate/wheel/binary rather than only the source checkout. Follow the existing publication order for interdependent crates.

Build release artifacts for GitHub consumption using authorized native runners and a documented supported matrix. Keep CPU baseline compatibility explicit; do not ship host-specialized binaries as portable defaults. Check artifact names, expected files, executable startup or library import, and failure visibility. A produced file is not a smoke-tested release.

Preserve credentials and publication boundaries. Do not expose secrets in logs, run untrusted PR code with release credentials, broaden token permissions, change branch protection, or publish/tag/merge without separate authorization. Supply-chain tooling findings require supported remediation or an explained existing policy exception, not arbitrary suppression.

## Return

Give a small matrix of required lanes, actual results, and unrun reasons. Distinguish ready for focused review, PR validation, staged release, and publication. List the remaining qualification gap rather than inventing a new process or promising future background work.

Read [gate adaptation](references/gates.md) when applying this to the reviewed repositories.
