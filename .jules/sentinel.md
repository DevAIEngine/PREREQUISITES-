## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-03-18 - Information Exposure in Error Responses
**Vulnerability:** The Flask `/api/publish` endpoint in `infrastructure/app.py` returned the raw exception string `str(e)` directly to the user in a JSON response when an error occurred, risking information exposure (e.g. database details or internal logic paths).
**Learning:** Returning unhandled exception messages directly to an API consumer is an anti-pattern. While debugging information is vital, it should be restricted to server-side logs.
**Prevention:** Always fail securely by catching exceptions, logging the detailed error server-side via a logging framework (`app.logger.error`), and returning a generic, safe error message to the client (e.g., 'An internal server error occurred').
