---
name: ui-accessibility
description: Implement or audit keyboard, focus, semantic controls, form feedback, responsive accessibility, and non-visual alternatives in UI work. Automated checks are evidence, not complete compliance.
license: MIT OR Apache-2.0
---
# UI Accessibility

## Start with the user task

Identify the critical workflow, its expected reading order, and how it works without a mouse.
Prefer native controls and semantic structure. Add ARIA for a defined interaction pattern,
not as decoration or a substitute for missing behavior. Reuse accessible local primitives
while testing their composition in the actual page.

## Inspect the full interaction

Controls need meaningful accessible names; forms need associated labels, instructions, and
errors. Support visible focus, logical Tab order, keyboard activation, and appropriate focus
movement after navigation or dialogs. Modal focus must remain within the modal and return to
the appropriate control or next logical workflow location on close. Do not hide a focused node.

Match combobox, menu, tabs, and grid behavior to the relevant pattern. A visual table does not
automatically require `role=grid`. Preserve text editing keys and native input behavior. Make
icon-only controls understandable and ensure tooltips are not the only label or instruction.

Check reflow/zoom, target size and spacing, contrast, color-independent status, long labels,
supported themes, and reduced motion. Avoid flashing or unnecessary autonomous motion. Critical
status announcements should be useful and restrained rather than streaming every telemetry tick
through an assertive live region.

## Keep complex views accessible

Large tables and virtualized lists need usable keyboard navigation and truthful row/selection
information. Graphs, charts, and 3D views need a practical structured alternative for core
information and actions. Do not leave configuration possible only through drag and drop.

Check focused controls underneath sticky headers, footers, and overlapping panels. Keyboard support alone does not establish a usable non-dragging pointer path: provide an appropriate click/tap alternative for dragging interactions unless a relevant exception applies. Exercise both paths, including graph connections and list reordering. See [focus and dragging checks](references/interaction-checks.md) for the WCAG distinctions.

## Gather honest evidence

Run the available automated checks and manual keyboard/browser checks separately. Use
screen-reader testing for the flows whose semantics cannot be established otherwise, or
explicitly mark that coverage unrun. A zero axe report or passing screenshot is not a claim
of complete WCAG conformance. Report concrete barriers, affected tasks, and reproducible fixes.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
