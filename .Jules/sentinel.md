## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-04-02 - [Fix unhandled exceptions and missing input validation in Veo API]
**Vulnerability:** Unhandled exceptions in the '/veo-studio/generate-scenes' endpoint exposed the application to Denial of Service (DoS) attacks via malformed JSON payloads.
**Learning:** Without strict type checking and validation of incoming JSON, unexpected types (like string instead of int) cause fatal TypeError and KeyError crashes in the Flask server.
**Prevention:** Always validate that request.json is a dictionary and that required nested keys (like 'scenes' and numeric 'duration') are present and typed correctly before processing.
