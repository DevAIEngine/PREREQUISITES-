## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-06-15 - Equivalent Visual Focus Indicators
**Learning:** When using inline React event handlers like `onMouseOver` for custom hover styles, keyboard users lose vital interactive feedback if not replicated.
**Action:** Always mirror `onMouseOver` and `onMouseOut` inline styles with identical `onFocus` and `onBlur` handlers to preserve keyboard accessibility.
