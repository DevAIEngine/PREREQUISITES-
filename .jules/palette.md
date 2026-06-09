## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-03-25 - [SeniorFriendlyGeminiUI Accessibility Improvements]
**Learning:** Found several accessibility gaps in `SeniorFriendlyGeminiUI.tsx`, including missing aria-labels on select dropdowns without text, missing aria-live on dynamic subtitle injections, and lack of visual focus outlines for keyboard navigation (particularly problematic for seniors).
**Action:** Added `aria-label` to the language `<select>`, appended `aria-live="polite"` to the subtitle `<div/>`, mapped existing `onMouseOver` animations to `onFocus`, and applied explicit `focus-visible:outline` utility classes so elements clearly show when tabbed to.
