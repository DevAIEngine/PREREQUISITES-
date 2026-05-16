## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-16 - [Fix HTML Template Focus States and Label Bindings]
**Learning:** Native HTML templates utilizing Tailwind lacked explicit `<label for="">` bindings to inputs and had no `focus-visible` outlines, making keyboard navigation and screen reader usage difficult.
**Action:** Used standard utility classes (`focus:outline-none focus-visible:ring-2`) on interactive elements and explicitly bound labels using the `for` attribute referencing corresponding input `id`s rather than relying on custom styles.
