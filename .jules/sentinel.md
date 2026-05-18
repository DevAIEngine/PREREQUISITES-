## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-18 - Unauthenticated Compute-Intensive Endpoint
 **Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` was missing authentication. Because it triggers compute-intensive operations (such as streaming and Gemini Live Scene Decomposition), leaving it unauthenticated exposes the system to denial of service or abuse of downstream AI services.
 **Learning:** In FastAPI, it is easy to accidentally omit dependencies on security requirements (like `Depends(HTTPBearer())`) when adding new endpoints.
 **Prevention:** Ensure `Depends(HTTPBearer())` or a similar authentication mechanism is used on any endpoint that triggers compute-intensive operations to prevent abuse.
