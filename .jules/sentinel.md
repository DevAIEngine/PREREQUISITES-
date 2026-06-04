## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-04 - Prevented Information Leakage via Raw Exception
**Vulnerability:** Raw exception strings (`str(e)`) were being returned directly to the client in HTTP 500 API responses.
**Learning:** Returning raw exceptions can inadvertently expose sensitive internal system details, such as file paths, database schemas, or third-party service configurations.
**Prevention:** Always log the raw exception on the server side securely and return a standardized, sanitized error message (e.g., "An internal error occurred") to the client.
