## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-24 - [Fix Inline JS Hover/Focus State Conflict]
**Learning:** Using inline React event handlers (`onMouseOver`, `onFocus`, etc.) for hover and focus states caused a state conflict where `onMouseOut` reverted styles while the element was still focused via keyboard, leading to poor keyboard accessibility.
**Action:** Migrated visual interaction states to CSS pseudo-classes (`:hover`, `:focus-visible`) with `!important` to override base inline styles, ensuring robust and accessible interaction states without conflicts.
