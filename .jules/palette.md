## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-07 - [Improve Form Accessibility]
**Learning:** HTML templates lacked explicit `for` attributes on `<label>` elements mapping to their corresponding input fields, and lacked visual focus indicators for keyboard navigation.
**Action:** Added `for` attributes to labels to properly link them with inputs (improving screen reader accessibility and label clickability) and applied Tailwind `focus-visible` utility classes to inputs to provide clear focus outlines for keyboard users.
