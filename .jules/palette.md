## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-10-02 - Migrate JS interaction events to CSS pseudo-classes
**Learning:** Using inline JS events (`onMouseOver`, `onFocus`) for visual states creates conflicts when a focused element is unhovered.
**Action:** Always prefer CSS pseudo-classes (`:hover`, `:focus-visible`) with `!important` to override inline styles and correctly handle interaction states without JS conflict, improving accessibility.
