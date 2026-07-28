# Week 8 Model-Selection Results

This document provides an audit trail of the models evaluated during Weeks 6 and 7. Unless otherwise stated, the models used a stratified 80/20 train-test split and a fixed random seed of 42. The selected Phase 3 model is clearly identified below.

## Model Comparison

| Model | Key configuration | Accuracy | Macro precision | Macro recall | Macro F1 | Weighted F1 | ESI Level 1 recall | Training time (s) | Inference time (ms/patient) | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stratified Random Baseline | `strategy="stratified"`; `random_state=42` | 0.3750 | Not recorded | Not recorded | 0.2040 | 0.3750 | 0.0000 | Not recorded | Not recorded | Baseline comparison only |
| Logistic Regression — **Selected** | Ten predictors; standard scaling; `max_iter=1000`; `random_state=42` | 0.5449 | 0.2757 | 0.2455 | 0.2215 | 0.4682 | 0.0000 | 1.6702 | 0.0009 | **Selected Phase 3 development baseline** |
| Decision Tree | Ten predictors; `max_depth=5`; `random_state=42` | 0.5434 | 0.2404 | 0.2417 | 0.2152 | 0.4591 | 0.0000 | 0.1263 | 0.0003 | Not selected |
| Class-weighted Logistic Regression | Ten predictors; `class_weight="balanced"`; `random_state=42` | 0.2500 | Not recorded | Not recorded | 0.2010 | 0.3150 | 0.6880 | Not recorded | Not recorded | Week 6 class-imbalance experiment |
| Refined Logistic Regression | Expanded feature set including one-hot encoded chief complaints | 0.6830 | Not recorded | Not recorded | 0.5080 | 0.6770 | 0.2500 | Not recorded | Not recorded | Week 6 feature-expansion experiment |
| Initial Random Forest | `n_estimators=200`; `max_depth=15`; `min_samples_leaf=3`; `class_weight="balanced_subsample"`; `random_state=42` | 0.4141 | 0.2949 | 0.3252 | 0.2784 | 0.4443 | 0.0000 | 13.0728 | 0.0218 | Not selected |
| Tuned Random Forest | `n_estimators=200`; `max_depth=None`; `min_samples_leaf=8`; `max_features=None`; `class_weight="balanced"`; `random_state=42` | 0.4756 | 0.3032 | 0.3133 | 0.3021 | 0.4845 | 0.0625 | 29.0586 | 0.0559 | Retained as an experimental comparison model |

Values marked **Not recorded** were not included in the saved Week 6 summary outputs and have not been estimated. This preserves an accurate audit trail rather than introducing unsupported results.

## Comparability Note

The Logistic Regression, Decision Tree and Random Forest models evaluated during Week 7 used the same ten triage-time predictors and the same train-test split. These results therefore formed the main controlled comparison used to select the final Phase 3 model.

The class-weighted and refined Logistic Regression models were additional Week 6 experiments. In particular, the refined model used a larger feature set that included one-hot encoded chief complaints. Its higher performance shows that expanding the available predictors may be valuable, but its results are not directly comparable with the controlled ten-feature Week 7 benchmark. It was not the model formally recommended and pinned at the end of Week 7.

## Final Model Decision

Logistic Regression was selected as the official Phase 3 development baseline. It achieved the highest overall accuracy in the controlled Week 7 comparison and remained easier to explain, test and govern than the Random Forest models. Its training and inference requirements were also considerably lower than those of the tuned Random Forest.

The tuned Random Forest achieved the strongest macro F1-score and identified one of the 16 ESI Level 1 patients. However, it missed the remaining 15 critically urgent patients, produced 20 false ESI Level 1 alerts, reduced overall accuracy and showed evidence of overfitting. It also required substantially more training time and offered lower interpretability.

The selected Logistic Regression is pinned in `config.yaml` with ten predictors, standard scaling, `max_iter=1000` and `random_state=42`. The complete pipeline reproduced an accuracy of 0.545, macro F1-score of 0.221, weighted F1-score of 0.468 and ESI Level 1 recall of 0.000.

## Safety Limitation

The selected model did not correctly identify any of the 16 ESI Level 1 patients in the test set. It must therefore be treated as an experimental and reproducible development baseline, not as a model ready for clinical deployment.

Future work should prioritise improved triage-time predictors, class-imbalance handling, detailed error analysis and validation using representative Caribbean emergency department data.

Further reasoning is recorded in the [Week 7 model-choice decision journal](../decisions/2026-week-7-model-choice.md). The controlled Week 7 results are available in the [final benchmark table](../Week7/Final/csvs/week7_final_benchmark.csv).
