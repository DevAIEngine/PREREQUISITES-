## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-06-19 - Dynamic Content Screen Reader Access
**Learning:** Screen readers won't announce dynamically appended subtitles or chat messages unless the container has `aria-live`.
**Action:** Always add `aria-live="polite"` to dynamically populated content containers to ensure screen readers announce new text without stealing immediate user focus.
