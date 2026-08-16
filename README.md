# Healthcare AI System

## Project Overview

Healthcare AI System is a practical AI and healthcare analytics project developed as part of the CMITP AI Internship.

The project combines healthcare database development, SQL analytics, REST API integration, real-world healthcare data analysis, exploratory data analysis, machine learning preprocessing, predictive modeling, model evaluation, and Git/GitHub version control.

The project evolved from a structured healthcare database and analytics workflow into a real-world healthcare machine-learning pipeline using the Diabetes 130-US Hospitals dataset.

The current AI workflow focuses on predicting **early hospital readmission within 30 days** from healthcare encounter data.

---

## Healthcare AI Prediction Workflow

The machine-learning workflow follows:

```text
Real-World Healthcare Dataset
          ↓
Data Ingestion
          ↓
Data Profiling & Quality Analysis
          ↓
Missing Data Analysis
          ↓
Target Engineering
          ↓
Exploratory Data Analysis
          ↓
Feature Analysis
          ↓
Train/Test Split
          ↓
Preprocessing Pipeline
          ↓
Logistic Regression Baseline
          ↓
Model Evaluation
          ↓
Threshold Analysis
          ↓
Model Comparison
          ↓
Joblib Model Persistence
```

### Dataset

The project uses the **Diabetes 130-US Hospitals for Years 1999-2008** dataset.

Dataset characteristics:

* **101,766 hospital encounters**
* **50 original columns**
* Healthcare and hospital encounter information
* Target engineered from the `readmitted` field
* Binary target: `early_readmission`

Target definition:

* `1` → readmission within 30 days
* `0` → no readmission within 30 days

The raw dataset is excluded from Git version control because of its size. Dataset information and reproducibility instructions are provided under `data/raw/`.

---

## Machine Learning

The project implements an end-to-end Scikit-learn workflow.

### Data Preparation

* Dataset profiling
* Duplicate detection
* Missing-value analysis
* Question-mark / invalid-value detection
* Feature analysis
* Target engineering
* Feature selection
* Numerical and categorical feature identification
* Stratified train/test splitting

### Exploratory Data Analysis

EDA was performed using:

* Pandas
* Matplotlib
* Seaborn

Visual analysis includes:

* Target distribution
* Age distribution
* Hospital stay distribution
* Medication distribution
* Laboratory procedure distribution
* Readmission rate by age
* Correlation analysis

Generated figures are stored under:

```text
reports/figures/
```

### Preprocessing

The Scikit-learn preprocessing workflow includes:

* Missing-value handling
* Categorical feature encoding
* Numerical feature scaling
* Reusable `ColumnTransformer` pipeline

### Models Evaluated

The following models were compared:

* Logistic Regression
* Decision Tree
* Random Forest

### Model Results

| Model               | Accuracy | Precision | Recall |     F1 |    ROC-AUC |
| ------------------- | -------: | --------: | -----: | -----: | ---------: |
| Logistic Regression |   64.18% |    16.64% | 55.13% | 25.57% |     0.6440 |
| Decision Tree       |   60.68% |    16.63% | 62.88% | 26.30% |     0.6550 |
| Random Forest       |   60.80% |    16.41% | 61.38% | 25.90% | **0.6595** |

Because early readmission represents only **11.16%** of encounters, accuracy alone is not sufficient to judge model performance. Recall, F1-score, and ROC-AUC were also considered.

Random Forest produced the highest ROC-AUC among the tested models, while Logistic Regression was retained as the reproducible baseline pipeline saved with Joblib.

### Model Persistence

The trained Logistic Regression preprocessing + model pipeline is saved using Joblib:

```text
models/early_readmission_model.joblib
```

The model file is excluded from Git tracking through `.gitignore`.

---

## REST API Integration

The project also includes a reusable REST API integration module developed using Python's `requests` library.

The API client demonstrates:

* GET
* POST
* PUT
* PATCH
* DELETE
* JSON response processing
* HTTP headers
* Authentication patterns
* Sessions
* Environment-variable usage
* Timeout handling
* API error handling

JSONPlaceholder is used as a public testing service. No real patient or personally identifiable healthcare data is transmitted.

Implementation:

```text
src/api/api_client.py
```

Documentation:

```text
docs/api-integration.md
```

---

## Healthcare Database & SQL Analytics

The earlier project workflow includes a relational SQLite healthcare database containing:

* Departments
* Doctors
* Patients
* Appointments

The database workflow demonstrates:

* Relational database design
* Primary keys
* Foreign keys
* SQL DDL
* SQL DML
* SQL queries
* Filtering
* Sorting
* Aggregation
* Grouping
* JOIN operations
* Healthcare data extraction

---

## Project Objectives

* Develop a practical healthcare AI workflow
* Work with real-world healthcare data
* Perform healthcare data profiling and quality analysis
* Perform exploratory data analysis
* Prepare healthcare data for machine learning
* Engineer meaningful predictive features
* Build Scikit-learn machine-learning models
* Evaluate classification performance using multiple metrics
* Compare different machine-learning algorithms
* Save a trained model using Joblib
* Practice REST API integration
* Practice relational healthcare database development
* Apply SQL-based healthcare analytics
* Maintain professional Git/GitHub workflows
* Build reproducible and well-documented AI projects

---

# Technologies Used

## Programming

* Python

## Data Processing

* Pandas
* NumPy

## Data Visualization

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-learn
* Joblib

## Database

* SQLite
* SQL

## API Integration

* Requests
* REST
* JSON

## Development & Collaboration

* Visual Studio Code
* Jupyter Notebook
* Google Colab
* Git
* GitHub

## Environment & Dependency Management

* Python `venv`
* Conda
* pip
* `requirements.txt`

---

# Project Architecture

```text
Healthcare-AI-System/
│
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
│
├── models/
│
├── reports/
│   ├── figures/
│   └── model_comparison.csv
│
├── docs/
│   └── api-integration.md
│
├── notebooks/
│
├── src/
│   │
│   ├── api/
│   │   └── api_client.py
│   │
│   ├── database/
│   │   ├── database_setup.py
│   │   ├── insert_data.py
│   │   ├── sql_queries.py
│   │   └── verify_database.py
│   │
│   ├── data_ingestion/
│   │   ├── load_diabetes_data.py
│   │   ├── profile_data.py
│   │   └── missing_analysis.py
│   │
│   ├── eda/
│   │   └── exploratory_analysis.py
│   │
│   ├── preprocessing/
│   │   ├── prepare_data.py
│   │   ├── feature_analysis.py
│   │   ├── split_data.py
│   │   └── build_pipeline.py
│   │
│   └── ml/
│       ├── train_model.py
│       ├── evaluate_model.py
│       ├── threshold_analysis.py
│       ├── compare_models.py
│       └── save_model.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Reproducibility

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies from `requirements.txt`.
4. Download the public healthcare dataset.
5. Place the dataset in `data/raw/`.
6. Run the data-ingestion and analysis scripts.
7. Run the preprocessing workflow.
8. Train and evaluate the machine-learning models.
9. Save the trained pipeline using Joblib.

The project intentionally excludes the virtual environment, raw dataset, processed data, and trained model artifacts from Git version control where appropriate.

---

## Project Status

**Completed**

The project demonstrates a complete learning-oriented healthcare AI workflow from data ingestion and analysis through machine-learning training, evaluation, model persistence, API integration, database development, and GitHub-based project management.

> **Educational Notice:** This project is intended for AI/ML learning and experimentation. Model predictions are not intended for clinical diagnosis, treatment decisions, or direct patient-care use.
