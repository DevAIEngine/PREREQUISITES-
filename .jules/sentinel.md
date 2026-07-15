## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-07-15 - Prevented Stack Trace Leakage
**Vulnerability:** The infrastructure/app.py endpoint leaked exception details directly to the client in the API response, leading to potential info exposure.
**Learning:** Exception details must be sanitized before being returned in HTTP responses. Generic error messages avoid leaking sensitive application internals.
**Prevention:** Replace direct exposure of `str(e)` in the JSON response with standard logging (e.g. `app.logger.error`) and a generic client-facing error message.
