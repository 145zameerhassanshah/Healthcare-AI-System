from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "diabetic_data.csv"


def load_healthcare_data():
    """Load the raw healthcare dataset."""
    return pd.read_csv(DATA_PATH)


def main():
    df = load_healthcare_data()

    print("\n--- DATASET LOADED ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n--- FIRST 5 RECORDS ---")
    print(df.head())

    print("\n--- COLUMN NAMES ---")
    print(df.columns.tolist())

    print("\n--- DATA TYPES ---")
    print(df.dtypes)

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum().sort_values(ascending=False).head(15))


if __name__ == "__main__":
    main()