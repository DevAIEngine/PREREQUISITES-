## 2026-03-17 - Unquoted GITHUB_OUTPUT in Pull Request Workflow
**Vulnerability:** Unquoted `$GITHUB_OUTPUT` variable was used in `.github/workflows/3-open-a-pull-request.yml` allowing potential word splitting and globbing.
**Learning:** Shell scripts run by GitHub Actions can fail unexpectedly or introduce subtle vulnerabilities (e.g. interpreting `*` in variables as wildcards) if system variables like `$GITHUB_OUTPUT` are not properly quoted.
**Prevention:** Always surround variables like `$GITHUB_OUTPUT` with double quotes (e.g., `"$GITHUB_OUTPUT"`) to prevent globbing and word splitting, especially when `actionlint` or `shellcheck` are used to analyze workflow syntax.
