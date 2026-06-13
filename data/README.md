
Tiny correction: when you paste that into GitHub, the inner code block may confuse the markdown editor because it has triple backticks inside triple backticks. So paste this safer version instead:

```markdown
# Data Folder

This folder is reserved for datasets used in the CariSurg portfolio project.

The Week 0 emergency triage dataset is **not uploaded to this public repository** because it is healthcare-related data. Even when a dataset is reduced or de-identified, raw clinical data should not be shared publicly unless permission is clearly given by the programme or dataset provider.

## Expected Data Location

When running the Week 0 notebooks, the dataset should be stored locally or in Google Drive and loaded from a private path.

Example path:

`/content/drive/MyDrive/CARISURG/Week0/EmergencyTriageDataset_Reduced_Dirty.csv`

## Privacy Note

No real patient data, private credentials, API keys, or sensitive files should be committed to this repository.

Only documentation describing the dataset should be placed here unless the programme gives permission to upload the actual data.
