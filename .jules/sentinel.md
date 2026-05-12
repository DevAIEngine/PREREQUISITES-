## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-12 - Missing Authentication on Compute-Intensive Endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` lacked authentication, allowing any user to trigger the initialization of a compute-intensive Gemini Live WebSocket stream.
**Learning:** Endpoints that consume significant backend or downstream AI resources (e.g., LLMs, video rendering) must always be protected by robust authentication to prevent unauthenticated denial-of-service (DoS) or resource exhaustion attacks.
**Prevention:** Always apply `HTTPBearer` or similar authentication dependencies (e.g., `Depends(HTTPBearer())`) on resource-intensive API routes, validating against environment variables like `GUCE_API_KEY`.
