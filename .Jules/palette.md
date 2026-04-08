## 2024-05-18 - Accessibility: Decorative Emojis in Buttons
**Learning:** Overriding visible text with `aria-label` when buttons contain emojis violates WCAG 2.5.3 (Label in Name) by breaking the connection between visible text and screen reader announcement.
**Action:** Always wrap decorative emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible visible text.
