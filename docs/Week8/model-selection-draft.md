# Week 8 Draft Model-Selection Results

This table provides an audit trail of the models evaluated during Weeks 6 and
7. The models were compared using a stratified 80/20 train-test split with a
random seed of 42. Values marked **To add** will be transferred from the
original notebook outputs before the final submission rather than estimated.

| Model | Key hyperparameters | Accuracy | Macro precision | Macro recall | Macro F1 | Weighted F1 | ESI-1 recall | Training time (s) | Inference time (ms/patient) | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stratified random baseline | `strategy="stratified"`; `random_state=42` | **To add** | **To add** | **To add** | **To add** | **To add** | **To add** | **To add** | **To add** | Baseline comparison only |
| Logistic Regression — **Selected** | `max_iter=1000`; standard scaling; `random_state=42` | 0.5449 | 0.2757 | 0.2455 | 0.2215 | 0.4682 | 0.0000 | 1.6702 | 0.0009 | **Selected Phase 3 baseline** |
| Decision Tree | `max_depth=5`; `random_state=42` | 0.5434 | 0.2404 | 0.2417 | 0.2152 | 0.4591 | 0.0000 | 0.1263 | 0.0003 | Not selected |
| Class-weighted Logistic Regression | `class_weight="balanced"`; `random_state=42` | 0.2500 | **To add** | **To add** | 0.2010 | 0.3150 | 0.6880 | **To add** | **To add** | Week 6 refinement; not selected |
| Refined Logistic Regression | Expanded feature set including one-hot encoded chief complaint | 0.6830 | **To add** | **To add** | 0.5080 | 0.6770 | 0.2500 | **To add** | **To add** | Week 6 refinement; not selected |
| Initial Random Forest | `n_estimators=200`; `max_depth=15`; `min_samples_leaf=3`; `class_weight="balanced_subsample"`; `random_state=42` | 0.4141 | 0.2949 | 0.3252 | 0.2784 | 0.4443 | 0.0000 | 13.0728 | 0.0218 | Not selected |
| Tuned Random Forest | `n_estimators=200`; `max_depth=None`; `min_samples_leaf=8`; `max_features=None`; `class_weight="balanced"`; `random_state=42` | 0.4756 | 0.3032 | 0.3133 | 0.3021 | 0.4845 | 0.0625 | 29.0586 | 0.0559 | Experimental model only |

## Draft Model Decision

Logistic Regression was selected as the Phase 3 development baseline. Although
the tuned Random Forest achieved a stronger macro F1-score and detected one
additional ESI Level 1 patient, the improvement was limited and came with lower
accuracy, false critical alerts, substantial overfitting, higher computational
cost and reduced interpretability. Logistic Regression was therefore retained
as the more defensible and reproducible experimental baseline. It is not ready
for clinical deployment.

The full reasoning is recorded in the Week 7 decision journal:
`docs/Week7/decision-journal.md` **(replace this path if the journal has a
different filename).**

> **Draft status:** The confirmed Week 7 results have been added. The missing
> Week 6 baseline and refinement values will be copied from the original
> notebook outputs before the Week 8 final submission.
