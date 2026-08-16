# Dataset

This project uses the Diabetes 130-US Hospitals for Years 1999-2008
dataset.

The dataset contains hospital encounters involving patients with
diabetes and is used for educational machine-learning experimentation.

## Dataset File

`diabetic_data.csv`

The raw CSV is intentionally excluded from Git version control because
of its large file size.

## Target

The project derives a binary target:

- `1` = early readmission within 30 days
- `0` = no early readmission within 30 days

## Reproducibility

Download the original public dataset and place:

`diabetic_data.csv`

inside:

`data/raw/`

The project scripts can then reproduce the data ingestion,
preprocessing, analysis, and machine-learning workflow.