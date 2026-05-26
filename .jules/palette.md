## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-26 - Improve form accessibility and keyboard focus states
**Learning:** Explicitly map `<label>` tags to inputs using the `for` attribute and apply focus states via utility classes (e.g., `focus-visible:ring-2 focus:outline-none`) instead of injecting custom `<style>` blocks.
**Action:** Always ensure that all form fields have explicitly associated labels and all interactive elements have visible keyboard focus indicators.
