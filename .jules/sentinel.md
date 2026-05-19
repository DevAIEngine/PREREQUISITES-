## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-05-19 - [Missing Authentication on Compute-Intensive Endpoint]
**Vulnerability:** The `/api/v1/capture/stream` endpoint was accessible without authentication, exposing the system to denial-of-service (DoS) and abuse of downstream AI services (Gemini Live). Also lacking secure API Key validation logic.
**Learning:** Found a missing authentication check on a critical endpoint. In implementing the fix, used `secrets.compare_digest` to prevent timing attacks, and implemented strict fail-secure configuration checking (raising a 500 Internal Server Error when the `GUCE_API_KEY` environment variable is missing) instead of fail-open fallback.
**Prevention:** Always enforce `Depends(HTTPBearer())` on endpoints that trigger compute-heavy operations. Validate secrets securely via `secrets.compare_digest`, and never allow fail-open logic for critical security configurations.
