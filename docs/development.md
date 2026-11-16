# Development Guide

## 1. Prerequisites

Install:

- Git.
- Nix.
- Flakes support.
- Podman.
- Podman Compose.

## 2. Clone the Repository

```bash
git clone <REPOSITORY_URL>
cd nako
```

## 3. Enter the Nix Shell

```bash
nix develop
```

## 4. Inspect Project Outputs

```bash
nix flake show
```

Check flake evaluation:

```bash
nix flake check --no-build
```

## 5. Development Dependencies

The development shell provides Python 3.14 and the project's required Python libraries.

Check Python:

```bash
python --version
```

Check available packages:

```bash
python -c "import numpy, pandas, sklearn, fastapi, joblib; print('Dependencies available')"
```

Check Nginx:

```bash
nginx -v
```

Check Podman:

```bash
podman --version
podman compose version
```

## 6. Source Code Organization

| Location | Purpose |
|---|---|
| `src/train.py` | Model training |
| `src/nako/features.py` | Feature extraction |
| `src/nako/predict.py` | Prediction functionality |
| `src/nako/api.py` | FastAPI application |
| `web/` | Browser interface |
| `nix/` | Container image derivations |
| `deploy/` | Deployment configuration |

## 7. Git Workflow

Check modifications:

```bash
git status
```

Inspect changes:

```bash
git diff
git diff --cached
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Document project architecture and deployment"
```

Inspect tracked datasets and models:

```bash
git ls-files data models
```

Datasets and trained model artifacts are intentionally version-controlled.

Do not add them to `.gitignore`.

## 8. Updating Dependencies

The project pins Nix dependencies through `flake.lock`.

Update the lockfile when intentionally updating dependencies:

```bash
nix flake update
```

Review the changes:

```bash
git diff flake.lock
```

Commit dependency changes separately where practical.

## 9. Supported Systems

The flake uses `flake-utils.lib.eachDefaultSystem`.

Default systems:

- `x86_64-linux`
- `aarch64-linux`
- `x86_64-darwin`
- `aarch64-darwin`

The development shell is defined per supported system.

Container image outputs are intentionally Linux-only because they use Nix Docker-compatible image construction.

Successful evaluation on all platforms does not guarantee that every package builds on every platform.

---

