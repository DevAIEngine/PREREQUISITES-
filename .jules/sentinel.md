## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## $(date +%Y-%m-%d) - Prevented Information Leakage in Publishing Route
**Vulnerability:** Raw exception strings (`str(e)`) were being returned directly in 500 API responses in `infrastructure/app.py`.
**Learning:** Returning raw stack traces or exceptions to clients can leak sensitive environment details or internal architecture constraints, providing reconnaissance info to attackers.
**Prevention:** Always log raw errors securely on the server-side via standard logging frameworks and return sanitized, generic error responses to clients.
