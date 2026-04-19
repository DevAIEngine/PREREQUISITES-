## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-05-20 - [Add Application-Level Authentication to Public Endpoints]
**Vulnerability:** Public API endpoints in `infrastructure/app.py` were missing application-level authentication, relying implicitly on Cloud Run ADC which does not prevent unauthorized external HTTP requests.
**Learning:** In the GUCE architecture, Cloud Run ADC is not sufficient for app-level route protection on public services; endpoints must be protected using application-level authentication like an `X-API-Key` validator.
**Prevention:** Always implement explicit authentication decorators (like `require_api_key` using `hmac.compare_digest`) on public-facing routes even when deployed in environments with service-level ADC.
