## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2025-05-05 - Missing Authentication on Capture Stream Endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` lacked any authentication, leaving a critical pipeline entrypoint exposed to unauthorized access.
**Learning:** Fast API endpoints handling state initialization and data ingestion must enforce strict authentication. In secure applications, environment variables like `GUCE_API_KEY` must be validated using constant-time string comparisons (like `hmac.compare_digest`) to prevent timing attacks. Additionally, failure to configure these secrets should result in a 500 error to ensure secure defaults.
**Prevention:** Always implement `HTTPBearer` dependencies using `hmac.compare_digest` for sensitive endpoints and fail securely if required configuration is missing.
