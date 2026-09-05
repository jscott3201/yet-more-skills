# Review questions that uncover real UI defects

## Data path

What exact payload reaches the view? Which code validates it? Does the UI preserve unit,
timestamp, quality, resource identity, and revision? Are generated types consumed or patched?
Can an absent field become zero, an unknown state become normal, or an out-of-range number
become a plausible rounded value? Inspect serialization, not only types.

## Async path

What happens if a request completes after switching sites or closing a form? If two submissions
overlap, which result owns the error banner and draft? Does cancellation release a local wait
while a remote action remains unknown? Does cleanup target the current instance's resources?
Use an explicit interleaving to demonstrate the defect instead of saying “possible race.”

## Interaction path

Can a keyboard user complete the same task? Does sorting move a draft or selected action to
the wrong row? Is a dialog correctly named and does focus return somewhere useful? Does a
nested button submit a form accidentally? Does a visually disabled control still expose an
unauthorized action through another path? Backend authorization must be checked separately.

## Evidence path

Did the command use the package owning the changed file? Did the filter run any tests? Was
the browser served the current build or stale output? Were snapshots inspected? Did a
dependency or config change invalidate earlier validation? Reuse valid checks, but do not
promote an unrun check because another related one passed.

## A compact finding

Use: affected code; triggering sequence; observable failure; severity under local policy;
minimal corrective direction; test that demonstrates it. Avoid large speculative rewrites,
duplicate findings, and generic checklists pasted into a review. A suggestion to improve
readability should not be dressed up as a production incident without evidence.

## Sources

Use documentation matching the installed version.

- [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [React effect lifecycle](https://react.dev/reference/react/useEffect)
- [Svelte state guidance](https://svelte.dev/docs/svelte/$state)
- [Playwright testing practice](https://playwright.dev/docs/best-practices)
