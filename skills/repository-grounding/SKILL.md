---
name: repository-grounding
description: 'Establish repository context for a substantial change: applicable instructions, actual source, ownership, dependencies, and meaningful checks. Reuse known context; not a mandatory preflight for tiny edits.'
license: MIT OR Apache-2.0
---

# Repository Grounding

Read enough of the actual repository to work safely. Scale the inspection to the task; a spelling correction does not need an architecture survey or a formal record.

## Find the working context

Read applicable instructions and the requested issue, handoff, or plan. Identify the working directory, intended branch or PR, relevant source and tests, and unrelated work to preserve. Inspect current files before treating an old handoff as implementation evidence. Do not reset, clean, stash, or move someone else's changes to make the workspace convenient.

Start with the named path or nearest owning package, the relevant symbol, and its meaningful test. Search names or signatures before retrieving large bodies; read a complete semantic unit with the imports, invariants, or callers needed to interpret it. Batch adjacent reads that answer the same question rather than making many tiny calls. Do not load the whole tree, lockfile, plan archive, or every skill reference as an orientation ritual.

Trace important callers and contracts as the change requires. Expand when the owner is unknown, a result is incomplete, a test contradicts the model, or a public, generated, concurrency, persistence, or security boundary is affected. Stop orientation once the owner, relevant contract, and validation path are clear; implementation may reveal a new question. A narrow search is not evidence of repository-wide absence.

Use an available code index or memory service when it helps; confirm consequential claims in source and check coverage when relying on absence. Missing optional tools are not a blocker. Do not install or rebuild an index just to complete this step.

Read the repository's actual validation commands and their package, feature, and environment scope. A familiar command is not necessarily the project's gate. Separate focused checks from staged release qualification; preserve native-only platform policy where applicable.

## Reuse what remains valid

Keep context in the working conversation or existing handoff. Refresh changed files, instructions, or prerequisites when new information invalidates them; do not repeatedly rediscover unchanged context. Do not create revision ledgers or mandatory status templates.

Proceed with reasonable reversible assumptions when the intent is clear. Ask about a material unresolved product, compatibility, ownership, or permission choice; continue independent authorized work where possible. An unavailable optional index and an unmerged required API are different kinds of gaps.

Return only the useful orientation: source of truth, likely change surface, checks to run, and any actual blocker. Distinguish observed facts from interpretation.
