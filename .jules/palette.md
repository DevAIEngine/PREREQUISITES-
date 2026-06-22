## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-06-22 - [Dynamically Appending Messages Need ARIA Live]
**Learning:** The cinematic chat interface in SeniorFriendlyGeminiUI dynamically appends text bubbles as the 'Director' speaks. Without an aria-live region, visually impaired users utilizing screen readers would be unaware of incoming messages, rendering the core Voice-to-Docu interface unusable.
**Action:** Added `aria-live="polite"` to the container wrapping the dynamically mapped messages. This ensures screen readers announce new incoming text passively without aggressively stealing immediate user focus.
