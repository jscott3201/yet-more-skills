# Verified platform baseline

Baseline date: 2026-09-04. Re-check this matrix when either runtime changes.

Tested CLI versions: Codex `0.153.2`; OpenCode `1.18.23`.

| Concern | Codex | OpenCode 1.18.23 |
| --- | --- | --- |
| Shared repo discovery | `.agents/skills/<id>/SKILL.md` from the working directory toward the repository root | `.agents/skills/<id>/SKILL.md` from the working directory toward the worktree root |
| Shared user discovery | `~/.agents/skills/<id>/SKILL.md` | `~/.agents/skills/<id>/SKILL.md` |
| Required frontmatter | `name`, `description` | `name`, `description`; optional `license`, `compatibility`, string metadata |
| Codex UI metadata | `agents/openai.yaml` | Ignored |
| Explicit-only skill | `policy.allow_implicit_invocation: false` in `agents/openai.yaml` | No equivalent verified in 1.18.23; use a separate explicit command/adapter or do not expose it |
| Skill-directory symlinks | Supported | Loader traversal verified locally; avoid duplicate IDs across roots |
| Reload | Skill file changes are normally detected; config-level enable/disable requires restart | Config and discovery state are loaded per process; fully exit and relaunch after activation changes |

Primary references:

- Codex: <https://learn.chatgpt.com/docs/build-skills>
- OpenCode 1.x: <https://opencode.ai/docs/skills/>
- OpenCode configuration: <https://opencode.ai/docs/config/>

The OpenCode V2 documentation uses different config shapes and precedence. Do not apply V2 examples to a 1.18.x installation.
