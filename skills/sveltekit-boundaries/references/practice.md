# Request isolation and rendering checks

## A useful cross-user test

Start two independent requests with different authenticated users and site selections. Delay
one data source so their execution overlaps. Verify each response contains only its authorized
context, and a later unauthenticated request cannot reuse either result. This tests a real
consequence of shared mutable module state rather than only looking for a particular syntax.

## Load boundaries

Review which code runs only on the server and which may also run during client navigation.
Keep credentials and private implementation objects out of returned data. Avoid browser-only
APIs during server evaluation. Document whether an external call uses the request's identity
or an application service credential, and ensure that distinction does not disappear inside a
shared helper.

Read the installed version's invalidation behavior before forcing full-page reloads. A stale
detail after a mutation may need correct invalidation of its dependency, not a second client
fetching system. Parent/child loads should be composed according to actual dependencies.

## Forms

A validation error should preserve useful inputs and connect messages to controls. Test the
enhanced path and the non-JavaScript path when progressive enhancement is part of the product
contract. A post/redirect/get flow and a background mutation have different navigation and
recovery behavior; preserve the existing deliberate choice.

## Hydration

Inspect nondeterministic initial values, timezone/locale assumptions, browser-only reads, and
differing authorization contexts when server and client markup disagree. A client-only effect
may be appropriate for a truly browser-only capability, but it is not a general repair for an
incorrect server view. A loading shell must remain accessible and not reveal private cached data.

## Do not spread server assumptions

This skill is intentionally separate from Svelte component work. It neither requires SvelteKit
for a new widget nor replaces an existing Rust API with server actions. Server execution,
credentials, adapters, and deployment complexity must earn their place in the current project.

## Sources

Use documentation matching the installed version.

- [Server-only modules](https://svelte.dev/docs/kit/server-only-modules)
- [Loading data](https://svelte.dev/docs/kit/load)
- [State management](https://svelte.dev/docs/kit/state-management)
- [Form actions](https://svelte.dev/docs/kit/form-actions)
