# Raw Dataset Documentation

## Overview

This directory contains the original input datasets used in the Nako project.

## Files

| File | Description |
|---|---|
| `train.xlsx` | Original training dataset |
| `test.csv` | Original test dataset |

## Dataset Provenance

Complete the following information using the original dataset publication or download source.

| Property | Details |
|---|---|
| Dataset name | TO BE VERIFIED |
| Source URL | TO BE FILLED |
| Publication | TO BE FILLED |
| Version | TO BE FILLED |
| Download date | TO BE FILLED |
| Original license | TO BE VERIFIED |
| Original file checksums | See below |

## Data Integrity

The raw dataset files should not be modified during preprocessing.

Generate SHA-256 checksums:

```bash
sha256sum train.xlsx test.csv
```

Record the checksums when introducing a new dataset version.

## Usage

The raw files are inputs to the data preparation process.

They should not be used directly for production inference.

## Licensing

The original dataset license must be checked independently.

The existence of a public download does not automatically grant permission to redistribute or use the data without restrictions.

---

