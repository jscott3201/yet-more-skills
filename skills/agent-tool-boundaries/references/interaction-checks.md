# Tool interaction checks

Exercise discover, inspect, act, and recover as one bounded task. Discovery should return exact usable identifiers and only the data needed for selection. Do not require the model to reverse-engineer display names or fetch an entire resource store. Authorization still applies to every read and write.

A result should make the next supported step clear. Test empty success, denied access, missing resources, validation failure, partial data, expired continuation, and a response interrupted after a mutation was admitted. Error text should explain a correction without leaking credentials or inviting arbitrary retries. If structured and textual results are both returned, test their semantic agreement.

Match schemas and capabilities to the deployed MCP revision. For example, the 2025-11-25 tools specification constrains structuredContent to an object, while 2026-07-28 permits any JSON value matching the output schema. Do not widen an existing server's output shape solely because newer documentation allows it. The host must actually support the intended revision.

Annotations such as read-only and idempotence help discovery but do not enforce authorization or make an operation retry-safe. A hostile result can be well-formed JSON; its content remains untrusted data. Keep tool-result instructions from changing the user's scope or triggering unrelated calls.

Sources, checked September 7, 2026: [MCP tools, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/server/tools), [MCP tools, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/server/tools).
