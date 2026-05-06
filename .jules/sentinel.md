## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2025-05-06 - Sentinel Secured GUCE Streaming Endpoint 🛡️
**Vulnerability:** Missing authentication on the sensitive `/api/v1/capture/stream` endpoint in `backend/main.py`. This endpoint initializes live WebSocket/Stream connections for A-Roll and Gemini Live Scene Decomposition. Without authentication, any user could potentially trigger this endpoint, leading to unauthorized access, resource exhaustion, or abuse of the core engine.
**Learning:** The FastAPI application lacked a global or endpoint-specific security dependency for this critical entrypoint, exposing a core function of the engine.
**Prevention:** Always secure sensitive endpoints that initiate state changes or allocate resources (like stream connections) with robust authentication, such as the `HTTPBearer` dependency utilizing `hmac.compare_digest` for secure token validation against expected environment variables like `GUCE_API_KEY`.
