---
name: edge-cloud-sync
description: 'Design or review offline edge/cloud telemetry and configuration synchronization: replay, ordering, acknowledgment, backpressure, and recovery. Not local WAL internals or a mandate to add a broker.'
license: MIT OR Apache-2.0
---

# Edge and Cloud Synchronization

Trace one record or operation from its origin through local persistence, transport, cloud admission, durable processing, and acknowledgment. Determine which guarantee the application actually promises at each boundary.

## Define identity and ownership

Use the current contract for event identity, device/site/tenant scope, ordering, and deduplication. Keep observation time, receive time, and ordering metadata distinct. Clock time alone is not a reliable unique identifier or total order across reconnects and device restarts.

Establish who owns configuration and how conflicts are reconciled. Telemetry upload, configuration delivery, and physical command execution have different risks; do not reuse a data replay mechanism as command authorization. Preserve unknown or ambiguous command outcomes until reconciled.

## Follow interruption and replay

Examine disconnects before and after local persistence, sending, server commit, and acknowledgment. A retry may deliver an already processed record. Deduplicate at the durable boundary required by the promised behavior, and define retention/expiry of deduplication state. Do not claim exactly-once behavior merely because the transport has acknowledgments.

Handle partial batches, reordered responses, checkpoint advancement, client or server restarts, and schema evolution. Advance a checkpoint only past work whose required acknowledgment has been established; do not discard unacknowledged data to make the queue look healthy.

## Bound offline operation

State queue and disk limits, backpressure, overflow policy, retry pacing, and fairness across sites or streams. Preserve data quality and loss visibility when the configured capacity is exhausted. Test sustained offline behavior rather than only a brief network outage.

Use the existing protocol, storage, and deployment model. Do not add a broker, conflict framework, hosted service, or new persistence format without a demonstrated need and the relevant scope.

## Verify end-to-end behavior

Use deterministic disconnect/restart seams and compare source records with durable downstream results. Cover duplicate delivery, lost acknowledgments, reordering, clock jumps, stale configuration, partial failure, quota exhaustion, and reconnect storms. A local queue test is not cloud durability evidence; a process-kill test is not a power-loss proof.

Report the tested guarantee, loss/duplication window if any, relevant resource bounds, and unrun platform or failure modes. Use language-specific storage and concurrency specialists for implementation details rather than duplicating them here.
