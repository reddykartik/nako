# Processed dataset

The training script reads `dataset.csv` from this directory.

## Schema

The recorded processed dataset contains 17,692 rows and these columns:

| Column | Description |
|---|---|
| `repo` | Repository identifier associated with the sample |
| `source_code` | Python source code supplied to the feature pipeline |
| `patch` | Patch text associated with the sample |
| `is_vulnerable` | Binary target label |

Target labels:

- `0`: non-vulnerable
- `1`: vulnerable

## Use in training

`src/train.py` reads `source_code` as model input and `is_vulnerable` as the target. It uses `repo` as the grouping variable for a single `GroupShuffleSplit`. The `patch` column is not passed to the model as an input feature in the recorded training implementation.

The split produces 13,811 training rows and 3,881 test rows. There is no separate validation set.

See `docs/dataset.md` and `docs/model.md` for more details.

## Reproducibility

The processed dataset is stored in version control in this project. Preserve the exact preprocessing procedure and document any changes to the dataset. Confirm that the source dataset's license permits redistribution of both the original and derived data.

