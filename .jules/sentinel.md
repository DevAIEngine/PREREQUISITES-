## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-10 - Secure Compute-Intensive Operations

**Vulnerability:** The `/api/v1/tensor-stream/optimize` endpoint (triggering compute-intensive optimizations) lacked explicit authorization via API Gateway or within the FastAPI backend structure, leaving the backend vulnerable to denial of service attacks via malicious payloads that could exhaust GCP resources or billing.
**Learning:** Adding `Depends(HTTPBearer())` securely mandates an `Authorization` header and validates the API key on the backend side, but fails securely (raising a 500 error instead of defaulting) if the key isn't explicitly configured in the environment. Secure timing comparisons via `secrets.compare_digest` protect against timing attacks.
**Prevention:** Ensure all compute-intensive endpoints (e.g. streaming, optimizations) are strictly authenticated, avoid insecure string comparisons for secrets, and explicitly fail with a 500 Internal Server Error when server-side secret validation environment variables are missing.
