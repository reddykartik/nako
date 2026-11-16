# Machine Learning Model

## 1. Overview

Nako uses supervised machine learning to classify Python source code into two classes:

- Non-vulnerable.
- Vulnerable.

The current implementation combines source-code feature extraction with a linear classification model.

## 2. Model Pipeline

The inference pipeline consists of the following conceptual stages:

```text
Python Source Code
       |
       v
Source-code feature extraction
       |
       +--------------------+
       |                    |
       v                    v
Raw source tokens       AST-derived tokens
       |                    |
       v                    v
TF-IDF representation  TF-IDF representation
       |                    |
       +----------+---------+
                  |
                  v
             Feature Union
                  |
                  v
             Linear SVM
                  |
                  v
             Prediction
```

The exact transformer configuration is defined in `src/train.py` and `src/nako/features.py`.

## 3. Feature Extraction

### Raw source-code features

Raw source-code tokens preserve lexical information from the submitted Python program.

TF-IDF converts token frequencies into numerical features.

### AST-derived features

The Abstract Syntax Tree represents the syntactic structure of Python source code.

AST-based feature extraction can capture structural information beyond the raw text representation.

The feature transformer is responsible for converting source code into AST-derived tokens.

Parsing failures and unsupported syntax must be handled explicitly.

## 4. TF-IDF

Term Frequency–Inverse Document Frequency is used to represent source-code tokens numerically.

Term frequency measures the importance of a token within a sample.

Inverse document frequency reduces the influence of tokens that appear in many samples.

The general TF-IDF formulation is:

\[
TFIDF(t,d)=TF(t,d)\times IDF(t)
\]

The vectorizer learns its vocabulary and IDF values from training data only.

The exact configuration, including tokenization and n-gram parameters, is defined in the training implementation.

## 5. Classifier

The current classifier is a Linear Support Vector Machine.

A linear SVM learns a decision boundary separating the two classes in the feature space.

The model produces a decision score.

The sign of the decision score determines the predicted class under the standard binary LinearSVC decision convention:

- Negative: class 0.
- Positive: class 1.

The magnitude represents the distance-related decision value, not a calibrated probability.

A larger absolute score indicates a stronger position relative to the learned decision boundary, but it is not a guarantee of correctness.

## 6. Training and Evaluation

The training workflow should:

1. Load the processed dataset.
2. Validate the dataset structure.
3. Create patch-grouped training, validation and test partitions.
4. Fit feature extraction on training samples.
5. Train the classifier.
6. Evaluate using held-out data.
7. Serialize the complete inference pipeline.

The random seed and split parameters should be recorded.

The current project has used seed 3 for its patch-grouped splitting workflow.

## 7. Evaluation Metrics

Report at least:

- Accuracy.
- Precision.
- Recall.
- F1-score.
- Confusion matrix.

For security-oriented classification, recall and precision should be considered separately.

A false negative means vulnerable code was classified as non-vulnerable.

A false positive means non-vulnerable code was classified as vulnerable.

Neither error should be hidden behind accuracy alone.

### Evaluation results

Populate this table using the final evaluation run.

| Metric | Validation | Test |
|---|---:|---:|
| Accuracy | TO BE FILLED | TO BE FILLED |
| Precision | TO BE FILLED | TO BE FILLED |
| Recall | TO BE FILLED | TO BE FILLED |
| F1-score | TO BE FILLED | TO BE FILLED |

Also document the number of samples in each partition and the class distribution.

Do not report training metrics as test performance.

## 8. Model Serialization

The trained pipeline is serialized using Joblib.

Artifact:

```text
models/vulnerability_model.joblib
```

The backend loads this artifact for inference.

The serialized artifact must include every fitted transformer needed to transform source code consistently with training.

This includes the raw and AST feature-extraction components and the trained classifier.

## 9. Model Reproducibility

To reproduce a model version, retain:

- Dataset revision.
- Training code revision.
- Nix lockfile revision.
- Random seed.
- Split configuration.
- Feature extraction configuration.
- Classifier hyperparameters.
- Evaluation results.
- Serialized model artifact.

## 10. Limitations

The model learns statistical relationships in the training data.

It does not execute programs, prove exploitability or replace a security audit.

Its predictions may be affected by:

- Unseen repositories.
- Unseen programming patterns.
- Dataset bias.
- Incorrect labels.
- Syntax errors.
- Distribution shifts.
- Differences between training and production inputs.

---
