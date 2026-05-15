## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-03-24 - [Native HTML Form Accessibility Pattern]
**Learning:** Found that static HTML template forms (like `audio_cloning.html`) lacked explicit `<label for="id">` attributes and visible keyboard focus states (`focus-visible`).
**Action:** Always map labels explicitly using `for` matching the input's `id`, and apply Tailwind's `focus:outline-none focus-visible:ring-2` pattern to all interactive elements to ensure screen readers and keyboard navigation users have a smooth experience.
