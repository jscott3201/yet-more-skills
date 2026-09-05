---
name: svelte-components-runes
description: Implement or review Svelte components and reactive modules, including version-supported runes, snippets, ownership, effects, and external integrations. Not for React components or automatic migrations.
license: MIT OR Apache-2.0
---
# Svelte Components and Runes

## Inspect the Svelte context

Read the installed Svelte version, compiler options, component mode, local conventions, and
checking/test commands. Distinguish a plain Svelte/Vite client from SvelteKit. Do not convert
a working legacy component or enable experimental compiler features as an incidental fix.
Match newly used APIs to the actual supported version.

## Model reactivity with one owner

Use reactive state for values that must drive reactive consumers. Prefer a derived value for
computations from state instead of maintaining a second value through an effect. Keep derived
expressions free of side effects. Understand whether data is deeply proxied, an ordinary
class instance, or raw state updated by replacement before choosing a mutation strategy.

Keep ownership explicit across props and bindings. Do not mutate parent-owned objects casually
or snapshot a changing prop into a one-time local value accidentally. Destructuring ordinary
reactive objects can lose a live relationship; distinguish that from Svelte's supported
`$props` syntax. Use stable keys for identity-bearing lists.

Effects are for external synchronization, with cleanup for listeners, observers, and imperative
widgets. Read dependencies intentionally and handle async work without stale result acceptance.
Do not make an effect callback async and expect a returned promise to become its teardown.
Prefer an event handler for a user action. Use version-supported attachment/action APIs without
migrating every existing integration to the newest syntax.

## Compose and validate

Use the project's snippet, event, and component conventions, not React children/hooks or
Radix `asChild` copied into a Svelte component. Preserve labels, focus, and keyboard behavior.
Use the Svelte-specific shadcn skill for its primitives.

Run the project's Svelte-aware type/compiler checks and focused component tests. When permitted
and available, official Svelte documentation/MCP analysis can help investigate unfamiliar syntax;
review suggestions against source and behavior. Tool availability does not justify claiming a
check ran, and an autofixer is not a replacement for tests or human-readable code.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
