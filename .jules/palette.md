## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-03-20 - [Dynamic Subtitle Accessibility & Interactive Focus]
**Learning:** Live-updating UI elements like real-time AI conversation subtitles lacked `aria-live` attributes, causing screen readers to remain silent when new text appeared. Additionally, massive action buttons lacked proper keyboard focus indicators.
**Action:** Added `aria-live="polite"` to dynamically populated message containers so screen readers announce updates without stealing focus. Ensured all interactive buttons pair `onMouseOver`/`onMouseOut` scaling with equivalent `onFocus`/`onBlur` keyboard accessibility. Added `aria-label` to the language `<select>`.
