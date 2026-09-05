# Svelte reactivity recipes

## State, derived value, and effect

A selected equipment ID is state. A display label derived from the selected item is a
computation. A subscription to an external telemetry stream is synchronization. Keeping those
roles separate prevents update cycles and duplicated state. Choose `$derived.by` for a
multi-step computation when the installed version supports it; do not wrap a function inside
`$derived` and mistake the function object for its computed result.

Large immutable API results may suit raw state plus replacement instead of deep proxies.
Profile that choice and maintain the update contract. Plain classes do not automatically gain
deep proxy behavior merely because an instance sits inside `$state`. A snapshot used at an
external boundary is a snapshot, not a subscription; do not expect it to keep updating.

## Props and drafts

A prop-derived value should continue to update when the prop changes. An intentional editable
draft is different: specify when it is reset and how server revisions interact with unsaved
input. Use explicit binding contracts where needed. Parent-owned data should not be changed
through a child merely because the language permits reaching the object.

## Lifecycle and async

Keep effect setup synchronous so cleanup is registered correctly. Start async work inside it
with an explicit cancellation/late-result guard where appropriate. Reads after asynchronous
boundaries are not a reason to assume all dependencies were tracked synchronously. Tests should
change the input while work is pending and verify that the old response cannot win.

SvelteKit server requests must not share mutable user state in a module singleton. That topic
belongs to `sveltekit-boundaries`; a browser-only Svelte app does not need server actions or
hydration policy added to solve a component issue.

## Optional Svelte tooling

The official Svelte AI docs provide documentation lookup and static analysis tools. Inspect
the installed tool's actual schema/CLI and permitted data boundary before sending code. When
using a shell, quote rune names so `$state` is not expanded as a shell variable. No automatic
external package download or mandatory custom subagent is introduced by this skill.

## Sources

Use documentation matching the installed version.

- [Svelte state](https://svelte.dev/docs/svelte/$state)
- [Svelte derived values](https://svelte.dev/docs/svelte/$derived)
- [Svelte effects](https://svelte.dev/docs/svelte/$effect)
- [Svelte official skill guidance](https://svelte.dev/docs/ai/skills)
- [SvelteKit state isolation](https://svelte.dev/docs/kit/state-management)
