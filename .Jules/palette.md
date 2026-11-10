## 2024-11-10 - Refactoring interaction states to CSS with !important in inline styles

**Learning:** When refactoring inline JavaScript interaction states (e.g., `onMouseOver`, `onFocus`) to CSS pseudo-classes on elements that use React inline `style={{...}}` attributes, you must apply the `!important` flag to the new CSS properties to successfully override the static inline styles.

**Action:** Always include `!important` when injecting CSS pseudo-classes to override inline style attributes in React.
