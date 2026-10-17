## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-03-24 - Unsanitized Exception Leak in Publish Endpoint
**Vulnerability:** Information leakage. The `infrastructure/app.py` directly exposed raw `Exception` strings (`str(e)`) to the client on a 500 server error, which could leak system paths, variable names, or other internal configurations.
**Learning:** Returning exception details un-sanitized in a Flask/jsonify response is an insecure pattern. It's crucial to differentiate between internal logging (which should be verbose for debugging) and client-facing error messages (which should be generic).
**Prevention:** Always log the full exception securely via `app.logger.error` on the server-side, and return a standardized, generic error string to the client.
