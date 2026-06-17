## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-03-20 - [Inline Hover States Missing Focus Equivalents & Silent Dynamic Content]
**Learning:** Found multiple instances where interactive elements had inline `onMouseOver` styles but lacked keyboard focus states, and dynamically populated content like chat subtitles lacked `aria-live` attributes, causing screen readers to miss updates.
**Action:** Replicated `onMouseOver`/`onMouseOut` styles in `onFocus`/`onBlur` for keyboard users, and added `aria-live="polite"` to dynamically updating UI regions like message containers.
