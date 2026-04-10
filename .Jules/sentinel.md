## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-05-18 - [Missing Authentication on API Endpoints]
**Vulnerability:** The infrastructure app (`infrastructure/app.py`) had several critical endpoints (like `/api/publish` and `/veo-studio/generate`) exposed without any authentication. This allowed unauthorized users to trigger expensive AI processes and create arbitrary files on Google Drive, creating a severe resource exhaustion and data integrity risk.
**Learning:** Due to the "Mini-Me" architecture, internal endpoints meant for communication between Cloud Run applications or from simple shell scripts need a robust and verified authorization layer like API Keys. Relying purely on network-level segregation (which was absent) is not enough for internet-accessible services.
**Prevention:** I implemented a `require_api_key` decorator enforcing that `X-API-Key` matches the `GUCE_API_KEY` environment variable. Moving forward, I should verify every sensitive endpoint is secured with this decorator and always use `jq` for constructing payload JSON to prevent Injection.
