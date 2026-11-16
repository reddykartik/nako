# Processed Dataset

## File

```text
dataset.csv
```

## Description

This file contains the prepared dataset used by the Nako model training workflow.

## Schema

| Column | Description |
|---|---|
| `repo` | Source repository identifier |
| `source_code` | Python source code |
| `patch` | Associated patch information |
| `is_vulnerable` | Binary vulnerability label |

## Labels

- `0`: Non-vulnerable.
- `1`: Vulnerable.

## Preparation

The processed dataset is derived from the original raw data.

The processing workflow should preserve repository and patch metadata to support dataset inspection and grouped splitting.

## Splitting

The project uses patch-based grouping to prevent samples associated with the same patch from appearing across multiple data partitions.

The grouping strategy is intended to reduce leakage between training and evaluation.

## Integrity

Calculate the dataset checksum:

```bash
sha256sum dataset.csv
```

## Versioning

This file is intentionally tracked by Git.

Changes should be accompanied by an explanation of the processing changes and their impact on the dataset.

---

