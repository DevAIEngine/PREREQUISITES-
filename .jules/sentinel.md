## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-13 - Information Leakage in Publish API
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` returned raw exception strings (`str(e)`) to the client when an error occurred.
**Learning:** Returning raw exception details can expose internal system state, file paths, or sensitive data to potential attackers, aiding in reconnaissance.
**Prevention:** Catch exceptions globally or locally, log the raw exception details securely on the server side using the application logger, and return a standardized, sanitized, generic error message to the client.
