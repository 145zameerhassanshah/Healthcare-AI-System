from pathlib import Path

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
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


def build_pipeline(X):

    numerical_features = (
        X.select_dtypes(include=["number"])
        .columns
        .tolist()
    )

    categorical_features = (
        X.select_dtypes(
            include=["object", "string", "category"]
        )
        .columns
        .tolist()
    )

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
                SimpleImputer(
                    strategy="most_frequent"
                ),
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

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y,
        )
    )

    print("\n--- TRAINING BASELINE ---")

    pipeline = build_pipeline(X_train)

    pipeline.fit(
        X_train,
        y_train,
    )

    probabilities = pipeline.predict_proba(
        X_test
    )[:, 1]

    print("\n--- THRESHOLD ANALYSIS ---")

    thresholds = [
        0.30,
        0.40,
        0.50,
        0.60,
        0.70,
    ]

    print(
        "\nThreshold | Accuracy | Precision | Recall | F1"
    )

    print("-" * 55)

    for threshold in thresholds:

        predictions = (
            probabilities >= threshold
        ).astype(int)

        accuracy = accuracy_score(
            y_test,
            predictions,
        )

        precision = precision_score(
            y_test,
            predictions,
            zero_division=0,
        )

        recall = recall_score(
            y_test,
            predictions,
            zero_division=0,
        )

        f1 = f1_score(
            y_test,
            predictions,
            zero_division=0,
        )

        print(
            f"{threshold:9.2f} | "
            f"{accuracy:8.4f} | "
            f"{precision:9.4f} | "
            f"{recall:6.4f} | "
            f"{f1:6.4f}"
        )

    print(
        f"\nROC-AUC remains: "
        f"{roc_auc_score(y_test, probabilities):.4f}"
    )


if __name__ == "__main__":
    main()