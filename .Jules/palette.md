## 2026-11-05 - [Replace Inline Interaction Handlers with CSS]
**Learning:** Using inline JavaScript event handlers (like onMouseOver and onFocus) for visual interaction states causes state conflicts and poor accessibility, especially since focus styles are often stripped when hovering out while maintaining keyboard focus.
**Action:** Always use CSS pseudo-classes (:hover, :focus-visible) instead of inline JS event handlers to ensure a predictable and accessible UI experience.
