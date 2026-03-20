1. **Understand the Goal**: As Sentinel, fix one small security issue.
2. **Identify the Issue**: The workflows `1-create-a-branch.yml`, `2-commit-a-file.yml`, `3-open-a-pull-request.yml`, and `4-merge-your-pull-request.yml` contain a command injection risk where `${{github.workflow}}` is directly interpolated into a `run` block as a string literal `"${{github.workflow}}"`. Since the workflow name is defined in the workflow file itself (`name: ...`), an attacker can submit a pull request modifying the `name` field to contain shell metacharacters, potentially leading to arbitrary code execution within the runner environment context with the permissions assigned to the workflow.
3. **Plan**:
   - For `1-create-a-branch.yml`, `2-commit-a-file.yml`, `3-open-a-pull-request.yml`:
     - Modify the `run` block to use an environment variable (e.g., `WORKFLOW_NAME`) instead of direct string interpolation.
     - Add a comment explaining the security concern.
     - Add `WORKFLOW_NAME: ${{ github.workflow }}` to the `env` block.
   - For `4-merge-your-pull-request.yml`:
     - Make the corresponding change.
   - Run `actionlint` to verify.
   - Document learning in `.jules/sentinel.md`.
   - Submit the PR.
