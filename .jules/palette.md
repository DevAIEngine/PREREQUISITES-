## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-04-28 - [Accessible Decorative Elements]
**Learning:** Discovered decorative background images and unhidden emojis causing accessibility issues for screen readers.
**Action:** Added `alt=""` and `aria-hidden="true"` to background images and wrapped decorative emojis in `<span aria-hidden="true">`, or applied it directly to their existing `<span>` elements.
