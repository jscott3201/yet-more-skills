---
name: ui-design-review
description: Design, polish, or critique a product UI with deliberate hierarchy, typography, layout, states, and responsive behavior. Explicit design pass; preserve established product tokens unless change is requested.
license: MIT OR Apache-2.0
---
# UI Design and Visual Review

## Ground the screen in its job

Read the brief, existing screen, shared tokens, neighboring components, and real content shape.
Determine what the operator needs to notice, understand, and do next. For an existing product,
visual consistency and clarity usually matter more than inventing a new identity. Do not
turn a workbench into a landing-page hero because a design skill prioritizes novelty.

For genuinely new visual direction, make a compact choice about hierarchy, density, typography,
and palette, then implement it. Do not create a separate design system document or mandatory
planning artifact unless requested. Respect explicit user aesthetics over generic preferences.

## Design all meaningful states

Work with realistic long names, counts, timestamps, units, and permission states. Include loading,
empty, error, unavailable, stale, selected, disabled, and pending outcomes as applicable. Use
concise action labels and specific recoverable errors. Do not invent business metrics or
customer evidence to make a mock screen look populated; label illustrative data clearly.

Use spacing and type to establish hierarchy. Reserve emphasis for the primary task and
meaningful status. Avoid decorating every datum as a card, hiding important controls in
tooltips, or using color alone for operational meaning. Motion should explain a transition,
respect reduced motion, and not compete with live data.

## Walk through a real task

Choose a representative task with a clear start and observable finish. Check whether the user can find the next action, understand the consequence, recognize completion, and recover from one realistic error without losing useful work. Repeated backtracking, hidden prerequisites, and unclear outcomes matter more than cosmetic novelty.

Keep inspection findings separate from usability evidence. A source or browser walkthrough can suggest a problem; it does not prove a measured improvement in task success or speed. Use realistic localized content and narrow layouts when those are supported, rather than evaluating only ideal short English labels.

## Implement, inspect, refine

Reuse framework-specific shadcn/local components. Inspect the rendered result when browser
tools are available: desktop and narrow view, both supported themes, long content, open
overlays, and failure states. Check alignment, overflow, contrast, focus visibility, and
text hierarchy. A screenshot alone does not prove interaction behavior.

Make a focused refinement pass and explain only consequential design decisions. Without a
rendered browser, report a source-level design review and leave visual validation explicitly
unrun. Do not claim pixel-perfect output or accessibility conformance from code inspection.

## Further guidance

Read [practice notes and sources](references/practice.md) only when the task needs more depth.
