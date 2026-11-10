1. Verify the GitHub Action workflow modifications.
```bash
git diff .github/workflows/
```
2. Add a Sentinel journal entry.
```bash
mkdir -p .jules
cat << 'HEREDOC' >> .jules/sentinel.md
## $(date +%Y-%m-%d) - [HIGH] Unpinned GitHub Action Dependencies
**Vulnerability:** GitHub Action workflows were referencing mutable tags (e.g., @v4, @v0.7.0) instead of immutable commit SHAs.
**Learning:** This is a supply chain vulnerability. A bad actor with access to the action's repository could force push a malicious change to the tag, automatically compromising all workflows depending on it.
**Prevention:** Always pin GitHub Actions to immutable commit SHAs (e.g., @11d5960a326750d5838078e36cf38b85af677262) and use tools like dependabot to keep them updated securely.
HEREDOC
cat .jules/sentinel.md
```
3. Install dependencies.
```bash
python3 -m pip install -r requirements.txt -r backend/requirements.txt pytest httpx flask fastapi pydantic uvicorn google-cloud-aiplatform google-api-python-client google-cloud-texttospeech google-auth-httplib2 google-auth-oauthlib
```
4. Run tests.
```bash
make test
```
5. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
6. Use the `submit` tool to submit the PR with the required branch name and Sentinel PR title format `🛡️ Sentinel: [HIGH] Fix Unpinned GitHub Action Dependencies`.
