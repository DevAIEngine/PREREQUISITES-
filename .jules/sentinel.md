## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-06-09 - Missing Security Headers
 **Vulnerability:** Missing HTTP Security Headers (X-Content-Type-Options, X-Frame-Options, Strict-Transport-Security, Content-Security-Policy).
 **Learning:** Standard backend frameworks (Flask, FastAPI) do not include baseline security headers by default, leaving applications vulnerable to MIME-sniffing, clickjacking, and XSS.
 **Prevention:** Always implement a global middleware or `after_request` handler to inject essential security headers into all responses upon application initialization.
