## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-13 - [Form Accessibility and Keyboard Focus]
**Learning:** Found multiple instances across account templates where `<label>` elements were lacking `for` attributes, resulting in unlinked form fields for screen readers. Furthermore, there was a consistent lack of keyboard focus states across interactive elements.
**Action:** Addressed these by correctly mapping label elements with `for` attributes and appending `focus:outline-none focus-visible:ring-2` base utility classes to inputs, and ensuring correct offset states (`focus-visible:ring-offset-2`) for buttons.
