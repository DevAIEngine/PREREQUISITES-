## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-05-17 - Dynamic Localized ARIA Labels
**Learning:** Hardcoding English `aria-label` attributes on elements with dynamically localized text creates an inaccessible experience for non-English screen reader users. Furthermore, to dynamically look up these labels without type warnings, the localization dictionary must be strongly typed (e.g., using `useState<keyof typeof translations>`), which requires moving the object outside the React component or declaring its type before the hook.
**Action:** Always extend the main localization object with ARIA-specific keys and use `keyof typeof` typing to safely inject language-specific `aria-label`s onto buttons and inputs.
