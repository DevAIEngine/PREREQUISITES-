## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-05 - [Fix Disconnected Form Labels in Templates]
**Learning:** Native HTML templates styled with utility classes often lack proper semantic relationships. Here, multiple account templates had visual labels physically next to inputs but lacked the `for` attribute tying them together, breaking screen reader context. Additionally, inputs lacked keyboard focus rings.
**Action:** Explicitly map `<label>` tags to their inputs using the `for` attribute and apply focus states via utility classes (e.g., `focus-visible:ring-2`) instead of injecting custom `<style>` blocks.
