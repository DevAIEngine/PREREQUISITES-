## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-07-04 - Fixing State Conflicts on Interactive Elements
**Learning:** Using inline JavaScript event handlers (like `onMouseOver` and `onFocus`) alongside inline styles for hover and focus states creates bugs. For example, if an element is focused using the keyboard and then hovered/unhovered with a mouse, the `onMouseOut` event triggers, removing the styles even while the element is still focused.
**Action:** Always migrate visual interaction states from inline JS to CSS pseudo-classes (e.g., `:hover`, `:focus-visible`) to avoid state conflicts and improve both accessibility and UI consistency.
