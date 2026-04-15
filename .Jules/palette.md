## 2026-10-27 - Hiding Emojis in Senior-Friendly Interfaces
**Learning:** Decorative emojis (like 🎥 or 📞) are frequently used in senior-friendly UIs to improve visual scannability, but they can confuse screen readers if not hidden. However, attempting to override the entire button text with an `aria-label` violates WCAG 2.5.3 (Label in Name).
**Action:** When adding decorative emojis to text labels, always wrap them in `<span aria-hidden="true">` to silence the screen reader on the emoji while preserving the native, visible text label as the accessible name.
