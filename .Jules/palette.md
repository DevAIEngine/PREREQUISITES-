## 2024-05-24 - Hide decorative emojis from screen readers
**Learning:** When improving accessibility for buttons with visible text and decorative emojis, overriding the visible text with `aria-label` violates WCAG 2.5.3 (Label in Name).
**Action:** Wrap the emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name.
