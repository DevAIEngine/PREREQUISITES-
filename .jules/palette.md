## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-23 - Keyboard Focus States for Inline Hover Styles
**Learning:** Components in this application often rely on React's inline event handlers (e.g., `onMouseOver`, `onMouseOut`) to achieve hover effects instead of using standard CSS pseudo-classes (`:hover`). This approach inherently leaves out keyboard users who navigate via `Tab`.
**Action:** When working with inline hover handlers, always explicitly replicate those exact style changes in `onFocus` and `onBlur` handlers to ensure equivalent visual focus indicators are provided for accessibility.
