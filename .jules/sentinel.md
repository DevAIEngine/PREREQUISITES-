## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-06-07 - Information Leakage in API Response
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` returned raw exception strings directly to the client (`str(e)`).
**Learning:** Exposing raw exceptions can leak internal infrastructure details or credentials to potential attackers.
**Prevention:** Always log exceptions securely on the server-side and return generic, sanitized error messages to the client.

## 2026-06-09 - Prompt Injection in Infrastructure API
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` directly embedded user-provided `transcript` data into an LLM prompt without sanitization.
**Learning:** Unsanitized user input in LLM prompts can lead to prompt injection attacks, allowing users to override system instructions.
**Prevention:** Always sanitize or strictly type user inputs before passing them into generative AI prompts.

## 2026-06-09 - Missing Input Validation in Orchestrator
**Vulnerability:** The `ProjectManifest` model in `backend/main.py` lacked strict length and pattern constraints, potentially allowing DoS via massive payloads or injection of unexpected characters.
**Learning:** FastAPI endpoints must leverage Pydantic's `Field` constraints to enforce strict boundary conditions on all incoming data.
**Prevention:** Always define `max_length`, `pattern`, and appropriate types for all user-facing Pydantic models.
