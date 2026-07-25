# Mercer Triage Model Handover — Draft Outline

## 1. Project Summary

This project investigates a machine-learning clinical decision-support tool for
emergency department triage at Mercer General Hospital. The pipeline uses
available patient and triage predictors to estimate Emergency Severity Index
(ESI) levels. The model is intended to support, rather than replace, clinical
judgement. Particular attention is given to ESI Level 1 performance because
failing to identify critically ill patients presents a serious clinical risk.

## 2. Final Model Decision

Logistic Regression was selected as the Phase 3 development baseline with
`max_iter=1000`, standardised predictors and a random seed of 42. Although the
tuned Random Forest produced a higher macro F1-score and detected one
additional ESI Level 1 patient, its improvement was not sufficient to justify
its lower accuracy, false critical alerts, overfitting, longer training time,
slower inference and reduced interpretability. The selected model is an
experimental baseline and is not ready for clinical deployment.

Full reasoning: `docs/Week7/decision-journal.md` **(confirm the exact link
before final submission).**

## 3. How to Run

The completed pipeline will be run from the repository root using:

```bash
python scripts/train.py --config config.yaml
```

The final handover instructions will explain how to:

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the pinned dependencies from `requirements.txt`.
4. Place the authorised dataset in the configured local data directory.
5. Run the training command.
6. Locate the saved model and evaluation results.

## 4. Data Location and Governance

The de-identified Mercer emergency triage dataset will be stored in the local
data directory specified in `config.yaml`. The dataset will be excluded from
the public GitHub repository using `.gitignore` and should not be redistributed.
Access should be limited to authorised project personnel. The final handover
will identify the approved internal data location and confirm the responsible
governance contact.

## 5. Known Limitations

- The models were developed using data from one healthcare setting, so their
  performance may not generalise to other hospitals or patient populations.
- ESI Level 1 cases are rare. The selected Logistic Regression model did not
  correctly identify an ESI Level 1 case in the Week 7 test set, so it must not
  be treated as clinically safe or deployment-ready.
- The model has not been prospectively validated in a live emergency department
  workflow and must not replace clinician judgement.

## 6. Final-Submission Items Still to Add

- Confirm the exact Week 7 decision-journal link.
- Add the approved internal dataset location and governance contact.
- Replace draft wording with the final one-page handover.
- Confirm that `config.yaml`, `scripts/train.py`, `requirements.txt` and the two
  pytest sanity checks run successfully.

## 7. Project Contacts

- Model and code questions: Ansarah Mohammed
- Clinical questions: Dr. De Fretias
- Clinical IT and deployment questions: Martina Griffith
- Data-governance contact: To be confirmed
