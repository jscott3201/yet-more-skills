---
name: ui-vitest-testing
description: Write, select, or debug Vitest and framework component tests, including Testing Library and browser-mode boundaries. Preserve repository isolation and avoid false-green test selections.
license: MIT OR Apache-2.0
---
# Vitest and Component Testing

## Inspect the test environment

Read package scripts, test configuration, installed Vitest major, setup files, framework renderer,
and existing fixtures. Distinguish Node, jsdom, and real-browser mode. Match the versioned
documentation; newer main-branch examples can require APIs absent from a pinned version.
Do not enable file parallelism where shared resources deliberately require isolation.

## Test the behavior at its boundary

Pure TypeScript logic belongs in fast unit tests. Components should be exercised through
meaningful roles, labels, and user interactions using the framework's actual testing adapter.
Use real-browser evidence for layout, native focus/selection, CSS, and behavior the emulator
does not model faithfully. Vite/browser transpilation does not replace type checking.

Add a regression that fails for the original defect. Cover relevant loading, empty, error,
permission, stale-result, and cleanup behavior. Assert the intended outcome and error, not
merely that an exception occurred or a mocked helper was called.

## Control async and isolation

Await user interactions and meaningful async assertions. Use deferred responses or controlled
clocks for races rather than arbitrary delays. Restore mocks, timers, listeners, and global
state. Give tests their own data/cache/session resources; teardown must not affect siblings.
Mock external boundaries intentionally without bypassing the behavior under test.

Run the smallest useful file/test selection first and confirm nonzero collected/executed tests.
Do not enable pass-with-no-tests or retries to manufacture green results. Snapshot updates need
a semantic explanation and review, not automatic reblessing. Separate a legitimate environment
limitation from a product failure and report both honestly.

## Report evidence

Name the actual package, filter, environment, and result. A focused component pass does not
imply all workspace tests or browser flows passed. Keep normal checks fast; broader browser,
stress, and artifact qualification belong to the existing staged workflow.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
