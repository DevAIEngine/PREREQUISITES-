## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-14 - [Add Authentication to Compute-Heavy Endpoints]
**Vulnerability:** The `/api/v1/capture/stream` endpoint was unauthenticated, leaving the system susceptible to unauthenticated abuse of the compute-intensive Gemini Live functionality (Denial of Wallet/Service attacks).
**Learning:** Endpoints that trigger expensive external API calls (e.g., Vertex AI, Gemini Live) must always require authentication to protect system resources and billing.
**Prevention:** Implement `fastapi.security.HTTPBearer` or a similar authentication scheme to validate requests against a secure token (e.g., `GUCE_API_KEY`) before allocating compute resources.
