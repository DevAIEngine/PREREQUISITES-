## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2026-04-15 - Missing Authentication on Publish Endpoints
**Vulnerability:** Public API endpoints in `infrastructure/app.py` were fully exposed without authentication, allowing unauthorized users to trigger workflows and invoke external APIs (e.g. Gemini, Vertex AI).
**Learning:** Endpoints mapped to high-cost or sensitive generative operations must enforce app-level authorization, regardless of Cloud Run's basic IAM protections.
**Prevention:** Always implement an authentication decorator (like `require_api_key`) and use a secure comparison like `hmac.compare_digest` to protect public application-level endpoints.
