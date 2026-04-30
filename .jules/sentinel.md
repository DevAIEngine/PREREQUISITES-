## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-03-24 - Missing Authentication on Sensitive Endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint was exposed without any authentication, allowing unauthorized access to initialize core state machine capabilities.
**Learning:** Security controls like `fastapi.security.HTTPBearer` must fail securely (returning 500) if the server is misconfigured (e.g., missing API key env var), to prevent bypasses. Furthermore, using string equality for token validation opens timing attack vulnerabilities.
**Prevention:** Always secure state-modifying endpoints. Validate tokens using `hmac.compare_digest` to prevent timing attacks, and enforce secure defaults (e.g., HTTP 500 when missing `GUCE_API_KEY`).
