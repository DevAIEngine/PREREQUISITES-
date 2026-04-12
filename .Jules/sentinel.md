## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-24 - Fix missing authentication on API endpoints
**Vulnerability:** Core API endpoints like `/api/publish` lacked any authentication, allowing unauthorized users to trigger expensive operations.
**Learning:** The endpoints in `infrastructure/app.py` were missing the `require_api_key` decorator that was expected by other components (like `make_episode.sh`).
**Prevention:** Always implement authentication on API endpoints that trigger costly backend operations.
