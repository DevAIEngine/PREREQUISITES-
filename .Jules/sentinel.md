## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2026-04-06 - JSON/Command Injection in Shell Scripts
 **Vulnerability:** Unsanitized interpolation of user input into JSON payload in a bash script (`make_episode.sh`).
 **Learning:** Interpolating user variables (like `$SCRIPT_URL`) directly into a JSON string via bash allows JSON structural injection and potentially command execution if quotes aren't escaped safely.
 **Prevention:** Always use `jq` with `--arg` or safe parameter passing methods when constructing JSON payloads with dynamic input in shell scripts.
