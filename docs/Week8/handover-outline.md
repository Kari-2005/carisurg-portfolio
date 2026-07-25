# Mercer Triage Model Handover — Draft Outline

## 1. Project Summary

This project investigates a machine-learning clinical decision-support tool for
emergency department triage at Mercer General Hospital. The modelling pipeline
uses ten triage-time predictors to estimate Emergency Severity Index (ESI)
levels. The model is intended to support, rather than replace, clinical
judgement. Particular attention is given to ESI Level 1 performance because
failing to identify critically ill patients presents a serious clinical risk.

## 2. Final Model Decision

Logistic Regression was selected as the official Phase 3 development baseline
with `max_iter=1000`, standardised predictors and a random seed of 42. It
achieved the highest overall accuracy and remained easier to explain, test and
govern than the Random Forest models.

Although the tuned Random Forest produced a higher macro F1-score and correctly
identified one additional ESI Level 1 patient, it missed 15 of the 16 ESI Level
1 patients and produced 20 false critical alerts. It also had lower accuracy,
showed substantial overfitting, required longer training time and was less
interpretable.

The selected Logistic Regression is an experimental development baseline. It is
not ready for clinical deployment.

Full reasoning:
[Week 7 model-choice decision journal](../decisions/2026-week-7-model-choice.md)

Supporting comparison:
[Week 7 cost-benefit memo](../Week7/Final/week-7-cost-benefit.md)

## 3. How to Run

The completed pipeline will be run from the repository root using the command:

`python scripts/train.py --config config.yaml`

The final handover instructions will explain how to:

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the pinned dependencies from `requirements.txt`.
4. Place the authorised dataset in the configured local data directory.
5. Run the training command.
6. Locate the saved model and evaluation results.

## 4. Data Location and Governance

The Mercer emergency triage dataset is not stored in the public GitHub
repository. An authorised copy will be stored locally or in an approved private
location and accessed through the path specified in `config.yaml`.

The dataset is excluded from the repository using `.gitignore` and must not be
redistributed or publicly committed. Access should be limited to authorised
project personnel. The final handover will confirm the approved internal data
location and responsible governance contact.

## 5. Known Limitations

- The models were developed using data from one healthcare setting, so their
  performance may not generalise to Mercer General Hospital or other patient
  populations.
- ESI Level 1 cases were rare. The selected Logistic Regression did not
  correctly identify any of the 16 ESI Level 1 patients in the Week 7 test set,
  so it must not be treated as clinically safe or deployment-ready.
- The model has not been prospectively validated in a live emergency department
  workflow and must not replace clinician judgement.

## 6. Final-Submission Items Still to Add

- Create and confirm the final `config.yaml`.
- Create and test the `scripts/train.py` entry point.
- Pin the required library versions in `requirements.txt`.
- Add `src/features.py` and `src/utils.py` if required by the final pipeline.
- Add and run the two required pytest sanity checks.
- Confirm the approved dataset location and data-governance contact.
- Replace this outline with the final one-page handover document.

## 7. Project Contacts

- Model and code questions: Ansarah Mohammed
- Clinical questions: Dr. De Fretias
- Clinical IT and deployment questions: Martina Griffith
- Data-governance contact: To be confirmed
