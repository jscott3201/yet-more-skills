# A small cross-language fixture corpus

Use the project's existing fixture format. Each case needs an input, the intended accept/reject outcome, and the important semantic value or error category. It does not need a new fixture framework.

| Input shape | Decision to make explicit |
| --- | --- |
| An integer identifier beyond JavaScript's exact Number range | Reject an unsupported numeric representation or preserve it through the agreed string/other exact representation before precision is lost. |
| Missing field, explicit null, zero, and false | Preserve the domain's distinct meanings; remember Python bool participates in integer APIs unless validation excludes it. |
| Repeated JSON object name | Keep the original JSON text and test the chosen duplicate-name policy; a dict/object literal cannot represent this case. |
| Unknown enum or newly added field | Prove the supported compatibility policy rather than assuming every old reader ignores additions. |
| Non-finite number, oversized payload, or excessive nesting | Verify bounded rejection at the actual public boundary. |
| Local time during an offset transition | Require the contract's timezone/disambiguation data or reject ambiguity; do not invent an instant. |
| Native conversion failure | Compare the documented Python exception and signature with the loaded extension and stubs. |

For example, the raw token `9007199254740993` is useful precisely because converting it through a JavaScript Number can destroy the original value. A test that constructs the expected result using the same lossy reader is not independent evidence. The correct product behavior may be rejection, not automatic coercion to a new representation.

Sources, checked September 7, 2026: [JSON interoperability, RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html), [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html), [PyO3 free-threading](https://pyo3.rs/main/free-threading). Match the project's schema and installed binding version; these sources do not choose its compatibility policy.
