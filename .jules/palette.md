## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-04 - [Forms A11y: Unassociated Labels & Missing Focus Indicators in Templates]
**Learning:** The native HTML templates in this app's design system omitted `for` attributes mapping to their `id`s, leaving inputs inaccessible to screen readers (since labels did not wrap the input elements). Furthermore, they lacked keyboard focus indicators.
**Action:** Added explicit `for` attributes to all form labels in the HTML templates and applied utility classes (`focus-visible:ring-2 focus-visible:outline-none focus-visible:ring-offset-2 focus-visible:ring-blue-500`) to inputs and buttons to ensure robust keyboard accessibility.
