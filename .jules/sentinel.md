## 2025-02-14 - [Fix Information Leakage in API Response]
**Vulnerability:** The `/api/publish` endpoint in `infrastructure/app.py` was returning raw exception strings (`str(e)`) to the client via a 500 JSON response, potentially exposing sensitive internal details (e.g., Google Drive/Sheets API keys, file paths, or backend structure).
**Learning:** Never return raw exception traces or error messages directly to the client. This is a common Information Exposure vulnerability that can aid attackers in reconnaissance.
**Prevention:** Always log the full exception details on the server side (e.g., `app.logger.error`) and return a standardized, sanitized error message (e.g., `'An internal server error occurred.'`) to the client.
