# Dataset Documentation

## 1. Overview

The dataset is used to train a binary classifier for identifying potentially vulnerable Python source code.

The project maintains original dataset files and a processed dataset separately.

```text
data/
├── raw/
│   ├── train.xlsx
│   ├── test.csv
│   └── README.md
│
├── processed/
│   ├── dataset.csv
│   └── readme
│
└── readme.md
```

## 2. Raw Dataset

The raw directory contains the original input files.

| File | Description |
|---|---|
| `train.xlsx` | Original training data |
| `test.csv` | Original test data |

The precise original dataset name, publication, version, URL, collection date and license must be recorded in `data/raw/README.md`.

Do not modify original files during preprocessing.

## 3. Processed Dataset

The processed dataset is stored in:

```text
data/processed/dataset.csv
```

The processed dataset contains the following fields:

| Column | Description |
|---|---|
| `repo` | Repository identifier associated with the source code |
| `source_code` | Python source-code sample |
| `patch` | Associated patch information |
| `is_vulnerable` | Binary classification label |

Label definitions:

| Value | Meaning |
|---|---|
| 0 | Non-vulnerable |
| 1 | Vulnerable |

## 4. Data Preparation

The preparation workflow includes:

1. Loading the original dataset files.
2. Inspecting column names and data types.
3. Identifying missing values.
4. Cleaning and normalizing source-code records.
5. Preparing vulnerability labels.
6. Preserving repository and patch metadata.
7. Constructing the processed dataset.

All transformations should be reproducible from the original dataset.

The preprocessing implementation and any intermediate transformations should be documented alongside the training code.

## 5. Dataset Quality

Dataset quality is important because the classifier can learn dataset-specific patterns rather than general vulnerability characteristics.

The following aspects should be investigated:

- Missing values.
- Duplicate source-code samples.
- Duplicate patches.
- Class distribution.
- Repository distribution.
- Source-code length distribution.
- Differences between vulnerable and non-vulnerable samples.
- Repository-specific patterns.
- Label inconsistencies.
- Potential correlations between metadata and labels.

## 6. Data Leakage Prevention

Multiple samples can be associated with the same patch.

Randomly splitting individual rows can place related samples in both training and evaluation sets.

This may result in overly optimistic evaluation metrics.

The project therefore uses patch-based grouping when splitting the processed dataset.

The intended grouping invariant is:

```text
A patch group must belong to only one split.
```

The training, validation and test partitions must not share patch groups.

The grouping strategy should be checked again whenever the dataset changes.

## 7. Feature Extraction and Splitting

The dataset must be split before fitting any vocabulary or IDF statistics.

The TF-IDF vectorizer must be fitted exclusively on training data.

Validation and test data must only be transformed using the already-fitted vectorizer.

This prevents evaluation information from leaking into the training process.

## 8. Dataset Versioning

Raw and processed datasets are tracked by Git.

Changes to the dataset should be committed with meaningful messages.

Example:

```bash
git add data/
git commit -m "Update processed vulnerability dataset"
```

For every significant dataset revision, record:

- Source version.
- File checksums.
- Number of samples.
- Number of unique repositories.
- Number of unique patches.
- Class distribution.
- Preprocessing changes.
- Known limitations.

## 9. Known Limitations

The dataset may not represent the complete distribution of Python software or real-world security vulnerabilities.

Potential issues include:

- Repository-specific patterns.
- Duplicate or related code samples.
- Incomplete vulnerability labels.
- Differences between vulnerable and fixed code.
- Limited representation of vulnerability categories.
- Dataset-specific correlations.

These limitations must be considered when interpreting model performance.

## 10. Dataset Provenance

Complete this section using the original dataset documentation:

| Field | Value |
|---|---|
| Dataset name | TO BE VERIFIED |
| Original source | TO BE VERIFIED |
| Publication | TO BE VERIFIED |
| Version | TO BE VERIFIED |
| Download date | TO BE VERIFIED |
| Original license | TO BE VERIFIED |
| Processing script | TO BE VERIFIED |

---
