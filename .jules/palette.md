## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-06-05 - [Accessible Focus States for Custom Hover Styles]
**Learning:** Custom inline hover styles (like `onMouseOver`) exclude keyboard users from receiving the same visual feedback.
**Action:** Replicated `onMouseOver`/`onMouseOut` inline background colors to `onFocus`/`onBlur` handlers for equivalent keyboard focus indicators on interactive elements.
