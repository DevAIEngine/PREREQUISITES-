## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.

## 2026-03-23 - Unhandled Exception (DoS) via Malformed JSON
**Vulnerability:** A malformed JSON payload (`{"scenes": "not a list"}`) sent to `/veo-studio/generate-scenes` could crash the Flask process or throw a 500 Internal Server Error due to unhandled `TypeError` inside a generator expression.
**Learning:** Blindly trusting `request.json` without validating its type and schema inside endpoint handlers can lead to DoS vulnerabilities.
**Prevention:** Always validate that incoming JSON payloads conform to expected schemas (using `isinstance` checks, defensive coding, or libraries like `pydantic`) and fail securely by returning a 400 Bad Request error rather than propagating language-level exceptions.
