---
name: memory-context-hygiene
description: Design, debug, or use persistent agent memory when retrieval freshness, scope, provenance, or stale task state matters. Not every repository search, transcript storage, or automatic reindexing.
license: MIT OR Apache-2.0
---

# Memory and Context Hygiene

Use memory to recover context, not to manufacture current authority. Distinguish durable decisions and user preferences from volatile task status, inferred summaries, and source-derived technical facts.

## Retrieve narrowly and verify consequential claims

Resolve the intended user, project, repository, and permitted source scope. Retrieve only what helps the current question and inspect the underlying source when correctness depends on it. An index hit is a pointer, not proof that an API is still implemented or a PR is merged. An empty result with incomplete coverage is not proof of absence.

Prefer current live state for volatile status. Keep past decisions with their rationale and conditions rather than silently rewriting history. When memory and current source disagree, show the conflict and determine whether the decision, implementation, or summary is stale. Do not automatically choose the newest timestamp; it may be a newer copy of an old claim.

## Write only useful, authorized memory

Follow the active application's persistence and privacy rules. Store a concise claim, its source, scope, and relevant validity condition when the write is authorized and future reuse is valuable. Do not save secrets, raw transcripts, speculative diagnoses, or unnecessary customer/device data. Honor deletion and scope restrictions, including derived summaries or indexes where the actual system requires it.

Use supported update/supersession behavior rather than creating competing versions of the same task fact. Respect optimistic concurrency or ownership controls exposed by the store. A second agent's stale summary must not overwrite a newer resolved decision simply because its write arrived last.

## Keep context economical

Retrieve for the next unresolved question, with the relevant project and task scope, rather than loading a whole project archive or memory timeline. Use a supported limit and follow-up reference; broaden when missing coverage or contradictory evidence matters. Reuse an adequate result until new edits, changed scope, or stale state invalidate it.

Preserve user constraints, authority, unresolved failures, operation outcomes, and source pointers through compaction. A summary is lossy and cannot replace decisive source. Do not compress repeatedly by habit or claim that writing a summary removes tokens already in the host's context; actual masking and compaction require runtime support. Use ordinary source search when a memory service is missing; do not install, reindex, migrate, or invent memory APIs to proceed.

For memory-system changes, test tenant/project isolation, stale retrieval, duplicate writes, conflicts, interrupted persistence, deletion behavior, and recovery. Separate source-of-truth records from derived embeddings, graphs, and caches. Rebuilding a derived index must not silently resurrect deleted or superseded authority.

Return the useful context, important freshness limits, and actual writes performed—not a new memory-management ceremony.
