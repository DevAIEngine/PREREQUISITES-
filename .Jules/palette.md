## 2026-04-24 - Accessibility of Decorative Emojis
**Learning:** Decorative emojis injected directly into text or buttons without `aria-hidden` can cause WCAG 2.5.3 (Label in Name) violations, as screen readers will attempt to read the emoji description, leading to confusing or verbose announcements.
**Action:** Always wrap decorative emojis in `<span aria-hidden="true">` to ensure they are ignored by screen readers while maintaining visual design. Ensure decorative background images have `alt=""` and `aria-hidden="true"`.
