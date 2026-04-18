## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-05-15 - [Added Authentication to Sensitive Endpoints]
**Vulnerability:** Missing authentication on sensitive endpoints `/api/publish` and `/api/orchestration/publish`. Cloud Run ADC is not sufficient for app-level route protection on public services.
**Learning:** Endpoints must be protected using application-level authentication.
**Prevention:** Always add an `X-API-Key` validator logic like `hmac.compare_digest` to prevent timing attacks.
