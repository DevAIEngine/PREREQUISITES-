## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-01 - Missing Authentication on Capture Stream Endpoint
**Vulnerability:** The /api/v1/capture/stream endpoint was unauthenticated, exposing the core ingestion pipeline.
**Learning:** Critical endpoints should always default to a secure-by-default posture. Furthermore, if the expected API key environment variable is not present, the system should fail securely (return 500) rather than fallback to an insecure state.
**Prevention:** Apply a global or router-level HTTPBearer dependency that validates against an environment-sourced API key using constant-time comparison (hmac.compare_digest) to prevent timing attacks.
