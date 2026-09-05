# Browser acceptance slices

## Navigation and state

Visit a deep route directly, refresh it, switch sites, open an overlay, and use back/forward
navigation. Check selected context, data isolation, focus, and whether the correct API base
and runtime config are in use. Test a service-unavailable or expired-session response without
silently converting it to an empty-success screen.

## Equipment configuration

Open with the keyboard, enter invalid values, inspect field feedback, correct them, submit,
and observe the real pending and confirmed outcome. Test a conflict or uncertain completion.
A network mock is useful for controlled errors; a separate integration test is needed for the
real browser-to-service contract. Record which one was used.

## Robust waiting

Wait for the exact visible state or a relevant response tied to the user action. Background
polling and WebSockets can make broad network-idle assumptions wrong. Auto-retrying assertions
should express user-observable expectations; avoid one-shot reads followed by an immediate
equality check when the UI is expected to update asynchronously.

## Visual comparisons

Use deterministic fixture data instead of screenshotting live changing telemetry. Match the
environment when comparing reference images. Keep browser/font differences separate from
product changes and avoid forgiving every mismatch with a large threshold. Examine changed
regions before rebaselining. A stable screenshot does not prove keyboard operation or that
an apparent success corresponds to an authoritative backend result.

## Failure triage

Read the first relevant failure and trace rather than increasing every timeout. Check server
readiness, environment, selector semantics, permissions, and actual app state. Preserve a
reproducible test failure instead of adding unconditional retries. Capture only the artifacts
useful to understanding the failure; do not collect or publish sensitive session contents.

## Sources

Use documentation matching the installed version.

- [Playwright best practices](https://playwright.dev/docs/best-practices)
- [Playwright assertions](https://playwright.dev/docs/test-assertions)
- [Playwright screenshots](https://playwright.dev/docs/test-snapshots)
- [Playwright accessibility checks](https://playwright.dev/docs/accessibility-testing)
