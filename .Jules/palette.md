## 2024-04-11 - Screen Reader Compatibility for Emoji Buttons
**Learning:** Decorative emojis in buttons with visible text cause screen readers to announce both the emoji name and the text, creating a confusing experience (e.g., "Crystal ball Tell a Story"). Overriding the text with `aria-label` violates WCAG 2.5.3 (Label in Name) as the visible text must be part of the accessible name.
**Action:** Always wrap decorative emojis inside buttons with `<span aria-hidden="true">` to preserve the visual design while ensuring the accessible name matches the visible text cleanly.
