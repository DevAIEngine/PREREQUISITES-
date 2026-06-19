## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-19 - DoS Risk via Unbounded Input in User Identifier
**Vulnerability:** The `/api/v1/capture/stream` endpoint accepted a `user_id` query parameter and included it in the `ProjectManifest` model without any length validation, allowing excessively long inputs that could lead to Denial of Service or backend instability.
**Learning:** Even when input isn't directly executed, unbounded string inputs in high-throughput endpoints (like streaming entry points) can cause memory exhaustion or parsing bottlenecks, especially when creating UUIDs or formatting strings.
**Prevention:** Always enforce maximum length constraints using FastAPI's `Query` or Pydantic's `Field` (e.g., `max_length=255`) on all user-provided identifier fields.
