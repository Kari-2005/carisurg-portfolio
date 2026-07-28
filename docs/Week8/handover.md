# Week 8 Model Handover

**Project:** Mercer Emergency Triage Model  
**Student:** Ansarah Mohammed  
**Status:** Experimental development baseline — not approved for clinical use

## Purpose

This repository contains a reproducible machine-learning pipeline for predicting Emergency Severity Index (ESI) levels using ten triage-time predictors. The final Phase 3 model is Logistic Regression, selected following the controlled model comparison completed during Week 7.

The model configuration, selected features, train-test split, preprocessing settings and fixed hyperparameters are recorded in `config.yaml`.

## Monday-Morning Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kari-2005/carisurg-portfolio.git
cd carisurg-portfolio

```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the pinned dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the authorised dataset

The dataset is intentionally excluded from GitHub to prevent unauthorised redistribution. Obtain the approved file through the programme’s authorised data-sharing process and place it at:

```text
data/yaleemmlc_admissionprediction_triage.csv
```

The filename and location must match the path recorded in `config.yaml`.

### 5. Run the sanity checks

```bash
pytest tests/ -v
```

The expected result is:

```text
3 passed
```

These checks confirm that the required data schema is enforced and that the model pipeline can train and generate predictions using synthetic data.

### 6. Train the selected model

```bash
python scripts/train.py --config config.yaml
```

A successful run creates:

```text
outputs/logistic_regression_pipeline.joblib
outputs/training_metrics.json
```

## Reproduced Results

The verified pipeline used 55,121 complete rows, with 44,096 training rows and 11,025 testing rows.

| Metric | Result |
|---|---:|
| Accuracy | 0.545 |
| Macro F1-score | 0.221 |
| Weighted F1-score | 0.468 |
| ESI Level 1 recall | 0.000 |

## Repository Guide

| Location | Purpose |
|---|---|
| `config.yaml` | Final model, features, split, preprocessing and output settings |
| `src/data.py` | Data loading and train-test splitting |
| `src/features.py` | Schema validation and feature preparation |
| `src/model.py` | Model construction, training and evaluation |
| `src/utils.py` | Configuration, output-directory and metrics utilities |
| `scripts/train.py` | One-command training entry point |
| `tests/` | Data and model sanity checks |
| `docs/Week8/model-selection.md` | Auditable comparison of models tested during Weeks 6–7 |

## Known Limitations and Safety Warning

The selected Logistic Regression model failed to identify any of the 16 ESI Level 1 patients in the test set. It must not be used to independently assign triage categories, replace clinical judgement or support deployment decisions in its current form.

The dataset is not confirmed as representative of Caribbean emergency departments, and performance may change across hospitals, populations and workflows. Future development should prioritise improved critical-patient recall, stronger triage-time predictors, class-imbalance handling, subgroup evaluation, calibration, external validation and clinician-led review.

The model is retained as an interpretable and reproducible development baseline only. Any future clinical use would require formal governance, privacy review, prospective validation and continued human oversight.
