# Port-aware checks

## A React example is a design reference only

First identify the installed Svelte component serving the same role. Read its props and
composition mechanism rather than mechanically translating tags. A trigger wrapper must
preserve all required primitive behavior even when the visual result looks identical.
Avoid adding a React dependency to reuse one component example.

## Migration containment

Svelte 5 and Bits UI changes may alter event or child composition. Determine the precise
packages that need alignment, inspect the current migration notes, and keep the change local.
Retain legacy-compatible patterns where the repository still supports them. Do not introduce
a new compiler mode or experimental feature only to match an example from main-branch docs.

## Dialog and combobox acceptance

Check the visible label and programmatic name, Tab behavior, Escape, focus return, and the
non-pointer interaction. Test a nested popover inside a dialog rather than assuming isolated
primitives compose correctly. When a form submission fails, preserve the draft and move or
announce focus appropriately without repeatedly interrupting the user.

Binding the open state should not create a second owner fighting the primitive. Reopening
must show the intended fresh or retained input state. Do not close the dialog prematurely
merely because a request was accepted rather than confirmed.

## Style and accessibility are coupled

A clipped focus ring, hidden label, tiny icon-only trigger, or body scroll lock can regress
usability while passing type checks. Inspect the complete page at narrow and wide sizes and
with the supported themes. Keep the semantic role of status colors consistent with adjacent
operational screens and provide a text/icon cue as well.

## Sources

Use documentation matching the installed version.

- [shadcn-svelte documentation](https://www.shadcn-svelte.com/docs)
- [Svelte 5 migration guidance](https://www.shadcn-svelte.com/docs/migration/svelte-5)
- [Svelte official skills](https://svelte.dev/docs/ai/skills)
- [Combobox interaction pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
