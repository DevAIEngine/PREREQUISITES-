## 2025-04-04 - Initial Setup
**Learning:** Initializing palette journal.
**Action:** Ready to document UX learnings.

## 2025-04-04 - Hide Decorative Emojis for Screen Readers
**Learning:** When improving accessibility for buttons with visible text and decorative emojis, do not override the visible text with `aria-label` as it violates WCAG 2.5.3 (Label in Name).
**Action:** Wrap the emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name.
