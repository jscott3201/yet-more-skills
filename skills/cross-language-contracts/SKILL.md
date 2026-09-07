---
name: cross-language-contracts
description: "Change or verify a contract shared by Rust, Python, and TypeScript consumers using independent fixtures and compatibility cases. Use for cross-language drift and schema evolution, not a single-language internal refactor."
license: MIT OR Apache-2.0
---

# Cross-Language Contract Verification

Identify the producer, transport or binding, authoritative schema, generated artifacts, and actual consumers. Cover the languages and versions that participate in the requested change; do not require all three languages when only two are involved. A matching type declaration is not evidence that the shipped runtime path implements it.

## State the observable contract

Record the few decisions that can diverge: accepted values, rejection behavior, missing versus null, enum evolution, numeric range and precision, bytes, timestamps and timezone meaning, units, ordering, and resource identity. Include error categories and partial or unknown outcomes where callers act on them. Keep language-specific exceptions or representations behind an explicit adapter rather than forcing identical internal types.

For PyO3, verify Python signatures and stubs against the loaded extension, including defaults, conversion failures, and exceptions. Ownership, cancellation, free-threading, and native ABI qualification still need their existing specialists when those contracts change; a serialization fixture cannot establish thread safety.

## Build independent evidence

Reuse a small shared corpus of literal accepted and rejected examples. Preserve raw wire bytes or JSON text for cases where parsing can erase evidence, such as duplicate object names or large numeric tokens. Document the intended result independently of the implementation under test. A serializer reading its own output can reproduce the same mistake on both sides.

Exercise each affected reader against the same cases and each affected producer through a different consumer or an independent expected representation. Compare semantic values where order or formatting is intentionally unspecified; compare exact bytes only when canonical encoding is actually promised. Generated-code compilation, runtime fixture execution, and artifact import tests answer different questions.

## Evolve without accidental drift

Change the owning schema or implementation first, then regenerate through the existing command and inspect the resulting public surface. Keep handwritten adapters out of generated output. Test old-producer/new-consumer and new-producer/old-consumer behavior only where those combinations are supported. Adding an optional field or enum case is not automatically harmless to strict readers or exhaustive consumers.

Preserve unknown fields or reject them according to the contract, not a parser's convenient default. Do not silently translate missing telemetry into zero, arbitrary integers into rounded JavaScript numbers, or a local timestamp into a known instant. Reuse existing version negotiation and migration policy rather than inventing a new protocol.

## Keep validation proportionate

Start with the changed boundary and a representative installed consumer. Expand to native wheel or release matrices when ABI or support promises require it, using the repository's native-only test posture. Run the available language checks and name unrun ones. Do not replace independent expected values with newly generated output simply to make a failing fixture pass.

Read [fixture design and sources](references/fixtures.md) for concrete cases.
