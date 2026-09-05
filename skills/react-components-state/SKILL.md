---
name: react-components-state
description: Implement or review React components, state ownership, effects, hooks, composition, and forms. Use only in React; do not apply React patterns to Svelte.
license: MIT OR Apache-2.0
---
# React Components and State

## Choose one owner

Determine which state comes from the server, URL, local interaction, or editable draft. Use
the existing query/router/store patterns. Derive display values from their inputs instead of
copying them into state and synchronizing with another effect. Keep state near the component
that owns it; lift only what cooperating components actually share.

Keep render logic pure. Put user-triggered actions in event handlers and use effects to
synchronize with external systems. Effects must handle changing dependencies and clean up
subscriptions. Fix stale closures rather than suppressing hook dependency checks. Development
Strict Mode should expose lifecycle problems, not be disabled to conceal them.

## Compose for a concrete use

Prefer a small typed component API with native semantics and explicit variants. Use compound
components or shared context when they simplify a real family of interactions, not for every
button. Native booleans such as `disabled` are fine; avoid combinatorial mode flags that allow
contradictory states. Preserve identity with meaningful keys. Do not define component types
inside render when their remounting would lose state or focus.

Reuse the installed shadcn/local primitive APIs and preserve ref, event, and accessibility
props across wrappers. Do not nest buttons or replace a link with click-only text. Keep controlled
input values and validation feedback coherent through loading, failed submit, and reset.

## Respect runtime and version

React 19 support does not mean React Compiler is enabled, nor that a Vite SPA has Server
Components. Do not import Next.js APIs or replace valid `useContext`/ref patterns en masse
because a community skill prefers newer syntax. Inspect actual compatibility requirements.

## Validate behavior

Exercise changing props, reorder/remove, keyboard use, failed async work, and mount/unmount.
Test the user-visible outcome with the project's renderer and use browser evidence for focus,
layout, or other behavior its DOM emulator does not model reliably. Reach for `react-performance`
only when render cost or subscriptions are the actual issue.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
