# A lightweight check ladder

## Routine UI slice

Start with the changed package's relevant type/component test. Run the existing lint and
production build as required by the repository. Add a targeted browser flow when the change
affects actual interaction, routing, auth, overlays, or layout. Do not make every text change
run all engines and every dataset, and do not skip meaningful local tests because PR CI is light.

## Shared or boundary change

A generated API change needs the contract generation/check pipeline and affected consumers.
A shared control needs representative consumer tests. A runtime config or authentication change
needs the real loading/permission/context flows. A dependency upgrade needs the supported
toolchain and compatibility checks rather than just a successful installation.

## Staged release

Build once using the intended reproducible environment, then validate the output under
production-equivalent hosting. Exercise direct navigation, refresh, lazy loading, missing config,
unavailable APIs, upgrade/stale-tab behavior, and supported themes/viewports. Test supported
browsers as specified by the product. Use native containers only when they represent the real
deployment/test need, not a complicated substitute for an available native environment.

## Artifacts

Preserve the existing public/private artifact boundary. Build output, package assets, reports,
and debugging traces serve different audiences. Do not bundle environment files, credentials,
private source, or browser session captures accidentally. Check release assets through the
authorized repository workflow; this skill does not create publication permission.

## Evidence vocabulary

Say which checks ran and on what scope. “Built” does not mean “type-checked”; “jsdom passed”
does not mean “browser-qualified”; “preview worked” does not mean “production hosting verified.”
Keep the report short but precise, and preserve existing stopping/repair limits rather than
adding another gate from this skill pack.

## Sources

Use documentation matching the installed version.

- [Vite environment behavior](https://vite.dev/guide/env-and-mode)
- [Playwright best practices](https://playwright.dev/docs/best-practices)
- [SvelteKit server boundaries](https://svelte.dev/docs/kit/server-only-modules)
