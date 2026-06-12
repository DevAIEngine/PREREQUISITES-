## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-06-12 - Inline React Focus Styles
**Learning:** When applying custom interaction styles (like hover background colors) using inline React event handlers (`onMouseOver`/`onMouseOut`), those styles aren't automatically applied to keyboard focus states.
**Action:** Always explicitly replicate those styles in `onFocus` and `onBlur` handlers to ensure equivalent visual focus indicators for keyboard-only users.
