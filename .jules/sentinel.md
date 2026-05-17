## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2024-05-17 - [CRITICAL] Added Missing Authentication to Capture Stream Endpoint
**Vulnerability:** Missing authentication on a compute-intensive endpoint (`/api/v1/capture/stream`) that triggers video streaming and Gemini Live.
**Learning:** High-value or compute-intensive endpoints (like those triggering AI models) must be protected against abuse. FastAPI's `Depends(HTTPBearer())` provides a clean way to enforce API key presence. Crucially, verifying the API key must use `secrets.compare_digest()` to prevent timing attacks when comparing the provided token with the expected value.
**Prevention:** Always ensure endpoints that trigger expensive operations or external API calls are protected with authentication and use safe comparison methods for secrets.

## 2024-05-17 - [CRITICAL] Enforced Secure Fail-Open Prevention on API Key Check
**Vulnerability:** Implementing API key authentication with an insecure default fallback (e.g., `os.environ.get("GUCE_API_KEY", "default")`) creates a critical fail-open vulnerability if the environment variable is accidentally omitted in production.
**Learning:** Security mechanisms must fail securely. If a required security configuration (like an API key) is missing, the application must completely halt access (e.g., by raising a 500 error) rather than falling back to a known/insecure default which acts as a backdoor.
**Prevention:** When implementing API key authentication via environment variables, do not use insecure fallback defaults. Instead, strictly verify the variable exists and raise a 500 Internal Server Error if missing.
