## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-07-10 - Migrate Inline Events to CSS Pseudo-classes
**Learning:** When applying custom interaction styles in React components that heavily rely on inline `style={}` attributes, using inline JS events for both hover and focus creates a state conflict (e.g., `onMouseOut` reverting styles while the element is still focused). Using `!important` in injected CSS rules successfully overrides the base inline styles without requiring complete restyling.
**Action:** Prefer migrating visual interaction states to CSS pseudo-classes (e.g., `:hover`, `:focus-visible`) rather than relying on inline React event handlers.
