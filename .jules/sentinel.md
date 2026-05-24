## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.

## 2026-05-24 - Missing Authentication on Compute-Intensive Stream Endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint was exposed without any authentication, allowing potential unauthenticated denial-of-service or financial drain via unrestricted triggering of downstream compute-intensive operations (e.g., Gemini Live).
**Learning:** Endpoints that trigger expensive background operations must always have authentication (like `HTTPBearer`) implemented at the entry point. Furthermore, API key verification logic should be fail-secure (e.g., return a 500 status if the key is missing from the environment) rather than falling back to a default value, and should use `secrets.compare_digest` to mitigate timing attacks.
**Prevention:** Enforce an architecture rule that all stateful or compute-heavy endpoints (like those returning a streaming/websocket connection manifest) require a valid authentication token via a FastAPI `Depends()` injection. Ensure environment variables used for security verification are strictly validated upon request or application startup.

## 2026-05-24 - Information Leakage in API Error Responses
**Vulnerability:** A broad `except Exception as e` block in the `/api/publish` endpoint returned `str(e)` directly to the user in a JSON response. This exposes internal stack traces, system paths, or third-party API keys nested in errors, posing a significant information leakage risk.
**Learning:** Returning unhandled exception strings directly to clients is an insecure fail-open behavior. APIs should "fail securely" by suppressing raw error output to the external client and returning a standardized, sanitized error message (e.g., "Internal server error") while securely logging the raw trace on the server side.
**Prevention:** Implement global error handlers or strict try-catch schemas that mandate logging the exception to internal channels while stripping out dynamic error values before emitting the HTTP response.
