## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2025-03-05 - Prevent Information Leakage in infrastructure/app.py
**Vulnerability:** The `/api/publish` endpoint returned raw exception strings `str(e)` directly to the client in 500 error responses.
**Learning:** Returning raw exception strings can leak sensitive internal system information (e.g., file paths, database schemas, or third-party API error details) to an attacker, providing reconnaissance data for further exploitation.
**Prevention:** Always log the detailed exception on the server-side using secure logging mechanisms (e.g., `app.logger.error`) and return a generic, standardized error message (e.g., "An internal server error occurred") to the client.
