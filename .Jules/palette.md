## 2024-05-19 - Added ARIA focus and label association to Director Documentary Form
**Learning:** Native HTML templates utilizing Tailwind often lack explicit label associations and focus visible states out-of-the-box, which are essential for accessibility.
**Action:** Always ensure `<label>` elements have a `for` attribute matching the `id` of their input, and apply utility classes like `focus:outline-none focus-visible:ring-2` to inputs and buttons for keyboard navigation visibility.
