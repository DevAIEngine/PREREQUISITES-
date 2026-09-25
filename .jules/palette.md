## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-24 - Inline Event Handlers vs CSS Pseudo-classes
**Learning:** Using inline JS events (`onMouseOver`/`onMouseOut`/`onFocus`/`onBlur`) for both hover and focus creates state conflicts (e.g., `onMouseOut` reverting styles while the element is still focused).
**Action:** Migrated visual interaction states to CSS pseudo-classes (`:hover`, `:focus-visible`) with `!important` to override base inline styles.
