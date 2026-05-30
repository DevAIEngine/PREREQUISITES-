## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.

## 2026-05-30 - Adding aria-live and form labels for dynamic elements
**Learning:** Native HTML forms without corresponding `for` attributes on `<label>` elements fail to correctly associate for screen readers. Furthermore, dynamically populated content containers (like API result blocks) require an `aria-live` attribute (e.g. `aria-live="polite"`) so that screen readers announce the newly inserted text without stealing immediate focus.
**Action:** When adding accessible attributes to form inputs, ensure each `<label>` explicitly maps to an input ID, and use `aria-live` for asynchronously loaded message/result containers to ensure screen reader users are notified when data arrives.
