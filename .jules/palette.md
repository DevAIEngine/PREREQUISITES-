## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-27 - Inline Interaction State Conflict Resolution
**Learning:** Using inline JS events (e.g., `onMouseOver`, `onFocus`) for both hover and focus states creates interaction conflicts (e.g., `onMouseOut` overriding an active focus state), which breaks keyboard accessibility.
**Action:** Always manage visual interaction states using CSS pseudo-classes (`:hover`, `:focus-visible`) to ensure reliable styling across both pointer and keyboard interactions.
