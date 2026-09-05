# Boundary review examples

## Safe integer is a wire decision

JavaScript numbers cannot represent every Rust `u64` or Python integer. Before accepting an
integer field, read its wire contract. A contract bounded to the ECMAScript safe-integer range
can use a checked number. A wider integer needs an agreed lossless representation at the
producer boundary, not a cast in the browser. Do not silently change an existing API to string
or bigint. JSON serialization of bigint also requires an explicit strategy.

For a timestamp, verify its unit and range before arithmetic. Distinguish source time from
receive time; use a monotonic clock for local durations when appropriate. Do not interpret a
timezone-free label as an absolute instant. Display rounded values without overwriting the
original value used by validation or submission.

## Optional fields

With `exactOptionalPropertyTypes`, omission and explicitly assigning `undefined` need not be
interchangeable. More importantly, HTTP PATCH or domain commands may distinguish omitted,
null, and supplied values even when a local type permits all of them. Write tests against
serialized output, not just the TypeScript object before serialization.

A closed versioned document may reject unknown fields while a separately defined read model
allows extension fields. Follow the actual contract rather than imposing one permissive or
strict decoder everywhere. UI error text must not expose the original sensitive payload.

## Generated clients

Find the authoritative schema, generated client package, and documented generation and drift-check commands. Run the repository-owned workflow rather than editing generated output by hand. Nominal identifiers, resource states, source observations, and commands have distinct contracts; a generic adapter must not erase their relationships.

## Compile-time tests versus runtime tests

Compile-time negative tests should exercise the compiler deliberately and ensure the expected
error still exists. Runtime tests should parse realistic payloads, prove rejection is atomic,
and assert the actual typed error. An arbitrary thrown exception is not necessarily the
intended validation result. Property tests are useful for serialization invariants, but a
round trip through two implementations sharing the same mistake is not an independent oracle.

## Sources

Use documentation matching the installed version.

- [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [Type assertions and ordinary types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [Safe integers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger)
