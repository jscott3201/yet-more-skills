---
name: ui-graph-editors
description: Implement or review React Flow or another installed graph editor for equipment topology, authoring, dependency flows, selection, and graph persistence. Not a generic instruction to add a canvas.
license: MIT OR Apache-2.0
---
# UI Graph Editors

## Separate model from presentation

Inspect the installed graph library and domain contract. Keep semantic nodes, ports, and edges
separate from layout coordinates, viewport, selection, and transient drag state. Use stable
domain identities and explicit port identity; array order or current coordinates are not IDs.
Do not persist library-internal objects as a new domain format without a deliberate contract.

Validate connections and edits against actual types/capabilities. A visually connected wire
does not establish a valid executable model. Show backend diagnostics and preserve invalid
draft work when the workflow supports repair; do not silently normalize away meaningful errors.

## Make editing coherent

Model a user action as one undoable change, not hundreds of independent mousemove saves.
Coordinate selection, inspectors, undo/redo, clipboard, and dirty state. Handle concurrent
revisions and stale save responses; cancelling a local save does not roll back a remote write.
Sanitize imported graphs and bound nodes, edges, nesting, and payload sizes.

## Scale from measurements

For React Flow, follow its installed version's advice on stable component definitions,
callback identity, and narrow subscriptions. Do not subscribe an inspector to every node
coordinate just to learn the selected ID. Profile representative large graphs before adding
memoization, workers, or hiding offscreen content. Preserve keyboard focus and selection when
visibility changes.

For Svelte-based graph libraries, inspect their own bindings and APIs; do not mechanically
translate React hooks. This skill's domain safeguards apply, but React-specific optimization
recipes are not cross-framework APIs.

## Keep essential work accessible

Provide a structured list/table and form route for core inspection and editing. Support
documented keyboard interactions, meaningful node labels, and non-color error cues. Test
add/remove/connect, duplicate/import, undo/redo, save/reload, conflicts, and long labels in a
real browser. A screenshot or serialized graph round trip alone is not behavioral validation.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
