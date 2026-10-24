## 2026-03-19 - [Fix Divs as Buttons Anti-pattern]
**Learning:** The 'Bento Box' gallery and Studio Selectors used clickable divs. This broke keyboard navigation and screen readers for core interactive components.
**Action:** Replaced interactive divs with semantic `<button>` tags, mapped existing `onMouseOver` visual hover states to `onFocus` for keyboard focus indicators, and added `aria-label`s for context.
## 2026-10-24 - [CSS Injection in JSX Template Literals]
**Learning:** When using Python string replacement to inject CSS rules into existing React JSX `<style>` tags that utilize template strings (`` {` ... `} ``), the injected CSS must strictly reside within the backticks. Placing CSS rules outside the backticks but inside the JSX tag evaluates them as JavaScript expressions, resulting in fatal syntax errors (e.g., `.studio-card:hover { ... }` causes a compiler crash).
**Action:** Always verify the exact structure of the `</style>` block and carefully target string replacements to insert new rules directly before the closing backtick (`\`} `) instead of after it.
