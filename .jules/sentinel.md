## 2025-02-14 - Fix Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action dependency (`skills/action-keyphrase-checker@v1`) allowed for a mutable tag that could potentially be replaced with a malicious commit, leading to a supply chain attack.
 **Learning:** Always use specific, immutable commit SHAs for third-party GitHub Actions to guarantee the exact code that runs, thus preventing unexpected behavior or security compromises if a tag is maliciously updated.
 **Prevention:** Implement automated linting (e.g., using `actionlint`) or review processes to ensure all third-party Action dependencies reference immutable commit SHAs instead of mutable tags.
## 2024-05-24 - Overly Permissive Workflow Token
**Vulnerability:** The workflow in `.github/workflows/4-merge-your-pull-request.yml` granted `contents: write` permissions unconditionally, which violates the principle of least privilege.
**Learning:** Workflows checking out repositories and posting issue comments do not typically need `contents: write` unless they are modifying code or tags directly in the repo.
**Prevention:** Always restrict default workflow permissions to minimal needs, such as `contents: read` to checkout code, and define additional specific permissions, such as `issues: write`, only when necessary.
## 2026-03-19 - [Overly Permissive GITHUB_TOKEN Workflows]
**Vulnerability:** Workflows grant global `contents: write` and `actions: write` permissions when only specific jobs require them.
**Learning:** In GitHub Skills/Learning Lab course repositories, workflows often require `contents: write` to advance course progress (e.g., in `finish_exercise` jobs), or `actions: write` to enable/disable workflows. When hardening workflow permissions, apply restrictive permissions (e.g., `contents: read`) globally and delegate necessary `write` permissions only to the specific jobs that require them to mitigate risk of abuse or compromise.
**Prevention:** Apply the principle of least privilege by setting global `permissions:` to `read-all` or minimum viable (e.g., `contents: read`) at the top of workflows, and then strictly define necessary `write` access at the individual `job` level only where required.
