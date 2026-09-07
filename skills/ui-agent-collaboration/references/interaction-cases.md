# Review one complete collaboration

Use a concrete task such as editing a configuration draft. Start with an existing value, request a suggestion, change part of it, inspect the diff, apply within existing authority, and verify the result. Then repeat with one failure rather than building a gallery of ideal chat screens.

A useful difficult case: a proposal targets one account and revision; the user switches accounts before accepting it. The old proposal must not become an action on the newly selected resource. Another case: the request was admitted, but the result stream disconnected. The UI should expose uncertainty and reconciliation, not claim cancellation or send a fresh mutation automatically.

Check whether the user can identify the next action, understand which data supports the suggestion, correct a mistaken value, and continue without the agent. A source-level walkthrough yields design hypotheses. Observations from actual participants or instrumented task runs are separate evidence; do not turn a heuristic impression into a measured usability improvement.

For accessibility, keep proposal controls in the ordinary focus order and expose a concise execution status without streaming every token into an assertive live region. Announce meaningful state changes and leave detailed logs available on demand. A tool's structured data is not itself an accessible UI.

Sources, checked September 7, 2026: [Microsoft Research human-AI interaction guidelines](https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/), [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), [MCP tool boundaries](https://modelcontextprotocol.io/specification/2026-07-28/server/tools). The guidelines inform design choices; the deployed application's authority and operation semantics remain authoritative.
