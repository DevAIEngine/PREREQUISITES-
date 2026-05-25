## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-25 - Information Leakage in API Error Responses
**Vulnerability:** Information leakage due to returning raw exception strings in API responses.
**Learning:** In Flask and other frameworks, directly returning `str(e)` to the client can expose internal implementation details, stack traces, or other sensitive information, which can be useful to an attacker.
**Prevention:** Securely log the raw error on the server side (`app.logger.error`) and return a standardized, sanitized, and generic error message to the client (`{"error": "An internal server error occurred"}`).
