# Week 8 Model Handover

**Project:** Mercer Emergency Triage Model  
**Student:** Ansarah Mohammed  
**Status:** Experimental development baseline — not approved for clinical use

## Project Summary

This repository contains a modular and reproducible machine-learning pipeline for predicting Emergency Severity Index (ESI) levels using ten triage-time predictors. Data loading, feature preparation, model training and evaluation have been separated into reusable modules under `src/`. The complete pipeline is controlled through `config.yaml`, tested using pytest and run through a single command-line entry point.

## Final Model Decision

Logistic Regression was selected as the final Phase 3 development baseline because it achieved the highest overall accuracy in the controlled Week 7 comparison while remaining more interpretable, computationally efficient and straightforward to govern than the Random Forest models.

The selected model and its hyperparameters are pinned in `config.yaml`:

- Model: Logistic Regression
- Maximum iterations: 1,000
- Random seed: 42
- Standard scaling: enabled
- Train-test split: 80/20 with stratification

The full comparison is available in [`model-selection.md`](model-selection.md).

## How to Run

Clone the repository and enter the project folder:

```bash
git clone https://github.com/Kari-2005/carisurg-portfolio.git
cd carisurg-portfolio
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on macOS and Linux:

```bash
source .venv/bin/activate
```

Install the pinned dependencies:

```bash
pip install -r requirements.txt
```
Run the sanity checks:

```bash
pytest tests/ -v
```

The expected result is `3 passed`.

Train and evaluate the selected model:

```bash
python scripts/train.py --config config.yaml
```

A successful run creates:

```text
outputs/logistic_regression_pipeline.joblib
outputs/training_metrics.json
```

## Data Location and Governance

The authorised dataset must be placed at:

```text
data/yaleemmlc_admissionprediction_triage.csv
```

The raw dataset is intentionally excluded from this public repository. It must be obtained through the programme’s authorised data-sharing process and stored in accordance with applicable privacy and governance requirements.

## Reproduced Results

| Metric | Result |
|---|---:|
| Accuracy | 0.545 |
| Macro F1-score | 0.221 |
| Weighted F1-score | 0.468 |
| ESI Level 1 recall | 0.000 |

## Known Limitations

- The selected model failed to identify any of the 16 ESI Level 1 patients in the test set, creating an unacceptable under-triage risk for clinical deployment.
- The dataset has not been confirmed as representative of Caribbean emergency departments, so external validity remains uncertain.
- The model has not undergone prospective clinical validation, subgroup fairness evaluation or formal governance and privacy review.

The model is retained as an interpretable and reproducible development baseline only. It must not independently assign triage categories, replace clinical judgement or be deployed in its current form.
