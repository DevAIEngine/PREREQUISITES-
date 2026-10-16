1. **Migrate visual interaction states to CSS**
   - Replace inline JS event handlers (`onMouseOver`, `onMouseOut`, `onFocus`, `onBlur`) on interactive elements (Studio Selectors, Bento Box buttons, End Session button) with semantic CSS pseudo-classes (`:hover`, `:focus-visible`). This avoids state conflicts where `onMouseOut` reverts styling while the element is still focused.
   - Inject the corresponding CSS rules using `!important` to reliably override the base inline `style={}` attributes.
2. **Verify modification**
   - Run `grep` to verify the CSS injection and the removal of the inline event handlers.
3. **Frontend verification**
   - Since a React component was modified, run Playwright verification to ensure it renders without syntax errors.
   - Install `playwright` locally using `pnpm`.
   - Create `verify.html` and `verify.js`.
   - Run verification and check the result.
   - Clean up ad-hoc artifacts (Playwright, temporary scripts).
4. **Complete pre-commit steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
5. **Submit the PR**
   - Use the submit tool with a descriptive commit message explaining the UX improvement.
