## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-05-16 - Add Authentication to Compute-Intensive Endpoint
**Vulnerability:** Missing authentication on the sensitive `/api/v1/capture/stream` endpoint which triggers compute-intensive operations (e.g., Gemini Live, video streaming).
**Learning:** Endpoints that consume significant backend resources (tokens, compute) must be guarded against unauthenticated Denial of Service (DoS) attacks or abuse of downstream AI services. When validating tokens, using `secrets.compare_digest()` is critical to prevent timing attacks.
**Prevention:** Always use `Depends(HTTPBearer())` or a similar authentication mechanism on any endpoint that triggers compute-intensive operations. Validate keys with constant-time comparison functions like `secrets.compare_digest()`.
