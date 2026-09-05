---
name: domain-language
description: Clarify ambiguous domain terms using code, examples, and boundary cases. Propose consistent vocabulary when terminology is the task; not an automatic glossary, ADR, or schema migration.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Domain Language

Make the language match both the domain expert's intent and the system's behavior. Reading an existing glossary is ordinary context gathering; use this skill when the meaning itself is unclear or being revised.

## Find the conflicting meanings

Inspect existing terminology in schemas, APIs, source, user-facing text, and project documentation. Use available code-search or index tools, and verify meaningful usages in source. Do not assume a project has a particular glossary filename or documentation layout.

Look for one word used for different concepts, different words used for one concept, or an implementation term that obscures a user-visible distinction. Keep documented meaning, observed behavior, owner intent, and recommendation separate.

## Stress-test a definition

Propose a short definition with important near-misses. Try ordinary examples, lifecycle transitions, failure cases, and ambiguous boundaries. In building software, concepts such as observation, command acceptance, physical readback, fault acknowledgement, and verified recovery should not collapse merely because they share a status field.

A name is useful only if it preserves the important distinction. Do not rename public interfaces for aesthetic consistency while hiding a semantic difference. When terminology changes a wire contract, stored data, or compatibility promise, surface that implementation impact before proceeding.

## Record only what earns a place

For a discussion, return proposed wording and the evidence or contradiction it resolves. Edit a glossary, API description, or decision note only when documentation changes are in scope. Use the existing project format rather than creating new directories and numbering schemes.

Preserve rationale for a surprising, costly-to-reverse decision when it will help future work. A routine naming clarification rarely needs an architecture record. Ask for owner guidance when the intended domain meaning is genuinely undecidable from available evidence; do not silently substitute a convenient technical interpretation.
