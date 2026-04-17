## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-18 - Added API Key Authentication to Publish Endpoints
**Vulnerability:** Endpoints `/api/publish` and `/api/orchestration/publish` in `infrastructure/app.py` were missing authentication, relying only on Cloud Run ADC which does not provide app-level route protection.
**Learning:** It is critical to validate `X-API-Key` headers against environment variables using `hmac.compare_digest` to prevent timing attacks, as public-facing services require application-level authentication.
**Prevention:** Always implement a `require_api_key` decorator using `hmac.compare_digest` for sensitive endpoints.
