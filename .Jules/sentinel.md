## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## YYYY-MM-DD - [Authentication Bypass on Public Endpoints]
**Vulnerability:** Missing application-level authentication on public endpoints in `infrastructure/app.py`.
**Learning:** Cloud Run ADC is not sufficient for app-level route protection on public services; endpoints must be protected using application-level authentication like an `X-API-Key` validator.
**Prevention:** Use an `X-API-Key` header populated by the `GUCE_API_KEY` environment variable and validate securely using `hmac.compare_digest` to prevent timing attacks.
