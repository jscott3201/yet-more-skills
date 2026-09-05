---
name: bounded-pr-slice
description: Shape a substantial requested change into one reviewable PR outcome with scope, contracts, and acceptance evidence. Not a requirement to write a brief before routine edits.
license: MIT OR Apache-2.0
---

# Bounded PR Slice

A slice should be understandable as one outcome, not a count of files or tasks. Use the current repository context and requested goal; the skill itself does not authorize implementation or publication.

## Shape the change

Explain what will become possible or correct, what remains out of scope, which contracts matter, and how the result will be demonstrated. Name a prerequisite only when it actually blocks the behavior. Identify source owners and the likely affected components without pretending to know the final implementation before reading them.

Prefer an end-to-end capability over disconnected horizontal work. A protocol correction may include the codec, caller handling, and regression fixture in one PR. A UI workflow may need its API integration and failure state together. Split unrelated outcomes or a migration with independently meaningful stages; do not split a coherent fix into administrative fragments.

## Leave room to implement

State invariants and acceptance behavior rather than pseudocode or mandatory helper names. Let the implementer adjust local design after inspecting the code. Revisit the plan when a public contract, data migration, new service, consequential dependency, or ownership conflict changes the promised outcome—not whenever a routine detail differs.

Use existing focused checks, plus the consumer tests needed by the change. Keep heavy native-platform, fuzz, durability, and performance qualification in its established release lane unless the change specifically needs it now. Do not remove required checks to fit a small PR.

For delegated work, identify the owner of shared contracts and generated files. Independent lanes may proceed under the repository's policy; this brief neither requires nor forbids parallel work on its own.

A few paragraphs or an existing issue are usually enough. Hand over the outcome, boundaries, acceptance evidence, and unresolved decisions. Do not require a separate planning file, ledger, or approval for an already clear authorized change.
