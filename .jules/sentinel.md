## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-04-28 - [Add HTTPBearer Authentication to FastAPI Endpoint]
**Vulnerability:** Missing authentication on the sensitive `/api/v1/capture/stream` endpoint allowed unauthorized access, and string comparison for tokens could be subject to timing attacks.
**Learning:** Implementing `hmac.compare_digest` for token comparison is crucial to mitigate timing attacks, and we must fail securely (return 500) if the environment `GUCE_API_KEY` is not configured to avoid insecure default states.
**Prevention:** Use `HTTPBearer` and `hmac.compare_digest` for authentication flows. Ensure tests cover missing environment variables using `pytest` and `monkeypatch`.
