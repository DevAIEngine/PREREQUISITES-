## 2026-10-26 - [Fix Inline State Mutation Conflict]
**Learning:** Legacy components heavily relying on inline styles and JS event handlers (like `onMouseOver` and `onFocus`) created severe state conflicts where mouseout events would strip focus visibility from keyboard users.
**Action:** Migrated interactive visual states to robust CSS pseudo-classes (`:hover` and `:focus-visible`) injected into the component's existing `<style>` block. Used `!important` tags on injected rules to successfully override the legacy inline base styles without requiring a full structural refactor.
