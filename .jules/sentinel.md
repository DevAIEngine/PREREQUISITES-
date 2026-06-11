## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-06-11 - [Fix Information Leakage in Error Responses]
**Vulnerability:** The API endpoint caught exceptions and directly returned `str(e)` to the client, which could leak sensitive system information, credentials, or internal paths.
**Learning:** Returning raw exception details from `try/except` blocks to users is a security risk.
**Prevention:** Always log raw exception details securely on the server side (e.g., using `app.logger`) and return a standardized, generic error message (like "An internal server error occurred") to clients.
