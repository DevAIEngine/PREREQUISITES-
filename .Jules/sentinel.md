## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-18 - [Missing API Key Authentication on Public Endpoints]
**Vulnerability:** Public Flask endpoints (/api/publish, /api/orchestration/publish) lacked application-level authentication, relying solely on Cloud Run ADC.
**Learning:** Cloud Run ADC does not protect public-facing application routes from unauthenticated HTTP requests.
**Prevention:** Always implement application-level authentication (e.g., X-API-Key with secure hmac validation) for sensitive endpoints exposed to the public internet.
