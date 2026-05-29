## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2025-05-29 - Prevent Information Leakage in API Responses
**Vulnerability:** Raw exceptions (`str(e)`) were being returned directly to the client in `infrastructure/app.py` when an error occurred in the `/api/publish` endpoint.
**Learning:** This is a common pattern in rapid prototyping that can easily leak internal system states, stack traces, or other sensitive infrastructure details to malicious actors.
**Prevention:** Always log the raw exception server-side for debugging using `app.logger.error`, and return a sanitized, generic error message (like "An internal server error occurred") to the client.
