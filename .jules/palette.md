## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-10-24 - Fix State Conflict in Interactive Elements
**Learning:** Using inline JS events (`onMouseOver`/`onMouseOut`/`onFocus`/`onBlur`) for both hover and focus creates state conflicts where an element can lose its focus styling if hovered out while still focused.
**Action:** Always migrate visual interaction states to CSS pseudo-classes (e.g., `:hover`, `:focus-visible`) rather than relying on inline React event handlers, especially when components heavily rely on inline styles. Use `!important` in CSS rules to override base inline styles when migrating.
