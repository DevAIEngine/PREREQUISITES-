## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-28 - [Keyboard Focus Parity for Inline Hover Styles]
**Learning:** Found custom interaction styles (e.g., hover background colors) applied to interactive elements using inline React event handlers like `onMouseOver` and `onMouseOut` without keyboard equivalents.
**Action:** Explicitly replicated those styles in `onFocus` and `onBlur` handlers to ensure equivalent visual focus indicators for keyboard-only users.
