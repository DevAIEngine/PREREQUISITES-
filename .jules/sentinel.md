## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2024-05-18 - Prevented Information Leakage via Unsanitized Error Responses
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` returned raw exception strings (`str(e)`) in its 500 JSON response, exposing potentially sensitive internal implementation details (e.g., path structures, database schemas, API token configurations).
**Learning:** Even simple APIs intended for internal infrastructure must assume error payloads can leak to unauthorized observers. Exposing raw errors breaks the "Fail Securely" principle and can facilitate further attacks.
**Prevention:** Always log the raw `Exception` object securely server-side and return generic, sanitized error messages (e.g., "An internal error occurred during the operation") to clients.
