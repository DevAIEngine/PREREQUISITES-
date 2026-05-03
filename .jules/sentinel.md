## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2023-10-27 - [CRITICAL] Added Authentication to Missing `/api/v1/capture/stream` endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` did not have authentication checking. Furthermore, `hmac.compare_digest` was not being used to securely compare API keys.
**Learning:** Security dependencies such as `fastapi.security.HTTPBearer` must be applied to secure endpoints. Default settings might expose services without the user knowing.
**Prevention:** Apply `Depends(get_current_user)` parameter to sensitive endpoints and raise `500 Internal Server Error` if security keys are missing from the configuration environment to prevent insecure defaults.
