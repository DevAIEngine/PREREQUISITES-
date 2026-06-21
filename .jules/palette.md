## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-24 - Screen Reader Accessibility for Dynamic API Results
**Learning:** When API result blocks are dynamically populated, screen readers may miss the updates, leaving visually impaired users unaware of success or error states.
**Action:** Include `aria-live="polite"` on dynamically updated containers to ensure screen readers announce new text without stealing immediate focus.
