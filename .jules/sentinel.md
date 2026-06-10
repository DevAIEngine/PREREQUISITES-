## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-03-18 - Information Leakage via Exception Messages
**Vulnerability:** Raw exception strings (`str(e)`) were returned to clients in API responses on 500 Internal Server Errors.
**Learning:** Returning raw exception data can leak sensitive system architecture, database configurations, or third-party API details to end-users or attackers.
**Prevention:** Always log the full exception stack trace securely on the server side, and return a standardized, sanitized error message (e.g., "An internal server error occurred") to clients.
