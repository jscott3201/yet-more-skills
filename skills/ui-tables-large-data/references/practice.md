# Dense data review cases

## Manual pagination and selection

TanStack Table documents that a selected-row model can only return rows present in its
supplied data, while selection state can retain IDs beyond the current page. An action that
serializes only the selected visible row objects may therefore omit previously selected IDs.
Decide the product contract explicitly, use stable IDs, and test multiple pages.

Do not use the default row index as lasting identity for server-refreshed or sortable assets.
A checked row should continue to mean the same equipment after sorting, not the equipment
that moved into that screen position. Reset or reauthorize selection at site/session changes.

## Virtualization

A headless virtualizer determines which items to render; the application still owns markup,
measurements, state, and behavior. Define realistic row height behavior, handle expanded rows,
and keep focus from disappearing when the focused row leaves the rendered window. Test fast
scrolling, returning to a selected item, keyboard navigation, and resizing.

A virtualized table that downloads the entire fleet may still be too expensive on a field
device. Measure payload, parsing, retained data, transformations, and mounted DOM separately.
Prefer an existing server query/pagination contract over inventing browser-only filtering
that cannot represent the full dataset correctly.

## Useful empty/error states

Distinguish no configured assets from no matches, loading a new page, a stale page after
failed refresh, denied access, and an expired cursor. Preserve useful filter context and offer
a specific recovery action. Do not announce success for an action that affected only a subset
unless that partial result is explicit.

## Browser acceptance

Use varied data: long multilingual names, missing units, extreme numeric widths, stale status,
and narrow windows. Check sticky headers/columns do not obscure focus, column actions have
names, and row actions do not accidentally toggle selection or submit a containing form.
Keep a full-value detail route when display text is truncated.

## Sources

Use documentation matching the installed version.

- [TanStack Table row selection](https://tanstack.com/table/v8/docs/guide/row-selection)
- [TanStack Virtual introduction](https://tanstack.com/virtual/latest/docs/introduction)
- [WCAG focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
