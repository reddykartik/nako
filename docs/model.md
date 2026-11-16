# Model and evaluation

## Pipeline

The training implementation is in `src/train.py`. It builds a scikit-learn `Pipeline` containing:

1. A `FeatureUnion` with raw-source and AST-derived feature branches.
2. A `LinearSVC` classifier.

### Raw source branch

The raw branch uses `TfidfVectorizer` configured with:

- `analyzer="word"`
- `ngram_range=(1, 2)`
- `token_pattern=r"(?u)\b\w+\b"`

This represents source code as word unigrams and bigrams weighted by TF-IDF.

### AST branch

`ASTTokenTransformer` in `src/nako/features.py` parses each source string using Python's `ast` module. Its visitor appends each visited node's class name, such as `FunctionDef`, `Call`, or `Name`, to a token sequence.

A `TfidfVectorizer` with `ngram_range=(1, 3)` transforms these sequences.

These features describe AST node-type patterns. They do not encode a full semantic understanding of the program and do not directly identify vulnerability rules.

### Classifier

The feature branches are combined using `FeatureUnion` and passed to:

```python
LinearSVC(
    C=10.0,
    max_iter=2000,
    random_state=3,
)
```

The fitted pipeline is serialized to:

```text
models/vulnerability_model.joblib
```

Because the vectorizers and AST transformer are part of the pipeline, the saved pipeline contains the fitted feature transformations as well as the classifier.

## Training and evaluation procedure

The code uses one `GroupShuffleSplit` with `test_size=0.15`, `random_state=3`, and `groups=df["repo"]`.

| Partition | Rows |
|---|---:|
| Training | 13,811 |
| Test | 3,881 |

There is no separate validation set in the recorded implementation. The model is fitted on the 13,811-row training partition and evaluated on the 3,881-row held-out test partition.

The split is grouped by repository, not by patch. It is not stratified.

## Recorded test results

| Metric | Result |
|---|---:|
| Accuracy | 0.7825303 |
| Balanced accuracy | 0.6993567 |
| ROC-AUC | 0.8812965 |

Classification report:

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| 0 — non-vulnerable | 0.76 | 0.98 | 0.85 | 2,521 |
| 1 — vulnerable | 0.91 | 0.42 | 0.58 | 1,360 |
| Macro average | 0.83 | 0.70 | 0.71 | 3,881 |
| Weighted average | 0.81 | 0.78 | 0.76 | 3,881 |

Confusion matrix (actual labels are rows; predicted labels are columns; label order `[0, 1]`):

```text
[[2464   57]
 [ 787  573]]
```

This means:

- 2,464 non-vulnerable examples were correctly classified as class `0`.
- 57 non-vulnerable examples were classified as class `1`.
- 787 vulnerable examples were incorrectly classified as class `0`.
- 573 vulnerable examples were correctly classified as class `1`.

## Interpretation and limitations

The model has a high precision for the vulnerable class in this test set (approximately 0.91), but its recall for that class is only approximately 0.42. It misses 787 of the 1,360 vulnerable test examples.

The ROC-AUC score measures ranking discrimination across decision thresholds; it does not mean that 88% of predictions are correct. Accuracy alone also hides the difference in performance between the two classes. Balanced accuracy and per-class recall are important when reviewing this model.

Nako is an experimental machine-learning classifier. It is not a replacement for code review, static analysis, testing, or a professional security assessment. A prediction of non-vulnerable must not be interpreted as proof that code is safe.

The AST feature extractor calls `ast.parse`. Python code that cannot be parsed can raise an exception during feature extraction. Confirm the inference code's error handling before describing how malformed or unsupported input is handled.
