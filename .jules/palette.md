## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-06-07 - Localized ARIA Labels & Live Regions
**Learning:** Found an accessibility issue where ARIA labels on dynamic language toggles were missing or hardcoded in English. Additionally, dynamically inserted subtitles lacked an `aria-live` region, meaning screen readers wouldn't announce new content. Lastly, typing state hooks derived from translation keys requires extracting the translation object outside the component block to prevent TS initialization errors.
**Action:** Extend the localization object with `ariaLangSelect` keys for each language, strongly type the hook (`useState<keyof typeof translations>`), and wrap subtitle rendering areas with `aria-live="polite"` to ensure continuous, non-interruptive accessibility announcements.
