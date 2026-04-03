## 2025-05-15 - [Accessibility: Emojis and Text in Buttons]
**Learning:** When combining emojis and visible text in buttons, do not override the visible text with `aria-label` as it violates WCAG 2.5.3 (Label in Name). Screen readers may fail to announce the visible text.
**Action:** Wrap decorative emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name derived from the visible text.
