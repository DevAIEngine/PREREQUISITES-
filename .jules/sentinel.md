## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-05-11 - Missing Authentication on Video Capture API
**Vulnerability:** The `/api/v1/capture/stream` endpoint was accessible without authentication.
**Learning:** High-impact endpoints (e.g. streaming, capturing) can be left unauthenticated during iterative development, exposing the system to denial of service or abuse of downstream AI services.
**Prevention:** Always use `Depends(HTTPBearer())` or a similar authentication mechanism on any endpoint that triggers compute-intensive operations, such as Gemini Live, or initiates data streams.
