# yet-more-skills

82 focused agent skills for engineering workflows, Rust, Python/PyO3, TypeScript packages and UI work, and agent experience. Each lives in `skills/<name>/` with instructions, agent metadata, and optional references or scripts.

## Discover, preview, install

Requires Python 3.11+. Start with a focused selection, not every skill body:

```sh
python3 install.py --list --search 'rust async' --limit 5
python3 install.py --list --set python --search 'packaging' --json
python3 install.py --set workflow-lite
python3 install.py --set workflow-lite --apply
# Install one skill; preview by default:
python3 install.py --skill context-efficiency --dest /path/to/repo/.agents/skills
```

`--list` is read-only and lists all skills unless filtered with `--set` or repeatable `--skill`. `--search` further matches all whitespace-separated words as case-insensitive substrings in name, title, description, or group. It is metadata search, not semantic ranking; read the description before selecting. `--limit N` returns at most N alphabetically ordered matches and explicitly reports omissions. Search and limits require `--list` and never change installation selections.

`--list --json` emits one JSON document containing `pack` and catalog `skills`, sorted by name. With `--limit`, it also includes `total_matches` and `truncated`. An empty match is a successful empty list within the selected scope; malformed input is an error. Diagnostics use stderr. Listing does not prepare or validate the destination, so it works with existing customized skills. `--json` requires `--list`; listing cannot be combined with `--apply`.

Installation defaults to `~/.agents/skills`. Use `--dest` for a repository-specific destination or another supported discovery root. Existing skills are never overwritten: a collision stops the entire selection before copying. Choose only absent names or a separate destination. An interrupted copy may leave partial new folders. Updating this repository does not automatically refresh installed copies.

| Set | Contents |
| --- | --- |
| `workflow` | 16 planning, diagnosis, design, delivery, and review skills |
| `core` | 6 Rust core skills; default installation selection |
| `protocol`, `storage` | Rust core plus relevant specialists |
| `python-core`, `python` | Core or complete Python skills |
| `bindings`, `python-rust` | PyO3 bindings, alone or with Python skills |
| `typescript-core`, `typescript` | Core or complete original TypeScript/UI selections |
| `typescript-packages` | TypeScript contracts and package-consumer checks |
| `cross-language` | Language API skills and shared-contract verification |
| `react-ui`, `svelte-ui` | Framework-specific UI selections |
| `ui-review` | UI review specialists |
| `workflow-lite` | Grounding, evidence, diagnosis, scoping, and handoff |
| `agent-systems` | Tool boundaries and memory/context hygiene |
| `agent-experience` | Agent systems, CLI design, and collaboration UX |
| `building-systems`, `equipment-ui` | Edge/cloud sync, FDD validation, and equipment 3D UI |
| `skill-review-additions` | Seven earlier workflow/system additions |
| `engineering-additions` | Four package, cross-language, CLI, and collaboration additions |
| `full` | All 82 skills; explicit opt-in |

Existing sets retain their membership. `python-additions` and `typescript-additions` remain available. Add the efficiency specialist with `--skill context-efficiency`; no additional bundle is required. [catalog.json](catalog.json) contains names, descriptions, and invocation policies.

## Use and keep work proportional

Ask an agent to use `$skill-name`, such as `$rust-api-design`, `$typescript-package-boundaries`, `$cross-language-contracts`, or `$ui-agent-collaboration`. Choose by the actual boundary, not by loading an entire language collection. Explicit-only policies live in `agents/openai.yaml`; runtime support varies.

The Rust, Python, TypeScript, grounding, research, orchestration, memory, and handoff skills now carry more concrete scoped-reading and stopping rules. Routine work does not need to load another skill first. Use `$context-efficiency` for excessive retrieval, repeated exploration, verbose output, or a deliberate token/cost investigation. Its [recipes](skills/context-efficiency/references/recipes.md) and [research](skills/context-efficiency/references/research.md) are on-demand depth, not compulsory startup reading.

For a repository-wide default outside skill activation, an [optional instruction fragment](examples/context-policy.md) can be adapted into existing agent instructions. It is not installed automatically. Fewer reads are not permission to miss contracts, skip required checks, or silently narrow requested research. No measured end-to-end token savings are claimed.

Agents and Codebase Memory tools are optional. This repository does not install roles, tools, hooks, global configuration, or model settings. User instructions and repository policy govern scope, required gates, and authority.

## Validate

```sh
python3 -m unittest discover -s tests -v
# Authoring checks require PyYAML:
python3 tools/validate_metadata.py
python3 -m unittest discover -s tools -p 'test_*.py' -v
# Focused discovery/context-efficiency regressions:
python3 -m unittest discover -s tests -p 'test_context_efficiency.py' -v
```

Tests cover packaging, installer/discovery behavior, metadata, and the interpreter probe. [Legacy](evals/scenarios.json), [review](evals/review-scenarios.json), [engineering](evals/engineering-scenarios.json), and [context-efficiency](evals/context-efficiency-scenarios.json) scenarios remain authored, not executed model evaluations. Review cases use [the review manifest](evals/review-changed-skills.json); engineering and efficiency cases declare their reviewed skills. Legacy per-skill coverage remains incomplete. The [evaluation guide](evals/README.md) explains behavioral comparisons; [efficiency validation notes](evals/context-efficiency-checks.md) state exactly what this pass exercised.

## License

Original work is available under [MIT](LICENSE-MIT) or [Apache-2.0](LICENSE-APACHE), at your option. Existing MIT notices are retained with the seven workflow adaptations carrying upstream provenance. The installer includes license texts with each installed skill.
