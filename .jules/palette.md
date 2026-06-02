## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-06-02 - Localized ARIA Labels for Multilingual Selectors
**Learning:** Hardcoded English `aria-label` attributes on dynamically localized elements create an inconsistent screen reader experience. It is crucial to extend localization objects to include ARIA strings. When typing dynamically populated components, inferred types (like `useState<keyof typeof translations>`) must be defined outside the component to prevent TypeScript "Block-scoped variable used before its declaration" errors.
**Action:** When implementing multilingual selectors, always include ARIA labels within the existing localization object, strictly type the state to that object, and define the object prior to the component initialization.
