## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-24 - [Fix Inline State Conflicts on Interactive Elements]
**Learning:** Using inline JS events for both hover (`onMouseOver`) and focus (`onFocus`) creates a state conflict where `onMouseOut` reverts visual styles even while the element remains focused via keyboard navigation, negatively impacting accessibility.
**Action:** Migrated visual interaction states from inline JS event handlers to CSS pseudo-classes (`:hover` and `:focus-visible`) using `!important` to override existing inline styles and ensure consistent visual feedback for both pointer and keyboard interactions.
