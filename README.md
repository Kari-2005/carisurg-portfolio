# CariSurg Portfolio

This repository contains my CariSurg MedTech Pathways portfolio. It documents my technical, clinical, and research work across the programme, with a focus on emergency department triage, healthcare data cleaning, clinical reasoning, and AI-assisted decision support.

## Purpose

The purpose of this repository is to keep my CariSurg work organised, reproducible, and easy to review.

It is intended for:

- CariSurg tutors and reviewers
- Clinical or technical reviewers
- Future collaborators who need to understand the project structure quickly
- My own portfolio development throughout the programme

## Project Context

The early work in this repository focuses on a reduced emergency triage dataset from the fictional Mercer General Hospital Emergency Department.

Week 0 introduced Python, pandas, data cleaning, exploratory analysis, visualisation, and simple clinical reasoning.

Week 1 focused on literature review and a proposal for AI-assisted emergency triage support.

This repository is structured to support audit-ready work, with clear folders for notebooks, written documents, data notes, and future reusable source code.

## Repository Structure

```text
carisurg-portfolio/
├── data/          # Data notes only; dataset is not uploaded publicly
├── docs/          # Written reports, proposals, PDFs, figures, and evidence
├── notebooks/     # Jupyter notebooks for data cleaning and analysis
├── src/           # Reserved for reusable Python code later in the programme
├── .gitignore     # Files and folders Git should not track
├── LICENSE        # MIT licence
├── README.md      # Main project overview
└── requirements.txt
```

## How to Run the Notebooks

1. Clone the repository:

