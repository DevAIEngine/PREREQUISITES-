## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-03-18 - Information Exposure via Unhandled Exceptions
**Vulnerability:** Returning the raw exception string `str(e)` directly to the API client on error.
**Learning:** This exposes the internal application workings, stack traces, and potential file paths or database queries to external users, allowing attackers to footprint the system.
**Prevention:** Always log the full exception details on the server side (`logger.error`) and return a generic, standardized error message (e.g., 'An internal server error occurred') to the client.
