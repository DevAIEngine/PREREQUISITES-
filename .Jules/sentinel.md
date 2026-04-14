## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2025-04-14 - Fix missing authentication on API endpoints
**Vulnerability:** The API endpoints `/api/publish` and `/api/orchestration/publish` lacked authentication, allowing unauthorized access.
**Learning:** Endpoints that trigger expensive orchestration processes must be authenticated. Cloud Run ADC is not sufficient for app-level route protection when the service allows public invocation.
**Prevention:** Implemented a custom `require_api_key` decorator using `hmac.compare_digest` to validate an `X-API-Key` header against `GUCE_API_KEY` to securely protect endpoints.
