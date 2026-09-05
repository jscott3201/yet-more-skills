---
name: domain-language
description: Clarify ambiguous domain terminology, stress-test definitions with scenarios, and propose terminology-specific glossary or ADR wording grounded in code and repository conventions. Use when naming or domain-language meaning is the task; not for general architecture or product decisions, and documentation edits require scope.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex and OpenCode 1.x"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Domain Language

Build a shared language that matches both the domain expert's meaning and the system's actual behavior. Reading an existing glossary is an ordinary grounding step; use this skill when the language itself is being resolved or documented.

## Ground the vocabulary

1. Find repository-local glossaries, context maps, architecture records, schemas, public contracts, and naming conventions. Do not assume `CONTEXT.md` or `docs/adr/` is the repository standard.
2. Use Codebase Memory to locate definitions and usages, then inspect exact code for the load-bearing cases. Check coverage before claiming a term is absent or consistently used.
3. Separate current documented meaning, current implementation behavior, owner intent, and recommendation.

## Resolve ambiguity

- Call out one word used for multiple concepts or several words used for one concept.
- Propose a canonical term with a tight definition and explicitly named near-misses.
- Stress-test the definition with concrete boundary cases, failure cases, lifecycle transitions, and relationships to neighboring concepts.
- When code, documentation, and conversation disagree, surface the contradiction. Do not silently choose an authority that the repository does not establish.
- Keep domain definitions free of incidental implementation detail. Put implementation and architecture decisions in the repository's decision-record format instead.

Read [recording-language.md](references/recording-language.md) only when producing a glossary or decision-record proposal.

## Persistence boundary

For explanation or design discussion, return proposed wording and affected concepts without editing files. Write or revise a glossary, context map, or ADR only when documentation changes are explicitly requested or included in an authorized implementation brief. Follow the repository's existing location, numbering, status, and template; introduce a fallback format only after noting that none exists.

Recommend a durable decision record only when the decision is costly to reverse, surprising without its context, and the result of a real tradeoff. Material unresolved choices still belong to the owner-decision gate.

Return a compact record of terms, proposed definitions, evidence, tested scenarios, contradictions, documentation candidates, and remaining owner decisions.
