# Installation and discovery

[Back to the README](../README.md#quick-start)

Use the installer from the root of your `yet-more-skills` checkout with Python 3.11+. It copies selected skill folders; it does not install an agent or configure one. Preview first and choose a destination your agent actually scans.

## User-level or project-only

Without `--dest`, installation uses `~/.agents/skills`. For project-only use, set the destination explicitly. Replace the example path before running these commands; keep the quotes if your path contains spaces.

```sh
python3 install.py --set react-ui --dest "/path/to/your-project/.agents/skills"
python3 install.py --set react-ui --dest "/path/to/your-project/.agents/skills" --apply
```

Choose one installation scope to begin with. Copying a skill into this collection's own `.agents/skills` directory does not install it into a different project. Other hosts may use other discovery roots; consult their documentation rather than assuming a Codex path applies.

Select a single skill or add one to a set:

```sh
python3 install.py --skill context-efficiency
python3 install.py --set core --skill rust-async-concurrency
```

These commands only preview. Add `--apply` to copy. Repeat `--skill` to select multiple names; use at most one `--set`. Duplicate selected names are removed, but a name already present at the destination still causes a collision.

## All installation sets

Use `python3 install.py --list --set NAME` to inspect a set before installing it.

| Set | Selection |
| --- | --- |
| `workflow-lite` | Five skills for grounding, evidence, diagnosis, scoping, and handoff |
| `workflow` | Broader planning, design, coordination, delivery, and review |
| `core` | Six Rust core skills; the default when installing without a selection |
| `protocol` | Rust core plus memory, concurrency, protocol codecs, and workspace guidance |
| `storage` | Rust core plus memory, concurrency, durability, numerics, and workspace guidance |
| `python-core` / `python` | Core Python skills / the complete Python selection |
| `bindings` / `python-rust` | PyO3 binding skills / Python plus bindings |
| `typescript-core` / `typescript` | Shared TypeScript/UI foundations / the broader UI selection, including both frameworks |
| `react-ui` / `svelte-ui` | Separate framework-specific UI selections |
| `typescript-packages` | TypeScript contracts and package-consumer checks |
| `cross-language` | Rust, Python, and TypeScript API skills with shared-contract verification |
| `ui-review` | Correctness, accessibility, design, security, browser, and performance review |
| `agent-systems` / `agent-experience` | Tools and memory / those skills plus CLI and collaboration UX |
| `building-systems` | Edge/cloud synchronization and building fault-detection validation |
| `equipment-ui` | Equipment visualization with Three.js / React Three Fiber |
| `python-additions` | Python and PyO3 skills, without selecting any existing `rust-*` skill |
| `typescript-additions` | The same TypeScript/UI selection as `typescript`, retained as an add-on name |
| `skill-review-additions` | Simplification, prototypes, agent tools, memory, edge/cloud sync, fault detection, and equipment 3D |
| `engineering-additions` | CLI design, TypeScript packages, cross-language contracts, and collaboration UX |
| `full` | Every skill; opt in deliberately rather than using it as a default |

The complete descriptions and invocation policies are in [catalog.json](../catalog.json). Browse the [skill folders](../skills) to read the instructions themselves. `context-efficiency` is available individually and in `full`; it is not added to the existing named sets automatically.

## Discovery options

```sh
python3 install.py --list --search 'rust async' --limit 5
python3 install.py --list --set python --search 'packaging' --json
python3 install.py --list --skill context-efficiency --json
```

`--list` reads catalog metadata without loading skill bodies or touching the destination. Without filters it lists all skills. `--set` and repeatable `--skill` select the scope; `--search` then matches all whitespace-separated words as case-insensitive substrings across names, titles, descriptions, and groups. This is not semantic ranking: a word in an exclusion can match, so read the description.

`--limit N` returns at most N alphabetical matches and discloses omissions. With `--json`, the output is one document containing `pack` and `skills`; a limit also adds `total_matches` and `truncated`. An empty match is an empty success within the selected scope, not an error. Diagnostics go to stderr.

`--search`, `--limit`, and `--json` require `--list`. Listing cannot be combined with `--apply`, and search never changes installation selections. Run `python3 install.py --help` for the full CLI reference.

**The agent cannot find a skill?** Check that you added `--apply`, used a location that the host scans, and opened the intended project. In Codex, check `/skills`; if newly copied files still do not appear, follow the host's refresh guidance. Avoid duplicating the same skill across user and project locations just to force discovery.

**There are too many matches?** Narrow the set or search words before increasing the limit. You can also select a known name directly with `--skill`.

## Updating installed skills

Installed skills are **copies**, not live links to this checkout. Updating the repository does not update those copies, and a collision stops the whole installation selection before any copying begins.

To update, fetch the newer repository content, compare the relevant skill folders with your installed versions, and merge the changes you choose while preserving customizations and license notices. Alternatively, preview and install into a separate temporary destination for comparison. The installer has no overwrite or automatic-update mode.

An interrupted copy can leave partial new folders; inspect the destination before retrying. To remove a skill, remove only its installed folder after preserving any local changes. Keep the original collection and unrelated agent configuration intact.

## What the installer leaves alone

The installer does not change `AGENTS.md`, your agent configuration, hooks, permissions, model settings, or third-party tool installations. It copies the selected skill folders and includes the repository's MIT and Apache license texts. Preserve additional license and attribution files that accompany adapted skills.

The preview is read-only, and existing folders, files, and dangling symlinks at selected destination names are treated as collisions. Source symlinks are rejected. These are copy safeguards, not a substitute for reviewing third-party instructions and scripts before use.
