---
name: source-verification
description: Verify decision-critical external or repository claims from bounded primary evidence at a named revision, and make unresolved claims explicitly UNKNOWN.
license: MIT OR Apache-2.0
metadata:
  category: research
  phase: evidence
---

# Source Verification

Set a claim and source budget before searching. Verify only facts needed for the current decision, then stop when each claim is proven or classified `UNKNOWN`.

## Evidence contract

- Prefer official documentation, standards, release notes, source at an exact revision, and executable tests. Use secondary sources only to discover primary evidence or to document an unresolved disagreement.
- For repository implementation claims, use the supplied Codebase Memory identity and focused read tools before broad native search; check coverage before exhaustive claims and retain the exact revision. For external-only claims or personal configuration, use primary documentation or the relevant local files directly and mark the repository layer not applicable. Graph results do not establish external API behavior.
- For a PDF-only primary source, use the relevant PDF artifact skill for bounded page-aware extraction. Retain the source path or URL plus page numbers, and pass only the needed extracted evidence—not the binary artifact—to unrelated agents.
- Record the URL or path, revision or publication date, and the single claim each source supports.
- Verify version-sensitive names, signatures, limits, defaults, feature flags, deprecations, and transport-specific behavior rather than relying on memory.
- Distinguish current behavior from proposals, examples, stale releases, and interpretation.
- When reliable sources conflict, preserve the conflict and name the runtime or source check that would resolve it.
- Classify an unproven claim `UNKNOWN` with one concrete verification step. Do not fill the gap with inference.
- Return the smallest evidence excerpt needed to support the claim. Do not include raw search results, command logs, full documents, full diffs, or source dumps.

## Output

Return a bounded ledger containing only load-bearing claims:

| Claim | Classification | Primary source/revision | Evidence | Confidence | Consequence |
|---|---|---|---|---|---|

Classification is `FACT`, `INFERENCE`, `UNKNOWN`, or `RECOMMENDATION`. Link to or cite stored evidence instead of reproducing it.
