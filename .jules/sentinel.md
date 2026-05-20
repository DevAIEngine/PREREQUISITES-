## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2025-05-20 - [Missing Authentication on Compute-Intensive Endpoint]
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` lacked authentication. This endpoint initializes a live WebSocket/Stream connection for A-Roll and Gemini Live processing, making it vulnerable to denial of service or abuse of downstream AI services by unauthorized users.
**Learning:** Endpoints that trigger compute-heavy or expensive operations (like AI models or video processing) must be protected with authentication (e.g., `Depends(HTTPBearer())`) to prevent unauthorized usage and resource exhaustion.
**Prevention:** Always enforce authentication using `fastapi.security.HTTPBearer` and validate tokens against a securely managed environment variable (e.g., `GUCE_API_KEY`) using `secrets.compare_digest()` to prevent timing attacks. Ensure the environment variable existence is validated and fails securely (500 error) if missing.
