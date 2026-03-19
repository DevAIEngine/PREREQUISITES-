## 2024-05-24 - Unpinned GitHub Action Dependency

**Vulnerability:** Unpinned GitHub Action Dependency (`@v0.8.1` instead of commit SHA) in `.github/workflows/0-start-exercise.yml`.
**Learning:** Pinning GitHub Action dependencies to mutable tags like `@v0.8.1` exposes the repository to supply chain attacks. If a malicious actor compromises the action repository or forces an update to the tag to point to a malicious commit, the workflow will automatically fetch and execute the compromised code.
**Prevention:** Always pin third-party GitHub Actions to a specific, immutable commit SHA rather than a branch or tag name. Provide an explanatory comment indicating the tag that the commit SHA corresponds to.