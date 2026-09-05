---
name: rust-storage-durability
description: "Implement or review Rust WAL, recovery, snapshots, transactions, storage epochs, and derived indexes. Use for persistence correctness and measured storage-path changes."
license: MIT OR Apache-2.0
---

# Rust Storage and Durability

Identify what an acknowledged operation promises before optimizing storage. Follow the repository's on-disk format, mutation funnels, and current compatibility policy. A greenfield policy permits deliberate redesign, not accidental data loss or unsupported durability claims.

## Map authority and commit order

Trace validation, authoritative mutation, WAL/write staging, durability action, visible commit, index maintenance, and acknowledgment. Determine which state is primary, which is derived, and what a reader can observe between steps. Establish behavior for partial I/O, sync errors, process termination, and concurrent recovery/checkpoint activity.

Distinguish writing to a userspace buffer, flushing to an OS handle, requesting file synchronization, and obtaining the platform/device guarantees the product claims. `flush` and `File::sync_all` answer different questions. Atomic replacement is not automatically durable publication. Review file and directory synchronization, rename behavior, locking, and filesystem assumptions on each supported native OS.

Do not weaken acknowledgment ordering merely to improve throughput. If batching/group commit is proposed, specify the durability mode and how concurrent callers learn success or failure. Keep retries and idempotence explicit after an ambiguous storage result.

## Preserve readers and derived state

Hold the required epoch/read guard from authoritative file selection through actual snapshot/WAL consumption. A saved path is not a retention lease. Review lock order across recovery, rotation, prune, backup, and callbacks; avoid re-entering mutation while holding a guard that excludes it.

Keep indexes and caches synchronized with every mutation path, not just the common insert method. Cover update, delete, rollback where supported, replay, restore, compaction, schema defaults, and rebuild. Derived accelerators must not become an unvalidated replacement for authoritative values. Check stale IDs, generations, candidate sets, and deterministic tie-breaking after changes.

For parser/planner or retrieval optimizations, preserve the language and value contract: types, null/missing distinctions, duplicate behavior, ordering promises, errors, and visibility. Do not introduce new grammar or a new query policy as an incidental fast path.

## Design failure evidence

Use a fault-injection seam around relevant I/O boundaries where available. Verify truncated/corrupt data handling, selected authoritative state, and deterministic diagnostics. Fail closed or recover only as documented; do not silently skip corruption to produce a healthy-looking database.

Test live versus replayed/restored results and compare indexed retrieval with a trustworthy unindexed/exact path. Inject failure around the commit boundary, snapshot publication, and retention changes. A process-kill test leaves OS caches intact; label it process-crash evidence, not a power-loss proof.

## Measure the correct operation

Separate in-memory mutation, buffered WAL append, durable commit, checkpoint, startup recovery, and query performance. State batch size, durability mode, dataset size, cache state, memory, and write amplification where measured. Include tail latency and recovery cost when a foreground optimization defers work.

Return preserved invariants, failure tests, measured results, and platform or failure-mode gaps. Do not publish durability claims beyond the tested contract.

Read [storage ownership boundaries](references/boundaries.md) when changing persistence or derived indexes.
