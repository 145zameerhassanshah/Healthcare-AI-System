from pathlib import Path

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
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
    """Load and clean the raw healthcare dataset."""

    df = pd.read_csv(DATA_PATH)

    # Dataset-specific missing-value marker.
    df = df.replace("?", pd.NA)

    # Target:
    # 1 = readmitted within 30 days
    # 0 = not readmitted within 30 days
    df["early_readmission"] = (
        df["readmitted"] == "<30"
    ).astype(int)

    return df


def prepare_features(df):
    """Separate model features X from target y."""

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


def build_pipeline(X):
    """Create preprocessing + Logistic Regression pipeline."""

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

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42,
    )

    pipeline = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor,
            ),
            (
                "model",
                model,
            ),
        ]
    )

    return pipeline


def main():

    print("\n--- LOADING DATA ---")

    df = load_data()

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    X, y = prepare_features(df)

    print("\n--- FEATURES ---")
    print(f"Feature columns: {X.shape[1]}")

    print("\n--- TARGET ---")
    print(y.value_counts())
    print(
        y.value_counts(normalize=True)
        .mul(100)
        .round(2)
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print("\n--- TRAIN / TEST ---")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    pipeline = build_pipeline(X_train)

    print("\n--- TRAINING MODEL ---")

    pipeline.fit(
        X_train,
        y_train,
    )

    print("Logistic Regression trained successfully.")


if __name__ == "__main__":
    main()