```bash
git clone https://github.com/Kari-2005/carisurg-portfolio.git
cd carisurg-portfolio
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Open the notebooks:

```bash
jupyter lab
```

Then navigate to relevant week folder:
For example:
```text
notebooks/Week0/
notebooks/Week5/
```
Some notebooks may also be run in Google Colab if the dataset is stored privately in Google Drive. The raw datasets are not stored in this public repository, so file paths may need to be updated before running the notebooks.

## Data Privacy

The healthcare-related datasets used in this repository are not uploaded publicly.

Even when data is reduced or de-identified, raw clinical data should not be shared publicly unless permission is clearly given by the programme or dataset provider.

When running the notebooks, datasets should be stored locally or in a private Google Drive location. This repository only includes notebooks, written outputs, summary figures, and data notes needed for review.

## Current Contents

### Week 0

Week 0 includes:

- Environment setup and Python readiness
- Gender column cleaning
- SBP, DBP, and MAP cleaning
- Exploratory visualisation
- Clinical explanation of MAP
- Discussion of SpO₂ as an additional triage metric
- Rule-based at-risk patient logic
- Career planning slide deck

### Week 1

Week 1 includes:

- Literature review on emergency department triage
- AI-assisted triage research summaries
- Problem statement and proposed solution for Mercer General Hospital
- Proposal documents with Vancouver-style references

## Tools Used

- Python
- pandas
- NumPy
- matplotlib
- Jupyter Notebook / Google Colab
- Git and GitHub
- Zotero for reference management

### Week 2

Week 2 focused on project setup, documentation, version control, and reference management. The goal was to make the `carisurg-portfolio` repository public, organised, reproducible, and easy for a clinical or technical reviewer to understand.

Week 2 includes:

- Restructuring the repository into clear folders for `data/`, `docs/`, `notebooks/`, and `src/`
- Creating and updating key repository files, including `README.md`, `LICENSE`, `.gitignore`, and `requirements.txt`
- Moving Week 0 and Week 1 work into the organised repository structure
- Practising the GitHub workflow using a feature branch, commits, pull request, and merge
- Setting up Zotero for reference management
- Updating the Week 1 proposal with auto-generated citations and bibliography
- Sharing evidence of the GitHub workflow through a pull request screenshot

Main Week 2 takeaway:

This week strengthened the audit-readiness of the project. The repository was organised so that future reviewers could quickly understand the project purpose, locate deliverables, and follow the development workflow.

### Week 3

Week 3 focused on healthcare workflows and systems thinking. The goal was to understand how an AI-assisted triage tool would fit into the real emergency department workflow rather than designing the tool only from a technical perspective.

Week 3 includes:

- Mapping the current Mercer General Hospital emergency department triage workflow
- Creating a flow or relationship diagram showing the triage process from arrival to disposition
- Identifying possible AI plug-in points within the triage workflow
- Naming key workflow constraints such as limited nurse time, EHR delays, inconsistent data capture, alert fatigue, and staff workload
- Identifying clinical stakeholders and their main concerns
- Expanding the literature review to include workflow, implementation, and deployment-focused sources
- Updating the preliminary proposal with a systems-thinking section, diagram, constraints, and stakeholder considerations

Main Week 3 takeaway:

This week helped shift the project from a model-focused idea to a workflow-aware clinical support tool. The proposed AI system should support triage staff within existing emergency department constraints, not add unnecessary workload or disrupt patient flow.

### Week 4

Week 4 focused on ethics, safety, and risk awareness in healthcare technology. The goal was to identify the main risks of AI-assisted triage and propose practical mitigations before any model is considered for clinical use.

Week 4 includes:

- Developing a risk register with risks across AI-technical, operational, ethical, and equity categories
- Assessing likelihood and impact for each named risk
- Proposing mitigations and measurable signals of success
- Documenting a real-world healthcare AI harm case with root-cause analysis
- Expanding the literature review to include ethics, safety, fairness, and governance sources
- Adding a risk analysis section to the preliminary proposal
- Reflecting on AI augmentation versus AI replacement in clinical work

Main Week 4 takeaway:

This week strengthened the safety and ethics foundation of the project. The proposed triage tool should be treated as clinical decision support, not a replacement for clinicians, and should be evaluated carefully for bias, automation risk, alert fatigue, patient safety, and Caribbean external validity.

### Week 5

Week 5 focused on assessing whether a 225-feature emergency department dataset was suitable for baseline triage modelling in Week 6. The work included data profiling, missingness review, ESI class distribution analysis, demographic and chief complaint exploration, data-quality visualisations, leakage checks, and a clinical feasibility memo for Dr. De Fretias and the Mercer General Hospital Emergency Department Board.

Week 5 includes:

- Full exploratory data analysis notebook: `notebooks/Week5/Week5_Final_AnsarahMohammed.ipynb`
- Three-page feasibility memo: `docs/Week5/Week5_Feasibility_Memo_AnsarahMohammed.pdf`
- Data-quality visualisations and supporting figures in `docs/Week5/`
- Top-10 feature shortlist for Week 6 baseline modelling
- Notes on key caveats, including outcome leakage, ESI class imbalance, and Caribbean external validity

Main Week 5 conclusion:

The dataset is suitable for building a Week 6 baseline triage model, provided leakage columns such as `disposition` and `previousdispo` are excluded, rare ESI classes are evaluated carefully, and findings are treated as exploratory until validated in a Caribbean emergency department setting.

### Week 6

Week 6 focused on developing and evaluating two simple baseline models for predicting Emergency Severity Index (ESI) triage level. The purpose was to establish a clear and reproducible starting point before considering more advanced machine-learning approaches. Particular attention was given to patient safety, class imbalance and the models’ ability to recognise rare ESI Level 1 patients.

My contributions this week included:

- Preparing selected triage-time variables for baseline modelling
- Dividing the dataset into an 80% training set and a 20% testing set using stratification
- Using a fixed random seed of 42 to support reproducibility
- Training and evaluating a logistic regression classifier
- Training and evaluating a decision tree classifier limited to a maximum depth of 5
- Comparing both models with a stratified random-guess baseline
- Calculating overall accuracy and per-class precision, recall and F1-score
- Comparing macro and weighted F1-scores
- Producing confusion matrices for both required models
- Selecting ESI Level 1 recall as the primary clinical safety metric
- Documenting the main model failures and their possible consequences for patients
- Exploring an additional refined logistic regression model using a broader set of triage-time information
- Preparing a three-page baseline model report and a one-minute clinical explainer video

Key Week 6 files include:

- Final modelling notebook: `notebooks/Week6/Week6_Final_Ansarah.ipynb`
- Final baseline model report: `docs/Week6/Final/Week6_Final_Baseline_Model_Report_Ansarah.pdf`
- Logistic regression confusion matrix: `docs/Week6/Final/week6_final_confusion_logistic_regression.png`
- Decision tree confusion matrix: `docs/Week6/Final/week6_final_confusion_decision_tree.png`
- Baseline model comparison table: `docs/Week6/Final/week6_baseline_model_comparison.csv`
- Supporting figures and clinical explainer materials: `docs/Week6/Final/`

Main Week 6 conclusion:

The logistic regression and decision tree achieved higher overall accuracy, macro F1 and weighted F1 scores than the stratified random baseline. However, neither required model correctly identified any of the 16 ESI Level 1 patients in the testing set. This showed that reasonable overall performance did not necessarily indicate safe performance for the rarest and most urgent patients.

An additional refined logistic regression model correctly identified 4 of the 16 ESI Level 1 patients, increasing ESI Level 1 recall from 0.000 to 0.250. However, it still missed 12 critically urgent patients. The models are therefore treated as experimental benchmarks rather than tools that are ready for clinical use.

### Week 7

Week 7 focused on model optimisation and the trade-offs between predictive performance, interpretability, computational cost and practical deployment. The two original Week 6 baseline models were rebuilt and compared with a more complex Random Forest classifier using the same ten triage-time predictors, 80/20 stratified train-test split and fixed random seed of 42.

My interim work this week included:

- Rebuilding the original Logistic Regression and depth-limited Decision Tree baselines
- Training an initial class-weighted Random Forest
- Optimising the Random Forest using three-fold stratified cross-validation
- Comparing accuracy, macro precision, macro recall, macro F1 and weighted F1
- Measuring training time and inference time per patient
- Assessing model interpretability using Random Forest feature importance
- Reviewing confusion matrices and ESI Level 1 under-triage errors
- Examining ESI Level 1 precision to identify possible false-alarm and alert-fatigue risks
- Assessing overfitting by comparing training and validation macro F1
- Preparing an interim benchmark table and provisional Phase 3 recommendation

Key Week 7 interim files include:

- Interim model optimisation notebook: `notebooks/Week7/Week7_Interim_Model_Ansarah.ipynb`
- Draft model benchmark: `docs/Week7/Interim/week7_draft_benchmark.md`
- Supporting figures and model outputs: `docs/Week7/Interim/`

Main Week 7 interim conclusion:

The tuned Random Forest achieved the strongest macro F1-score and distributed its performance more evenly across the five ESI categories. However, it correctly identified only one of the 16 ESI Level 1 patients, produced several false critical alerts, reduced overall accuracy and required considerably more training time than the simpler models.

Logistic Regression therefore remains the more defensible current baseline for Phase 3, while the Random Forest is retained as an experimental candidate for further feature development, error analysis and clinical review. This recommendation remains provisional until the final Week 7 cost-benefit memo is completed.

## Contributing

This is an individual learning portfolio for the CariSurg MedTech Pathways programme.

Suggestions, corrections, or feedback from tutors and reviewers are welcome through GitHub issues or pull requests.

## Licence

This repository is licensed under the MIT Licence. See the `LICENSE` file for details.

## Author

Ansarah Mohammed  
Electrical and Computer Engineering Student  
CariSurg MedTech Pathways Trainee
