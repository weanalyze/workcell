# update version in pyproject.toml
poetry version patch
# tag and push by github actions
git checkout main
git tag $(poetry version -s)
git push --tags origin main $(poetry version -s)