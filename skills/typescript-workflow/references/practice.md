# Applying this pack without creating ceremony

## A useful first pass

For a fault-detail screen, inspect the route, current API-client export, current fault view,
corresponding tests, and the token/component files used by neighboring screens. Ask which
states the operator must distinguish. Do not start with a new global state store, dashboard
template, or an inventory of the entire repository.

The normal sequence is source inspection, focused change, focused check, broader relevant
check. Reuse results when the inputs did not change. Do not promise a full visual review when
only source text was available.

## Repository fit

Identify the framework, generated client ownership, and separate typecheck, lint, test, and build scripts. Preserve deliberate test isolation until a scoped change proves it can safely change.

Treat React and Svelte as separate tracks. Do not assume SvelteKit, a deployment adapter, or a state architecture exists without inspecting the repository.

## Specialist selection

| Change | Read when useful |
|---|---|
| Component behavior | React or Svelte component skill, accessibility |
| API shape or validation | TypeScript contracts, data/forms |
| Async race, stream, worker | Async resources |
| shadcn change | The framework-specific shadcn skill |
| Dense asset screen | Tables/large data, operational workflows |
| Slow UI | Browser performance, then framework performance |
| Graph authoring | Graph editors, contracts, browser validation |
| Production artifact | Vite tooling, CI/release |

An optional browser, shadcn, or Svelte MCP integration must already be available and permitted.
Use a local CLI or ordinary source/docs instead when appropriate; do not auto-install a plugin
or transmit private source to an external analysis service.

## Completion language

Distinguish implemented, type-checked, unit-tested, browser-tested, visually inspected, and
not run. Include the actual package/filter when reporting a test command. No mandatory
timestamps, digests, tracking database, or additional review panel is introduced by this pack.

## Sources

Use documentation matching the installed version.

- [Codex skills](https://developers.openai.com/codex/skills)
