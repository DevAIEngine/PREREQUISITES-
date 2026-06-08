## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-06-08 - Information Leakage in API Responses
**Vulnerability:** Raw exception strings (str(e)) returned directly to the client in HTTP 500 responses.
**Learning:** Exposing internal exception details can reveal sensitive system information, infrastructure paths, or logic flaws to potential attackers.
**Prevention:** Always catch exceptions securely by logging the raw error server-side and returning a generic, sanitized error message to the client.
