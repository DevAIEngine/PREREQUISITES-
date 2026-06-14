## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-06-14 - Information Leakage in API Response
**Vulnerability:** Returning the raw exception string (`str(e)`) to the client on a 500 error in the `/api/publish` endpoint in `infrastructure/app.py`.
**Learning:** Exposing raw exceptions can leak internal system details, paths, or database structures to attackers, violating the fail-secure principle.
**Prevention:** Always log the full exception on the server side using the application logger and return a standardized, generic error message (e.g., "An internal error occurred") to the client.
