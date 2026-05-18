## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-03-24 - [Semantic Labels & Focus States in Native Templates]
**Learning:** Native HTML templates in the accounts dashboard lacked semantic association (e.g., `for` attributes mapping to `id`s) and keyboard focus styles for inputs and buttons, leading to poor keyboard navigation and screen reader accessibility. Tailwinds default focus states on buttons don't show up unless explicitly added in these templates.
**Action:** Added `for` attributes mapping to explicit `id`s and ensured base Tailwind utility classes (`focus-visible:ring-2 focus:outline-none`) are present on interactive elements like inputs, textareas, and buttons.
