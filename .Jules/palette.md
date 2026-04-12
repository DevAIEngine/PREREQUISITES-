## 2026-04-12 - Hide decorative emojis from screen readers
**Learning:** Overriding visible text containing emojis with `aria-label` violates WCAG 2.5.3 (Label in Name).
**Action:** Wrap decorative emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the exact visible text in the accessible name.
