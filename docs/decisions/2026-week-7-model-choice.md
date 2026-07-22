# Week 7 Decision Journal: Phase 3 Model Choice

**Date:** 22 July 2026  
**Decision owner:** Ansarah Mohammed  
**Project:** Caribbean ED Validation of Machine-Learning Triage Support

## Context

- The Week 7 task required a more complex model to be compared honestly with the Week 6 Logistic Regression and Decision Tree baselines using predictive performance, compute cost and interpretability.
- The aim was not simply to select the model with the highest score, but to identify the most defensible model for continued Phase 3 development in a healthcare setting.

## Alternatives Considered

- **Logistic Regression:** The simpler Week 6 baseline, with high interpretability, low computational requirements and the highest overall accuracy in the controlled comparison.
- **Decision Tree:** A transparent baseline limited to a maximum depth of five, but with similar performance to Logistic Regression and no improvement in ESI Level 1 detection.
- **Tuned Random Forest:** A more complex model combining multiple decision trees, with improved macro-level performance but increased training time, reduced overall accuracy and lower interpretability.

## Performance Summary

| Measure | Logistic Regression | Decision Tree | Tuned Random Forest |
|---|---:|---:|---:|
| Accuracy | 0.5449 | 0.5434 | 0.4756 |
| Macro F1-score | 0.2215 | 0.2152 | 0.3021 |
| ESI Level 1 recall | 0.0000 | 0.0000 | 0.0625 |
| Training time | 1.6702 s | 0.1263 s | 29.0586 s |
| Inference time per patient | 0.0009 ms | 0.0003 ms | 0.0559 ms |
| Interpretability | High | High | Moderate |

## Decision

**Logistic Regression will remain the official Phase 3 development baseline, while the tuned Random Forest will be retained as an experimental comparison model.**

## Reasoning

- Logistic Regression achieved the highest overall accuracy and was considerably easier to explain, test and govern than the Random Forest.
- Although the Random Forest improved macro F1-score and identified one ESI Level 1 patient, it still missed 15 of the 16 critically urgent patients and produced 20 false ESI Level 1 alerts.
- The Random Forest also showed substantial overfitting and required considerably more training time, while the feature-expanded Week 6 Logistic Regression results suggested that improving the available predictors may be more valuable than increasing model complexity alone.

## Things I Do Not Yet Know

- Whether either model would perform similarly when tested using local Mercer General Hospital data, workflows and patient populations.
- Whether additional triage-time predictors, improved handling of class imbalance or alternative model settings could meaningfully improve ESI Level 1 detection without creating an unacceptable number of false alerts.

## Follow-up Actions

- Investigate clinically useful predictor expansion and feature engineering.
- Continue detailed error analysis for ESI Levels 1 and 2.
- Explore class-weighting and other methods for handling the rare ESI Level 1 class.
- Treat all models as experimental decision-support candidates rather than systems ready for clinical deployment.
