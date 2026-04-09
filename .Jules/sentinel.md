## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2026-04-09 - [Add missing authentication to infrastructure API endpoints]
**Vulnerability:** The API endpoints in `infrastructure/app.py` (like `/api/publish` and `/veo-studio/generate`) were completely unauthenticated, allowing anyone to trigger expensive video generation and drive operations.
**Learning:** Missing authentication on internal/orchestration endpoints can lead to significant financial loss (API token exhaustion) and unauthorized data access.
**Prevention:** Always implement authentication (e.g., API keys, OIDC) on all endpoints, even those intended for internal orchestration.
