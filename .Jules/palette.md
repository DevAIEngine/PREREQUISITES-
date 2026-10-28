## 2024-10-28 - [Keyboard Focus Conflict with Inline Hover Styles]
**Learning:** Using inline React event handlers (like `onMouseOver` and `onFocus`) for visual interaction states creates bugs where `onMouseOut` reverts styles even if the element is still focused via keyboard, breaking accessibility.
**Action:** Always migrate interaction visual states to CSS pseudo-classes (`:hover`, `:focus-visible`) rather than relying on inline React events, using `!important` to override base inline styles if necessary.
