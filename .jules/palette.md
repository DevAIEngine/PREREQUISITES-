## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-06-01 - Dynamic API Result Blocks Screen Reader Accessibility
**Learning:** In dynamically populated content containers (like the results block in the director documentary view), screen readers fail to announce the newly inserted text by default, requiring visually impaired users to hunt for updates after submitting a request.
**Action:** When creating or updating dynamic result blocks, always ensure the container includes the `aria-live="polite"` attribute so the screen reader will naturally announce the new content without stealing focus abruptly from the user.
