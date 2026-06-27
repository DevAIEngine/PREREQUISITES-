## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-24 - [Add aria-live to subtitles output]
**Learning:** Dynamically populated content containers (like the AI output text in `SeniorFriendlyGeminiUI.tsx`) lack implicit screen reader support when updated async.
**Action:** Added `aria-live="polite"` to dynamically updating text containers to ensure smooth, non-interruptive screen reader announcements for new content.
