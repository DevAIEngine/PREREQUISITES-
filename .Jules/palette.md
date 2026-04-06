## 2024-04-06 - [Emoji Screen Reader Accessibility]
**Learning:** When improving accessibility for buttons with visible text and decorative emojis, do not override the visible text with `aria-label` as it violates WCAG 2.5.3 (Label in Name). Instead, wrap the emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name.
**Action:** Always use `<span aria-hidden="true">` around decorative emojis in UI buttons.
