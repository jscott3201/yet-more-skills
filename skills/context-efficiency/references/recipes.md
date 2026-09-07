# Retrieval and output recipes

Use only the part that answers the present question. These are examples to adapt to the actual repository and tool contract, not mandatory commands or a replacement for required gates.

## Choose a context shape

| Task | Start with | Expand when |
| --- | --- | --- |
| Local Rust correction | Owning function, relevant types, focused regression, crate's existing command | Lifetimes, features, unsafe code, public callers, or failing tests cross that boundary |
| Python behavior fix | Owning module, affected callers, regression, relevant pyproject sections | Package origin, plugins, native conversion, worker lifetime, or packaging changes the behavior |
| TypeScript/UI correction | Component or data owner, relevant state, local tests and package scripts | Shared state, routing, tokens, generated contracts, accessibility, or browser evidence matters |
| Library-version question | Installed version and the exact official documentation section | Versions disagree, compatibility is unclear, or the contract depends on another layer |
| Broad requested review | Scope map of the requested areas, followed by bounded questions | Findings reveal dependencies or missing evidence needed for the promised review |

A semantic unit is not a fixed line count. A function body alone can omit decorators, imports, trait contracts, shared state, or comments that establish its invariants. Conversely, reading a 4,000-line file when the needed unit is already known is not automatically safer. Avoid both blind snippets and entire-repository ingestion.

## Search, select, then read

Use a provided path directly. When its location is unknown, a filename search or a symbol outline can locate it cheaply. Search for relevant references, then read a complete implicated unit with enough surrounding context. An installed language server can distinguish actual references from text matches; use ordinary search when it is unavailable.

Scope text searches to the likely package and include the actual symbol or error string. A failed search can reflect ignore rules, excluded generated code, spelling, unsupported index coverage, or the wrong scope. Adjust the relevant constraint; do not turn every search into an unbounded scan or treat zero hits as proof of absence. If several adjacent units are needed, retrieve them together rather than spending many turns rediscovering offsets.

For this repository, narrow discovery before loading a body:

```sh
python3 install.py --list --search 'rust async' --limit 5
python3 install.py --list --set python --search 'packaging' --json
python3 install.py --list --skill context-efficiency --json
```

Search matches all whitespace-separated words as case-insensitive substrings in name, title, description, or group. It is not semantic ranking; a word in an exclusion can match. Read the returned description and its scope before selecting. Results are alphabetical. With a limit, JSON reports `total_matches` and `truncated`; text states when matches were omitted. Refine the query or increase the limit when necessary. No match is an empty success within the selected metadata scope, not proof the collection cannot help.

## Keep test and log evidence intact

Prefer the repository's existing focused runner and readable failure mode. Keep selected package/test scope, test counts where available, exit status, and the decisive diagnostics. A command that selected no tests is not evidence for the intended behavior. Quiet output reduces display volume; it does not reduce how many tests executed.

For a genuinely verbose authorized command, capture output once in an allowed local artifact and inspect relevant portions. This Bash example assumes the shown test path exists in the target project:

```bash
log=$(mktemp "${TMPDIR:-/tmp}/agent-check.XXXXXX") || exit 1
if python3 -m pytest tests/test_client.py -q >"$log" 2>&1; then
  status=0
else
  status=$?
fi
printf 'exit=%s; full_log=%s\n' "$status" "$log"
printf '%s\n' 'Last 60 lines only; inspect the retained log for omitted evidence:'
tail -n 60 "$log"
exit "$status"
```

This preserves the tested command's status even under `set -e`. The excerpt is explicitly incomplete. Do not diagnose from the tail alone when the causal frame, earlier error, selected count, or setup failure lies elsewhere. The log may contain sensitive data: keep it within the authorized boundary, do not publish it automatically, and follow retention policy. Verify a recipient can access the artifact before handing off only its path.

Do not use `command | head` or `command | grep ...` as proof of success: the displayed subset and pipeline status may not establish the command's outcome. Use the host's actual status metadata or deliberately preserve it. An output reducer must preserve status and offer raw recovery; if its summary is ambiguous, inspect retained output rather than rerunning a mutation. If no artifact can be retained, request a sufficiently complete bounded result instead of discarding decisive evidence.

## UI and tool data

Return the rows or fields needed for the current decision rather than a whole API response. Use real cursor/limit semantics; preserve IDs, units, scope, missing values, quality, errors, and completion state. Apply filtering before data enters model context, through a tool's supported arguments or an authorized local computation. Parsing an entire response after printing it does not undo the input cost.

Use a targeted DOM/console/trace excerpt for a specific interaction defect. Use a rendered screenshot or browser interaction when the question is visual or behavioral; text output cannot replace that evidence. Reuse unchanged observations and capture a fresh state when the application changed. Avoid collecting every browser, viewport, trace event, and telemetry tick for a local correction, without weakening the actual test policy.
