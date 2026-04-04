## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2024-03-15 - [Fix unhandled exceptions in veo_generate_scenes]
**Vulnerability:** The `/veo-studio/generate-scenes` endpoint in `infrastructure/app.py` did not validate incoming JSON. An invalid `scenes` structure or non-numeric `duration` caused Python unhandled exceptions (`TypeError`), leaking error stack traces.
**Learning:** Even internal API endpoints expecting a specific data structure must sanitize and type-check all incoming JSON. A missing `duration` value or an unexpected type can crash the route and expose the application state.
**Prevention:** Always validate that `request.json` contains the expected keys, verify they are the correct type, and handle invalid shapes gracefully with a `400 Bad Request` instead of triggering a 500 error.
