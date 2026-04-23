## 2026-04-21 - Prevent WCAG 2.5.3 Violations with Decorative Emojis
**Learning:** Decorative emojis in buttons or visible text can override intended screen reader labels or violate WCAG 2.5.3 (Label in Name) if not hidden. Wrapping them in `<span aria-hidden="true">`, while using fragments when mixed with text, correctly hides them from assistive tech while preserving visual appeal.
**Action:** Always wrap decorative emojis and icons in `<span aria-hidden="true">`, particularly inside interactive elements, and use `alt=""` and `aria-hidden="true"` for decorative background images.
