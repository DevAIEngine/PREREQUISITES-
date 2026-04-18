## 2024-05-20 - Inline String Emojis and Decorative Images Accessibility
**Learning:** The app's components extensively use inline string emojis and decorative background images that cause screen reader noise if left without ARIA handling.
**Action:** Ensure all decorative emojis are wrapped in `<span aria-hidden="true">` and decorative images have `alt="" aria-hidden="true"` to keep the experience intuitive and accessible.
