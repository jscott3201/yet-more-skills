---
name: agent-cli-design
description: "Design or review command-line interfaces used by people and agents: discoverable commands, non-interactive execution, structured output, exit status, and safe mutation. Not a mandate to add a CLI or replace its parser."
license: MIT OR Apache-2.0
---

# Agent-Friendly CLI Design

Make the existing CLI easy to discover, compose, and recover from without sacrificing human use. Read its parser, callers, documented compatibility, and supported platforms first. This skill applies to Python, Rust, and TypeScript implementations; it does not require a new parser or an agent framework.

## Separate discovery from execution

Keep help and capability listing read-only and usable before credentials, network access, or destination setup when those are unnecessary for discovery. Describe required arguments, defaults, units, scope, and a small working example. Return stable resource identifiers rather than requiring a caller to scrape a display label or invent a path.

Non-interactive use must not unexpectedly open a browser, prompt forever, start a pager, or choose an ambiguous target. Explain missing input and the next supported action. Preserve an interactive path where useful; do not make automation imitate keystrokes. Existing user and repository authority still governs installation, writes, publication, and destructive actions.

## Treat output as a public contract

Provide a documented machine mode when needed. Keep its result channel free of banners, progress spinners, ANSI decoration, and incidental logs; route diagnostics separately. Choose one JSON document or an explicitly framed stream, not an accidental mixture. Preserve meaningful empty, partial, failed, and outcome-unknown states. Define exit status together with the payload rather than reporting success merely because some rows were printed.

Keep IDs, units, timestamps, field meanings, and ordering stable where promised. Bound large listings through the existing limit/filter/page mechanism and disclose truncation. Do not add schema versioning or a second API protocol without a compatibility need. Keep secrets out of output and diagnostics; machine readability does not justify dumping all internal state.

## Make effects and interruption honest

Reuse the application's validation, authorization, preview, and reconciliation path. A dry run should not perform the mutation it previews; document any unavoidable external reads. Missing confirmation is not permission to enable a force flag. Retrying an interrupted mutation requires its actual idempotence or outcome check.

Build child-process arguments as argument vectors rather than interpolated shell commands. Also handle option-like user values, working directory, environment inheritance, input limits, and platform-specific process behavior. Own child lifetimes and output drains. A caller disappearing or a pipe closing does not prove a remote action was rolled back.

## Test the consumer path

Run the installed or built entry point, not only parser helpers. Exercise help, no-TTY input, invalid arguments, spaces and Unicode, empty and large results, stderr separation, nonzero failures, cancellation, and the supported broken-pipe policy. Parse machine output with an independent reader and verify that read-only modes leave the destination untouched.

Return the supported interaction contract and observed tests. Use the existing agent-tool-boundaries or language specialist only when that boundary also needs work.

Read [consumer checks and sources](references/consumer-checks.md) for focused examples.
