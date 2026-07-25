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

The completed pipeline will be run from the repository root using:

```bash
python scripts/train.py --config config.yaml
