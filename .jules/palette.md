## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-20 - [Fix Interaction State Conflict]
**Learning:** Using inline JS events (`onMouseOver`, `onFocus`) for visual feedback in React creates a state conflict where blur events override hover states.
**Action:** Migrated interactive visual feedback from inline React event handlers to CSS pseudo-classes (`:hover`, `:focus-visible`) using `!important` to reliably override inline styles.
