## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2024-05-16 - Replicating Focus Visibility in Custom Inline Styled Components
**Learning:** When applying custom interaction styles (e.g., hover styles like box-shadows) to interactive elements using React inline styles without external CSS classes, equivalent styles must be explicitly replicated in `onFocus` and `onBlur` event handlers. This ensures screen reader and keyboard-only users receive equivalent visual focus indicators.
**Action:** Always replicate `onMouseOver` or generic interactive styles to `onFocus` and `onBlur` for custom UI components lacking native or utility-class focus management.
