## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2024-05-21 - [Secure Compute-Intensive Endpoint Auth]
**Vulnerability:** The compute-intensive `/api/v1/capture/stream` endpoint was exposed without any authentication, leaving it open to potential abuse, unmetered AI usage, and DoS.
**Learning:** Found that security was completely missing for the endpoint responsible for initiating streaming and AI decomposition.
**Prevention:** Implementing `fastapi.security.HTTPBearer` along with `secrets.compare_digest` to prevent timing attacks, and ensuring a fail-secure fallback (HTTP 500) if the configured expected token is missing entirely.
