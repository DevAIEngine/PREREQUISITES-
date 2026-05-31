## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-31 - Prevent Information Leakage in Publish API
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` returned the raw exception string `str(e)` directly in the JSON response payload.
**Learning:** Exposing raw exception strings can leak sensitive internal state, stack traces, or configuration details to malicious actors querying the API, which violates the "Fail securely" principle.
**Prevention:** Always log the full exception string to internal server logs (`app.logger.error()`) for debugging purposes, but return a sanitized, generic error message (e.g., "An internal server error occurred") to the API client.
