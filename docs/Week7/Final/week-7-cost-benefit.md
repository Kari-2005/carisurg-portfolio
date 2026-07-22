# Week 7 Cost–Benefit Memo: Model Optimisation and Trade-offs

**To:** Dr. De Fretias, Mercer General Hospital ED Board, & Martina Griffith, Clinical IT Lead  
**From:** Ansarah Mohammed  
**Date:** 22 July 2026  
**Subject:** Phase 3 Triage Model Recommendation  

**Logistic Regression should remain the Phase 3 development baseline because the tuned Random Forest did not improve critical-patient detection enough to justify its lower accuracy, greater complexity and higher false-alert rate.**

## Dataset and Methods

This analysis compared the original Week 6 Logistic Regression and Decision Tree models with a more complex Random Forest model. All three models used the same emergency department dataset, ten triage-time predictors, 80/20 stratified train-test split and random seed of 42. Keeping these conditions constant allowed the modelling approaches to be compared fairly. The predictors were age, oxygen-device use, oxygen saturation, chest pain, shortness of breath, altered mental status, triage glucose, heart rate, respiratory rate and systolic blood pressure. Information recorded after triage was excluded because it would not be available when a real prediction was made.

A Random Forest was selected because it extends the Decision Tree baseline by combining multiple trees while still allowing overall feature importance to be reviewed. It therefore provided a practical test of whether moderate additional complexity could improve performance without moving directly to a less interpretable neural network. The test set contained 11,025 encounters, including only 16 ESI Level 1 patients. Models were compared using accuracy, macro precision, macro recall, macro F1-score, weighted F1-score, training time, inference time and interpretability. ESI Level 1 performance was examined separately because missing the most urgent patients presents the greatest safety risk. Week 6 also included a feature-expanded Logistic Regression model with additional predictors. It was not included in this controlled comparison because its performance could have been influenced by the extra information rather than the model type alone.

## Benchmark Results

**Table 1. Controlled comparison of the Week 6 baseline models and tuned Random Forest**

| Measure | Logistic Regression | Decision Tree | Random Forest |
|---|---:|---:|---:|
| Accuracy | 0.5449 | 0.5434 | 0.4756 |
| Macro precision | 0.2757 | 0.2404 | 0.3032 |
| Macro recall | 0.2455 | 0.2417 | 0.3133 |
| Macro F1-score | 0.2215 | 0.2152 | 0.3021 |
| Weighted F1-score | 0.4682 | 0.4591 | 0.4845 |
| ESI Level 1 recall | 0.0000 | 0.0000 | 0.0625 |
| Training time | 1.6702 s | 0.1263 s | 29.0586 s |
| Inference per patient | 0.0009 ms | 0.0003 ms | 0.0559 ms |
| Interpretability | High | High | Moderate |

*Timing results were recorded in Google Colab and may vary with the available hardware.*

These timings compare the relative computational demands of the models only. They do not include the additional costs of hospital-system integration, memory use, monitoring, retraining, maintenance or investigation of model errors in Mercer’s actual IT environment.

The Random Forest achieved the highest macro F1-score, indicating more balanced performance across the five ESI levels. However, its overall accuracy fell from 0.5449 for Logistic Regression to 0.4756.

Its improvement for ESI Level 1 was also limited. The Random Forest correctly identified only one of the 16 ESI Level 1 patients, giving a recall of 0.0625 and a miss rate of 93.8%. It predicted 21 patients as ESI Level 1, but 20 of these alerts were incorrect. Two genuine ESI Level 1 patients were also assigned to ESI Level 4, representing serious under-triage.

## Arguments Supporting Logistic Regression

### 1. Higher overall accuracy

Logistic Regression correctly classified a greater proportion of patients than the Random Forest. Accuracy should not be considered alone because the ESI classes are imbalanced, but a decrease of approximately seven percentage points is still important. The Random Forest did not provide enough improvement in critical-patient detection to justify this loss.

### 2. Greater interpretability

Logistic Regression is easier to explain to clinicians and governance staff. Its coefficients can show how individual variables influence predictions. The Random Forest combines many decision trees, making a single prediction more difficult to explain quickly. In a healthcare setting, clinicians should be able to understand and question model recommendations.

### 3. Lower technical burden

Logistic Regression trained in approximately 1.67 seconds, compared with 29.06 seconds for the Random Forest. Although both models predicted patients quickly, the Random Forest would require more memory, testing, monitoring and maintenance. The simpler model therefore presents a lower initial burden for Mercer IT Governance.

## Arguments Against Logistic Regression

### 1. Weak minority-class performance

Logistic Regression achieved a macro F1-score of only 0.2215. Its higher accuracy was influenced mainly by the more common ESI Level 2 and Level 3 patients, while performance on the less common classes remained poor.

### 2. Limited ability to capture complex relationships

Emergency triage may depend on interactions between multiple vital signs and patient characteristics. Random Forests can recognise non-linear patterns more easily than Logistic Regression. The stronger Random Forest macro scores suggest that some useful relationships may have been missed by the simpler model.

### 3. Failure to identify ESI Level 1 patients

Logistic Regression did not correctly identify any of the 16 ESI Level 1 patients. It is therefore not suitable for clinical deployment in its current form. Retaining it means using it as a development baseline, not approving it for patient care.

## Risks and Unknowns

The greatest limitation is the small number of ESI Level 1 patients. Because only 16 were present in the test set, the Random Forest’s improvement represents only one correctly identified patient and may not be stable.

False alerts are another concern. Twenty of the Random Forest’s 21 ESI Level 1 warnings were incorrect. Frequent false warnings could increase staff workload and contribute to alert fatigue, where clinicians become less responsive to repeated alerts.

The Random Forest also showed evidence of overfitting. Its training macro F1-score was approximately 0.761, while its cross-validation score was approximately 0.288. This suggests that it learned the training data much better than it generalised to unseen patients.

The ten selected predictors may also be insufficient to distinguish all five ESI levels. The improved feature-expanded Logistic Regression results from Week 6 suggest that adding useful triage information may provide more benefit than immediately increasing model complexity.

Finally, the dataset was not collected at Mercer General Hospital. Differences in patient populations, documentation and workflow could affect performance. Local retrospective validation would therefore be required before any clinical pilot.

## Recommendation

Logistic Regression should remain the official Phase 3 development baseline because it achieved the highest overall accuracy, required less computation and was easier to explain and govern.

The Random Forest should remain an experimental comparison model. Its stronger macro F1-score suggests that greater model complexity may eventually provide value, but its current improvement was not clinically sufficient. It missed 15 of the 16 ESI Level 1 patients, generated 20 false critical alerts, reduced accuracy and showed substantial overfitting.

Phase 3 should prioritise improved predictor selection, class-weighting approaches and detailed error analysis for ESI Levels 1 and 2. Any future model should be validated using local Mercer data, used only as decision support and leave final triage authority with clinicians.

## Final Decision

**Retain Logistic Regression as the Phase 3 development baseline, continue evaluating the Random Forest experimentally, and prioritise better predictors and local validation before deployment.**
