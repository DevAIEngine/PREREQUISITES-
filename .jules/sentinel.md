## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-03-23 - Prevent Stack Trace Leakage in Error Responses
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` was returning the raw exception string (`str(e)`) to the client during a 500 Internal Server Error.
**Learning:** Returning raw exception details in HTTP responses can inadvertently expose sensitive infrastructure information, internal logic, or stack traces to malicious actors.
**Prevention:** Always log the full exception details internally (e.g., using `app.logger.error`) and return a sanitized, generic error message (e.g., "An internal error occurred") to the client.
