## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2025-04-05 - [MEDIUM] Fix unhandled exceptions in /veo-studio/generate-scenes
**Vulnerability:** The `/veo-studio/generate-scenes` endpoint directly accessed keys from `request.json` without verifying if the payload was a dictionary, or if required keys like `scenes` and `duration` existed and were of correct types.
**Learning:** Unvalidated JSON payloads can cause `TypeError` or `KeyError`, leading to unhandled exceptions and potentially exposing internal server state.
**Prevention:** Always validate that `request.json` is a dictionary and explicitly check the structure and types of all required nested data before processing.
