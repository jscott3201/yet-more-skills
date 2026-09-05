---
name: ui-tables-large-data
description: Build or review dense asset tables, large lists, pagination, sorting, filtering, selection, and virtualization. Use the installed framework adapters; do not assume all rows are loaded.
license: MIT OR Apache-2.0
---
# UI Tables and Large Data

## Define the data boundary

Determine which rows are loaded, which operations run on the server, and what the displayed
counts mean. Use stable row identity rather than an array index. Include sorting, filters,
cursor/page, site, and time range in the relevant request/cache identity. Preserve explicit
unknown totals instead of inventing a count from the current page.

Choose client-side operations only when the complete relevant dataset and performance budget
support them. Do not present sorting or filtering of one page as a global result. Keep
pagination and sort/filter modes consistent, and handle changed datasets or invalid cursors.

## Selection and editing

Separate selected IDs from the current visible rows. Define whether selection survives paging,
filtering, and context changes. Label bulk actions precisely: selected rows, current page,
or all matching results are different scopes. Revalidate authority and resource versions on
submission. Keep inline drafts from attaching to a different row after sorting or refresh.

## Render efficiently without hiding semantics

Start with measured data size and interaction cost. Pagination, better queries, fewer columns,
or simpler cells may be enough. Virtualization reduces mounted DOM, not necessarily network
payloads or expensive data transformations. Use the installed virtualizer and preserve row
measurement, scroll position, keyboard navigation, and accessible context.

Avoid mounting an expensive chart, popover tree, or independent subscription in every cell.
Keep formatting and unit/quality presentation consistent; truncation needs a usable route
to the full value. Keep errors and stale values visible rather than rendering every missing
number as zero.

## Validate

Test sorting with edits/selection, filtering across pages, deleted rows, large names, narrow
layouts, resizing, keyboard operation, and bulk scope. Use real-browser evidence for scrolling,
virtualization, focus, and layout. Inspect memory and repeated interaction when claiming a
large-data performance improvement.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
