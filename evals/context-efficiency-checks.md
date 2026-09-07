# Context-efficiency validation

September 7, 2026

## Executed

`python3 -m unittest discover -s tests -p 'test_context_efficiency.py' -v`

The focused suite passed: **27 tests**. It exercises the real installer entry point in temporary fixture packs, including dedicated subprocess checks for non-interactive JSON output, process exit status, and preservation of a customized installed skill. The option matrix runs in-process to avoid repeated process-startup cost; it uses the same parser and implementation, not a replacement CLI.

Coverage includes literal case-insensitive multiword search, Unicode, set/name scoping, deduplication, filter-before-limit behavior, visible truncation, empty success, unchanged unfiltered JSON, invalid-mode failures without writes, malformed metadata, read-only discovery with existing destinations, no skill-body reads during discovery, installation references/licenses, and no-overwrite behavior. A fixture asserts reduced serialized output bytes for a filtered result; it is not a token or cost benchmark.

The suite also checks activation/boundary/behavior scenario coverage, available scenario-ID uniqueness, the changed skills' local references, and Python 3.11 syntax compatibility. Execution used **Python 3.13.5**; syntax checking does not establish execution on 3.11.

Separate local checks confirmed catalog/frontmatter/sidecar agreement for the **11 added or revised skill bodies**, preservation of the existing **81 catalog entries**, and unchanged membership of all **24 named installation sets**.

## Scope and limits

The local validation workspace was assembled from previously supplied skill archives plus current repository reads and the edited files, not a fresh full repository checkout. The focused suite uses isolated fixture packs for CLI behavior. This pass did not execute the complete existing repository suite or claim a full checkout-level metadata audit.

The **39 context-efficiency scenarios** are authored and structurally checked, not executed agent evaluations. No model A/B comparison, third-party runtime benchmark, or end-to-end token/cost reduction was measured. Rust/Python/TypeScript/browser examples describe intended use; they are not application-level test results from this repository.

Run the normal full repository checks in a complete checkout. For behavioral evidence, compare a few equivalent real tasks with the old and new instructions, counting retries and worker usage while preserving success criteria. Keep observations in ordinary notes; no new tracking service or benchmark ceremony is required.
