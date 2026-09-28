## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-03-19 - [Fix Inline Hover States in End Session Button]
**Learning:** Using inline React events (`onMouseOver`/`onMouseOut`) for hover and focus states creates conflict since JS events can fire irregularly (e.g. `onMouseOut` triggering while element is focused) and complicates focus handling for screen readers.
**Action:** Migrated inline event interactions to CSS pseudo-classes (`:hover`, `:focus-visible`) to standardize interaction and keyboard accessibility.
