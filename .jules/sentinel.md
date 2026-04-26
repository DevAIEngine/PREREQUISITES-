## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-04-26 - [Missing Authentication on API Stream Endpoint]
**Vulnerability:** The `/api/v1/capture/stream` endpoint was exposed without any authentication, allowing unauthorized users to trigger core capabilities and allocate resources without validation.
**Learning:** Even internal or experimental endpoints must enforce strict authentication. Not defaulting to secure access control represents a significant gap. Also, token verification must always utilize constant-time comparisons (`hmac.compare_digest`) to thwart timing attacks. Furthermore, fail securely by returning a 500 error if environment credentials are unexpectedly missing to prevent failing open.
**Prevention:** Always implement an explicit authentication layer (e.g., `FastAPI HTTPBearer` dependency) across all exposed API endpoints. Create shared dependencies so that enforcing this behavior across future endpoints is trivial.
