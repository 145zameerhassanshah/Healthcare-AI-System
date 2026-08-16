# Healthcare AI System

## Project Overview

Healthcare AI System is a practical AI and healthcare analytics project developed as part of the CMITP AI Internship.

The project demonstrates an end-to-end workflow starting from project setup and Git version control, followed by relational healthcare database development, synthetic healthcare data generation, SQL-based analytics, exploratory data analysis, data preprocessing, machine learning, and model evaluation.

The system is designed as a practical learning project to demonstrate how healthcare data can be stored, managed, analyzed, and prepared for Artificial Intelligence and Machine Learning applications.

---
## API Integration

The project includes a REST API integration module developed using Python's
`requests` library. The implementation communicates with an external public
REST API, sends HTTP requests, receives JSON responses, validates responses,
and extracts selected information from the returned data.

The API client demonstrates the core REST methods:

- GET – retrieve resources
- POST – create resources
- PUT – replace resources
- PATCH – partially update resources
- DELETE – delete resources

JSONPlaceholder is used as a public testing service, so no real patient or
personally identifiable healthcare data is transmitted.

The implementation is available in:

`src/api/api_client.py`

Detailed API concepts and implementation notes are documented in:

`docs/api-integration.md`

## Project Objectives

- Build a structured healthcare database using SQLite
- Design relational tables for departments, doctors, patients, and appointments
- Generate realistic synthetic healthcare records for development and analysis
- Practice SQL data retrieval and analytical queries
- Perform filtering, sorting, aggregation, grouping, and relational joins
- Extract integrated healthcare information from multiple tables
- Perform Exploratory Data Analysis (EDA)
- Identify patterns, distributions, relationships, and data-quality issues
- Prepare healthcare data for Machine Learning
- Apply preprocessing and feature engineering techniques
- Develop a baseline Machine Learning model
- Evaluate model performance using appropriate metrics
- Practice professional Git and GitHub version-control workflows
- Maintain project history using branches, commits, merges, and pull requests
- Understand REST API architecture and HTTP request/response workflows
- Retrieve and process JSON data from external services using Python
- Extract selected information from API responses
- Practice API integration using GET, POST, PUT, PATCH, and DELETE methods
---

# Technologies Used

## Programming

- Python

## Database

- SQLite
- SQL

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-learn

## Development Tools

- Visual Studio Code
- Google Colab
- Jupyter Notebook
- Git
- GitHub

---
## Environment & Dependency Management

- Python `venv`
- Conda
- pip
- requirements.txt
# Project Architecture

```text
Healthcare-AI-System/
│
├── database/
│   └── HospitalDB.db
│
├── src/
│   ├── database_setup.py
│   ├── insert_data.py
│   ├── verify_database.py
│   ├── sql_queries.py
│   │
│   ├── api/
│   │   └── api_client.py
│   ├── eda/
│   ├── preprocessing/
│   └── ml/│
├── notebooks/
│
├── reports/
│
├── docs/
│
├── .gitignore
├── README.md
└── requirements.txt
