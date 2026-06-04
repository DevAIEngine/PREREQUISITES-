## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-10-25 - Localized ARIA Labels and Live Regions
**Learning:** Dynamically populated AI chat UI requires `aria-live='polite'` on the subtitle wrapper to announce new messages without hijacking focus, and inline localized dropdowns require dynamic `aria-label` translations mapped correctly via TypeScript string literal unions to maintain strict a11y across languages.
**Action:** Always verify that dynamic content containers use `aria-live` and that multi-language selects bind their ARIA properties to the respective localized translation objects with strictly typed hooks.
