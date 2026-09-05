# Component integration review

## Backends are not aliases

For a custom trigger, inspect the installed primitive's composition contract. A Radix
`asChild` example does not establish how Base UI's render composition or React Aria works.
Read local wrappers too: a copied component may intentionally expose a narrower API than the
primitive. Do not introduce two incompatible primitive families to repair one dialog.

An app-owned Sheet may be adapted from shadcn and built on Radix Dialog.
Its presence does not establish that other shadcn components or presets are installed. Preserve its explicit title, description, trigger,
and focus behavior when extracting or enhancing it.

## Forms and pending actions

Inspect whether the local Button implements a loading API; do not invent `isLoading` or
`isPending` props. Keep pending labels understandable and prevent unintended duplicate actions.
Ensure non-submit buttons inside forms have the correct type. Use native select/radio/checkbox
semantics when they fit rather than choosing a visually richer but behaviorally wrong widget.

## Controlled customization

Name the visual role before adding a token: fault severity, selected row, muted supporting
text, and destructive action are different roles. Reuse existing supported theme variables.
Retain sufficient contrast in both themes and avoid color as the only status cue.

An upstream recommendation that every page use Cards, or every option set use a ToggleGroup,
is not a domain requirement. Choose markup and interactions according to the information and
input semantics. A dense operations table should not become a wall of marketing cards.

## Registry trust

Treat a registry as a code/dependency supplier. Preview the files and changes, especially
package scripts, authentication helpers, and remote assets. Stay within configured registries
or obtain the necessary approval for new sources. Source ownership means local responsibility
for maintenance; automatic overwrite is not an upgrade strategy.

## Sources

Use documentation matching the installed version.

- [Official shadcn skills documentation](https://ui.shadcn.com/docs/skills)
- [Official shadcn skill inspected](https://github.com/shadcn-ui/ui/blob/main/skills/shadcn/SKILL.md)
- [Modal dialog interaction](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
