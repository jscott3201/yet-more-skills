---
name: cross-platform-agent-instructions
description: Create or review shared AGENTS.md and Agent Skills for Codex and OpenCode with version-verified discovery, precise triggers, progressive disclosure, and staged config changes. Use only for dual-harness agent configuration, not application code.
license: MIT OR Apache-2.0
metadata:
  compatibility: "Codex and OpenCode; verify installed versions"
  upstream-repository: "https://github.com/mattpocock/skills"
  upstream-commit: "6654f6b60cd9d5be8b54c6fafe44346dabeb3b76"
  adaptation: "Bounded Codex/OpenCode workflow"
---

# Cross Platform Agent Instructions

Maintain one semantic source wherever the two harnesses can share it, and isolate platform syntax in thin adapters. Do not duplicate a skill body into two mutable installations.

## Verify the live platforms first

1. Resolve installed Codex/OpenCode versions and read applicable local instruction files.
2. Inspect existing discovery roots, duplicate IDs, symlinks, invocation policy, agent permissions, and config validators without exposing credentials or session records.
3. Fetch current official documentation for the exact installed generation before relying on config fields or restart behavior.
4. Preserve unrelated skills, permissions, plugins, prompts, and broken-but-unrelated links. Treat config changes as startup-sensitive.

Read [platform-matrix.md](references/platform-matrix.md) for the verified baseline used when this skill was authored. Re-verify any row that is version-sensitive.

## Author the shared semantic package

- Use one lowercase kebab-case directory per skill with a required `SKILL.md`.
- Keep portable frontmatter to `name`, `description`, `license`, and string-valued `metadata`. Store compatibility as metadata for the shared subset; Codex's validator rejects a top-level `compatibility` field even though OpenCode accepts it. Put Codex UI/invocation settings in `agents/openai.yaml`.
- Make `description` a precise trigger pointer: what the skill does, when it applies, and the nearest important exclusion.
- Keep always-needed decisions in `SKILL.md`; move branch-specific procedures and examples into linked references. Add scripts only when deterministic repeated execution earns their maintenance cost.
- State authorization boundaries in the skill that could otherwise imply edits, Git/GitHub actions, credentials, publication, or destructive work.
- Use repository-native tool and role names only in platform adapters or clearly conditional text.

For an explicit-only workflow, enforce the platform policy when supported. When a target runtime lacks explicit-only skills, do not assume a prose hint is equivalent; provide a platform command/adapter or leave the skill unexposed there.

## Stage and validate

Stage configuration-time changes outside the live config while OpenCode is running. Produce the skill directories, platform adapter or allowlist diff, deployment targets, and rollback plan. Validate every skill with the Codex validator and the installed OpenCode discovery diagnostic. Validate a modified OpenCode config with its repository validator and resolved config command before deployment.

Activate only after all OpenCode processes have exited, back up the exact live targets, deploy the validated set, and start a fresh process. A config-file approval is not authority to restart, remove unrelated skills, or overwrite another source.

Return the canonical source path, activation map per harness/agent, exact validation results, restart requirement, and unresolved compatibility claims.
