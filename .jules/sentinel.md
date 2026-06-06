## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-03-20 - Information Leakage in API Responses
**Vulnerability:** Raw exception strings (`str(e)`) were being returned directly to the client in the `/api/publish` endpoint's error response.
**Learning:** Returning unhandled exception messages to clients can leak sensitive internal implementation details, such as database schemas, file paths, or third-party service errors.
**Prevention:** Always log the raw error securely on the server-side and return a standardized, sanitized error message to the client to prevent information disclosure.
