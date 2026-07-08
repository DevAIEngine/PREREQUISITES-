## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-19 - [Migrate Interaction States to CSS]
**Learning:** Using inline JS events for both hover and focus creates a state conflict (e.g., onMouseOut reverting styles while the element is still focused).
**Action:** Migrated visual interaction states to CSS pseudo-classes (:hover, :focus-visible) rather than relying on inline React event handlers.
