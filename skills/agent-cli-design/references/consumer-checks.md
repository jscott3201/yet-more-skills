# CLI consumer checks

Start with a small real interaction: discover a command, select an exact resource, inspect a result, and recover from one failure. Avoid adding a universal CLI envelope before a caller needs it.

| Case | Observable evidence |
| --- | --- |
| Help or listing with no configured destination | Exit succeeds without creating directories or attempting a write. |
| Structured success | The complete stdout value parses; descriptions remain data, not executable instructions. |
| Invalid option or missing required target | Nonzero status, useful diagnostic, no partial mutation and no misleading success payload. |
| Existing destination | Preview/apply obey the existing overwrite policy; listing still works. |
| Large or streamed response | Limits and continuation are explicit; an incomplete stream is not silently accepted as complete. |
| Cancellation after admission | Report confirmed versus uncertain effects and the supported reconciliation step. |

For a subprocess test, pass an argument list, use a temporary working directory, capture stdout and stderr separately, and set a test timeout. Account for platform differences instead of assuming POSIX signals work everywhere. Do not print secrets in failing assertion messages.

Python's subprocess API distinguishes return codes and streams; its high-level timeout behavior is not identical to every lower-level Popen operation. In Node, forcing process.exit can truncate pending output; use the documented lifecycle and an exit code when that fits the program. With Rust/clap, preserve the existing parser's help and error behavior rather than hand-parsing every failure.

Sources, checked September 7, 2026: [Python subprocess](https://docs.python.org/3/library/subprocess.html), [Node process lifecycle](https://nodejs.org/api/process.html), [clap Command](https://docs.rs/clap/latest/clap/struct.Command.html). Use documentation for the supported runtime and installed parser version.
