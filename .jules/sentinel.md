## 2024-03-18 - Command Injection Risk in Workflow
**Vulnerability:** Found untrusted input `${{ github.event.pull_request.title }}` used directly within a command injection context in `action-keyphrase-checker`.
**Learning:** Even custom actions might improperly sanitize inputs if they execute scripts or take raw input directly without environment variable bindings, or if they evaluate inputs in a dangerous way. Wait, looking closer, `action-keyphrase-checker` takes it as a parameter, not as a shell script.
But wait, what about `${{ github.event.pull_request.body }}`?
Ah! `PR_BODY: ${{ github.event.pull_request.body }}` is used as an environment variable in `.github/workflows/3-open-a-pull-request.yml`, which is actually the correct and secure way to handle it!
Let's see if there are any other issues.
## 2024-03-18 - Command Injection in GitHub Actions via github.workflow
**Vulnerability:** Untrusted context variables like `${{ github.workflow }}` were being interpolated directly into shell `run` blocks using double quotes (e.g., `gh workflow disable "${{github.workflow}}"`). Since `github.workflow` resolves to the `name` field of the workflow, and attackers can control this field when submitting PRs, this created a command injection vulnerability.
**Learning:** Any context variable that can be influenced by a user (like `github.event.pull_request.title`, `github.head_ref`, or even the seemingly safe `github.workflow` from the `name` field) is dangerous when directly interpolated into scripts.
**Prevention:** Always bind context variables to intermediate environment variables within the step's `env` block and reference them in the script as `$VAR_NAME` (e.g., `env: WORKFLOW_NAME: ${{ github.workflow }}` -> `run: gh disable "$WORKFLOW_NAME"`).
