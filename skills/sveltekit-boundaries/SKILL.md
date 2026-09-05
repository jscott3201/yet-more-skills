---
name: sveltekit-boundaries
description: 'Work on an actual SvelteKit application: server/universal load, actions, SSR, request-local state, hydration, and deployment adapters. Do not introduce SvelteKit into a plain Vite SPA.'
license: MIT OR Apache-2.0
---
# SvelteKit Server and Client Boundaries

## Apply only when SvelteKit exists

Inspect the routes, adapter, load functions, actions, environment modules, and deployment mode.
Do not assume SSR, prerendering, or a particular host from the presence of Svelte alone.
A static client and a server-rendered application have different trust and deployment boundaries.

## Preserve the boundary

Keep secrets and privileged dependencies in server-only modules. Data returned to the browser
is public to that user even if a server-only load produced it. Validate parameters and perform
authorization at the server boundary; hidden buttons and client checks are not authorization.

Request-specific user, tenant, or database state must not live in mutable shared module state.
Use the framework's request-local/context facilities and establish ownership deliberately.
Test concurrent requests from different users. Scope caches to every identity affecting the
result and avoid caching private results under public keys.

Use the appropriate load path for each input. Avoid fetch waterfalls that are not dependencies,
but do not defeat required authorization checks for parallelism. Propagate useful structured
errors without leaking secrets. Keep server output and the initial client view compatible;
do not suppress hydration symptoms before finding the inconsistent state.

## Forms and navigation

Use the existing action/enhancement approach when present. Validate on the server and preserve
the submitted draft and field errors. Distinguish a submission in progress from a committed
change. Revalidation and navigation must not discard dirty state silently. Do not use a
server mutation during load as an incidental initialization side effect.

## Verify the deployed shape

Run the package's Svelte-aware checks, route tests, and relevant browser flows. Exercise direct
route visits, invalid input, unauthorized access, expired sessions, concurrent request isolation,
and adapter-specific production behavior. A Vite dev server pass does not qualify a server
adapter or a static deployment. Keep hosting changes and new runtime dependencies scoped.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
