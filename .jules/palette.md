## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-25 - [Migrate Inline JS Hover to CSS Pseudo-classes]
**Learning:** Using inline React `onMouseOver` and `onMouseOut` events for hover styles causes state conflicts with keyboard focus indicators (e.g., `onMouseOut` overriding focus styles) and fails to address color contrast issues on hover.
**Action:** Migrated visual interaction states to CSS `:hover` and `:focus-visible` pseudo-classes using `!important` to override base inline styles, which successfully resolves the focus conflict and allows improving contrast (e.g., white text on red background).
