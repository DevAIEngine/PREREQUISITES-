## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-04-08 - [Fix JSON/Command Injection in curl payload]
**Vulnerability:** Shell scripts using raw string concatenation (e.g., `'{"script_url": "'$SCRIPT_URL'"}'`) in `curl` payloads are vulnerable to JSON injection. If user input contains quotes, the JSON structure breaks or can be maliciously manipulated.
**Learning:** Never use string concatenation to build JSON in bash scripts when handling arbitrary input.
**Prevention:** Always use `jq -n --arg` (e.g., `jq -n --arg url "$SCRIPT_URL" '{"url": $url}'`) to safely escape user input and generate valid JSON.
