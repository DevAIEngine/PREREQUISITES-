## 2026-03-18 - Unpinned GitHub Action Dependency
 **Vulnerability:** Unpinned GitHub Action Dependency
 **Learning:** Using mutable tags (like @v0.7.0) for GitHub Actions allows a potential attacker to compromise the repository if the tag is modified or overwritten.
 **Prevention:** Always pin GitHub Actions to an immutable commit SHA to guarantee the specific code version executed and prevent supply chain attacks.
## 2026-03-18 - Command Injection Vulnerability in GitHub Actions
 **Vulnerability:** Command Injection Risk in GitHub Actions `run` steps.
 **Learning:** Directly interpolating `${{ github.workflow }}` inside a `run` block allows for bash command injection if the workflow name is maliciously crafted.
 **Prevention:** Map GitHub context variables to environment variables (e.g., `WORKFLOW_NAME: ${{ github.workflow }}`) and reference the environment variable inside the `run` block.
