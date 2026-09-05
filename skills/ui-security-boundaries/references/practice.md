# Defensive review examples

## Equipment names and annotations

Treat a device name or operator note as text unless the application explicitly supports richer
content. Check rendering sinks and navigation targets, not just where data was fetched. A
generated type that calls the field `string` gives no assurance about HTML, script URLs, or
remote references. Reuse a maintained sanitizer when rich content is required; do not invent
regular-expression HTML sanitization.

## Public configuration

Browser configuration can specify a non-secret service address, but it is visible to users
and cannot grant permissions. Validate it under the application's allowed-origin/deployment
policy before constructing requests. Do not solve local configuration problems with wildcard
origins, broad filesystem exposure, or client-side credential embedding.

## Sessions and commands

Match the current backend session design. Cookie-based sessions may require explicit CSRF
integration; a different design has different requirements. Preserve that integration rather
than applying a universal token-storage recipe. Validate every dangerous action server-side,
even when the browser previously received a capability list.

A delayed response from an earlier principal must not repopulate a cleared cache after logout.
Test ordering as well as the clear operation itself. For physical actions, maintain the
required approval/admission/status path and explicitly represent uncertain completion.

## Imports and plugins

An imported graph or provider configuration can be both large and hostile. Check the declared
shape and semantic bounds before changing application state. Do not allow imported labels,
SVG, or URLs to silently become executable content. A component registry is a software supply
source: review proposed files and scripts before adoption, and retain appropriate attribution.

## Test safety

Use test services and simulation for action flows. Do not aim browser automation at actual
equipment or production operators' sessions. Security fixture content is for defensive tests;
keep it isolated from logs and exports that other tools might interpret unsafely.

## Sources

Use documentation matching the installed version.

- [OWASP DOM XSS prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)
- [Vite public environment variables](https://vite.dev/guide/env-and-mode)
- [SvelteKit server-only boundaries](https://svelte.dev/docs/kit/server-only-modules)
