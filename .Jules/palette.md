## 2026-04-14 - Wrap decorative emojis in buttons with aria-hidden
**Learning:** Emojis inside buttons can interfere with the accessible name and violate WCAG 2.5.3 (Label in Name) if they override the visible text or are read out by screen readers.
**Action:** Wrap decorative emojis in `<span aria-hidden="true">` to hide them from screen readers while preserving the accessible name. If inside a JSX expression, use React fragments `<>...</>` to avoid string syntax errors.
