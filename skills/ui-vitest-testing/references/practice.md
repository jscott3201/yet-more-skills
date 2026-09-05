# Test selection and anti-false-green checks

## Three distinct layers

Pure functions can test parsing, sorting, validation, and state reducers cheaply. Framework
component tests test rendering and user-visible transitions. Browser tests verify native
interaction and integration. Avoid moving every test to the browser or claiming the emulator
proves CSS layout, focus trapping, and real platform behavior.

Current Vitest documentation and a repository's pinned major may differ. Read the installed major before choosing documentation for
exact browser-provider configuration. This pack intentionally does not ship a drop-in Vitest
configuration that could override the application's current policies.

## Async test example in prose

Render a site selector and detail view with controllable responses. Start A, switch to B,
resolve B, then resolve A. Assert B remains the displayed context and no A-only fields or
actions appear. Resolve or cancel all pending work, then verify cleanup. This tests the actual
race, unlike a test that awaits each request sequentially.

## Mocking

Mock the server boundary when testing UI error handling, not the state hook whose behavior
is the subject of the test. Restore replaced globals and distinguish resetting call history
from restoring an implementation. Fake timers need deliberate advancement and restoration;
avoid mixing real network behavior with a frozen clock accidentally.

## Discovery

Read the runner summary for selected and executed counts. A misspelled filter, excluded file,
or test that never asserts can produce misleading results. Keep negative type tests in the
compiler path rather than assuming Vitest executes TypeScript's static checks. A generated
client imported from stale dist also needs the owning package's build/generation step.

## Scope and shared resources

If a repository sets `fileParallelism: false`, do not change it without
identifying the shared-state reason and proving independent tests. Coordinate local servers,
ports, caches, and build output across agent tasks; one test's cleanup must not stop another
task's server.

## Sources

Use documentation matching the installed version.

- [Vitest v4 browser mode](https://v4.vitest.dev/guide/browser/)
- [Vitest mocking](https://vitest.dev/guide/mocking.html)
- [Testing Library queries](https://testing-library.com/docs/queries/about)
