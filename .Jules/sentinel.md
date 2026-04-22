## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2026-04-22 - Missing Authentication on API Endpoints
**Vulnerability:** The `/api/publish` and `/api/orchestration/publish` endpoints in `infrastructure/app.py` were missing authentication, exposing them publicly and allowing unauthorized access to sensitive functionality.
**Learning:** In the GUCE architecture, Cloud Run ADC is not sufficient for app-level route protection on public services. Application-level authentication must be explicitly implemented.
**Prevention:** All sensitive endpoints must use a decorator (like `require_api_key`) to validate credentials such as an `X-API-Key` header against the `GUCE_API_KEY` environment variable using a secure time-constant comparison (`hmac.compare_digest`).
