## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2024-04-29 - [Missing Authentication on Core Capture Endpoint]
**Vulnerability:** The core entrypoint endpoint `/api/v1/capture/stream` in `backend/main.py` lacked any authentication, meaning any user could initialize capture streams and project state machines without proving authorization.
**Learning:** This is a severe vulnerability as it exposes a critical component of the GUCE pipeline to unauthorized access, potentially causing a Denial of Service (DoS) or leaking/maliciously injecting A-Roll data. The default FastApi structure lacked built-in HTTPBearer configurations that check standard `GUCE_API_KEY` environmental variables using secure `hmac.compare_digest` to mitigate timing attacks.
**Prevention:** Ensure that all endpoints exposed, especially those initializing core operations or WebSocket connections, are safeguarded using dependencies like `HTTPBearer` linked to required environmental token states. Also, fail securely by returning a 500 error if the secure environmental state (`GUCE_API_KEY`) is completely missing rather than allowing open access or insecure fallbacks.
