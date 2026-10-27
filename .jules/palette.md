## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-25 - [Micro-UX Interaction Refactor]
**Learning:** Legacy components (`NEXUS_LEGACY_APP.tsx`) frequently rely on inline style attributes combined with explicit Javascript event listeners (`onMouseOver`, `onFocus`, etc.). This causes conflict states (e.g. `onMouseOut` overriding `onFocus`). Attempting to use Python script replacement without idempotency checks (`if 'unique_string' not in content:`) frequently leads to appending duplicate CSS.
**Action:** Always wrap style block injections in idempotency checks to avoid unintentional duplication. Use `!important` when transitioning interaction states (like `:hover`) to CSS to successfully override inline styles on legacy elements.
