## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-24 - [Fix Missing Keyboard Focus Indicators]
**Learning:** When applying custom interaction styles (like background color changes on hover) using inline React event handlers (`onMouseOver` and `onMouseOut`), keyboard users miss out on those cues unless equivalent `onFocus` and `onBlur` handlers are explicitly added.
**Action:** Always replicate `onMouseOver`/`onMouseOut` logic in `onFocus`/`onBlur` when using inline style interactions to ensure visual focus indicators are present for keyboard navigation.
