# Nako — Python Vulnerability Detection

Nako is a machine-learning project that classifies submitted Python source code as either vulnerable or non-vulnerable. It provides a browser-based interface backed by a FastAPI prediction service.

> **Important:** Nako is an experimental classifier, not a security scanner or proof that code is safe. It can miss vulnerable examples. Do not use its output as the sole basis for security decisions.

## What it contains

- A text-based feature pipeline using TF-IDF over source code.
- An AST-derived feature branch that extracts Python AST node-type names and vectorizes them with TF-IDF.
- A `LinearSVC` classifier.
- A FastAPI endpoint for predictions.
- A static HTML/CSS/JavaScript frontend served by Nginx.
- A Podman Compose deployment definition.
- A Nix-based development and image-build environment.

## Repository layout

```text
.
├── data/
│   ├── raw/
│   └── processed/
├── deploy/
│   ├── compose.yaml
│   ├── nginx.conf
│   └── nginx-dev.conf
├── docs/
├── models/
│   └── vulnerability_model.joblib
├── nix/
│   ├── backend-image.nix
│   └── frontend-image.nix
├── src/
│   ├── train.py
│   └── nako/
│       ├── api.py
│       ├── features.py
│       └── predict.py
├── web/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── flake.nix
└── flake.lock
```

## Run the application

Enter the Nix development environment:

```bash
nix develop
```

Start the services:

```bash
podman compose -f deploy/compose.yaml up
```

Open the frontend at:

```text
http://localhost:8080
```

Stop the services:

```bash
podman compose -f deploy/compose.yaml down
```

The Compose configuration exposes the frontend on host port `8080`. The backend is exposed to the Compose network on port `8000`; it is not published directly to the host by the supplied Compose configuration.

## Model overview

The training pipeline combines two feature branches:

1. Raw source-code tokens, represented using word-level TF-IDF with unigrams and bigrams.
2. AST node-type tokens, extracted from Python source and represented using TF-IDF with n-grams up to length three.

The two branches are combined with `FeatureUnion` and passed to `LinearSVC`.

The training code uses a single repository-grouped train/test split. It does not create a separate validation set. See [Dataset](docs/dataset.md) and [Model and evaluation](docs/model.md).

## Evaluation

The recorded test-set results are:

| Metric | Result |
|---|---:|
| Accuracy | 0.7825 |
| Balanced accuracy | 0.6994 |
| ROC-AUC | 0.8813 |

The confusion matrix, with rows as actual labels and columns as predicted labels in the order `[0, 1]`, is:

```text
                 Predicted 0   Predicted 1
Actual 0              2464           57
Actual 1               787          573
```

For the vulnerable class (`1`), recall is approximately `0.42`. The model therefore missed 787 vulnerable examples in this test set. This is a substantial limitation and must be considered when interpreting predictions.

## Documentation

- [Architecture](docs/architecture.md)
- [Dataset and split](docs/dataset.md)
- [Model and evaluation](docs/model.md)
- [API](docs/api.md)
- [Development environment](docs/development.md)
- [Deployment](docs/deployment.md)
- [Useful commands](docs/commands.md)
- [Reviewer checklist](docs/review-checklist.md)

## Limitations

- The classifier learns statistical patterns from its training dataset; it does not perform a full security analysis.
- AST features are structural node-type names, not semantic vulnerability rules.
- The recorded vulnerable-class recall is low (approximately 0.42).
- A negative prediction does not establish that code is secure.
- Python source that cannot be parsed by `ast.parse` may fail during AST feature extraction unless handled by the prediction layer. Check the current inference implementation before relying on behavior for invalid or unsupported syntax.
- The evaluation is based on one repository-grouped split and should not be interpreted as a guarantee of performance on all repositories or real-world code.

## Data and model artifacts

The processed dataset and serialized model are stored in the repository. See `data/raw/README.md` and `data/processed/readme` for dataset documentation. Confirm that the original dataset's redistribution terms permit committing and sharing the raw files and derived dataset before publishing the repository.

