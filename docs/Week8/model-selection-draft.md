# Week 8 Draft Model-Selection Results

This table provides an audit trail of the models evaluated during Weeks 6 and
7. The models were compared using a stratified 80/20 train-test split with a
random seed of 42. Values marked **To add** will be transferred from the
original notebook outputs before the final submission rather than estimated.

| Model | Key hyperparameters | Accuracy | Macro precision | Macro recall | Macro F1 | Weighted F1 | ESI-1 recall | Training time (s) | Inference time (ms/patient) | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stratified Random Baseline | `strategy="stratified"`; `random_state=42` | 0.3750 | **To add** | **To add** | 0.2040 | 0.3750 | 0.0000 | **To add** | **To add** | Baseline comparison only |
| Logistic Regression — **Selected** | `max_iter=1000`; standard scaling; `random_state=42` | 0.5449 | 0.2757 | 0.2455 | 0.2215 | 0.4682 | 0.0000 | 1.6702 | 0.0009 | **Selected Phase 3 baseline** |
| Decision Tree | `max_depth=5`; `random_state=42` | 0.5434 | 0.2404 | 0.2417 | 0.2152 | 0.4591 | 0.0000 | 0.1263 | 0.0003 | Not selected |
| Class-weighted Logistic Regression | `class_weight="balanced"`; `random_state=42` | 0.2500 | **To add** | **To add** | 0.2010 | 0.3150 | 0.6880 | **To add** | **To add** | Week 6 refinement; not selected |
| Refined Logistic Regression | Expanded feature set including one-hot encoded chief complaint | 0.6830 | **To add** | **To add** | 0.5080 | 0.6770 | 0.2500 | **To add** | **To add** | Week 6 refinement; not selected |
| Initial Random Forest | `n_estimators=200`; `max_depth=15`; `min_samples_leaf=3`; `class_weight="balanced_subsample"`; `random_state=42` | 0.4141 | 0.2949 | 0.3252 | 0.2784 | 0.4443 | 0.0000 | 13.0728 | 0.0218 | Not selected |
| Tuned Random Forest | `n_estimators=200`; `max_depth=None`; `min_samples_leaf=8`; `max_features=None`; `class_weight="balanced"`; `random_state=42` | 0.4756 | 0.3032 | 0.3133 | 0.3021 | 0.4845 | 0.0625 | 29.0586 | 0.0559 | Experimental comparison model |

## Draft Model Decision

Logistic Regression was selected as the official Phase 3 development baseline.
It achieved the highest overall accuracy and remained easier to explain, test
and govern than the Random Forest models. It also required considerably less
training time than the tuned Random Forest.

Although the tuned Random Forest achieved a stronger macro F1-score and
correctly identified one of the 16 ESI Level 1 patients, it missed the remaining
15 and produced 20 false ESI Level 1 alerts. It also had lower overall accuracy,
showed substantial overfitting and required more computational resources.

Logistic Regression was therefore retained as the more defensible development
baseline. The tuned Random Forest will remain an experimental comparison model.
Neither model is considered ready for clinical deployment.

The full reasoning is recorded in the
[Week 7 model-choice decision journal](../decisions/2026-week-7-model-choice.md).

The final Week 7 comparison is available in the
[Week 7 final benchmark table](../Week7/Final/csvs/week7_final_benchmark.csv).

> **Draft status:** The confirmed Week 7 results and available Week 6 headline
> metrics have been added. The missing Week 6 precision, recall and timing
> values will be copied from the original notebook outputs before the Week 8
> final submission.
