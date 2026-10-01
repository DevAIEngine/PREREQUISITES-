## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-24 - Resolve Hover/Focus State Conflicts
**Learning:** In highly customized interfaces using inline React event handlers for both `onMouseOver`/`onMouseOut` and `onFocus`/`onBlur`, state conflicts occur (e.g. `onMouseOut` reverting styles while the element is still focused).
**Action:** Always migrate interactive visual states (like hover and focus) to CSS pseudo-classes (e.g., `:hover`, `:focus-visible`) and inject CSS rules using `!important` to safely override inline styles rather than managing them via component state or events.
