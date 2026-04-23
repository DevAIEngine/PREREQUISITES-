## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-05-24 - Missing Authentication on Capture Stream Endpoint
**Vulnerability:** The highly sensitive `/api/v1/capture/stream` endpoint was unauthenticated, potentially allowing unauthorized streaming capture sessions.
**Learning:** We need to ensure that FastAPI endpoints handling sensitive actions like streaming use standard authentication procedures (e.g. `HTTPBearer`) correctly validated against backend authorization keys (such as `GUCE_API_KEY`).
**Prevention:** Always implement `HTTPBearer` with proper environment-backed validation for sensitive API endpoints instead of assuming environment-level ADC protections.
