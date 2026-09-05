# yet-more-skills

77 focused agent skills for engineering workflows, Rust, Python/PyO3, and TypeScript UI work. Each lives in `skills/<name>/` with its instructions, optional agent metadata, and supporting references or scripts.

## Install

Requires Python 3.11+. Select a focused set or individual skill, preview, then apply:

```sh
python3 install.py --set workflow-lite
python3 install.py --set workflow-lite --apply
# Or choose one skill:
python3 install.py --skill edge-cloud-sync --dest ~/.codex/skills
```

The destination defaults to `~/.agents/skills`. Use `--dest /path/to/repo/.agents/skills` for a repository install, or `--skill NAME` (repeatable) for individual skills. Existing skills are never overwritten; choose only absent names or a separate destination. An interrupted copy may leave partial new folders.

| Set | Contents |
| --- | --- |
| `workflow` | 16 planning, diagnosis, design, delivery, and review skills |
| `core` | 6 Rust core skills; the default selection |
| `protocol`, `storage` | Rust core plus relevant specialists |
| `python-core`, `python` | Core or complete Python skills |
| `bindings`, `python-rust` | PyO3 bindings, alone or with Python skills |
| `typescript-core`, `typescript` | Core or complete TypeScript/UI skills |
| `react-ui`, `svelte-ui` | Framework-specific UI selections |
| `ui-review` | UI review specialists |
| `workflow-lite` | Grounding, evidence, diagnosis, scoping, and handoff |
| `agent-systems` | Agent tool boundaries and memory/context hygiene |
| `building-systems`, `equipment-ui` | Edge/cloud sync and FDD validation; equipment 3D UI |
| `skill-review-additions` | All seven new workflow/system specialists |
| `full` | All 77 skills; opt in with `--set full` |

See [catalog.json](catalog.json) for names, descriptions, and invocation policies. `python-additions` and `typescript-additions` remain available for selective installation.

## Use

Ask your agent to use `$skill-name`, for example `$diagnosis-loop` or `$rust-api-design`. Choose skills for the task rather than loading the whole collection. Explicit-only invocation policies are recorded in `agents/openai.yaml`; runtime support varies.

Delivery coordination can use available agents and Codebase Memory tools when useful; neither is a prerequisite imposed by these skills. This repository does not install roles, tools, hooks, or global configuration. User instructions and repository policy govern scope, required gates, and authority.

## Validate

```sh
python3 -m unittest discover -s tests -v
# Authoring check (requires PyYAML):
python3 tools/validate_metadata.py
python3 -m unittest discover -s tools -p 'test_*.py' -v
```

Tests cover packaging, installer behavior, and the interpreter probe. [Legacy scenarios](evals/scenarios.json) and [review scenarios](evals/review-scenarios.json) remain authored, unexecuted cases, not proof of agent quality or runtime compatibility. The review cases require activation and boundary coverage for each skill listed in [the review manifest](evals/review-changed-skills.json); legacy cases do not yet provide complete per-skill coverage. See [the evaluation guide](evals/README.md) for behavioral comparisons.

## License

Original work is available under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option. Existing MIT notices are retained with the seven workflow adaptations that carry upstream provenance. The installer includes license texts with each installed skill.
