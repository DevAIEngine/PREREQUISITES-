## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-05 - Fixing Inline Event Handlers state conflict on React Buttons
**Learning:** For components that heavily rely on inline styles with JSX (common in this app), using inline JS events like `onMouseOut` and `onFocus` creates a state conflict when an element is focused but no longer hovered.
**Action:** Always migrate these UI visual state changes to CSS pseudo-classes (`:hover` and `:focus-visible`) with `!important` to cleanly override inline style components and properly handle multi-state interactions.
