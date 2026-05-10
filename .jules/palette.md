## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-10 - Typing Dynamic ARIA Labels in TypeScript
**Learning:** When adding `aria-label` to elements with localized content in React, mapping string states directly to a translation dictionary key without explicit typing causes TypeScript compilation errors.
**Action:** Always move static translation objects outside the component and type the state using `keyof typeof translations`. Then cast the change event correctly (e.g. `e.target.value as keyof typeof translations`).
