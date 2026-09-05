---
name: rust-protocol-codecs
description: "Implement or review Rust wire codecs and protocol state machines, especially BACnet and Modbus. Use for framing, conformance, identity, bounds, or serial timing behavior."
license: MIT OR Apache-2.0
---

# Rust Protocols and Codecs

Locate the applicable protocol version and authoritative source before making a conformance claim. A repository comment, a peer implementation, or a passing round trip is supporting evidence, not a substitute for the specification. For licensed sources, use the repository's local navigation; do not invent clauses or redistribute source text.

## Define the boundary

Identify whether the change belongs to value encoding, APDU/PDU, network addressing, transport framing, transaction management, or physical serial timing. Preserve layer ownership and existing sans-I/O boundaries. Keep raw link provenance separate from effective routed destination semantics. Do not infer explicit service choices, tags, or addressing intent solely from a payload that happens to look compatible.

Translate the relevant contract into a few conditions: accepted inputs, output representation, reserved values, size limits, failure result, and state effects. Distinguish permissive decoding from canonical encoding only when the specification allows it. Preserve unknown or vendor data where required rather than dropping it as an optimization.

## Implement defensive parsing and encoding

Validate length fields before indexing, slicing, reserving, or multiplying. Distinguish incomplete input from invalid input in streaming parsers. A successful decode must advance or otherwise satisfy the documented progress contract; repeated zero-progress output can become a busy loop. Bound nesting, reassembly memory, pending transactions, and retained bytes.

Use explicit endian conversions and safe borrowed slices/chunks rather than native struct layout, `transmute`, or unchecked reads. Account for unaligned input. Do not add allocator or runtime dependencies to an intentionally `no_std`/`no_alloc` codec.

Validate all fallible fields before committing output where the API promises transactional encoding; otherwise specify and test partial-output behavior. Keep configured capacity distinct from representable wire promises. Quantized or sentinel encodings may not advertise an exact internal limit.

## Preserve state-machine semantics

Match responses using the required identity and peer/session context, not just a table position. Test duplicate, delayed, out-of-order, wrong-unit/service, and stale-session responses. Keep cancellation, retries, completion, and shutdown resource accounting consistent. A network timeout does not prove a write was not executed.

Use explicit clocks/events for timing logic. Separate parser throughput from the ability of an OS, adapter, driver, and scheduler to meet serial deadlines. Zero-copy code does not establish MS/TP or RTU timing compliance. Physical timing claims require the applicable host/device test evidence, not a microbenchmark or a blanket RTOS assertion.

## Verify

Combine independent vectors, boundary tests, malformed inputs, stream chunking, stateful event tests, and a bounded fuzz harness. Interoperability success covers tested peers/scenarios, not all conformance. Exercise enabled transport/features and relevant callers. No production device discovery or writes without authorization.

Return the exact behavioral change, source/version used, tests run, resource/timing bounds, and any unsupported conformance or hardware claims. Keep public support documentation within the evidence.

Read [repo examples](references/repo-examples.md) for concrete patterns and pitfalls.
