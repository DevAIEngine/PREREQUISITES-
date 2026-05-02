## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-15 - Missing Authentication on Stream Endpoint
**Vulnerability:** The `/api/v1/capture/stream` endpoint in `backend/main.py` was completely unauthenticated. It allowed arbitrary project initialization, leaving the system vulnerable to unauthorized resource creation and potential DoS.
**Learning:** Endpoints mapped directly to core orchestration state machines must have an explicit authentication dependency (e.g., `Depends(get_current_user)`) rather than assuming perimeter security.
**Prevention:** Implement `fastapi.security.HTTPBearer`, securely comparing API keys with `hmac.compare_digest` to prevent timing attacks, and enforcing strict 500 errors if the target `GUCE_API_KEY` is missing from the environment.
