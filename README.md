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

Then navigate to:

```text
notebooks/Week0/
```

## Data Privacy

The original Week 0 emergency triage dataset is not uploaded to this public repository because it is healthcare-related data.

Even if data is reduced or de-identified, raw clinical data should not be shared publicly unless permission is clearly given by the programme or dataset provider.

When running the notebooks, the dataset should be stored locally or in a private Google Drive location.

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

## Contributing

This is an individual learning portfolio for the CariSurg MedTech Pathways programme.

Suggestions, corrections, or feedback from tutors and reviewers are welcome through GitHub issues or pull requests.

## Licence

This repository is licensed under the MIT Licence. See the `LICENSE` file for details.

## Author

Ansarah Mohammed  
Electrical and Computer Engineering Student  
CariSurg MedTech Pathways Trainee
