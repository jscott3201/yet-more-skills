---
name: typescript-async-resources
description: Implement or review asynchronous UI work, cancellation, request races, bounded streams, workers, and resource cleanup in TypeScript. Applies across React and Svelte.
license: MIT OR Apache-2.0
---
# TypeScript Async Resources

## Identify ownership before concurrency

Name the owner of each request, subscription, timer, observer, worker, and object URL. Define
what happens when its component, route, selected site, authenticated session, or resource
revision changes. Reuse the existing query or lifecycle library instead of building a second
competing request manager.

## Make async outcomes precise

Start independent operations together only when they are truly independent and within the
permitted concurrency budget. A large `Promise.all` can overload a device or service. Decide
whether sibling results are useful after one failure; aggregate errors intentionally.

Thread cancellation into operations that accept it and guard acceptance of late responses.
Aborting a local fetch does not establish that a server write or physical action was undone.
Preserve pending/unknown outcomes and the existing idempotency contract. Do not automatically
replay non-idempotent writes after transport uncertainty.

Associate results with their original site/session/input identity. A late response must not
update a newly selected context, close a different editor, or overwrite a newer draft. Test
response reordering, cancellation during parsing, and double submission.

## Bound retained work

Apply explicit limits to stream buffers, pending requests, retry attempts, and worker queues.
Coalesce display-only telemetry only where the domain permits it; never silently discard
command acknowledgements, audit history, or gap evidence. Release listeners, observers,
timers, URLs, and workers when their owner exits, including error paths.

A worker can remove CPU work from the UI thread but adds startup, copying/transfer, and
scheduling cost. Define message validation, cancellation, and ownership of transferred buffers.
Do not transfer a buffer that another consumer still expects to use.

## Evidence

Prefer deterministic deferred responses, controlled clocks, and explicit lifecycle assertions
over arbitrary sleeps. Validate both the state visible to the user and the resources left
behind. Run representative stream load separately from normal unit tests.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
