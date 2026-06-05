## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-05 - Information Leakage in API Responses
**Vulnerability:** Raw exception strings (`str(e)`) were being returned directly to clients in HTTP 500 error responses in `infrastructure/app.py`.
**Learning:** This exposes internal server state, stack traces, or configuration details to external users, violating the fail securely principle.
**Prevention:** Securely log the raw error on the server side (e.g., using `app.logger.error`) and return a standardized, sanitized error message to the client.
