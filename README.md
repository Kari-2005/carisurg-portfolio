# CariSurg Week 0 Portfolio

## Introduction

This repository contains my Week 0 submissions for the CariSurg MedTech Pathways Programme. Week 0 focuses on orientation, onboarding, Python readiness, basic data cleaning, exploratory data analysis, clinical understanding, and GitHub submission.

The purpose of this repository is to keep all seven Week 0 assignments in one place. Each assignment will show a different part of the onboarding process, from setting up my environment and cleaning data to visualizing patient information and thinking about simple at-risk patient logic.

This repository is also part of my practice in using GitHub to document technical work clearly and professionally.

## Background on CariSurg MedTech Pathways

CariSurg MedTech Pathways is a programme focused on helping Caribbean students build skills in healthcare technology, clinical AI, and medical innovation. One of the main ideas behind the programme is that Caribbean students should be part of building and understanding the technologies that may shape healthcare in the region.

Healthcare is becoming more data-driven, and AI tools are increasingly being used to support patients and clinicians. However, Caribbean healthcare systems have their own realities, including resource limitations, different patient populations, and different clinical settings. Because of this, it is important for students in the Caribbean to understand both the technology and the healthcare context.

For Week 0, I worked with a reduced and de-identified emergency triage dataset from the fictional Mercer General Hospital Emergency Department. The dataset includes patient information and common vital signs such as pulse, temperature, respiratory rate, blood pressure, and oxygen saturation.

## Week 0 Overview

Week 0 is about getting comfortable with the tools and workflow that will be used during the programme. This includes:

- Setting up Google Colab and Google Drive
- Confirming the Python environment
- Using pandas for data cleaning
- Creating visualizations
- Writing short clinical explanations
- Creating simple rule-based logic
- Uploading work to GitHub

The main goal for this week is not to create a perfect project, but to show progress, submit consistently, and become more confident using the tools.

## Week 0 Assignment Tracker

| Day | Assignment | Status |
|---|---|---|
| Day 1 | Clean only the `Gender` column using Python | Completed |
| Day 2 | Group column-cleaning task | To be added |
| Day 3 | Data visualization of different dataset columns | To be added |
| Day 4 | Paragraph on a chosen vital sign and abnormal ranges | To be added |
| Day 5 | Paragraph about other metrics not being considered | To be added |
| Day 6 | Pseudocode for at-risk patient rule | To be added |
| Day 7 | Final notebook, GitHub repo link, and career slide deck | To be added |

---

# Assignment 1: Cleaning the Gender Column in the Mercer General ED Triage Dataset

## Overview

This assignment is my Week 0 Day 1 submission for the CariSurg MedTech Pathways Programme. For this task, I worked with the Mercer General Emergency Department triage dataset and focused only on cleaning the `Gender` column.

The purpose of this assignment was to practise basic data cleaning using Python and pandas. Even though the task focused on one column, it showed me how important it is to check and clean data before doing any deeper analysis, visualization, or machine learning.

## Dataset Context

The dataset is based on emergency triage information. In a real emergency department, triage data helps healthcare workers understand how urgent a patient’s condition may be. This type of data may include demographic information and vital signs that support clinical decision-making.

For this assignment, the focus was not on building a model yet. The focus was on preparing one part of the dataset properly by cleaning inconsistent values in the `Gender` column.

## Problem Identified

When I checked the `Gender` column, I noticed that the same gender categories were written in different ways.

Some of the values included:

- `Male`
- `MALE`
- `Female`
- `FEMALE`
- `1`
- `0`

This was an issue because Python may treat these as separate categories even though some of them mean the same thing. For example, `Male`, `MALE`, and `1` all represent male patients, but they are not written in the same format.

If this was not cleaned, it could affect future analysis, graphs, summaries, or machine learning work.

## Objective

The main objective of this assignment was to clean the `Gender` column by converting inconsistent gender values into a standard numerical format.

The cleaned format used was:

| Value | Meaning |
|---:|---|
| `0` | Female |
| `1` | Male |
| `2` | Non-binary / future consideration |

The current dataset only contained male and female values, but I included non-binary values in the mapping as a future consideration.

## My Cleaning Approach

For this assignment, I approached the cleaning by first converting all the values to lowercase before mapping them.

Instead of mapping every capitalized version separately, such as `Male`, `MALE`, and `male`, I made the values consistent first. I converted the column values to strings, removed extra spaces, and made everything lowercase.

This means that values like:

- `MALE`
- `Male`
- `male`

would all become:

```text
male
```

before being mapped.

I felt this made the code cleaner and easier to manage because I did not have to list every possible capitalization of the same word.

I also added extra cases for `m` and `f` in case future datasets use abbreviations instead of full words. Another thing I added was non-binary options such as `non-binary`, `nonbinary`, and `nb` for future datasets that may include more gender categories.

## Gender Mapping Used

```python
gender_map = {
    # Male values
    'male': 1,
    'm': 1,
    '1': 1,

    # Female values
    'female': 0,
    'f': 0,
    '0': 0,

    # Non-binary values for future consideration
    'non-binary': 2,
    'nonbinary': 2,
    'nb': 2,
    '2': 2
}
```

## Code Used to Clean the Column

Before applying the mapping dictionary, I converted the values to strings, removed extra spaces, and made everything lowercase.

```python
df_raw['Gender_Cleaned'] = (
    df_raw['Gender']
    .astype(str)
    .str.strip()
    .str.lower()
    .map(gender_map)
)
```

