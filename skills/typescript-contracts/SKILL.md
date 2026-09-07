---
name: typescript-contracts
description: Design or review strict TypeScript APIs, runtime validation, generated Rust/OpenAPI clients, discriminated states, and serialization boundaries. Not a request to rewrite generated code.
license: MIT OR Apache-2.0
---
# TypeScript Contracts and Rust Boundaries

## Preserve the authority boundary

Find the schema or Rust type that owns the wire contract and the generation command. Change
that source when the contract must change; do not patch generated TypeScript to get a green
build. Keep application adapters separate from generated output. A schema's existence is not
proof that the endpoint, device capability, or execution path is implemented.

## Type and validate deliberately

- Preserve the project's strictness. Use narrowing, useful discriminated unions, and explicit
  public boundaries rather than `any`, non-null assertions, or double casts that hide uncertainty.
  `as`, `satisfies`, and branded types are not runtime input validation.
- Accept untrusted API/config/storage/message input as unknown until the existing validator
  or an appropriate checked boundary accepts it. Validate bounded shape and semantic constraints
  once at the ownership boundary; avoid redundant expensive parsing throughout the UI.
- Separate missing, null, invalid, unavailable, and known-zero values when the domain does.
  Preserve identifier families, units, timestamps, quality, revisions, and producer epochs.
  Do not infer freshness from an identifier's ordering or coerce opaque IDs to numbers.
- Check the wire representation before bridging Rust integers, Python integers, decimals,
  bytes, or non-finite floats into JavaScript. Reject unsupported magnitudes rather than
  silently rounding. A bigint introduced after lossy JSON parsing cannot recover lost digits.
- Keep serialization and display formatting distinct. A localized label is not a persistence
  value. Model an editable draft separately from a validated domain object.

## Prove the boundary

Add accepted and rejected fixtures, exact discriminator cases, absent/null cases, out-of-range
numbers, unknown versions, and bounded malformed inputs. Compile consuming code and exercise
the runtime reader; neither substitutes for the other. Test changed generated artifacts through
the repository's contract pipeline and affected language consumers.

Keep abstractions proportionate: a concrete exported type and one validated adapter often beat
a generic schema framework. Report any missing authoritative source instead of inventing it.

When the change spans language consumers, use independent shared fixtures and the actual producer/consumer combinations, not only generated type agreement. The cross-language-contracts skill covers that seam when available. For an SDK or Node package, also check the distributed exports, declarations, and runtime imports with typescript-package-boundaries; a successful application bundle is not package-consumer evidence.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
