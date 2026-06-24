## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-06-24 - Prevent Exception Information Leakage
**Vulnerability:** Raw exception strings (`str(e)`) were being returned directly to the client in the `/api/publish` endpoint error response.
**Learning:** Returning raw exception details can expose sensitive architectural information or data structures (like internal API keys, database paths, or stack traces) to malicious actors.
**Prevention:** Always log the raw exception on the server side using the application logger, and return a standardized, sanitized error message to the client.
