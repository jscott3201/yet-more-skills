# Harness compatibility notes

Reviewed against the sources below on September 5, 2026. Check the actual installed version before changing configuration. Documentation review is not a runtime compatibility test.

| Concern | Codex documentation baseline | Other harnesses |
| --- | --- | --- |
| Skill body | `SKILL.md` with `name` and `description`; deeper resources can be linked | Start from the Agent Skills format, then verify the host |
| Local discovery | Repository/user `.agents/skills` locations are documented | Do not assume the same roots or precedence |
| Invocation | `policy.allow_implicit_invocation: false` in `agents/openai.yaml` disables implicit use | This file may be ignored; verify a native equivalent or do not expose an explicit-only workflow |
| Changes | Automatic detection is documented; restart is a fallback when an update does not appear | No blanket process-shutdown requirement is established by this review |
| Duplicate names | Codex does not merge duplicate named installations | Verify the target's behavior; avoid shadow copies |
| Frontmatter | Validate with the actual target and the chosen authoring checks | The portable standard allows fields that particular helpers may reject |

Do not advertise OpenCode runtime testing from this table. None was performed in this review. Keep a narrow shared frontmatter subset when portability is useful, without describing one helper's field restrictions as a universal Codex rule.

Sources: [Codex skills](https://developers.openai.com/codex/skills), [Agent Skills specification](https://agentskills.io/specification), and [description guidance](https://agentskills.io/skill-creation/optimizing-descriptions).
