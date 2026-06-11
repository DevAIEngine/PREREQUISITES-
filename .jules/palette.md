## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2025-02-23 - Localized ARIA Labels & Live Regions
**Learning:** Avoid hardcoding English `aria-label` attributes on elements with dynamically localized text, and include `aria-live="polite"` on dynamically populated containers like message feeds to ensure screen readers announce newly inserted text without stealing immediate focus.
**Action:** Extend the localization object with ARIA-specific keys, type them correctly in TypeScript using string literal unions outside the component to prevent 'Block-scoped variable' errors, and apply `aria-live="polite"` where dynamic content loads.
