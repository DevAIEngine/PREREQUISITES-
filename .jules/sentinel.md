## 2024-04-24 - [Missing Authentication on WebSocket Initializer]
**Vulnerability:** The `/api/v1/capture/stream` endpoint, which acts as the core entrypoint for the "Cell Phone First UI" to initialize a WebSocket and trigger Gemini Live, lacked any form of authentication or authorization checks.
**Learning:** This architectural gap could allow unauthenticated users to initiate costly background tasks (like Gemini Live streaming) resulting in potential Denial of Wallet (DoW) and unauthorized access to the core engine's processing capabilities.
**Prevention:** Always secure public-facing endpoints that trigger heavy asynchronous tasks or downstream paid API calls. Ensure `fastapi.security.HTTPBearer` and `Depends` are configured on all entrypoints to the Sovereign Assembly Pipeline.
