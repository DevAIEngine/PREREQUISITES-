## 2025-04-25 - [HTTPBearer Missing Header Default Status]
**Vulnerability:** Fast API Authentication Default Returns
**Learning:** When using `fastapi.security.HTTPBearer`, an endpoint requested without an Authorization header returns a `403 Forbidden` status by default, rather than `401 Unauthorized`. Tests designed to catch missing or invalid headers must account for this behavior when making assertions on status codes.
**Prevention:** Always write security tests that explicitly handle the `403` return code for missing credentials natively blocked by `HTTPBearer`, and `401` for custom credential validation failures.
