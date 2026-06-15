## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-15 - Prevent Information Leakage in API Responses
**Vulnerability:** Raw exception strings (`str(e)`) were being returned directly to the client in `infrastructure/app.py`.
**Learning:** Returning exception strings inside a JSON response can expose internal stack traces, paths, or database errors.
**Prevention:** Always log the raw error on the server side using `app.logger` and return a sanitized, standardized message to the client.
