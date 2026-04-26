## 2026-04-26 - Prevent Screen Reader Emoji Duplication
**Learning:** Decorative emojis inside buttons and headers (like 📞, 🎥) caused WCAG 2.5.3 (Label in Name) violations and screen reader duplication.
**Action:** Wrapped decorative emojis in <span aria-hidden='true'> across interactive components.
