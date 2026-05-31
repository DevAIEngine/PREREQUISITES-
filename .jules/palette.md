## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-20 - Adding ARIA Live to dynamic content blocks
**Learning:** Found a recurring pattern in the admin HTML templates where dynamic result blocks (`<div id="results">`) are populated via JavaScript after a fetch request, but lack an `aria-live` attribute. This causes screen readers to miss the results entirely when the DOM updates silently.
**Action:** When updating dynamically populated content containers in the frontend (such as API result blocks), always include an `aria-live="polite"` attribute to ensure screen readers announce the newly inserted text without stealing immediate user focus.
