## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-04-11 - [Missing Authentication and Shell Injection]
**Vulnerability:** The `/api/publish` and `/api/orchestration/publish` endpoints in `infrastructure/app.py` lacked authentication. Additionally, `make_episode.sh` was vulnerable to string injection due to unsafe JSON construction.
**Learning:** Exposing orchestration endpoints without authentication can lead to unauthorized pipeline executions. Unsafe string concatenation in bash scripts can be exploited when handling user input like script URLs.
**Prevention:** Always secure sensitive endpoints with API keys or other auth mechanisms. Use `jq --arg` or similar safe serialization methods in shell scripts instead of raw string interpolation.
