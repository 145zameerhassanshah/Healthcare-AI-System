from pathlib import Path

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
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
    df = pd.read_csv(DATA_PATH)

    df = df.replace("?", pd.NA)

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


def build_pipeline(X):

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

    return Pipeline(
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


def main():

    print("\n--- LOADING DATA ---")

    df = load_data()

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    pipeline = build_pipeline(X_train)

    print("\n--- TRAINING ---")

    pipeline.fit(
        X_train,
        y_train,
    )

    print("Model trained.")

    print("\n--- PREDICTION ---")

    y_pred = pipeline.predict(X_test)

    y_probability = pipeline.predict_proba(
        X_test
    )[:, 1]

    print(
        f"Predictions generated: {len(y_pred)}"
    )

    print("\n--- ACCURACY ---")

    accuracy = accuracy_score(
        y_test,
        y_pred,
    )

    print(f"Accuracy: {accuracy:.4f}")

    print("\n--- CLASSIFICATION REPORT ---")

    print(
        classification_report(
            y_test,
            y_pred,
            target_names=[
                "No Early Readmission",
                "Early Readmission",
            ],
        )
    )

    print("\n--- CONFUSION MATRIX ---")

    matrix = confusion_matrix(
        y_test,
        y_pred,
    )

    print(matrix)

    print("\n--- ROC-AUC ---")

    roc_auc = roc_auc_score(
        y_test,
        y_probability,
    )

    print(f"ROC-AUC: {roc_auc:.4f}")


if __name__ == "__main__":
    main()