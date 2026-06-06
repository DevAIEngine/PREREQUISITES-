## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-06-06 - [Accessible Form Inputs and Live Regions]
**Learning:** For dynamic interfaces, missing `aria-live` attributes on telemetry outputs prevents screen readers from announcing critical updates, and sliders without `for` labels or focus rings cannot be operated efficiently by keyboard users.
**Action:** Added explicit `for` associations to labels, applied Tailwind `focus-visible:outline` classes to interactive elements, and added `aria-live="polite"` to the telemetry container to ensure equitable access to benchmark results.
