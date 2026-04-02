## 2024-04-02 - Hide decorative emojis alongside visible text in buttons
**Learning:** Overriding visible text in buttons with an `aria-label` to provide context for an emoji violates WCAG 2.5.3 (Label in Name).
**Action:** When improving accessibility for buttons with visible text and decorative emojis, wrap the emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name derived from the visible text.
