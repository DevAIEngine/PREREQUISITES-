## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-27 - [Fix Missing Form Label Associations and Focus States]
**Learning:** Across multiple HTML templates in the accounts directory, form `<label>` tags were missing `for` attributes linking them to their corresponding inputs (`<input>`, `<textarea>`). Additionally, the inputs lacked clear visual focus states (`focus-visible:ring-2`) for keyboard accessibility.
**Action:** Added explicit `for="[id]"` attributes to all `<label>` tags to map them to the input `id`s, and applied Tailwind `focus:outline-none focus-visible:ring-2` utility classes to the interactive elements to ensure clear keyboard focus indicators.
