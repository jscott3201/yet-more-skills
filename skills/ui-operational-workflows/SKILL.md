---
name: ui-operational-workflows
description: Design or review building-automation, FDD, energy, device configuration, and agent-assisted operator screens. Preserve data quality, authority, provenance, and physical-command uncertainty.
license: MIT OR Apache-2.0
---
# Building Operations UI Workflows

## Find the real domain state

Read the current Rust/API contracts and implemented endpoints before designing status or actions.
Keep observed state, computed findings, operator intent, server acceptance, Edge admission,
provider execution, readback, and verification distinct where the contract does. A schema or
planned capability is not a shipped implementation.

Preserve missing, invalid, stale, unknown, and known-zero values. Never render missing telemetry
or `NO_EVAL` as normal operation. Show units and the meaningful time/quality context. Separate
source time from receive time and display timezone explicitly when interpretation requires it.
Do not silently interpolate away gaps or aggregate incompatible units/windows.

## Make actions honest

Scope every view and action to the current site, equipment, resource revision, and authorized
capability. Clear or retire prior-context drafts, selections, subscriptions, and caches according
to policy. Backend authorization remains authoritative; disabling a button does not enforce it.

For impactful actions, show the target and consequence and follow the existing approval path.
Acknowledging a finding does not clear a physical fault. Cancelling a local task does not undo
an uncertain command. Optimistic “applied” states are inappropriate without the required
confirmation. Reuse operation identity and reconciliation; do not invent a retry protocol.

## Design for investigation and recovery

Prefer navigable tables and detail panels for large asset collections. Use charts/graphs as
complementary explanations, not the only path to inspect or configure. Keep evidence reachable
and distinguish severity, priority, acknowledgement, suppression, and verification. Configuration
drafts need validation, conflict handling, and explicit pending/confirmed outcomes.

Agent suggestions and generated plans must remain proposals until the authorized application
workflow accepts them. Show uncertain or unavailable capabilities rather than fabricating an
enabled button or direct database/device access path.

Test stale and reordered telemetry, site switching, partial service failure, permission loss,
unknown command completion, invalid units/time, and resource revision changes. State which
outcomes were exercised; do not use polished UI to imply unverified backend capability.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
