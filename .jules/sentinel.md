## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-06-25 - Information Exposure in Exception Handling
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` returned the raw exception string directly to the client (`jsonify({'error': str(e)})`).
**Learning:** Directly exposing exception details to clients can leak sensitive system information (e.g., directory paths, configuration values, stack traces).
**Prevention:** Catch exceptions, log the raw `str(e)` securely on the server side using the application logger, and return a standardized, non-descript error message (e.g., 'An internal server error occurred') to the client.
