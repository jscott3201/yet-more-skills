---
name: context-efficiency
description: "Reduce agent token waste from excessive retrieval, tool output, repeated exploration, or delegation. Use for context/cost problems; not auth tokens, UI design tokens, or permission to skip required evidence."
license: MIT OR Apache-2.0
---

# Right-Sized Agent Work

Optimize total work needed for a correct result, not the shortest individual prompt. Use existing tools and policy; no mandatory budget report, index, compression service, or model change.

## Match effort to the question

For a local correction, start with applicable instructions, the owner, and its meaningful test. Trace callers and contracts for a behavioral change. For requested broad research, cover the requested breadth in focused questions rather than importing everything at once. Reuse known context and proceed with reversible assumptions; do not ask the user to choose a budget before routine work.

Expand when a test contradicts the model, ownership is unclear, coverage is incomplete, or a public, concurrency, persistence, security, or physical-action boundary demands it. Stop exploring a question once its decision has adequate evidence. Finish required checks and the requested outcome; a token target never turns incomplete work into success.

## Admit useful context only

Before a read, identify what uncertainty it resolves. Locate paths or symbols first; retrieve the relevant complete semantic unit and necessary surrounding invariants. Batch adjacent useful reads instead of many tiny calls. Use exact IDs and continuation returned by tools. Empty, failed, and truncated results differ; widen scope when absence matters.

Select the relevant skill description, then its body and only the references needed now. Do not load a whole catalog's bodies, every specialist, or an archive to answer one local question. Do not re-read unchanged evidence or repeat a failed lookup unchanged.

## Keep output bounded and recoverable

Filter and project large data in the authorized execution environment before returning it to the model. Keep full failure evidence in an allowed retrievable artifact when practical; return the actual exit status, selected scope/counts, decisive error, and source pointer. Do not hide failures behind a successful pipe, an arbitrary head/tail, or quiet output. Inspect omitted context when it could change the diagnosis. Do not rerun a mutation just to recover its output.

Use available symbol navigation or output reducers only when they help. Verify their semantics and raw recovery; do not install hooks, upload source, or bypass permissions through another execution tool. [Retrieval and output recipes](references/recipes.md) covers language and log cases.

## Avoid moving the bill elsewhere

Keep bounded lookups local. Delegate independent work only when it repays setup, duplication, and integration; request findings and evidence pointers, not transcripts. Preserve constraints, unresolved errors, unknown outcomes, and usable references in handoffs. Actual compaction, cache control, and model routing belong to the supported host; a skill cannot remove already-loaded context or grant new capabilities.

For a cost investigation, compare equivalent successful tasks including retries and workers. Output bytes are not billed tokens, and cached tokens still occupy context. Do not impose arbitrary context percentages or weaken reasoning globally. [Research and measurement notes](references/research.md) explains alternatives and limits.
