---
name: vite-build-tooling
description: Diagnose Vite, TypeScript, package scripts, bundling, development configuration, and deployment artifacts. Match the installed Vite generation; do not apply Next.js conventions.
license: MIT OR Apache-2.0
---
# Vite Build and Tooling

## Establish the execution path

Read the package manager/version, lockfile, scripts, Vite config, framework plugin, TypeScript
config, Node requirements, and deployment adapter. Keep the repository's package manager and
reproducible installation policy. Do not regenerate another manager's lockfile or update all
dependencies as a repair shortcut.

Vite generations differ. Match configuration and plugins to the installed version: do not
copy old Rollup/esbuild-specific tuning into a Vite 8 Rolldown/Oxc project without verifying
the compatibility path. Conversely, do not apply current APIs to an older pinned version.

## Separate checks and boundaries

Transpilation is not type checking. Run the package's type checker independently of the Vite
build; Svelte components also need the project's Svelte-aware checking path. Keep lint,
tests, dependency analysis, and production build distinct in the result.

Browser-exposed environment variables are public and normally compiled into the artifact.
Preserve an existing deployment-time runtime configuration path instead of replacing it with
build-time `VITE_*` values. Validate runtime config before mounting the application. Never put
credentials in public environment variables, source maps, or downloadable config.

## Optimize and diagnose from evidence

Check plugin ordering, duplicate framework copies, aliases, package exports, browser/server
boundaries, and cache state before changing architecture. Use supported package entry points;
a smaller-looking deep import may violate exports or stop upgrades. Inspect the emitted chunks
and request waterfall before adding manual chunk rules or broad eager preloading.

Test the built application at its actual base path, including reload/deep-link routing, assets,
lazy chunks, runtime config, and failure behavior. `vite preview` is a local inspection tool,
not proof that the production hosting configuration works.

Keep development server origins and filesystem access narrow. Do not repair tests by exposing
the whole workspace or disabling security checks for normal development. Preserve existing
scoped test-only accommodations and verify their conditions.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
