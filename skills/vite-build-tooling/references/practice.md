# Build investigation recipes

## A passing build with broken types

Inspect what the `build` script runs. A project may run `vite build`
separately from `tsc --noEmit`; inspect and run the relevant checks independently. A minimal useful
report names each command and its outcome rather than saying “frontend validated” after
running only one. Do not weaken strictness or skip a generated package to make the command pass.

## Version-sensitive documentation

Vite's current migration guide describes changes from the prior major. Start from the
installed major's docs and inspect the plugin version too. The reviewed community Vite skill
still describes an earlier Vite 8 beta snapshot; use it for discovery, not as the authority
over a current pinned toolchain. A build target of `esnext` is not a default compatibility
policy: preserve the supported browser fleet.

## Fresh deployment checks

Build with the normal production command. Serve its output under the intended URL prefix
and equivalent routing/config behavior. Visit a deep route directly, refresh it, trigger a
lazy route, and validate config load failure. After deploying a new build, check how a
previously open tab handles a missing old chunk. Do not introduce a service worker merely
to solve cache invalidation; it changes upgrade and offline semantics.

## Secrets and development access

Public configuration may include a non-secret API endpoint or feature display setting.
It must not confer authorization. Test attacker-controlled or malformed config URLs under
the project's origin policy. Avoid logging raw secrets during build diagnosis. A `server.fs`
relaxation for a test fixture must be conditional and as narrow as the fixture requires.

## Workspaces

Find the package actually owning a file before selecting a test filter. Rebuild or regenerate
local dependencies when required by their package exports; source and installed dist may be
different. Diagnose stale artifacts by inspecting resolution, not by repeatedly deleting every
cache or reinstalling the monorepo. Do not use force installs that conceal peer incompatibility.

## Sources

Use documentation matching the installed version.

- [Vite features and TypeScript](https://vite.dev/guide/features)
- [Vite migration](https://vite.dev/guide/migration)
- [Vite environment and modes](https://vite.dev/guide/env-and-mode)
