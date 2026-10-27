## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-21 - Fix Focus Accessibility Bug

**Learning:** Using inline JavaScript event handlers (`onMouseOver`, `onMouseOut`, `onFocus`, `onBlur`) to handle interactive styling states on buttons often creates severe state conflicts in React. Specifically, the `onMouseOut` event triggers and reverts styling to its default state even if the element is currently focused via keyboard navigation, actively breaking accessibility and preventing visible focus rings for keyboard users.
**Action:** Always prefer using CSS pseudo-classes (`:hover` and `:focus-visible`) for interaction states instead of attaching inline component-level event listeners. When working with existing inline styles, use `!important` tags within the CSS rules to successfully override the React-injected inline styles.
