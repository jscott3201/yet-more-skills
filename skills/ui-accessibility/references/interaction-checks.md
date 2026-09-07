# Focus and non-dragging interactions

Focus visibility and focus not being obscured are related but different checks. Tab to controls while sticky headers, footers, drawers, and overlays are present. Under WCAG 2.2's Focus Not Obscured (Minimum), a focused component must not be entirely hidden by author-created content, subject to the criterion's notes. Keeping the focused control comfortably visible is a useful design goal beyond that minimum.

For dragging, test keyboard access and a single-pointer method without dragging separately. Keyboard reordering alone does not establish the latter. Examples include move-up/down buttons, choosing a destination from a menu, or selecting two endpoints to connect graph nodes. The alternative must perform the same relevant task, not merely display an inaccessible result.

Test at realistic zoom and narrow sizes. Keep focus on the moved item or an appropriate successor, announce the meaningful result, and ensure pointer alternatives have understandable names. Do not declare full conformance from these two checks.

Sources, checked September 7, 2026: [Focus Not Obscured (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), [Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html), [WCAG 2.2](https://www.w3.org/TR/WCAG22/).
