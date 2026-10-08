## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-08 - [Fix Interaction State Conflicts]
**Learning:** The 'Studio Selector', 'End Session', and 'Bento Box' components used inline event handlers for hover and focus states, which caused a state conflict when an element was focused but the mouse moved off it.
**Action:** Replaced inline JS event handlers with CSS pseudo-classes (`:hover` and `:focus-visible`) to handle visual states, ensuring consistent styles without conflicting interactions.
