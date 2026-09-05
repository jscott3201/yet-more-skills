---
name: ui-data-forms
description: Design or review UI server-state caching, query identity, editable forms, validation, mutation outcomes, and site/session transitions. Reuse the current framework and data libraries.
license: MIT OR Apache-2.0
---
# UI Data, Cache, and Forms

## Separate four kinds of state

Identify server data, navigable URL state, transient interaction state, and unsaved form drafts.
Keep each under its existing owner. A query cache is not a form draft, and a global store does
not need a duplicate of every query result. For Svelte use its installed adapters and reactive
idioms rather than importing React hooks.

Query identity must include every input that changes the resource, including relevant site,
tenant/session boundary, filters, sorting, page/cursor, and time window. Follow the application's
authenticated cache lifetime; scope keys and reset sensitive caches at identity transitions.
Do not show one site's stale data as another site's fresh response.

## Forms remain usable under failure

Preserve field labels, units, descriptions, constraints, and specific error feedback. Parse
display input separately from validated domain values; blank is not automatically zero.
Support dirty/reset states and prevent a background refetch from silently overwriting edits.
Keep server validation authoritative and handle revision conflicts explicitly.

Track submission ownership. Prevent accidental duplicate sends and associate errors/results
with the submitted draft and resource. A late result must not update a different resource.
Use optimistic updates only where rollback and reconciliation are meaningful and permitted.
Never claim a physical control action succeeded based only on a queued request or HTTP success.

## Handle async and cache outcomes

Thread supported cancellation through transports, invalidate or reconcile the relevant cache
after confirmed changes, and distinguish cancellation from failed or unknown remote completion.
Bound retries and do not replay non-idempotent actions blindly. Retain useful stale data only
with an honest stale/refetch-error indicator.

Test initial load, empty results, partial failure, validation, permission loss, context change,
response reordering, dirty drafts, revision conflict, and retry. Use existing data tooling;
do not add a new form/cache library unless the task requires it and the tradeoff is approved.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
