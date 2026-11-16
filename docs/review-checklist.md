# Reviewer checklist

## Project structure

- [ ] `README.md` describes the project and links to the detailed documentation.
- [ ] Training, inference, API, frontend, deployment, and Nix files are present.
- [ ] Dataset and model artifact paths match the code.

## Dataset

- [ ] `data/processed/dataset.csv` has the documented columns: `repo`, `source_code`, `patch`, `is_vulnerable`.
- [ ] Label meaning is documented: `0` non-vulnerable, `1` vulnerable.
- [ ] The split is described accurately as repository-grouped using `groups=df["repo"]`.
- [ ] Documentation does not claim that the split is patch-grouped.
- [ ] Documentation does not claim a separate validation set.
- [ ] Upstream dataset provenance and license are verified and recorded.

## Model

- [ ] Raw-source TF-IDF settings match `src/train.py`.
- [ ] AST extraction is described as AST node-type token extraction.
- [ ] `FeatureUnion` and `LinearSVC` settings match the implementation.
- [ ] Evaluation metrics and confusion matrix match the recorded training output.
- [ ] The 787 false negatives and low vulnerable-class recall are clearly disclosed.
- [ ] The model is not described as a production-grade security guarantee.

## API and frontend

- [ ] FastAPI `GET /` responds.
- [ ] FastAPI `POST /predict` accepts a `source_code` string.
- [ ] Nginx serves the frontend.
- [ ] Nginx forwards `/api/predict` to the backend.
- [ ] The browser prediction flow works end to end.

## Deployment

- [ ] Compose starts both services.
- [ ] Frontend is reachable at `http://localhost:8080`.
- [ ] Static CSS and JavaScript assets load.
- [ ] The prediction request succeeds through the frontend route.
- [ ] Fresh Nix-built image archives are successfully loaded and used before claiming a reproducible image workflow.

## Release

- [ ] Dataset and model redistribution permissions are checked.
- [ ] No secrets, credentials, local runtime files, or Nix `result` symlinks are committed.
- [ ] `git status --short` has been reviewed before committing.