The `.astype(str)` part makes sure the values are treated as text. The `.str.strip()` part removes extra spaces before or after each value. The `.str.lower()` part converts everything to lowercase. The `.map(gender_map)` part then applies the mapping dictionary and converts the values into the chosen numerical categories.

## Future Consideration for Non-binary Values

Although the dataset did not include non-binary values, I wanted to include them in the mapping for future use. Real-world healthcare datasets may include more than just male and female categories, so I thought it was better to make the cleaning process more flexible.

I did not add any fake non-binary data to the dataset. I only added the mapping so that if a future dataset contains non-binary values, the code can handle them instead of turning them into missing values.

It is also important to remember that the numbers are only category labels. For example, `2` does not mean non-binary is greater than male or female. The numbers are just used to represent different groups.

For future machine learning work, one-hot encoding may be better because gender is a category, not a ranked number.

## Validation

After creating the cleaned column, I checked the results using:

```python
df_raw['Gender_Cleaned'].value_counts(dropna=False)
```

This showed how many values were mapped into each category.

I also checked for missing or unmapped values using:

```python
df_raw['Gender_Cleaned'].isnull().sum()
```

This was important because if any original value was not included in the dictionary, it would show up as `NaN` after mapping. Checking for missing values helped me confirm whether the cleaning worked properly.

After confirming that the cleaned column was correct, I replaced the original dirty `Gender` column with the cleaned version.

```python
if 'Gender' in df_raw.columns:
    df_raw = df_raw.drop(columns=['Gender'])

df_raw = df_raw.rename(columns={'Gender_Cleaned': 'Gender'})
```

## Final Result

After cleaning, the `Gender` column was standardized into numerical values:

| Value | Meaning |
|---:|---|
| `0` | Female |
| `1` | Male |
| `2` | Non-binary / future consideration |

This makes the column easier to work with for future analysis and helps avoid confusion caused by inconsistent formatting.

## Why This Cleaning Step Matters

This task showed me that even a simple column can create problems if the values are inconsistent. If the same category is written in different ways, it can affect summaries, graphs, and any future machine learning work.

By cleaning the `Gender` column, the dataset became more consistent and easier to use. This is an important first step before doing exploratory data analysis or building any type of clinical AI model.

## Reflection for Assignment 1

This assignment helped me understand why data cleaning matters before doing any analysis. At first, the `Gender` column looked simple, but after checking it properly, I saw that the same values were written in different ways.

One thing I did differently was converting all the gender values to lowercase before mapping them. This made the code cleaner because I did not have to map every capitalized version separately. I also added possible `m` and `f` abbreviations, along with non-binary options, to make the code more useful for future datasets.

By using pandas and a mapping dictionary, I was able to clean the column in a structured way. I also learned the importance of checking the cleaned results instead of assuming the code worked correctly.

Overall, this was a useful first step in getting comfortable with Python, pandas, Google Colab, and GitHub for the rest of Week 0.

---

# Assignment 2: Group Column-Cleaning Task

This section will be updated after completing the Day 2 group task.

## Planned Focus

For Assignment 2, the goal will be to work as part of a group to clean another column in the dataset. This will build on the same skills used in Assignment 1, such as checking unique values, identifying inconsistencies, applying cleaning methods, and validating the final result.

---

# Assignment 3: Data Visualization

This section will be updated after completing the Day 3 visualization task.

## Planned Focus

For Assignment 3, the goal will be to create visualizations using different columns in the triage dataset. This may include histograms, scatter plots, or other basic plots to help understand patterns in the data.

---

# Assignment 4: Chosen Vital Sign Explanation

This section will be updated after completing the Day 4 clinical explanation task.

## Planned Focus

For Assignment 4, I will choose one vital sign from the dataset and explain what it means in simple language. I will also describe the normal range and what abnormal values may suggest in an emergency department setting.

---

# Assignment 5: Other Metrics Not Considered

This section will be updated after completing the Day 5 task.

## Planned Focus

For Assignment 5, I will discuss other clinical metrics or patient factors that may be important but are not being fully considered in the dataset or simple analysis.

---

# Assignment 6: At-Risk Patient Logic

This section will be updated after completing the Day 6 pseudocode task.

## Planned Focus

For Assignment 6, I will write pseudocode or a simple rule-based approach to flag patients as at-risk based on a clinical threshold that can be explained and defended.

---

# Assignment 7: Final Week 0 Submission

This section will be updated after completing the Day 7 final submission.

## Planned Focus

For Assignment 7, I will combine the Week 0 work into a final documented notebook and make sure the repository is organized for submission.

---

# Tools Used During Week 0

For Week 0, I used or will use:

- Python
- Google Colab
- Google Drive
- pandas
- NumPy
- matplotlib
- GitHub

# Repository Contents

| File | Description |
|---|---|
| `Week0_Tutorial1_EnvSetup_and_Cleaning_Gender.ipynb` | Notebook containing the Assignment 1 Gender column cleaning task |
| `README.md` | Explanation of the Week 0 repository, assignment background, cleaning method, and reflections |

More files will be added as I complete the remaining Week 0 assignments.

# Data Privacy Note

Since this dataset is related to healthcare and emergency triage, I understand that it is important to be careful when sharing data publicly. Even if the dataset is reduced and de-identified, raw healthcare data should only be uploaded if permission is given by the programme or dataset provider.

# Overall Week 0 Reflection

Week 0 is helping me build the foundation for the rest of the programme. I am learning how to work with a clinical dataset, document my steps, ask better questions, and use GitHub to show my progress.

Even though the first assignment was focused on one column, it showed me that small data issues can become bigger problems later if they are not handled properly. This week is helping me practise being consistent, careful, and clear in how I approach data-related tasks.
