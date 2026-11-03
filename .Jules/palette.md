## 2023-11-03 - [Inline JS Event Handlers Cause React Visual Bugs]
**Learning:** Found inline javascript event handlers like onMouseOver/Out and onFocus/Blur causing style state conflicts when elements are navigated with keyboard vs mouse.
**Action:** Replace inline JS interactions with CSS pseudo classes (:hover, :focus-visible) to prevent these bugs and improve accessibility.
