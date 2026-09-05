---
name: tracer-bullet-planning
description: Plan a large requested outcome as reviewable vertical PR slices with dependencies and meaningful acceptance evidence. Preserve implementation freedom; not automatic ticket publication or a rigid execution program.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Tracer-Bullet Planning

Turn a broad goal into a sequence of useful capabilities. Read the requested source plan and actual repository before decomposing it. Use available tools to resolve facts, not a compulsory memory service or planning template.

## Plan through the system

Prefer a thin working path across the necessary layers over separate batches for every schema, service, and screen. Each slice should leave a verifiable result, or be an explicitly justified step in a compatibility migration. Prefactoring earns its own PR when it leaves the system healthy and makes later work meaningfully easier.

For each slice, state its outcome, blockers, key contracts, likely change area, exclusions, and acceptance evidence. Keep implementation choices open until code inspection resolves them. Do not substitute pseudocode or a fixed file list for the behavior that needs to work.

Group related slices into milestones only when that helps review or rollout. Avoid both dozens of administrative micro-PRs and a giant unreviewable rewrite. A migration may need expand, migrate, and contract stages; a greenfield component may not need compatibility scaffolding at all. Follow the actual compatibility policy.

## Mark useful parallelism

Identify independent work such as cloud/edge or backend/UI lanes after settling their shared contracts. Name the integration owner and any combined check. Do not claim independence solely from different folders. A dependency graph is not permission to ignore repository concurrency rules.

Keep routine PR validation light and meaningful. Put larger native-platform matrices, long stress/fuzz runs, recovery campaigns, and release artifact qualification in the appropriate staged lane. Preserve required policy checks and native-only constraints.

## Leave a workable handoff

Recommend the first useful slice and explain what could change the plan. Ask for owner decisions only when credible alternatives materially alter the outcome, risk, or authority. Let the implementing agent revise routine details as evidence arrives.

Return readable Markdown when planning artifacts are requested; otherwise an outline may suffice. Issue creation, roadmap updates, and external publication require scope. Reuse existing tracker structure rather than inventing a parallel planning authority. Do not pretend a plan is executed work.
