from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "diabetic_data.csv"


DROP_COLUMNS = [
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

def main():
    df = pd.read_csv(DATA_PATH)
    df = df.replace("?", pd.NA)

    df["early_readmission"] = (
        df["readmitted"].eq("<30").astype(int)
    )

    X = df.drop(
        columns=[
            column
        for column in [
            *DROP_COLUMNS,
            "early_readmission",
        ]
            if column in df.columns
        ]
    )

    numerical_features = X.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object", "string", "category"]
    ).columns.tolist()

    print("\n--- FEATURE ANALYSIS ---")

    print(f"\nTotal features: {X.shape[1]}")

    print(
        f"\nNumerical features: "
        f"{len(numerical_features)}"
    )

    print(numerical_features)

    print(
        f"\nCategorical features: "
        f"{len(categorical_features)}"
    )

    print(categorical_features)

    print("\n--- NUMERICAL SUMMARY ---")
    print(X[numerical_features].describe().T)

    print("\n--- CATEGORICAL CARDINALITY ---")

    for column in categorical_features:
        print(
            f"{column}: "
            f"{X[column].nunique(dropna=True)} unique values"
        )


if __name__ == "__main__":
    main()