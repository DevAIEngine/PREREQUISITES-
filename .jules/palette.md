## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2024-06-08 - Dynamic ARIA Labels in Multilingual Components
**Learning:** Hardcoding English `aria-label` attributes on elements with dynamically localized text creates a confusing experience for non-English screen reader users.
**Action:** Extend the central localization object (e.g., `translations[language]`) with ARIA-specific keys and apply them dynamically. Ensure the localization object is declared before the hook call or outside the component, and use TypeScript's `keyof typeof translations` for the state hook to prevent compilation errors when casting event targets.
