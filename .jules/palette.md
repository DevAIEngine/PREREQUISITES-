## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-21 - [Dynamic ARIA Labels for Multilingual UIs]
**Learning:** Hardcoding English `aria-label`s on elements with dynamically localized text is an anti-pattern that breaks the experience for international screen reader users. Furthermore, typing `useState` and `onChange` explicitly prevents TypeScript compilation errors.
**Action:** Always extend the component's localization object (`translations`) with ARIA-specific keys. Move the object outside the component block and strongly type it using `keyof typeof` to allow dynamic, accessible updates to `aria-label` attributes based on the currently selected language.
