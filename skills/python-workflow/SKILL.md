---
name: python-workflow
description: "Orient a substantial Python implementation or refactor: inspect interpreter, packaging, public contracts, tests, and native boundaries. Explicit entry point; not needed for tiny edits."
license: MIT OR Apache-2.0
---

# Python Workflow

Read AGENTS.md and the relevant package before editing. Treat scripts, installed libraries, services, notebooks, and extension packages as different products. Use the configured agent roles and review rules; this skill does not create another gate.

## Establish the execution context

Start with the owning package and relevant pyproject.toml, source, test, and command definitions. Establish the interpreter and package origin when execution or an environment mismatch makes them relevant. Inspect dependency, build-backend, typing, and pytest-plugin settings as needed; locating a lockfile does not mean reading it in full. Reuse known environment facts instead of collecting every dependency or every test for each edit. Do not infer a global 3.14 minimum from one repository or assume an activated environment is the one the command uses. Expand to nested projects and Rust binding crates when the boundary crosses them.

For a mixed package, map Python orchestration -> binding -> Rust core. Keep wire parsing, durable storage, and established native invariants in their owning layer. Avoid implementing a second protocol engine in the Python wrapper. A missing tool is an explicit limitation, not permission to install globally or silently change the stack.

## Make a small, meaningful change

State the behavior to change, consumers it affects, and one useful regression case. Preserve input validation, exception types, resource ownership, cancellation, and documented output semantics. Read an existing implementation and its callers before inventing an abstraction. Prefer ordinary functions, small classes, context managers, and existing dependencies over a generic framework.

Choose only the needed specialists: python-api-typing for interfaces; python-pytest for runner selection; python-test-design for behavioral evidence; python-performance for measurement; python-async-concurrency or python-threading-workers for lifecycle work; python-packaging-environments for environments; python-data-boundaries for domain values. Use rust-python-bindings for a mixed-language change when installed, or inspect the boundary directly. No skill requires all others to be loaded.

## Validate without competing work

Reuse repository commands. Begin with changed tests and consumers, then the appropriate local gate. Check formatting and the configured type checker where relevant. Do not treat import success or compileall as behavioral validation. Report Python tests, Rust nextest/doctests, and installed-wheel checks separately.

Keep a single writer unless the existing workflow permits more. Independent readers may inspect contracts or tests while implementation proceeds. Never run competing benchmarks or rebuild the same extension in a shared environment from multiple agents. One agent owns each virtual environment and build directory during a task.

Finish with the behavior changed, commands/results, interpreter and package origin, and remaining gaps. A few paragraphs are enough; no mandatory plan file or new tracking service.

Read [orientation notes](references/orientation.md) only when the environment or scope is unclear.
