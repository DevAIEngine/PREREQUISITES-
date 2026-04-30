## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-01 - Form Accessibility and Focus States in Tailwind Templates
**Learning:** Native HTML templates utilizing utility classes like Tailwind need explicit `<label>` mappings using the `for` attribute to inputs for screen readers to correctly interpret form fields. Focus states should also be added using utility classes (e.g., `focus-visible:ring-2`) instead of injecting custom `<style>` blocks for better accessibility.
**Action:** Always map labels to their corresponding inputs with `for` attributes and provide clear focus indicators on interactive elements.
