---
name: parallel-portfolio
description: Coordinate an explicitly authorized portfolio of up to two disjoint product PR lanes from one exact base through isolated worktrees, per-lane immutable review, a root-owned integration barrier, and one frozen delivery head. Use only when explicitly invoked and repository-local law permits parallel writers; not for ordinary delivery or shared-authority changes.
license: MIT OR Apache-2.0
metadata:
  category: delivery
  phase: orchestration
---

# Parallel Portfolio

This is an opt-in Phase 1 workflow for two genuinely independent product-code lanes. It changes concurrency, not scope, permissions, evidence standards, or merge authority. Ordinary `orchestrate` delivery remains serial.

## Admission gate

Admit a portfolio only when all of the following are proven:

- The user explicitly invoked `$parallel-portfolio` for the named outcome.
- Repository-local instructions explicitly permit parallel product writers. If they retain a sole-writer rule, return `REPLAN_REQUIRED` and propose one serial workflow-law PR; this skill cannot override them.
- No serial implementation cycle or other portfolio is active in the root session.
- At most two dependency-independent lanes start from one recorded target branch and exact base SHA.
- Each lane has a separate clean branch/worktree, one `lane_implementer`, and immutable owned and prohibited paths and symbols.
- The root has recorded the integration target, declared lane order, combined gates, and merge/close authority. Recommend a dedicated integration branch and PR.

Do not admit a lane that needs another lane's unpublished work, a manual barrier fix, or a shared authority surface. First land a serial foundation slice and re-ground from its merged head.

## Shared authority exclusion zone

Shared authority surfaces must be settled at the common base and remain read-only throughout the portfolio. No lane may edit:

- workspace manifests or dependency locks;
- public contracts, generated clients/artifacts, or API wire shapes;
- database migrations, `.sqlx`, schema ownership, or persistence authority;
- root packaging, deployment, broad scripts, CI, repository instructions, or workflow law;
- program/roadmap status or another repository's mutable planning authority.

Path disjointness is necessary but not sufficient. Reject hidden symbol, lifecycle, migration, generator, or runtime coupling.

## Portfolio workflow

1. Ground the portfolio once at the common base. Use Codebase Memory first, record coverage gaps, exact prerequisites, overlapping PRs, unrelated WIP, and repository law.
2. Load [the portfolio ledger](references/ledger.md) and publish a user-visible admission summary. Resolve any material choice with `owner-decision-gate` before writers start.
3. Create the lane worktrees/branches and a root-owned integration branch from the same exact base. The root owns all Git and GitHub mutations.
4. Spawn one `lane_implementer` per admitted lane. Supply the complete `PARALLEL_LANE_PACKET`; an incomplete packet is a hard stop. Each writer's first command must prove the packet worktree's absolute Git top-level, branch, current work HEAD/tree, and cleanliness. Initially the work HEAD/tree equals the immutable common base; an approved repair packet records the root's committed lane HEAD/tree without changing that base or the allowlists. Every mutating command or gate must use that explicit worktree. Writers do not delegate, commit, push, inspect another lane's worktree, or cross their allowlists.
5. Inspect each completed lane independently. Commit and open at most two lane PRs against the recorded target branch. Use `pr-gate-loop` for packet- and repository-required gates and immutable holistic/dataflow review for each lane PR, with separate cycle counters. Any permitted repair goes to the same original `lane_implementer` with a refreshed work HEAD/tree; never change its common base or ownership. Identify combined checks explicitly deferred to integration, including why they apply there; a deferred check is not a pass and cannot be omitted from the integration gate.
6. After every selected lane passes, rebuild the integration branch from the common base and apply the unchanged reviewed lane commits in declared order. Any conflict, generator drift, or required glue edit returns `REPLAN_REQUIRED`; do not repair at the barrier.
7. Run the combined smoke/rehearsal gates, open one integration PR, and use `pr-gate-loop` for holistic/dataflow review and checks on its exact head. Keep an independent integration-PR cycle record. The integration barrier is stricter: any finding requiring code or glue changes returns to re-planning without an integration repair batch.
8. Freeze the accepted integration head as the delivery/demo candidate. Merge only with valid exact-head authority, verify tree equality, and close or retain lane PRs only as explicitly authorized. Record the final target SHA and all lane/integration evidence.
9. Clean up only task-owned temporary worktrees and integration scratch state. End at `MERGED`, `READY_TO_MERGE`, or `REPLAN_REQUIRED`.

## Failure rules

Replan the affected lane or collapse the portfolio to serial delivery when ownership overlaps, a lane needs a shared manifest/lock/contract/migration/package surface, a dependency becomes ordered, a head moves outside the root-recorded commit/repair transitions, or required gate failures remain unresolved under `pr-gate-loop`. Replan the whole portfolio when the barrier conflicts, combined behavior requires glue, the common base changes, or one frozen integration head cannot represent the delivered result.
