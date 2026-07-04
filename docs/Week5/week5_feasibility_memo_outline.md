
# Week 5 Feasibility Memo Outline

## One-Sentence Verdict
This dataset is suitable for building a baseline triage model, provided leakage columns are excluded, rare ESI classes are handled carefully, and results are treated as exploratory until validated in a Caribbean emergency department setting.

## Dataset Summary
The dataset contains 55,121 emergency department encounters and 226 columns. These include patient demographics, triage vital signs, arrival details, disposition-related variables, and chief complaint flags. The main target variable is `esi`, which represents Emergency Severity Index triage level.

## Top 3 Quality Concerns

1. **Class imbalance**
   ESI level 1 cases are very rare compared with ESI levels 2, 3, and 4. This may make it harder for a model to learn the sickest patient group.

2. **Outcome leakage**
   Columns such as `disposition` and `previousdispo` may contain information known after triage. These should be excluded from Week 6 modelling because a real triage model would not have access to them at the time of decision-making.

3. **External validity**
   The dataset may not fully represent a Caribbean emergency department population, workflow, staffing pattern, or resource setting. Any model built from it would need local validation before clinical use.

## Top 3 Reasons to Proceed

1. **Real triage target**
   The dataset includes the `esi` triage label, so it can support baseline supervised modelling.

2. **Clinically relevant triage features**
   The dataset includes important vital signs such as heart rate, blood pressure, respiratory rate, oxygen saturation, temperature, and glucose.

3. **Rich chief complaint information**
   The dataset contains many chief complaint flags, which may help capture why patients attended the emergency department.

## Caveats

This Week 5 analysis does not build a model yet. The visualisations and summaries only show early data quality patterns. Correlation or association should not be treated as proof of prediction. Week 6 should test baseline models while excluding leakage columns and documenting all preprocessing decisions.

## Initial Top-10 Feature Shortlist

1. age
2. triage_vital_o2
3. triage_vital_o2_device
4. triage_vital_hr
5. triage_vital_rr
6. triage_vital_sbp
7. triage_vital_dbp
8. triage_vital_temp
9. triage_glucose
10. selected chief complaint flags
