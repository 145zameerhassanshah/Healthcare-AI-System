from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "diabetic_data.csv"


def load_data():
    return pd.read_csv(DATA_PATH)


def profile_data(df):
    print("\n--- DATASET SHAPE ---")
    print(df.shape)

    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())

    print("\n--- TARGET DISTRIBUTION ---")
    print(df["readmitted"].value_counts(dropna=False))

    print("\n--- TARGET PERCENTAGE ---")
    print(
        df["readmitted"]
        .value_counts(normalize=True, dropna=False)
        .mul(100)
        .round(2)
    )

    print("\n--- QUESTION MARK VALUES ---")
    question_mark_counts = (
        df.eq("?")
        .sum()
        .sort_values(ascending=False)
    )

    print(question_mark_counts.head(20))

    print("\n--- MISSING VALUES ---")
    missing = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )

    print(missing.head(20))

    print("\n--- UNIQUE VALUES ---")
    unique_counts = (
        df.nunique()
        .sort_values(ascending=False)
    )

    print(unique_counts.head(20))


def main():
    df = load_data()
    profile_data(df)


if __name__ == "__main__":
    main()