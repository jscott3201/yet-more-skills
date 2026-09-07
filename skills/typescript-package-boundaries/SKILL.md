---
name: typescript-package-boundaries
description: "Build or debug TypeScript libraries, SDKs, or Node packages at the consumer boundary: module resolution, exports, declarations, runtime support, and packed artifacts. Not ordinary React/Svelte component work or a forced ESM migration."
license: MIT OR Apache-2.0
---

# TypeScript Package Boundaries

Find who consumes the package, how it is installed, and which runtime and compiler versions are supported. Distinguish a bundled application, a Node library, a browser library, and a source-only workspace package. Their module and distribution contracts are not interchangeable.

## Follow the host, not a universal tsconfig

Inspect package.json, exports, type, imports, scripts, the emitted files, and the actual consumer's compiler configuration. Choose module and moduleResolution settings for that host. A Vite build passing with bundler resolution does not prove that an external Node consumer can resolve the same imports. TypeScript paths aliases do not by themselves rewrite emitted runtime imports.

Check relative extensions, package subpaths, conditional exports, and matching declaration entry points. Adding exports can remove previously reachable public entry points; preserve them or treat the change as an intentional compatibility decision. Do not convert every package to ESM or ship dual ESM/CJS builds without a real consumer requirement. When both forms are supported, check that stateful instances and types behave consistently across the supported loading paths.

Native TypeScript execution or a transpiler stripping types is not type checking. Keep the repository's type-check gate. Verify which syntax, tsconfig behavior, dependency loading, and runtime features the actual Node/tool version supports rather than assuming development-runner behavior transfers to production.

## Keep the distributed surface intentional

Trace runtime dependencies, peer dependencies, optional dependencies, and type-only dependencies separately. Keep browser-safe exports free of server-only imports and credentials. Do not assume tree shaking is an authorization or secret-removal boundary. Mark side effects according to actual initialization behavior rather than to improve a bundle-size score.

Keep generated declarations and clients reproducible from the authoritative source. Avoid imports into workspace-only internals, undeclared hoisted dependencies, or declarations that refer to files omitted from the package. Preserve current package-manager and lockfile policy; this is not permission for a broad dependency refresh.

## Prove a consumer can use the artifact

Use the existing build/pack workflow and inspect the package file list. Packing and installation may run lifecycle scripts, so inspect those scripts and keep execution within the authorized environment. A pack command is not permission to publish.

Install the resulting artifact into a clean temporary consumer outside source-workspace resolution. Import the public entry points, type-check a small real use, and execute it on the supported host. Include only claimed ESM, CJS, and browser paths; do not create an exhaustive platform matrix on every edit. Check that unsupported/private entry points fail as intended and that a missing declared dependency is not hidden by workspace hoisting.

Report the tested consumer/runtime combinations and remaining gaps. Use typescript-contracts for wire semantics and agent-cli-design for an actual CLI surface, when relevant and available.

Read [consumer cases and sources](references/consumers.md) for focused diagnostics.
