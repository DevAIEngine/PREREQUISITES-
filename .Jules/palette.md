## 2024-05-15 - Explicit Form Labels & Focus Indicators
**Learning:** Native HTML templates using Tailwind CSS (like those in `frontend/templates/`) often omit explicit `for` attributes on labels and focus states on interactive elements, relying on visual proximity instead. This degrades screen reader accessibility and keyboard navigation.
**Action:** When auditing standard HTML templates, explicitly map `<label>` tags to inputs using `for` and `id`, and always apply focus states via utility classes (e.g., `focus:outline-none focus-visible:ring-2`) to ensure full keyboard navigability.
