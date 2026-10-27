## 2026-10-27 - [Migrate Inline Interaction State to CSS Pseudo-classes]
**Learning:** Using inline JavaScript event handlers (`onMouseOver`, `onFocus`, etc.) for visual interaction states creates state conflicts, especially for keyboard navigation, as mouse exit can unintentionally remove the focus style even if the element is still focused by the keyboard.
**Action:** Prefer semantic CSS pseudo-classes (`:hover`, `:focus-visible`) to handle visual interaction states for better accessibility and state management.
