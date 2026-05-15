## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-15 - [Add authentication to capture stream endpoint]
**Vulnerability:** The `/api/v1/capture/stream` endpoint was unauthenticated, potentially allowing unauthorized users to trigger compute-intensive operations (e.g., Gemini Live).
**Learning:** Endpoints that trigger expensive cloud operations must be secured to prevent abuse.
**Prevention:** Always use `Depends(HTTPBearer())` or similar to authenticate endpoints that trigger significant backend processing or external API calls.

## 2024-05-15 - [Mitigate timing attacks on API key verification]
**Vulnerability:** Comparing API keys using the standard `!=` operator allows attackers to potentially guess the API key by measuring the time the comparison takes (timing attack).
**Learning:** String comparisons for secrets and authentication tokens must be resistant to timing attacks.
**Prevention:** Always use `secrets.compare_digest` when comparing sensitive tokens, passwords, or API keys.
