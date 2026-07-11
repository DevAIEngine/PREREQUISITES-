## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2025-02-21 - [Secure Error Handling]
**Vulnerability:** Raw exception strings (str(e)) were being directly returned to clients in 500 API responses in infrastructure/app.py.
**Learning:** Returning raw exception details can expose internal system information, stack traces, or other sensitive data, aiding potential attackers.
**Prevention:** Always log the raw exception details server-side using a secure logger, and return a sanitized, generic error message to the client.
