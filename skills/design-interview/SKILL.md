---
name: design-interview
description: Run a multi-round decision-tree interview only when the user explicitly asks to be grilled, interviewed, or to stress-test a design. Find facts independently and ask only decisions the user owns.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex; OpenCode requires an explicit-only adapter"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Design Interview

Use only after an explicit request for an interview. The goal is a decision-ready design record, not permission to build or publish it.

Map the topic as a decision tree. The **frontier** is the set of open decisions whose prerequisites are already settled. Work one frontier at a time so later questions do not depend on guessed earlier answers.

## Each round

1. Resolve discoverable facts from repository state, tools, and primary sources. Ask the user for decisions, preferences, risk tolerance, and intent—not facts the environment can establish.
2. Ask one to three frontier questions. Use the harness-native structured question tool when available; otherwise ask the same concise questions directly.
3. Give two or three mutually exclusive choices for each question, put the recommended choice first, and state its concrete tradeoff. Preserve the user's ability to give a custom answer.
4. Record the answer, its rationale, validity conditions, and newly opened branches. Recompute the frontier before the next round.

Do not dispatch agents merely to avoid doing bounded fact-finding. Delegate only an independent read-only question when collaboration is authorized and the result can arrive without blocking other frontier questions.

Stop when the frontier is empty, the user says the design is sufficiently resolved, or a fact/authority gap prevents an honest next question. Use the owner-decision gate for material contract, infrastructure, migration, publication, or authority choices before implementation depends on them.

Return a compact decision record with the agreed outcome, resolved branches, assumptions, out-of-scope branches, remaining unknowns, and the next authorized action. Do not edit project files or start implementation unless separately requested.
