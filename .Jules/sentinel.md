## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2026-09-27 - [Fix Information Leakage in API Response]
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` was exposing raw exception messages (`str(e)`) directly to the client via JSON responses on 500 errors.
**Learning:** Exposing raw exceptions to the client can leak sensitive internal system state or infrastructure details, creating an information disclosure vulnerability.
**Prevention:** Always catch exceptions, log the detailed error server-side for debugging, and return a generic, sanitized error message to the client.
