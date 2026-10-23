## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2023-10-24 - [Resolve Inline Hover/Focus State Conflict]
**Learning:** Using inline React events (`onMouseOver`, `onMouseOut`, `onFocus`, `onBlur`) to handle both hover and keyboard focus states creates a race condition. When a user focuses via keyboard and then moves their mouse over and off the element, `onMouseOut` reverts the style, silently stripping the visible focus indicator while the element remains focused.
**Action:** Always migrate custom visual interaction states to CSS pseudo-classes (`:hover`, `:focus-visible`) with `!important` to cleanly override inline style attributes and ensure robust accessibility for both mouse and keyboard users.
