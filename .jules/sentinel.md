## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-23 - Missing Authentication on Compute-Intensive Endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` lacked authentication, exposing a compute-intensive operation (Gemini Live Stream) to public access.
**Learning:** Endpoints that trigger expensive background operations (like streams or LLM models) must always be protected to prevent abuse and denial of service.
**Prevention:** Always use `Depends(HTTPBearer())` or a similar authentication mechanism on endpoints that trigger compute-intensive operations, securely verifying tokens via environment variables.
