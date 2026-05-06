## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-06 - Form Accessibility and Keyboard Focus
**Learning:** Native HTML templates utilizing Tailwind CSS need explicit label mapping (`for` attributes linked to input `id`s) for screen readers, and require explicit focus state utilities (e.g., `focus-visible:ring-2`) for adequate keyboard navigation visibility without injecting custom `<style>` blocks.
**Action:** When working on HTML templates with Tailwind, always ensure inputs have focus-visible classes applied directly and labels are natively mapped with `for` attributes.
