## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-14 - Add aria-live for dynamically populated content
**Learning:** Screen readers need explicit hints to announce new content arriving in dynamically populated areas (like WebSocket message feeds or AI output logs) without stealing the user's focus.
**Action:** Always add the `aria-live="polite"` attribute to containers that dynamically update their content so screen readers announce the new text automatically.
