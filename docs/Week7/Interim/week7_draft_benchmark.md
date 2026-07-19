# Week 7 Draft Model Benchmark

**Student:** Ansarah Mohammed  
**Project:** Caribbean ED Validation of Machine-Learning Triage Support  
**Dataset:** Mercer Emergency Department Triage Dataset  
**Test-set size:** 11,025 patient records  
**Random seed:** 42  

## Purpose

This draft benchmark compares the two original Week 6 baseline models with a tuned Random Forest classifier developed during Week 7.

All three models used the same ten triage-time predictor variables, the same 80/20 stratified train-test split and the same random seed of 42. This allowed the effect of additional model complexity to be examined without changing the patients or predictor variables used in the comparison.

The models were assessed using accuracy, macro precision, macro recall, macro F1-score, weighted F1-score, ESI Level 1 precision and recall, training time, inference time per patient and interpretability.

## Initial Benchmark Table

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 | ESI 1 Precision | ESI 1 Recall | Training Time (s) | Inference Time (ms/patient) | Interpretability |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Logistic Regression | 0.5449 | 0.2757 | 0.2455 | 0.2215 | 0.4682 | 0.0000 | 0.0000 | 0.9913 | 0.0007 | High |
| Decision Tree | 0.5434 | 0.2404 | 0.2417 | 0.2152 | 0.4591 | 0.0000 | 0.0000 | 0.0835 | 0.0002 | High |
| Tuned Random Forest | 0.4756 | 0.3032 | 0.3133 | 0.3021 | 0.4845 | 0.0476 | 0.0625 | 27.5167 | 0.0540 | Moderate |

*Training and inference times were measured in Google Colab and may vary depending on the available runtime hardware. Inference time was calculated per patient using the median of five test-set prediction runs.*

## ESI Level 1 Error Comparison

| Model | True ESI 1 Patients | Correctly Identified | Missed ESI 1 Patients | Miss Rate | Predicted as ESI 2 | Predicted as ESI 3 | Predicted as ESI 4 | Predicted as ESI 5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Logistic Regression | 16 | 0 | 16 | 100.0% | 9 | 7 | 0 | 0 |
| Decision Tree | 16 | 0 | 16 | 100.0% | 9 | 7 | 0 | 0 |
| Tuned Random Forest | 16 | 1 | 15 | 93.8% | 11 | 2 | 2 | 0 |


## Metric Justification

ESI Level 1 recall was treated as the primary clinical safety metric because it measures the proportion of genuinely critical patients correctly identified by the model. Missing an ESI Level 1 patient may delay immediate assessment, resuscitation or another life-saving intervention.

However, recall was not considered alone. A model could increase recall by predicting ESI Level 1 too frequently, creating unnecessary false alarms and over-triage. ESI Level 1 precision was therefore also reviewed.

Macro F1 was included because it gives equal importance to all five ESI categories and makes poor performance among uncommon classes more visible. Weighted F1 was also reported to describe overall patient-level performance, although it may be influenced more strongly by the common ESI Level 2 and Level 3 groups.

Accuracy was reported for completeness but was not used as the only measure because the dataset was imbalanced. Confusion matrices and the ESI Level 1 error table were used to show the direction and clinical seriousness of the classification errors.


## Computational and Interpretability Trade-Offs

The Decision Tree was the fastest model to train and predict. Logistic Regression also had a low computational cost and remained relatively easy to explain through its model coefficients.

The tuned Random Forest required considerably more training time because it combined predictions from many decision trees. Its inference time was also higher than the two baselines, although the absolute prediction time remained below one millisecond per patient in the Colab environment.

Logistic Regression and the bounded Decision Tree were rated as highly interpretable. The Random Forest was rated as moderately interpretable because global feature importance can show which variables influenced the model overall, but the combined decisions of many trees cannot be followed as directly as one small tree or a Logistic Regression model.


## Draft Findings

The tuned Random Forest achieved the strongest macro F1-score at 0.3021 and the strongest macro recall at 0.3133. This suggests that it distributed its performance more evenly across the five ESI classes than the two Week 6 baseline models.

The Random Forest also achieved a slightly higher weighted F1-score of 0.4845. However, its overall accuracy decreased to 0.4756, compared with approximately 0.545 for Logistic Regression.

The two Week 6 baseline models failed to identify any of the 16 ESI Level 1 patients. The tuned Random Forest identified one, increasing ESI Level 1 recall to 0.0625. However, 15 critical patients were still missed, including two assigned to ESI Level 4.

ESI Level 1 precision was only 0.0476, showing that most patients predicted as Level 1 were false alarms. This could increase staff workload and contribute to alert fatigue if the model were deployed.

Cross-validation also showed substantial overfitting. The selected Random Forest configuration achieved a training macro F1-score of 0.7609 but a validation macro F1-score of only 0.2879.

The tuned Random Forest therefore improved balanced performance across the five ESI classes, but its limited improvement in ESI Level 1 detection did not clearly justify its lower accuracy, greater computational cost, reduced interpretability and false critical alerts.

## Provisional Recommendation

**Retain Logistic Regression as the current baseline for Phase 3 while keeping the Random Forest as an experimental candidate for further error analysis and feature development.**

The Random Forest produced better macro-level performance, but it did not yet provide a large enough improvement in critical-patient recognition to justify replacing the simpler and more interpretable Logistic Regression model.

This recommendation is provisional and will be reviewed during preparation of the final Week 7 cost-benefit memo.
