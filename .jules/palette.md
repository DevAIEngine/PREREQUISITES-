## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-20 - [End Session Button Accessibility]
**Learning:** The 'End Session' button used inline React events for hover states which lacked focus styles and caused invisible text due to contrast issues.
**Action:** Migrated visual interaction states to CSS pseudo-classes (`:hover`, `:focus-visible`) and added appropriate color and outline styles.
