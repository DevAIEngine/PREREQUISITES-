## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-04-07 - [Fix JSON injection in make_episode.sh payload]
**Vulnerability:** Bash script passed unsanitized arguments directly into a JSON string payload for a curl command via string concatenation. This could allow JSON injection or command execution.
**Learning:** Never build JSON using bash string interpolation with user input.
**Prevention:** Always use `jq -n --arg` or similar safe parameterization when constructing JSON payloads in shell scripts.
