# Dataset

## Processed dataset

The training script reads:

```text
data/processed/dataset.csv
```

The recorded dataset contains 17,692 rows and four columns:

| Column | Meaning |
|---|---|
| `repo` | Repository identifier associated with the sample |
| `source_code` | Python source code used as model input |
| `patch` | Patch text associated with the sample |
| `is_vulnerable` | Binary target label |

The target values are:

- `0`: non-vulnerable
- `1`: vulnerable

The training code expects these columns to be present and uses `source_code` as the input and `is_vulnerable` as the target.

## Train/test split

The implementation uses `GroupShuffleSplit` with:

```python
GroupShuffleSplit(
    n_splits=1,
    test_size=0.15,
    random_state=3,
)
```

The grouping variable is:

```python
groups=df["repo"]
```

Therefore, the split is **repository-grouped**, not patch-grouped. The split produces:

| Partition | Rows |
|---|---:|
| Training | 13,811 |
| Test | 3,881 |
| Total | 17,692 |

The variable in the training script is named `train_val_idx` and the resulting dataframe is named `train_val`, but this is the training partition. The code does not create a separate validation partition. The model is fitted on this partition and evaluated on the held-out test partition.

`GroupShuffleSplit` keeps repository groups separate between the two partitions. It is not a stratified splitter, so class proportions are not guaranteed to be equal across partitions.

## Leakage considerations

Grouping by repository is intended to evaluate generalization to repositories not used for fitting. It does not, by itself, prove that no identical or related patch content appears across partitions. The current split groups by `repo`, not by `patch`.

If patch-level overlap is a concern, inspect whether identical patch values occur in both partitions before making any claim that patch-level leakage has been ruled out.

## Preprocessing and feature extraction

The training pipeline uses the `source_code` column in two parallel branches:

1. Raw source text is tokenized by `TfidfVectorizer` using word analysis, unigrams and bigrams, and the configured token pattern.
2. Python source is parsed into an AST. The custom visitor emits AST node class names, and a second TF-IDF vectorizer transforms those sequences.

The two feature matrices are combined by `FeatureUnion`.

The `patch` column is present in the processed dataset, but the shown training code does not pass it as a model input. It uses `repo` for grouping and `source_code` for model input.

## Provenance and licensing

The exact upstream dataset name, source URL, original license, and redistribution permissions must be recorded from the dataset's original source or accompanying documentation. Do not infer or invent these details. See `data/raw/README.md` and complete it with verified information before public redistribution.
