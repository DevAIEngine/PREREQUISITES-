## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-06-10 - Screen Reader Focus for Dynamically Updating Chat
**Learning:** When adding `aria-live="polite"` to dynamically updating message containers (like a chat interface), it ensures screen readers gracefully announce new messages without ripping the focus away from the user. Also, putting the language select ARIA label into the translations object makes it localized!
**Action:** Always add `aria-live="polite"` to chat or message output divs, and localize ARIA labels alongside the rest of the text content.
