## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-10-24 - Prevent Information Leakage in Vertex AI Pipeline Responses
**Vulnerability:** The infrastructure API returned raw exception strings (`str(e)`) directly to the client on error.
**Learning:** This pattern specific to the codebase exposes internal AI pipeline state and Vertex AI integration details to potential attackers, aiding in reconnaissance.
**Prevention:** Securely log the raw error on the server side using Flask's `app.logger.error` and return a standardized, sanitized error message to the client.
