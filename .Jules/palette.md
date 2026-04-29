## 2024-04-29 - [Form Accessibility in HTML Templates]
**Learning:** Native HTML forms without explicit `<label for="...">` mapping and missing `:focus-visible` styles on interactive elements (buttons, inputs) create significant barriers for keyboard and screen-reader users, even when using utility classes like Tailwind.
**Action:** Always map labels using the `for` attribute to the input's `id`, and explicitly define `focus-visible:ring-2 focus-visible:ring-blue-500 outline-none` to ensure clear, accessible focus states across all interactive elements.
