# Nako — Command Reference

All commands below are intended to be executed from the repository root unless otherwise stated.

## A. Initial setup

```bash
git clone <REPOSITORY_URL>
cd nako
```

Install Nix if it is not already installed:

```bash
sh <(curl -L https://nixos.org/nix/install) --daemon
```

Enable Flakes:

```bash
mkdir -p ~/.config/nix
```

Add to `~/.config/nix/nix.conf`:

```ini
experimental-features = nix-command flakes
```

## B. Development environment

Enter the environment:

```bash
nix develop
```

Check versions:

```bash
nix --version
python --version
podman --version
nginx -v
```

Check Python dependencies:

```bash
python -c "import numpy, pandas, sklearn, fastapi, uvicorn, joblib; print('OK')"
```

## C. Flake commands

Show available outputs:

```bash
nix flake show
```

Evaluate:

```bash
nix flake check --no-build
```

Check supported development systems:

```bash
nix eval --json \
  .#devShells \
  --apply 'builtins.attrNames'
```

Update dependencies intentionally:

```bash
nix flake update
```

Review lockfile changes:

```bash
git diff flake.lock
```

## D. Dataset inspection

List tracked dataset and model artifacts:

```bash
git ls-files data models
```

Inspect dataset:

```bash
python -c "import pandas as pd; d=pd.read_csv('data/processed/dataset.csv'); print(d.shape); print(d.dtypes); print(d.head()); print(d['is_vulnerable'].value_counts(dropna=False))"
```

Check duplicates:

```bash
python -c "import pandas as pd; d=pd.read_csv('data/processed/dataset.csv'); print('Duplicate rows:', d.duplicated().sum()); print('Unique repositories:', d['repo'].nunique()); print('Unique patches:', d['patch'].nunique())"
```

Calculate checksums:

```bash
sha256sum data/raw/*
sha256sum data/processed/dataset.csv
sha256sum models/vulnerability_model.joblib
```

## E. Training

Inspect the training script and its command-line interface:

```bash
python src/train.py --help
```

If the training script does not implement an argument parser, use its documented invocation.

The training workflow should:

1. Load the processed dataset.
2. Validate the data.
3. Create grouped splits.
4. Fit feature extraction on training data.
5. Train the classifier.
6. Evaluate on held-out data.
7. Save the complete inference pipeline.

After training, verify the model artifact:

```bash
ls -lh models/vulnerability_model.joblib
```

## F. Backend development

```bash
python -m uvicorn nako.api:app \
  --app-dir src \
  --host 127.0.0.1 \
  --port 8000
```

Test:

```bash
curl -X POST \
  http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"source_code": "print(1 + 1)"}'
```

## G. Image builds

```bash
nix build .#backend -o result-backend
nix build .#frontend -o result-frontend
```

Inspect:

```bash
file result-backend result-frontend
```

Load:

```bash
podman load -i result-backend
podman load -i result-frontend
```

## H. Deployment

Start:

```bash
podman compose -f deploy/compose.yaml up --force-recreate
```

Start in background:

```bash
podman compose -f deploy/compose.yaml up -d
```

Inspect:

```bash
podman ps
podman images
podman network ls
```

Logs:

```bash
podman compose -f deploy/compose.yaml logs -f
```

Stop:

```bash
podman compose -f deploy/compose.yaml down
```

## I. Application verification

Frontend:

```bash
curl -I http://127.0.0.1:8080/
```

Prediction:

```bash
curl -X POST \
  http://127.0.0.1:8080/api/predict \
  -H "Content-Type: application/json" \
  -d '{"source_code": "print(1 + 1)"}'
```

Expected response structure:

```json
{
  "prediction": 0,
  "decision_score": -1.0
}
```

The numerical values above are illustrative.

## J. Git

Check changes:

```bash
git status --short
```

Inspect unstaged changes:

```bash
git diff
```

Inspect staged changes:

```bash
git diff --cached
```

Stage:

```bash
git add .
```

Commit:

```bash
git commit -m "Complete project documentation"
```

Verify tracked assets:

```bash
git ls-files data models
```

