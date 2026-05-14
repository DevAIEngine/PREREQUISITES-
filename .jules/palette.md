## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-14 - Dynamic ARIA Labels for Localized Components
**Learning:** Hardcoding English ARIA labels on elements with dynamically localized text breaks accessibility. We must extend localization objects with ARIA-specific keys and use proper TypeScript typing (`keyof typeof`) to map them.
**Action:** Always include ARIA attributes in localization dictionaries and utilize TypeScript generics/type casting for dynamically updated labels to prevent type warnings.
