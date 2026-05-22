## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-22 - [Missing Authentication on Compute-Intensive Endpoint]
**Vulnerability:** The `/api/v1/capture/stream` endpoint, which initiates compute-heavy operations (e.g., A-Roll capture and Gemini Live streaming), lacked authentication, exposing it to unauthorized access and potential denial-of-service/financial abuse.
**Learning:** High-impact endpoints must always have explicit authentication checks. The application also lacked a check for missing environment variables, defaulting to a fail-open or error state that could leak information or cause unexpected behavior.
**Prevention:** Added `HTTPBearer` authentication. Implemented a strict check for the `GUCE_API_KEY` environment variable that raises a 500 error if missing (fail-secure). Used `secrets.compare_digest()` to prevent timing attacks during key validation.
