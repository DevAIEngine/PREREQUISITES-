## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2024-11-08 - Fixed Unpinned GitHub Action Dependencies
**Vulnerability:** GitHub Action dependencies were pinned to mutable version tags (e.g., `@v4`, `@v0.7.0`) instead of immutable commit SHAs.
**Learning:** This is a supply chain security risk. If a malicious actor gains access to a third-party action's repository, they could update the version tag to point to a compromised commit, automatically injecting malicious code into our CI/CD pipeline.
**Prevention:** Always pin GitHub Actions to their specific, immutable commit SHAs.
