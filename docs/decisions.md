Decisions
alternatives considered
why


Things to review
Virtual env activation scripts 
python -m venv .venv
./.venv/Scripts/Activate.ps1

Write about
    Secret scanning before every commit. pip install pre-commit, then create .pre-commit-config.yaml:
     Run pre-commit autoupdate (it replaces the rev values with the latest releases), then pre-commit install. The first run downloads its tools. If ruff blocks a later commit, run ruff check . --fix and fix what remains. To prove the secret scanner works, try committing a throwaway file containing a line like api_key = ''; detection depends on the hook's current rules, and you should delete the file without committing it either way.



