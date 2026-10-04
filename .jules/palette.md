## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-18 - [Fix Inline Hover State Conflict]
**Learning:** Using inline React event handlers for both hover (`onMouseOver`, `onMouseOut`) and focus (`onFocus`, `onBlur`) on the same element creates a state conflict where styles get reverted improperly.
**Action:** Migrated the visual interaction states to CSS pseudo-classes (e.g. `:hover`, `:focus-visible`) and injected `<style>` blocks using `!important` to successfully override inline styles.
