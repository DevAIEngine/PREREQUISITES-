
## 2024-05-20 - Decorative Image Screen Reader Noise
**Learning:** Decorative background `<img>` tags without `alt` or `aria-hidden` attributes cause significant screen reader noise in cinematic applications.
**Action:** Always add `alt=""` and `aria-hidden="true"` to background images that provide no semantic value to the document.
