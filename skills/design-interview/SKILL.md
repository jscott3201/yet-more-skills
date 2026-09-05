---
name: design-interview
description: Run a focused design interview only when explicitly requested. Research discoverable facts first and ask the user about consequential choices; not a mandatory interview before implementation.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Design Interview

Use an interview when the user asks to be interviewed, challenged, or guided through unresolved design decisions. Do not turn an ordinary request for research or implementation into a questionnaire.

## Find the open decisions

Read the brief, relevant source, and prior answers. Separate facts you can discover from choices only the user can make. Identify which decisions are truly open and which depend on earlier answers. Resolve enough factual context to present a meaningful recommendation.

Ask a small number of related questions at a time. Explain the recommended option and its concrete tradeoff while leaving room for a custom answer. Do not invent uncertainty to fill a question quota, ask for already supplied information, or demand preferences on routine reversible details.

## Adapt to the answers

Carry forward the user's actual decision and rationale. Revisit it only when new evidence changes its assumptions. Continue independent fact-finding when useful; do not invent background capabilities or require named research agents.

A product behavior, compatibility promise, irreversible migration, recurring cost, or authority boundary deserves explicit treatment. Helper names and local test organization generally do not. When a decision cannot yet be made, explain the missing evidence and avoid building dependent assumptions into the plan.

## Stop when the interview has done its job

Stop when consequential decisions are sufficiently resolved, the user asks to stop, or a genuine evidence gap blocks progress. Return the agreed outcome, important constraints, remaining uncertainty, and next useful action. A compact summary is enough; no separate decision record is required unless requested.

The interview does not authorize implementation, edits to durable project documents, infrastructure changes, or publication on its own. Honor the scope already given and do not infer new permission from silence.
