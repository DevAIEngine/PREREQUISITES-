## 2024-05-24 - Hiding Decorative Emojis for Senior Users
**Learning:** Screen readers reading decorative emojis (like 📞 or 🎥) creates confusing and noisy output for senior users navigating complex interfaces.
**Action:** Always wrap decorative emojis in a `<span aria-hidden="true">` when they are used alongside visible text labels (like "ANSWER CALL").
