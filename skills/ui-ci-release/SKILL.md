---
name: ui-ci-release
description: Plan or execute authorized frontend checks and staged release qualification for TypeScript, Vite, React, or Svelte artifacts. Explicit delivery task; does not authorize new CI, publication, or deployment.
license: MIT OR Apache-2.0
---
# UI CI and Release Evidence

## Follow existing delivery policy

Read the repository's actual scripts, CI, package manager, tool versions, and artifact/deployment
contract. Use focused local checks for routine changes and reserve broad browser, integration,
and environment qualification for the existing staged-release path. Do not add automatic CI,
alter branch rules, publish, or deploy merely because this skill is selected.

## Select checks by impact

TypeScript or Svelte-aware type checks, lint, unit/component tests, generated contract checks,
dependency checks, and production build are distinct. Run relevant commands and inspect their
results. Shared components, auth, routing, runtime config, and generated-client changes may
require consumer/browser coverage beyond the touched file. Do not claim coverage from a green
unrelated job or an empty test selection.

Keep parallelism within available CPU/memory and fixture isolation. Coordinate builds and
servers among agents. Use native hosts or native-architecture containers when needed; do not
introduce QEMU, cross-compilation, or architecture emulation into this workflow. Browser-engine
projects are distinct from CPU-architecture emulation.

## Qualify the artifact

Validate the produced artifact, not only development source: runtime configuration, deep-link
hosting, asset/base paths, lazy chunks, security/session integration, cache/upgrade behavior,
and error states. For SvelteKit, qualify the actual adapter/server or static output. Keep
secrets and unintended source maps out of public artifacts according to project policy.

Use the project's browser matrix and targeted accessibility/visual checks at the appropriate
stage. A tested browser/host does not certify untested ones. Preserve release-consumption
artifacts through the existing GitHub workflow only when explicitly authorized.

## Close with bounded evidence

Report commands and results, artifact/build context, tested browsers/environments, and important
unrun coverage. Distinguish a ready-to-review patch from a release or deployed application.
Failed or skipped checks remain failed or skipped; do not repair the report with retries,
suppressed rules, or unreviewed baseline changes.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
