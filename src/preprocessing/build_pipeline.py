from pathlib import Path

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "diabetic_data.csv"
)


DROP_COLUMNS = [
    "encounter_id",
    "patient_nbr",
    "weight",
    "max_glu_serum",
    "A1Cresult",
    "readmitted",
    "examide",
    "citoglipton",
]


def load_data():
    df = pd.read_csv(DATA_PATH)

    # Convert dataset-specific missing marker.
    df = df.replace("?", pd.NA)

    # Create binary target.
    df["early_readmission"] = (
        df["readmitted"] == "<30"
    ).astype(int)

    return df


def prepare_features(df):
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

    y = df["early_readmission"]

    return X, y


def build_preprocessor(X):
    numerical_features = X.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object", "string", "category"]
    ).columns.tolist()

    numerical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent"),
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                ),
            ),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_features,
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features,
            ),
        ]
    )

    return preprocessor


def main():
    df = load_data()

    X, y = prepare_features(df)

    preprocessor = build_preprocessor(X)

    print("\n--- PREPROCESSING PIPELINE ---")
    print(
        "Numerical features:",
        len(
            X.select_dtypes(
                include=["number"]
            ).columns,
        ),
    )

    print(
        "Categorical features:",
        len(
            X.select_dtypes(
                include=[
                    "object",
                    "string",
                    "category",
                ]
            ).columns,
        ),
    )

    print("\nPreprocessor created successfully.")


if __name__ == "__main__":
    main()