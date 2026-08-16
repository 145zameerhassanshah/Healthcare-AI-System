from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "diabetic_data.csv"
)


def load_data():
    df = pd.read_csv(DATA_PATH)

    # Dataset uses ? for unavailable values
    df = df.replace("?", pd.NA)

    return df


def create_target(df):
    df = df.copy()

    # 1 = readmitted within 30 days
    # 0 = otherwise
    df["early_readmission"] = (
        df["readmitted"] == "<30"
    ).astype(int)

    return df


def prepare_features(df):
    target = df["early_readmission"]

    drop_columns = [
        "encounter_id",
        "patient_nbr",
        "weight",
        "max_glu_serum",
        "A1Cresult",
        "readmitted",
        "early_readmission",
        "examide",
        "citoglipton",
    ]

    features = df.drop(
        columns=[
            column
            for column in drop_columns
            if column in df.columns
        ]
    )

    return features, target


def main():
    df = load_data()

    df = create_target(df)

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("\n--- TRAIN / TEST SPLIT ---")

    print(f"Total samples: {len(X)}")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    print("\n--- TRAIN TARGET DISTRIBUTION ---")
    print(y_train.value_counts(normalize=True).mul(100).round(2))

    print("\n--- TEST TARGET DISTRIBUTION ---")
    print(y_test.value_counts(normalize=True).mul(100).round(2))


if __name__ == "__main__":
    main()