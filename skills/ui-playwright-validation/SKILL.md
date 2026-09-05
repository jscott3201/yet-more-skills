---
name: ui-playwright-validation
description: 'Validate UI behavior in an actual browser using an existing Playwright setup: critical flows, keyboard/focus, screenshots, traces, and deployment-like behavior. No blind snapshot updates.'
license: MIT OR Apache-2.0
---
# Playwright Browser Validation

## Use the real setup

Inspect the installed Playwright version, browser projects, webServer configuration, fixtures,
test data, and artifact policy. Reuse the existing scripts. Do not change CI, install new browser
tooling, weaken authentication, or run against live equipment without appropriate authorization.
Use approved test services or simulation for writes.

Run the build/server path relevant to the claim. A dev-server test and a production-artifact
test are not identical. Confirm the server belongs to this task and the browser reaches the
intended instance; do not silently reuse an unrelated process on the same port.

## Assert what the user experiences

Use stable accessible roles, labels, and explicit app test IDs where necessary. Prefer
auto-waiting locators and retrying assertions over fixed sleeps or brittle CSS structure.
Wait for the meaningful state, not an arbitrary network-idle interval in an app with streaming
telemetry. Avoid force-clicks or direct JavaScript state mutation that bypass real behavior.

Isolate each test's browser/session/data context. Exercise loading, permission, failure,
navigation, context switch, and keyboard behavior for the changed flow. Assert that prohibited
or stale data does not appear as well as that the happy path succeeds.

## Inspect and diagnose

Capture useful traces and failure screenshots under the existing policy. For visual comparisons,
control viewport, browser, fonts, time-dependent fixtures, and animations appropriately. Review
actual diffs before updating baselines; do not mask the region containing the behavior under
test. Redact or avoid secrets and sensitive data in retained artifacts.

Keep smoke checks focused and use broader browser matrices at the project's appropriate stage.
A Chromium pass is not evidence for unrun Firefox/WebKit projects. Automated accessibility
checks complement keyboard and assistive-technology testing; they do not establish full
conformance. Report real runs, inspected artifacts, and unrun environments distinctly.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
