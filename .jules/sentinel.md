## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-13 - Missing Authentication on Compute-Intensive Endpoint
 **Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` was missing authentication.
 **Learning:** Endpoints that trigger compute-intensive downstream AI services (like Gemini Live or video streaming) must be protected with authentication to prevent Denial of Service (DoS) or abuse.
 **Prevention:** Always use `Depends(HTTPBearer())` or a similar authentication mechanism on any endpoint that triggers compute-intensive operations.
