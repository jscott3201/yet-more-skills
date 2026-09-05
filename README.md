# yet-more-skills

70 focused agent skills for engineering workflows, Rust, Python/PyO3, and TypeScript UI work. Each lives in `skills/<name>/` with its instructions, optional agent metadata, and supporting references or scripts.

## Install

Requires Python 3.11+. Preview first, then apply:

```sh
python3 install.py --set full
python3 install.py --set full --apply
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
| `full` | All 70 skills |

See [catalog.json](catalog.json) for names, descriptions, and invocation policies. `python-additions` and `typescript-additions` remain available for selective installation.

## Use

Ask your agent to use `$skill-name`, for example `$diagnosis-loop` or `$rust-api-design`. Choose skills for the task rather than loading the whole collection. Explicit-only invocation policies are recorded in `agents/openai.yaml`; runtime support varies.

The delivery workflow skills use named agent roles and Codebase Memory tools. They are optional and require compatible agent configuration; this repository does not install those roles or tools. Other skills can be used independently. User instructions and repository policy govern scope and authority.

## Validate

```sh
python3 -m unittest discover -s tests -v
```

Tests cover packaging, installer behavior, and the interpreter probe. The 140 prompts in [evals/scenarios.json](evals/scenarios.json) are unexecuted Rust/Python/UI evaluation cases, not proof of agent quality or runtime compatibility.

## License

Original work is available under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option. Existing MIT notices are retained with the seven workflow adaptations that carry upstream provenance. The installer includes license texts with each installed skill.
