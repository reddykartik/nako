# Development environment

## Nix

The repository uses a Nix flake. The flake definition and lock file are:

```text
flake.nix
flake.lock
```

Enter the project development shell with:

```bash
nix develop
```

The lock file records the resolved flake inputs. Keep `flake.lock` under version control so collaborators can use the same locked input revisions.

## Source layout

- `src/train.py` — training and evaluation pipeline.
- `src/nako/features.py` — AST-derived feature transformer.
- `src/nako/predict.py` — model loading and prediction logic.
- `src/nako/api.py` — FastAPI application.
- `web/` — static browser frontend.
- `deploy/` — Compose and Nginx configuration.
- `nix/` — container image definitions.

## Training

The training script reads `data/processed/dataset.csv` and writes the fitted pipeline to `models/vulnerability_model.joblib`.

Run the training command from the repository's configured Nix environment, using the project's Python import path as defined by its development shell. Verify the exact invocation against the current `flake.nix` before copying a command into automation or CI.

## Model artifact

The saved artifact is a Joblib-serialized scikit-learn pipeline. The complete fitted pipeline is required for inference because it contains the fitted vectorizers and AST transformer as well as the classifier.

Only load Joblib artifacts from trusted sources. Joblib/pickle-based formats can execute code during deserialization.
