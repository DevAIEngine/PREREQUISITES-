## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-06-09 - Information Leakage in API Response
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` returned raw exception strings directly to the client (`str(e)`).
**Learning:** Exposing raw exceptions can leak internal infrastructure details or credentials to potential attackers.
**Prevention:** Always log exceptions securely on the server-side and return generic, sanitized error messages to the client.
