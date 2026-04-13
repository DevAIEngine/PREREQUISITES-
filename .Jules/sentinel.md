## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-05-24 - [Fix JSON/Command Injection in make_episode.sh]
**Vulnerability:** Constructing JSON in shell scripts via string concatenation allows command and JSON injection.
**Learning:** Always use safe parameter passing methods like `jq --arg` when dynamically building JSON in bash to prevent execution of malicious user input.
**Prevention:** Use `jq -n --arg` to construct JSON payloads safely and ensure proper authentication headers (like `X-API-Key`) are present in API interactions.
