## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-24 - [Aria-Live on Dynamic AI Responses]
**Learning:** The Gemini Live UI dynamically updates subtitles in a flex container without screen reader announcements, causing visually impaired users to miss AI responses.
**Action:** Added `aria-live="polite"` to dynamically updated text containers to ensure screen readers announce incoming chat/subtitles without stealing immediate focus.
