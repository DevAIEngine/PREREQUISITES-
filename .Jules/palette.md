
## 2024-05-24 - [Emoji Accessibility in Buttons]
**Learning:** When improving accessibility for buttons with visible text and decorative emojis, do not override the visible text with `aria-label` as it violates WCAG 2.5.3 (Label in Name).
**Action:** Instead, wrap the emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name.
