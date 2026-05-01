## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-01 - explicitly map label tags and define focus states
**Learning:** Native HTML templates utilizing utility classes like Tailwind in this project (e.g., in `frontend/templates/`) lacked explicitly mapped `<label>` tags to inputs using the `for` attribute and focus states.
**Action:** Improve form accessibility by explicitly mapping `<label>` tags to inputs using the `for` attribute and applying focus states via utility classes (e.g., `focus-visible:ring-2`).
