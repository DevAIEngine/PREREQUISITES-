## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2024-03-24 - Missing Authentication on API Endpoint
**Vulnerability:** The critical `/api/v1/capture/stream` endpoint in `backend/main.py` was missing authentication, allowing unauthenticated access.
**Learning:** High-value endpoints need explicit authentication dependencies (like `fastapi.security.HTTPBearer`). Also, when comparing tokens, standard equality operators are susceptible to timing attacks, which is why `hmac.compare_digest` must be used. Additionally, if the environment variable containing the expected API key is missing, it should fail securely with a 500 status rather than allowing a bypass or arbitrary state.
**Prevention:** Use `Depends(get_current_user)` on sensitive endpoints. Always use `hmac.compare_digest` for token comparison and explicitly check that configuration secrets are populated on startup or per-request.
