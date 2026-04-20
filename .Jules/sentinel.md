## 2023-10-24 - [Fix exposed Werkzeug interactive debugger on 0.0.0.0]
**Vulnerability:** Flask `app.run` was hardcoded with `debug=True` and `host='0.0.0.0'`. This exposed the Werkzeug interactive debugger to all network interfaces, allowing arbitrary remote code execution (RCE).
**Learning:** Hardcoding debug mode on a globally bound host (`0.0.0.0`) is a critical security vulnerability.
**Prevention:** Always use environment variables (e.g., `FLASK_DEBUG`) to control debug mode, and ensure it defaults to `False` in production or default contexts.
## 2024-05-20 - [Fix Unauthenticated API Endpoints & Command Injection]
**Vulnerability:** Core publishing endpoints lacked authentication, and make_episode.sh constructed JSON insecurely, allowing injection.
**Learning:** Application-level authentication is required for public endpoints, and shell scripts must use safe JSON construction (e.g., jq).
**Prevention:** Always use require_api_key decorators and safe data handling techniques in shell scripts.
