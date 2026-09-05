# Adapting popular design guidance to operator software

## Keep intent, remove the template assumption

Anthropic's frontend design guidance emphasizes a deliberate visual point of view. Impeccable
adds a vocabulary for critique and refinement. Apply those ideas as an intentional hierarchy
and a rendered review, not as a requirement for a new font, unusual palette, hero section,
giant metric, or elaborate animation in every feature.

An established building-operations application needs recognizable status, readable density,
consistent controls, and low-friction inspection. Existing typography and tokens are assets,
not defaults that must be replaced to prove creativity. A bold visual treatment can suit a
public marketing brief; it is not automatically appropriate for a configuration panel.

## A fault list example

Put the equipment identity and actionable condition where scanning starts. Keep operational
severity distinct from workflow priority. Show current quality/freshness and relevant timing
without making every metadata field equally prominent. Detail can open progressively, but
do not hide the evidence needed to interpret a high-risk state.

Use a table when comparison across rows is the job. Use a chart when the temporal relationship
is the job. Use a graph when connections are the job. Avoid substituting visual novelty for
the representation that makes the task easier.

## Review states, not only a hero screenshot

Capture a useful populated view, a long-label/small-viewport view, an empty or error view,
and any overlay changed by the task. Review component boundaries at real scale. Do not mask
dynamic regions indiscriminately in screenshot tests; that can hide a status regression.

## Copy

Name actions by their outcome: save configuration, acknowledge finding, open evidence, or
retry connection. Do not say “Applied” when the system has only received a request. Explain
what the user can do about a failure without leaking internal implementation details.
Preserve the domain's necessary vocabulary, but avoid placeholder jargon and decorative labels.

No new document, hooks, detector suite, registry install, or subagent panel is required for
this pass. Use tools already available and useful to the actual feature.

## Sources

Use documentation matching the installed version.

- [Anthropic frontend-design skill reviewed](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)
- [Impeccable project reviewed](https://github.com/pbakaus/impeccable)
- [shadcn project-aware guidance](https://ui.shadcn.com/docs/skills)
- [Browser screenshot testing](https://playwright.dev/docs/test-snapshots)
