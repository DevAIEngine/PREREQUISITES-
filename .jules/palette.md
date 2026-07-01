## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2024-07-01 - Fix keyboard accessibility focus states for React buttons
**Learning:** React inline event handlers like `onMouseOver` and `onFocus` often create visual conflicts and jarring user experiences, especially for mouse users who trigger `onFocus` when clicking.
**Action:** Always migrate interactive visual states (like hover and focus) from inline JS event handlers to CSS pseudo-classes (`:hover`, `:focus-visible`). This ensures proper keyboard accessibility and prevents conflicting visual states.
