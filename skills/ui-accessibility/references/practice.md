# A practical accessibility pass

## Dialog-based configuration

Open from the keyboard; verify the accessible name and sensible initial focus. Traverse
controls and errors, submit invalid data, open a nested picker, close it, then close the
dialog. Check focus return and that the background was not operable while the dialog was
modal. Use descriptions selectively: dumping an entire complex dialog into `aria-describedby`
can create a poor announcement even though a description technically exists.

## Operational updates

Keep freshness and quality text visible, not encoded solely in green/red. An alarm episode,
acknowledgement, suppression, and clearance should not share one ambiguous badge. Live region
announcements should convey meaningful transitions without overwhelming assistive technology
during rapid updates. Preserve the operator's current focus and reading position.

## Responsive and dense content

Test a narrow viewport, browser zoom, long equipment names, and large text. A two-dimensional
data view may need intentional scrolling, but ordinary forms/navigation should not become
unusable. Sticky controls must not obscure the currently focused item. Apply the actual
target-size and spacing criterion, including its exceptions; do not equate every desirable
touch target guideline with the same WCAG requirement.

## Automation boundaries

Automated rules detect many structural problems. They cannot determine whether a task is
understandable, the focus sequence is sensible, or a graph has an adequate alternative.
Keep automated tests as regression protection and perform focused human/browser checks for
the rest. Capture the browser, page state, and steps when reporting a failure.

## Do not fix accessibility by suppressing signals

Do not remove a label or disable a rule because a snapshot changed. Avoid positive tabindex
ordering, invisible duplicate controls, keyboard traps, and arbitrary role assignments. Fix
the semantic structure or interaction that produced the failure. Respect existing keyboard
shortcuts without stealing common browser or assistive-technology commands.

## Sources

Use documentation matching the installed version.

- [WAI modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
- [WAI combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)
- [WCAG focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
- [WCAG target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [Playwright accessibility testing limits](https://playwright.dev/docs/accessibility-testing)
