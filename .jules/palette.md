## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-16 - [Migrate Inline JS Hover/Focus States to CSS]
**Learning:** Using inline JavaScript event handlers (`onMouseOver`, `onMouseOut`, `onFocus`, `onBlur`) to trigger CSS transformations creates state conflicts where an element loses focus styling while still selected via keyboard if the mouse moves away. This heavily deteriorates keyboard accessibility and focus navigation.
**Action:** Migrated interactive visual states to rely exclusively on CSS pseudo-classes (`:hover`, `:focus-visible`) within a stylesheet, ensuring seamless and robust keyboard/mouse interactions.
