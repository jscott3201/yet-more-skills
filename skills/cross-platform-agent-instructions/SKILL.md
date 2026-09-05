---
name: cross-platform-agent-instructions
description: Create, review, or improve agent skills and repository instructions for Codex or another named harness. Check triggers, portability, and real behavior; not application feature work or automatic configuration deployment.
license: MIT OR Apache-2.0
metadata:
  upstream-repository: https://github.com/mattpocock/skills
  adaptation: Workflow simplification; retained upstream attribution
---

# Skill Authoring and Harness Compatibility

Maintain one clear semantic workflow and isolate harness-specific settings. A single-harness task is valid; do not require a second platform, a plugin, or a live configuration migration.

## Inspect before changing

Read the existing skill, relevant repository instructions, supported discovery roots, and installed harness documentation. Check for duplicate names and overlapping triggers. A repository catalog describes the collection; it does not automatically control what a runtime loads.

Use a required `SKILL.md` with a short name and a precise description. Front-load the real task and nearest exclusion so the trigger remains useful when a host shortens metadata. Keep decision-critical guidance in the body and link deeper examples only when needed. Add a script only for repeated deterministic work worth maintaining.

For Codex, put invocation policy and display metadata in `agents/openai.yaml`. Set explicit-only workflows accordingly. Other hosts may ignore that file; verify their equivalent or keep the workflow unexposed there. Prose saying “explicit only” is not a runtime permission boundary. Do not copy another host's command interpolation or hooks into portable instructions as though they execute everywhere.

The portable specification and a particular validator can accept different fields. Check the actual target; do not generalize one helper's validation limits into universal runtime claims. See [compatibility notes](references/platform-matrix.md).

## Improve behavior, not packaging count

Prefer updating an existing skill when the trigger and decision are the same. Add a specialist when it covers a distinct failure boundary. Keep agents, indexes, MCP servers, and browser tools optional unless the task inherently needs them; explain a truthful fallback without fabricating tool access.

Test a realistic positive trigger, a nearby non-trigger, and a difficult behavior case. Compare old versus revised skill in clean equivalent contexts. Inspect outputs and relevant tool actions, not just whether the skill activated. Record structural checks separately from model execution and never report authored cases as passed evaluations.

## Deploy within scope

Preserve licenses, attribution, unrelated skills, and user customizations. Preview installation changes; do not overwrite or enable hooks, connectors, permissions, CI, or global configuration by implication. Verify discovery in the intended runtime. Restart only when the installed host actually needs it and the action is authorized, not as a universal deployment ritual.
