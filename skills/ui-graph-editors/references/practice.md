# Graph editor acceptance cases

## Identity and layout

Dragging an AHU node changes layout, not the identity of the equipment or the contract of its
connected ports. Renaming a label must not reassign an edge. Deleting and undoing a node must
restore the intended edges without manufacturing new domain identity. Reloading the model and
layout should preserve meaningful state, not transient hover or library internals.

## Performance

Measure panning, selecting, opening an inspector, dragging, and applying validation results
separately. Broad subscriptions can make every node movement wake unrelated panels. React
Flow's performance guide is relevant to React Flow, not proof that a Svelte graph library
uses the same object-identity rules. Inspect the implementation actually installed.

Batch transient pointer updates appropriately, but do not delay important validation or
command state. A worker-based layout process needs cancellation and late-result checks:
layout for graph revision A must not overwrite graph revision B after edits.

## Accessible authoring

Make node identity, connection endpoints, and validation errors available outside the canvas.
An equipment table plus a connection form can provide a practical alternative to drag-and-drop.
Keep focus stable when changing selection or opening an inspector. Distinguish application
keyboard shortcuts from text-field editing and browser shortcuts.

## Persistence and collaboration

Keep accepted domain mutations separate from local display layout when the existing API does.
A user's viewport should not invalidate a semantic model revision accidentally. Respect the
repository's revision/conflict contract rather than building an ad hoc last-writer-wins editor.
Round-trip tests should include port IDs, units/types, orphaned references, duplicates, and
unknown schema versions. Runtime execution and protocol qualification remain separate evidence.

## Optional visualization

A graph is a tool for understanding relationships, not a prerequisite for every settings page.
Do not add React Flow or another renderer to a simple table task solely because this skill
exists. Keep 3D or animated equipment views as optional presentation, not domain authority.

## Sources

Use documentation matching the installed version.

- [React Flow performance](https://reactflow.dev/learn/advanced-use/performance)
- [React Flow accessibility](https://reactflow.dev/learn/advanced-use/accessibility)
