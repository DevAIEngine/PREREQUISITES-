## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-05-26 - [Information Leakage via Error Messages]
**Vulnerability:** The Flask application in `infrastructure/app.py` returned raw exception strings `str(e)` to the client in the 500 Internal Server Error response for the publish route.
**Learning:** This is a common pattern when quickly prototyping APIs, but it leaks sensitive information about the internal state of the application or the stack trace to the client. Using a broad `Exception as e` catch block compounds the issue by potentially revealing unpredictable failure modes.
**Prevention:** Always log the exception securely on the server-side using standard logging libraries (`logger.error(..., exc_info=True)`) and return a sanitized, generic error message (e.g., "An internal server error occurred.") to the client.
