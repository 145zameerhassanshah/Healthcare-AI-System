from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "diabetic_data.csv"


TARGET_COLUMN = "readmitted"

DROP_COLUMNS = [
    "encounter_id",
    "patient_nbr",
    "weight",
    "max_glu_serum",
    "A1Cresult",
]


def load_raw_data():
    """Load the original healthcare dataset."""
    return pd.read_csv(DATA_PATH)


def prepare_dataset(df):
    """
    Clean the raw dataset and create a binary early-readmission target.
    """

    df = df.copy()

    # Normalize the dataset's '?' missing-value marker.
    df = df.replace("?", pd.NA)

    # Target:
    # <30 days = early readmission
    # NO or >30 days = not early readmission
    df["early_readmission"] = (
        df[TARGET_COLUMN].eq("<30").astype(int)
    )

    # Remove original target and identifier/sparse columns.
    columns_to_drop = [
        TARGET_COLUMN,
        *DROP_COLUMNS,
    ]

    columns_to_drop = [
        column
        for column in columns_to_drop
        if column in df.columns
    ]

    X = df.drop(columns=columns_to_drop)
    y = df["early_readmission"]

    return X, y


def main():
    df = load_raw_data()

    X, y = prepare_dataset(df)

    print("\n--- PREPARED DATASET ---")
    print(f"Original rows: {len(df)}")
    print(f"Features after selection: {X.shape[1]}")

    print("\n--- TARGET ---")
    print(y.value_counts())
    print(y.value_counts(normalize=True).mul(100).round(2))

    print("\n--- REMAINING MISSING VALUES ---")
    missing = X.isna().sum()
    print(
        missing[missing > 0]
        .sort_values(ascending=False)
        .head(20)
    )


if __name__ == "__main__":
    main()