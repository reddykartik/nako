# Project Review Checklist

This checklist is intended for independent reviewers.

## 1. Project Structure

- [ ] Repository structure is understandable.
- [ ] Source code is separated from deployment files.
- [ ] Documentation corresponds to the actual implementation.
- [ ] No accidental temporary files are committed.

## 2. Dataset

- [ ] Raw dataset provenance is documented.
- [ ] Dataset licensing is verified.
- [ ] Processed dataset schema is documented.
- [ ] Missing values and duplicates are investigated.
- [ ] Class distribution is reported.
- [ ] Repository distribution is investigated.
- [ ] Patch-based grouping prevents related samples from crossing splits.
- [ ] Preprocessing is reproducible.

## 3. Machine Learning

- [ ] Feature extraction is understandable.
- [ ] Raw source-code representation is documented.
- [ ] AST representation is documented.
- [ ] TF-IDF fitting is restricted to training data.
- [ ] Model configuration is documented.
- [ ] Evaluation metrics are reported.
- [ ] Confusion matrix is included.
- [ ] Limitations are acknowledged.
- [ ] Serialized inference pipeline matches training.

## 4. Backend

- [ ] API accepts valid source-code requests.
- [ ] Invalid inputs are handled appropriately.
- [ ] Model loading works.
- [ ] Prediction responses have the documented schema.
- [ ] Decision scores are not misrepresented as probabilities.

## 5. Frontend

- [ ] HTML loads successfully.
- [ ] CSS loads successfully.
- [ ] JavaScript loads successfully.
- [ ] Prediction requests reach the backend.
- [ ] Responses are displayed correctly.
- [ ] API failures are handled appropriately.

## 6. Infrastructure

- [ ] Nix development shell works.
- [ ] Flake lockfile is committed.
- [ ] Container images build successfully.
- [ ] Backend image includes the trained model.
- [ ] Frontend image contains the static application.
- [ ] Compose starts both services.
- [ ] Nginx reverse proxy works.
- [ ] Application can be stopped cleanly.

## 7. Reproducibility

- [ ] A fresh clone can be configured.
- [ ] Nix installation instructions work.
- [ ] Flakes can be enabled.
- [ ] Development dependencies are available.
- [ ] Datasets are present.
- [ ] Model artifact is present.
- [ ] Deployment instructions are complete.

## 8. Reviewer Notes

Record findings, reproducibility issues, possible dataset biases and suggested improvements here.

| Reviewer | Findings | Date |
|---|---|---|
| Reviewer 1 | | |
| Reviewer 2 | | |
| Reviewer 3 | | |

---

