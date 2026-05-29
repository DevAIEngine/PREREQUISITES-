## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-29 - [Localized ARIA Labels]
**Learning:** Hardcoding English `aria-label` attributes on localized elements creates a disjointed experience for non-English screen reader users.
**Action:** Extend the translation object with ARIA-specific strings and use `keyof typeof translations` to strictly type the state and dynamically update the `aria-label` alongside the visual text.
