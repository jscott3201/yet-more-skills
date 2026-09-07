# yet-more-skills

81 focused agent skills for engineering workflows, Rust, Python/PyO3, TypeScript packages and UI work, and agent experience. Each lives in `skills/<name>/` with its instructions, optional agent metadata, and supporting references or scripts.

## Install

Requires Python 3.11+. Discover a focused set, preview, then apply:

```sh
python3 install.py --list --set agent-experience
python3 install.py --list --set typescript-packages --json
python3 install.py --set workflow-lite
python3 install.py --set workflow-lite --apply
# Or choose one skill:
python3 install.py --skill cross-language-contracts --dest ~/.codex/skills
```

`--list` is read-only, lists all skills by default, and accepts the same `--set` and repeatable `--skill` filters. `--list --json` emits one JSON document containing `pack` and the selected catalog `skills`, sorted by name; diagnostics use stderr. Listing does not prepare or validate an installation destination, so it also works when that destination already contains customized skills. `--json` requires `--list`, and listing cannot be combined with `--apply`.

The destination defaults to `~/.agents/skills`. Use `--dest /path/to/repo/.agents/skills` for a repository install, or `--skill NAME` (repeatable) for individual skills. Existing skills are never overwritten; choose only absent names or a separate destination. An interrupted copy may leave partial new folders. Repository updates do not refresh previously installed copies automatically.

| Set | Contents |
| --- | --- |
| `workflow` | 16 planning, diagnosis, design, delivery, and review skills |
| `core` | 6 Rust core skills; the default installation selection |
| `protocol`, `storage` | Rust core plus relevant specialists |
| `python-core`, `python` | Core or complete Python skills |
| `bindings`, `python-rust` | PyO3 bindings, alone or with Python skills |
| `typescript-core`, `typescript` | Core or complete original TypeScript/UI selections |
| `typescript-packages` | TypeScript contracts and external package-consumer checks |
| `cross-language` | Rust, Python, and TypeScript API skills plus shared-contract verification |
| `react-ui`, `svelte-ui` | Framework-specific UI selections |
| `ui-review` | UI review specialists |
| `workflow-lite` | Grounding, evidence, diagnosis, scoping, and handoff |
| `agent-systems` | Agent tool boundaries and memory/context hygiene |
| `agent-experience` | Agent systems plus CLI design and human-agent collaboration UX |
| `building-systems`, `equipment-ui` | Edge/cloud sync and FDD validation; equipment 3D UI |
| `skill-review-additions` | The seven workflow/system specialists from the earlier review |
| `engineering-additions` | The four package, cross-language, CLI, and collaboration additions |
| `full` | All 81 skills; opt in with `--set full` |

Existing selections retain their membership. `engineering-additions` is useful for adding only the four new names to an older installation; existing-name collisions still stop the entire copy. See [catalog.json](catalog.json) for names, descriptions, and invocation policies. `python-additions` and `typescript-additions` remain available for selective installation.

## Use

Ask your agent to use `$skill-name`, for example `$diagnosis-loop` or `$rust-api-design`. Choose skills for the task rather than loading the whole collection. Explicit-only invocation policies are recorded in `agents/openai.yaml`; runtime support varies.

For a TypeScript SDK that fails outside its workspace, use `$typescript-package-boundaries`. For a Rust/Python/TypeScript payload change, use `$cross-language-contracts`. For an existing command-line interface used by automation, use `$agent-cli-design`. For editable agent proposals, scoped approval, and honest cancellation/recovery in an application, use `$ui-agent-collaboration`. These are distinct boundaries, not prerequisites for ordinary edits.

Delivery coordination can use available agents and Codebase Memory tools when useful; neither is a prerequisite imposed by these skills. This repository does not install roles, tools, hooks, or global configuration. User instructions and repository policy govern scope, required gates, and authority.

## Validate

```sh
python3 -m unittest discover -s tests -v
# Authoring check (requires PyYAML):
python3 tools/validate_metadata.py
python3 -m unittest discover -s tools -p 'test_*.py' -v
```

Tests cover packaging, installer/discovery behavior, and the interpreter probe. [Legacy scenarios](evals/scenarios.json), [review scenarios](evals/review-scenarios.json), and [engineering scenarios](evals/engineering-scenarios.json) are authored, unexecuted cases, not proof of agent quality or runtime compatibility. Review cases require activation and boundary coverage for each skill in [the review manifest](evals/review-changed-skills.json); engineering cases require activation, boundary, and behavior coverage for their listed skills. Legacy cases do not yet provide complete per-skill coverage. See [the evaluation guide](evals/README.md) for behavioral comparisons and the distinction between structural tests and model execution.

## License

Original work is available under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option. Existing MIT notices are retained with the seven workflow adaptations that carry upstream provenance. The installer includes license texts with each installed skill.
