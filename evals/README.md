# Behavior evaluation

The 58 scenarios in [review-scenarios.json](review-scenarios.json) are authored, not executed. They include one activation and one nearby boundary case for each of the 23 supplied skills, plus 12 cross-cutting behavior cases. Existing repository scenarios should remain in place.

## A useful first run

Start with the changed delivery coordinator, PR review loop, cross-platform authoring skill, and two new specialists relevant to the current repository. Use a clean equivalent context for the old skill and the revised skill; keep the model, settings, tools, fixture, and task scope comparable. For a newly added skill, compare against the existing collection without that skill. Make required fixture files or tool stubs available before judging the run.

An activation case asks whether the intended skill is chosen and used appropriately. A boundary case asks whether it stays out of a neighboring task. A behavior case asks what the agent actually does under misleading evidence, failure, or authority constraints. Explicit-only cases should be invoked explicitly; also test that a nearby ordinary task does not activate them automatically.

Inspect the output and relevant tool actions. Useful checks include whether code stayed in scope, required evidence was preserved, unsafe mutations were avoided, optional-tool absence was handled, and the final answer distinguished observed from unrun results. A skill-name mention alone is not a passing result.

Record the case, variant, model/settings, observed result, and a short evidence pointer in ordinary notes or an existing result format. Do not mark the source scenarios as executed merely because a structural test reads their JSON. Keep actual run outcomes separate. Repeat ambiguous routing results before treating one response as a reliable comparison.

Use time or token measurements only when genuinely collected from comparable runs. No benchmark claim from another skill repository transfers automatically to this collection.

Source: [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills).
