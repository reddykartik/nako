# Dataset Documentation Files

---

# Data Directory

This directory contains the datasets used by the Nako vulnerability detection project.

## Directory Structure

```text
data/
├── raw/
│   ├── README.md
│   ├── train.xlsx
│   └── test.csv
│
└── processed/
    ├── dataset.csv
    └── readme
```

## Raw Data

The `raw/` directory contains the original dataset files.

These files should be preserved in their original form. Any cleaning, transformation or feature extraction should happen through reproducible processing code rather than manual modification of the original files.

## Processed Data

The `processed/` directory contains the dataset prepared for model training and evaluation.

The main artifact is:

```text
processed/dataset.csv
```

It contains repository metadata, Python source code, patch information and vulnerability labels.

## Versioning

Both raw and processed datasets are intentionally tracked in Git.

Dataset modifications should be documented, and significant revisions should record their provenance and file checksums.

---

