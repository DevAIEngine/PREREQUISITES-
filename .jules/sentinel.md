## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-09 - [Missing Authentication on Streaming API Endpoint]
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` was completely exposed with no authentication. Anyone could initialize a live WebSocket stream and potentially abuse the Gemini Live backend and system resources without supplying a valid `GUCE_API_KEY`.
**Learning:** The streaming endpoint is the primary ingress point and its access protection was skipped. Furthermore, when verifying string-based secrets like API keys in FastAPI middleware/dependencies, standard equality (`==`) operators expose the system to timing attacks.
**Prevention:** Always secure all entry points. Ensure that when checking authentication headers against an API key, we use `hmac.compare_digest` to perform a constant-time comparison.
