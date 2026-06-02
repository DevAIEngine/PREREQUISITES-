## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2025-02-19 - [Prevent Information Leakage in API Error Responses]
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` was directly returning raw exception strings (`str(e)`) to the client upon encountering an error (`return jsonify({'error': str(e)}), 500`). This exposes internal system details and potentially sensitive stack trace information to end-users.
**Learning:** Directly exposing raw exceptions to clients is an information leakage risk.
**Prevention:** Always log the actual raw exception securely on the backend, and return a sanitized, standardized error message (e.g., "An internal server error occurred") to the user.
